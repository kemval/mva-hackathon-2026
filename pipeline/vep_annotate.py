#!/usr/bin/env python3
"""Annotate all PASS variants in a region-restricted VCF via Ensembl VEP REST,
extracting consequence, canonical HGVS, max gnomAD population AF, max SpliceAI
delta score, and any ClinVar clinical significance. Writes a flat TSV for
downstream filtering by pipeline/filter_candidates.py.

SpliceAI comes from VEP's own plugin (`&SpliceAI=1`), which is why no separate
splice-prediction service is needed -- the Broad's standalone SpliceAI Lookup API
was unreachable across three attempts, but Ensembl serves the same scores.

Usage:
    python3 vep_annotate.py --vcf PANEL.vcf.gz --out-tsv OUT.tsv --out-raw OUT.jsonl

See pipeline/README.md for the full command sequence used to produce the
Track 1 results, including the upstream bcftools region-restriction step.
"""
import argparse
import json
import subprocess
import time
import urllib.request

BATCH_SIZE = 150
VEP_URL = (
    "https://rest.ensembl.org/vep/human/region"
    "?content-type=application/json&canonical=1&hgvs=1&check_existing=1"
    "&af_gnomade=1&af_gnomadg=1&domains=1&SpliceAI=1"
)


def get_pass_variants(vcf):
    """Return list of (chrom, pos, ref, alt, gt, ad, gq) tuples for PASS records."""
    p1 = subprocess.run(
        ["bcftools", "view", "-f", "PASS", vcf],
        capture_output=True, text=True, check=True,
    )
    query_cmd = [
        "bcftools", "query", "-f",
        "%CHROM\t%POS\t%REF\t%ALT\t[%GT]\t[%AD]\t[%GQ]\n",
    ]
    p2 = subprocess.run(query_cmd, input=p1.stdout, capture_output=True, text=True, check=True)
    rows = []
    for line in p2.stdout.strip().splitlines():
        chrom, pos, ref, alt, gt, ad, gq = line.split("\t")
        rows.append((chrom, pos, ref, alt, gt, ad, gq))
    return rows


def to_vep_region_line(chrom, pos, ref, alt):
    # VEP REST region format: CHR START ID REF ALT QUAL FILTER (VCF-like, space sep)
    return f"{chrom} {pos} . {ref} {alt} . . ."


