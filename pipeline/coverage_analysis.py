#!/usr/bin/env python3
"""Measure what the sites-only VCF could only disclaim.

The Track 1 report carries one limitation under every negative result it
states: the input is a sites-only VCF, so absence of a call and absence of
coverage are indistinguishable. Call density against flanking sequence was used
as a proxy, with the proxy's weakness stated plainly. Given an alignment this
stops being a proxy.

Three questions, in the order the report needs them answered:

  1. CALLABILITY. What fraction of each gene is covered at or above a usable
     depth? This turns "no rare damaging variant found in CEP57" into either
     "and the gene was 98% callable" or "and a quarter of it was never read".

  2. THE FIVE DELETION WINDOWS. The report bounds a multi-exon BUB1B deletion
     to five intervals between heterozygous calls, the largest containing exons
     9-16, and names that the leading alternative second allele. A hemizygous
     deletion halves read depth. Each window is compared against the gene's own
     diploid baseline, so a real drop shows up as a ratio near 0.5.

  3. DEPTH PROFILE across BUB1B, so the two homozygous-alternate calls inside
     the exon 9-16 window -- formally consistent with hemizygosity -- can be
     read against their local coverage rather than against the genome.

Usage:
    python3 coverage_analysis.py --bam data-notes/raw/<name>.slice.bam
    python3 coverage_analysis.py --bam <bam> --min-depth 10 --out coverage.tsv

Requires samtools. See pipeline/README.md for the retrieval step.
"""
import argparse
import shutil
import statistics
import subprocess
import sys

# Padded gene bodies, matching data-notes/regions/*.tsv (+/-2 kb).
GENES = {
    "BUB1B":  ("15", 40158984, 40223137),
    "CEP57":  ("11", 95787965, 95839070),
    "TRIP13": ("5",    890849,   921357),
}
# Intervals between heterozygous calls where a multi-exon deletion is not excluded.
# From the report's "Limitations of scope" section.
WINDOWS = [
    (40160984, 40168264, "exons 1-2"),
    (40168264, 40181093, "exons 3-5"),
    (40182809, 40192892, "exons 6-8"),
    (40192892, 40209701, "exons 9-16"),
    (40209701, 40216470, "exons 18-20"),
]
BUB1B_GENE = (40160984, 40221137)


def depths(bam, chrom, start, end, min_mapq):
    """Per-base depth over a region. Returns {pos: depth}; uncovered bases absent."""
    cmd = ["samtools", "depth", "-a", "-Q", str(min_mapq),
           "-r", f"{chrom}:{start}-{end}", bam]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"samtools depth failed: {out.stderr.strip()}")
    d = {}
    for line in out.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) == 3:
            d[int(parts[1])] = int(parts[2])
    return d


def summarise(d, lo, hi, min_depth):
    span = hi - lo + 1
    vals = [d.get(p, 0) for p in range(lo, hi + 1)]
    covered = [v for v in vals if v >= min_depth]
    return {
        "span": span,
        "callable_frac": len(covered) / span if span else 0.0,
        "median": statistics.median(vals) if vals else 0,
        "mean": statistics.mean(vals) if vals else 0.0,
        "zero_frac": sum(1 for v in vals if v == 0) / span if span else 0.0,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bam", required=True, help="alignment slice from fetch_alignment_slice.sh")
    ap.add_argument("--min-depth", type=int, default=10,
                    help="depth at or above which a base counts as callable (default: 10)")
    ap.add_argument("--min-mapq", type=int, default=20,
                    help="minimum mapping quality (default: 20)")
    ap.add_argument("--out", help="write the per-window table here (default: stdout)")
    args = ap.parse_args()

    if not shutil.which("samtools"):
        sys.exit("samtools not found")

    lines = []
    lines.append("# 1. Callability per gene "
                 f"(callable = depth >= {args.min_depth} at MAPQ >= {args.min_mapq})")
    lines.append("gene\tspan_bp\tcallable_frac\tzero_frac\tmedian_depth")
    bub = None
    for gene, (chrom, lo, hi) in GENES.items():
        d = depths(args.bam, chrom, lo, hi, args.min_mapq)
        if gene == "BUB1B":
            bub = d
        if not d:
            lines.append(f"{gene}\t{hi-lo+1}\tNO DATA\t-\t-  "
                         f"# region absent from this slice")
            continue
        s = summarise(d, lo, hi, args.min_depth)
        lines.append(f"{gene}\t{s['span']}\t{s['callable_frac']:.4f}\t"
                     f"{s['zero_frac']:.4f}\t{s['median']:.0f}")

    if bub:
        base = summarise(bub, *BUB1B_GENE, args.min_depth)["median"]
        lines.append("")
        lines.append("# 2. Deletion windows vs the BUB1B diploid baseline "
                     f"(gene median depth = {base:.0f})")
        lines.append("# A hemizygous deletion halves depth: expect ratio ~0.5, not ~1.0.")
        lines.append("window\texons\tspan_bp\tmedian_depth\tratio_to_gene\tverdict")
        for lo, hi, label in WINDOWS:
            s = summarise(bub, lo, hi, args.min_depth)
            ratio = (s["median"] / base) if base else float("nan")
            verdict = ("DELETION LIKELY" if ratio < 0.65 else
                       "no depth loss" if ratio > 0.85 else "EQUIVOCAL")
            lines.append(f"{lo}-{hi}\t{label}\t{s['span']}\t{s['median']:.0f}\t"
                         f"{ratio:.2f}\t{verdict}")
        lines.append("")
        lines.append("# 3. BUB1B depth profile, 1 kb bins")
        lines.append("bin_start\tmedian_depth")
        lo, hi = BUB1B_GENE
        for b in range(lo, hi, 1000):
            vals = [bub.get(p, 0) for p in range(b, min(b + 1000, hi + 1))]
            if vals:
                lines.append(f"{b}\t{statistics.median(vals):.0f}")

    text = "\n".join(lines) + "\n"
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(text)
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
