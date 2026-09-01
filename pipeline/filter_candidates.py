#!/usr/bin/env python3
"""Apply the Track 1 rare-and-damaging filter to a VEP-annotated TSV.

Keeps variants that are BOTH rare in the general population (max gnomAD
subpopulation AF below --max-af) AND predicted to alter the protein (VEP impact
in --impacts on the canonical transcript). This is the step that reduces the
~1,300-variant annotated panel to the handful of reportable candidates.

Usage:
    python3 filter_candidates.py --tsv data-notes/annotated/vep_panel_annotated.tsv

See pipeline/README.md for the full command sequence.
"""
import argparse
import csv
import sys

COLS = ["chrom", "pos", "ref", "alt", "gene", "consequence", "impact",
        "hgvsc", "hgvsp", "gnomad_max_af", "spliceai_max_ds", "clinvar_sig",
        "rsids", "genotype", "allele_depth", "genotype_qual"]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tsv", required=True, help="annotated TSV from vep_annotate.py")
    ap.add_argument("--max-af", type=float, default=0.001,
                    help="exclusive upper bound on max gnomAD AF (default: 0.001)")
    ap.add_argument("--impacts", default="MODERATE,HIGH",
                    help="comma-separated VEP impact levels to keep (default: MODERATE,HIGH)")
    ap.add_argument("--out", help="write candidates here (default: stdout)")
    args = ap.parse_args()

    impacts = {i.strip().upper() for i in args.impacts.split(",") if i.strip()}

    with open(args.tsv, newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    kept = []
    for row in rows:
        if row.get("impact", "").upper() not in impacts:
            continue
        try:
            af = float(row.get("gnomad_max_af") or 0.0)
        except ValueError:
            # An unparseable AF is treated as unknown, not as rare: skip rather
            # than risk promoting a common variant into the candidate list.
            continue
        if af < args.max_af:
            kept.append(row)

    out = open(args.out, "w", newline="") if args.out else sys.stdout
    try:
        w = csv.DictWriter(out, fieldnames=COLS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for row in kept:
            w.writerow(row)
    finally:
        if args.out:
            out.close()

    print(f"{len(kept)} of {len(rows)} variants pass "
          f"(gnomAD max AF < {args.max_af}, impact in {sorted(impacts)})",
          file=sys.stderr)


if __name__ == "__main__":
    main()
