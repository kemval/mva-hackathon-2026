#!/usr/bin/env python3
"""Derive the permissive multi-exon-deletion windows in BUB1B from the data.

The Track 1 report bounds a hemizygous multi-exon BUB1B deletion using the
proband's own heterozygous calls: a het call is positive evidence of diploidy
at that position, so a deletion can only hide in the intervals *between* het
calls. The report used to name those windows in prose, and
`coverage_analysis.py` used to carry the same list hardcoded -- copied from the
report rather than derived, so when the list was short by one window neither
artefact could catch it. Two audit passes verified that the windows listed
contained the exons claimed, which was true, and never asked whether the list
was complete, which it was not.

This script derives the list instead of asserting it. It reads the het calls
from the region-restricted VCF, takes the gene body and canonical-transcript
exons from Ensembl, and emits every inter-het interval that fully contains at
least one coding exon -- with the summed CDS length of those exons, because a
whole-window deletion is only a *truncating* allele when that sum is not a
multiple of three. That distinction matters to the report's own argument: it
lowers the prior on a deletion in trans on the grounds that published biallelic
BUB1B-MVA pairs a truncating allele with a missense one, and an in-frame
window deletion is not a truncating allele.

Usage:
    python3 deletion_windows.py --vcf data-notes/mva_panel_variants.vcf.gz

Requires bcftools and network access to Ensembl REST. The VCF is proband data
and is not committed; see data-notes/README.md.
"""
import argparse
import json
import subprocess
import sys
import urllib.request

TRANSCRIPT = "ENST00000287598"  # BUB1B canonical
GENE = ("15", 40160984, 40221137)  # Ensembl GRCh38, matches data-notes/regions/


def het_calls(vcf, chrom, start, end):
    """PASS heterozygous call positions inside the gene body, ascending."""
    cmd = ["bcftools", "query", "-f", "%POS\t[%GT]\n", "-i", 'FILTER="PASS"',
           "-r", f"{chrom}:{start}-{end}", vcf]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"bcftools query failed: {out.stderr.strip()}")
    return sorted(int(line.split("\t")[0]) for line in out.stdout.splitlines()
                  if line.split("\t")[1] in ("0/1", "0|1", "1|0"))


def coding_exons(transcript):
    """[(exon_number, start, end, cds_length)] ascending by coordinate."""
    url = (f"https://rest.ensembl.org/lookup/id/{transcript}"
           "?expand=1;content-type=application/json")
    with urllib.request.urlopen(url, timeout=30) as fh:
        data = json.load(fh)
    exons = sorted(data["Exon"], key=lambda e: e["start"])
    cds_lo, cds_hi = data["Translation"]["start"], data["Translation"]["end"]
    out = []
    for n, e in enumerate(exons, 1):
        lo, hi = max(e["start"], cds_lo), min(e["end"], cds_hi)
        if lo <= hi:
            out.append((n, e["start"], e["end"], hi - lo + 1))
    return out


def windows(hets, exons, gene_start):
    """Inter-het intervals fully containing >=1 coding exon."""
    bounds = [gene_start] + hets
    rows = []
    for lo, hi in zip(bounds, bounds[1:]):
        inside = [e for e in exons if lo < e[1] and e[2] < hi]
        if inside:
            rows.append((lo, hi, inside))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vcf", required=True, help="region-restricted panel VCF")
    args = ap.parse_args()

    chrom, gstart, gend = GENE
    hets = [p for p in het_calls(args.vcf, chrom, gstart - 2000, gend + 2000)]
    inside = [p for p in hets if gstart <= p <= gend]
    exons = coding_exons(TRANSCRIPT)

    print(f"# BUB1B {chrom}:{gstart}-{gend}  "
          f"het calls: {len(hets)} padded / {len(inside)} in gene body")
    print("interval\tsize_bp\tcomplete_coding_exons\tcds_nt\tframe")
    for lo, hi, ex in windows(hets, exons, gstart):
        nums = [e[0] for e in ex]
        label = f"exons {nums[0]}-{nums[-1]}" if len(nums) > 1 else f"exon {nums[0]}"
        cds = sum(e[3] for e in ex)
        frame = "in-frame" if cds % 3 == 0 else "frameshift"
        print(f"{lo:,}-{hi:,}\t{hi - lo:,}\t{label}\t{cds}\t{frame}")


if __name__ == "__main__":
    main()
