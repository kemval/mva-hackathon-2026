#!/usr/bin/env python3
"""Annotate all PASS variants in the MVA gene panel VCF via Ensembl VEP REST,
extracting consequence, canonical HGVS, max gnomAD population AF, and any
ClinVar clinical significance. Writes a flat TSV for downstream filtering.

Usage: python3 vep_annotate_panel.py
Reads:  data-notes/mva_panel_variants.vcf.gz
Writes: data-notes/annotated/vep_panel_annotated.tsv
        data-notes/annotated/vep_raw_responses.jsonl (raw API responses, for audit)
"""
import json
import subprocess
import time
import urllib.request

VCF = "/Users/kiki/mva-hackathon-2026/data-notes/mva_panel_variants.vcf.gz"
OUT_TSV = "/Users/kiki/mva-hackathon-2026/data-notes/annotated/vep_panel_annotated.tsv"
OUT_RAW = "/Users/kiki/mva-hackathon-2026/data-notes/annotated/vep_raw_responses.jsonl"
BATCH_SIZE = 150
VEP_URL = (
    "https://rest.ensembl.org/vep/human/region"
    "?content-type=application/json&canonical=1&hgvs=1&check_existing=1"
    "&af_gnomade=1&af_gnomadg=1&domains=1"
)


def get_pass_variants():
    """Return list of (chrom, pos, ref, alt, gt, ad, gq) tuples for PASS records."""
    cmd = [
        "bcftools", "view", "-f", "PASS", VCF,
    ]
    p1 = subprocess.run(cmd, capture_output=True, text=True, check=True)
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
    best = 0.0
    for cv in colocated or []:
        freqs = cv.get("frequencies", {})
        for allele_freqs in freqs.values():
            for k, v in allele_freqs.items():
                if k.startswith("gnomadg") or k == "af":
                    try:
                        best = max(best, float(v))
                    except (TypeError, ValueError):
                        pass
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


def main():
    variants = get_pass_variants()
    print(f"Loaded {len(variants)} PASS variants from panel VCF")

    lines = [to_vep_region_line(c, p, r, a) for c, p, r, a, *_ in variants]
    gt_lookup = {(c, p, r, a): (gt, ad, gq) for c, p, r, a, gt, ad, gq in variants}

    rows_out = []
    with open(OUT_RAW, "w") as rawf:
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
                key = None
                # match back to original ref/alt via input line (positions may shift for indels in VEP norm)
                for k in gt_lookup:
                    if k[0] == chrom and k[1] == pos:
                        key = k
                        break
                gt, ad, gq = gt_lookup.get(key, ("", "", ""))

                canon = pick_canonical(r.get("transcript_consequences"))
                consequences = canon.get("consequence_terms", [])
                consequences_sorted = sorted(consequences, key=severity_rank)
                top_consequence = consequences_sorted[0] if consequences_sorted else r.get("most_severe_consequence", "")

                gnomad_af = max_gnomad_af(r.get("colocated_variants"))
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
                    "gnomad_max_af": f"{gnomad_af:.6f}",
                    "clinvar_sig": clinvar,
                    "rsids": rsids,
                    "genotype": gt,
                    "allele_depth": ad,
                    "genotype_qual": gq,
                })
            time.sleep(0.5)

    with open(OUT_TSV, "w") as out:
        cols = ["chrom","pos","ref","alt","gene","consequence","impact","hgvsc","hgvsp",
                "gnomad_max_af","clinvar_sig","rsids","genotype","allele_depth","genotype_qual"]
        out.write("\t".join(cols) + "\n")
        for row in rows_out:
            out.write("\t".join(str(row.get(c, "")) for c in cols) + "\n")

    print(f"Wrote {len(rows_out)} annotated rows to {OUT_TSV}")


if __name__ == "__main__":
    main()
