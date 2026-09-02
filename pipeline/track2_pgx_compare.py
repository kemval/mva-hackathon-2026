#!/usr/bin/env python3
"""Compare PharmCAT gene calls between the strict and missing-to-ref runs.

The difference between the two is the honest output of a pharmacogenomic screen run
against a variants-only VCF. Any gene whose call appears only under --missing-to-ref
rests on the assumption that a position absent from the file is homozygous reference --
which, with no reference blocks in the VCF, is not established.

Prints a per-gene comparison and the count of genes that change.

Usage:
    python3 track2_pgx_compare.py --strict <strict.phenotype.json> \
                                  --missing-to-ref <mtr.phenotype.json>
"""
import argparse
import json


def gene_calls(path):
    """Extract {gene: (diplotype label, phenotype, n_uncalled_haplotypes)}.

    Reads recommendationDiplotypes, falling back to sourceDiplotypes. Note that the
    `called` and `reportable` fields are null in PharmCAT 3.4 output and must not be
    used to decide whether a gene was called.
    """
    data = json.load(open(path))
    out = {}
    for gene, report in data["geneReports"].items():
        dips = (report.get("recommendationDiplotypes")
                or report.get("sourceDiplotypes") or [])
        if not dips:
            out[gene] = ("NOT CALLED", "", 0)
            continue
        labels = []
        for d in dips:
            a1, a2 = d.get("allele1"), d.get("allele2")
            if a1 and a2:
                labels.append(f"{a1['name']}/{a2['name']}")
            elif d.get("label"):
                labels.append(d["label"])
        phenos = sorted({p for d in dips for p in (d.get("phenotypes") or [])})
        out[gene] = ("; ".join(labels) or "(no diplotype)", "; ".join(phenos),
                     len(report.get("uncalledHaplotypes") or []))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", required=True)
    ap.add_argument("--missing-to-ref", required=True, dest="mtr")
    args = ap.parse_args()

    a, b = gene_calls(args.strict), gene_calls(args.mtr)
    genes = sorted(set(a) | set(b))
    changed = []

    print(f"{'gene':10} | {'STRICT':24} | {'MISSING->REF':24} | phenotype")
    print("-" * 100)
    for g in genes:
        x = a.get(g, ("-", "", 0))
        y = b.get(g, ("-", "", 0))
        if x[0] != y[0]:
            changed.append(g)
        flag = "  <<< CHANGES" if x[0] != y[0] else ""
        print(f"{g:10} | {x[0][:23]:24} | {y[0][:23]:24} | {y[1][:30]}{flag}")

    print(f"\n{len(changed)} of {len(genes)} genes change call when absent positions "
          f"are assumed reference.")
    if changed:
        print("  " + ", ".join(changed))
        print("\nAny call appearing only in the right-hand column is an artefact of that "
              "assumption, NOT a measurement. It must not be reported as a "
              "pharmacogenomic result.")


if __name__ == "__main__":
    main()