def vep_batch(lines):
    body = json.dumps({"variants": lines}).encode("utf-8")
    req = urllib.request.Request(
        VEP_URL, data=body, headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def max_gnomad_af(colocated):
    """Max AF across all gnomAD genome (gnomadg*) and exome (gnomade*) subpopulations.

    Returns None when VEP attached no gnomAD frequency at all for the position,
    rather than 0.0. The two are different claims -- "gnomAD has no record of
    this allele" is not "gnomAD records this allele at frequency zero" -- and
    this is the same blank-vs-zero distinction `max_spliceai_ds` already makes
    below. It is not hypothetical here: VEP returned no gnomAD frequency for
    15:40220612 (p.Asn1002Lys), which the earlier version wrote out as
    `0.000000`, while the variant is in fact a gnomAD exome singleton at
    AF 6.84e-7 (AC=1/1,461,878, direct API query). The old value was wrong in a
    permissive direction and the true value is still far below any rarity
    threshold used here, so no candidate was affected either way -- but the
    column now says "unknown" where it means unknown.

    NOTE (audit 2026-08-31): the as-run version of this function matched
    `k.startswith("gnomadg") or k == "af"`. That silently excluded every gnomAD
    *exome* frequency (the keys are `gnomade`, `gnomade_nfe`, ... and
    "gnomade".startswith("gnomadg") is False), while the bare `af` key it did
    include is the 1000 Genomes global AF, not gnomAD at all. The error was
    permissive rather than exclusionary -- it could only let a variant through
    the AF filter, never remove one -- so no candidate could have been missed.
    That was verified rather than assumed: the corrected computation below was
    replayed offline against the saved raw VEP responses
    (data-notes/annotated/vep_*raw_responses.jsonl) and yields an identical
    candidate set for both panels (primary 2/2, secondary 0/0; p.Leu737Ter's max
    AF rises 7.35e-5 -> 9.982e-5, still far below the 0.001 threshold). The
    published results therefore stand unmodified against this corrected script.
    """
    best = None
    for cv in colocated or []:
        freqs = cv.get("frequencies", {})
        for allele_freqs in freqs.values():
            for k, v in allele_freqs.items():
                if k.startswith("gnomadg") or k.startswith("gnomade"):
                    try:
                        f = float(v)
                    except (TypeError, ValueError):
                        continue
                    best = f if best is None else max(best, f)
    return best


def max_spliceai_ds(tx_consequences):
    """Max SpliceAI delta score across transcripts, or None if SpliceAI has no data.

    VEP's SpliceAI plugin attaches a per-transcript `spliceai` dict with four delta
    scores in 0-1 -- DS_AG/DS_AL (acceptor gain/loss), DS_DG/DS_DL (donor gain/loss)
    -- plus DP_* positional offsets, which are ignored here. SpliceAI's own
    high-recall threshold is 0.2; 0.5 is the recommended cutoff.

    Returns None rather than 0.0 when no transcript carries a `spliceai` key. The
    precomputed set does not reach every position: across the two panels 592 of
    2346 rows come back empty (227 indels and 365 SNVs, predominantly intronic,
    downstream and upstream positions). "Not scored" is a different claim from
    "scored zero", and collapsing the two would repeat the class of error the
    gnomAD AF field was already caught making (see max_gnomad_af above).
    """
    best = None
    for tx in tx_consequences or []:
        sa = tx.get("spliceai")
        if not sa:
            continue
        for k in ("DS_AG", "DS_AL", "DS_DG", "DS_DL"):
            if k in sa:
                try:
                    v = float(sa[k])
                except (TypeError, ValueError):
                    continue
                best = v if best is None else max(best, v)
    return best


def clin_sig(colocated):
    sigs = []
    for cv in colocated or []:
        cs = cv.get("clin_sig")
        if cs:
            sigs.extend(cs)
    return ";".join(sorted(set(sigs))) if sigs else ""


def pick_canonical(tx_consequences):
    for tx in tx_consequences or []:
        if tx.get("canonical") == 1:
            return tx
    return (tx_consequences or [{}])[0]


def severity_rank(term):
    order = [
        "transcript_ablation", "splice_acceptor_variant", "splice_donor_variant",
        "stop_gained", "frameshift_variant", "stop_lost", "start_lost",
        "transcript_amplification", "inframe_insertion", "inframe_deletion",
        "missense_variant", "protein_altering_variant", "splice_region_variant",
        "splice_donor_5th_base_variant", "splice_donor_region_variant",
        "splice_polypyrimidine_tract_variant", "incomplete_terminal_codon_variant",
        "start_retained_variant", "stop_retained_variant", "synonymous_variant",
        "coding_sequence_variant", "mature_miRNA_variant", "5_prime_UTR_variant",
        "3_prime_UTR_variant", "non_coding_transcript_exon_variant",
        "intron_variant", "NMD_transcript_variant", "non_coding_transcript_variant",
        "upstream_gene_variant", "downstream_gene_variant", "intergenic_variant",
    ]
    for i, t in enumerate(order):
        if term == t:
            return i
    return len(order)


def lookup_genotype(gt_lookup, chrom, pos, ref, alt):
    """Recover the source genotype for a VEP result row.

    Exact (chrom, pos, ref, alt) match first: VEP reports indels in its own
    normalised form (e.g. VCF "AT>A" comes back as "T>-" at pos+1), so allele
    strings do not always round-trip. Only when the exact key misses do we fall
    back to position, and then only if exactly one source record sits there --
    an ambiguous position (multi-allelic site) yields no genotype rather than a
    guess. This is why some rows in the annotated TSVs have empty genotype
    columns; every variant actually reported in the submission matched exactly.
    """
    exact = gt_lookup.get((chrom, pos, ref, alt))
    if exact:
        return exact
    at_pos = [v for k, v in gt_lookup.items() if k[0] == chrom and k[1] == pos]
    return at_pos[0] if len(at_pos) == 1 else ("", "", "")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vcf", required=True, help="region-restricted, indexed VCF(.gz)")
    ap.add_argument("--out-tsv", required=True, help="flat annotated TSV to write")
    ap.add_argument("--out-raw", required=True,
                    help="raw VEP JSON responses, one per line (audit trail)")
    args = ap.parse_args()

    variants = get_pass_variants(args.vcf)
    print(f"Loaded {len(variants)} PASS variants from {args.vcf}")

    lines = [to_vep_region_line(c, p, r, a) for c, p, r, a, *_ in variants]
    gt_lookup = {(c, p, r, a): (gt, ad, gq) for c, p, r, a, gt, ad, gq in variants}

    rows_out = []
    with open(args.out_raw, "w") as rawf:
        for i in range(0, len(lines), BATCH_SIZE):
            batch = lines[i : i + BATCH_SIZE]
            print(f"  VEP batch {i//BATCH_SIZE + 1}/{(len(lines)-1)//BATCH_SIZE + 1} ({len(batch)} variants)...")
            try:
                results = vep_batch(batch)
            except Exception as e:
                print(f"  ERROR on batch starting at {i}: {e}")
                time.sleep(2)
                continue
            for r in results:
                rawf.write(json.dumps(r) + "\n")
                chrom = r.get("seq_region_name", "")
                pos = str(r.get("start", ""))
                allele_string = r.get("allele_string", "")
                ref = allele_string.split("/")[0] if "/" in allele_string else ""
                alt = allele_string.split("/")[-1] if "/" in allele_string else ""
                gt, ad, gq = lookup_genotype(gt_lookup, chrom, pos, ref, alt)

                canon = pick_canonical(r.get("transcript_consequences"))
                consequences = canon.get("consequence_terms", [])
                consequences_sorted = sorted(consequences, key=severity_rank)
                top_consequence = consequences_sorted[0] if consequences_sorted else r.get("most_severe_consequence", "")

                gnomad_af = max_gnomad_af(r.get("colocated_variants"))
                spliceai_ds = max_spliceai_ds(r.get("transcript_consequences"))
                clinvar = clin_sig(r.get("colocated_variants"))
                rsids = ";".join(
                    cv.get("id", "") for cv in (r.get("colocated_variants") or []) if cv.get("id", "").startswith("rs")
                )

                rows_out.append({
                    "chrom": chrom,
                    "pos": pos,
                    "ref": ref,
                    "alt": alt,
                    "gene": canon.get("gene_symbol", ""),
                    "consequence": top_consequence,
                    "impact": canon.get("impact", ""),
                    "hgvsc": canon.get("hgvsc", ""),
                    "hgvsp": canon.get("hgvsp", ""),
                    "gnomad_max_af": "" if gnomad_af is None else f"{gnomad_af:.6f}",
                    "spliceai_max_ds": "" if spliceai_ds is None else f"{spliceai_ds:.2f}",
                    "clinvar_sig": clinvar,
                    "rsids": rsids,
                    "genotype": gt,
                    "allele_depth": ad,
                    "genotype_qual": gq,
                })
            time.sleep(0.5)

    with open(args.out_tsv, "w") as out:
        cols = ["chrom","pos","ref","alt","gene","consequence","impact","hgvsc","hgvsp",
                "gnomad_max_af","spliceai_max_ds","clinvar_sig","rsids","genotype",
                "allele_depth","genotype_qual"]
        out.write("\t".join(cols) + "\n")
        for row in rows_out:
            out.write("\t".join(str(row.get(c, "")) for c in cols) + "\n")

    print(f"Wrote {len(rows_out)} annotated rows to {args.out_tsv}")


if __name__ == "__main__":
    main()
