#!/usr/bin/env python3
"""Apply the pre-registered Track 2 rubric to the scored candidate table.

The judgement lives in data-notes/track2_scores.tsv, where every axis score
carries a written justification. This script does only the mechanical part:
enforce the hard gates, sum the axes, apply the declared tie-break order, and
emit the two rankings the rubric requires -- the full ranking, and the
approved-medications-only shortlist that answers the brief literally.

Keeping the arithmetic in code and the judgement in a reviewable table is the
point: a reader can disagree with any single score and recompute, and no
candidate can be promoted by an undocumented thumb on the scale.

Tie-break order is fixed by the rubric: axis B (evidence), then D (case-specific
safety), then A (mechanistic directness).

Usage:
    python3 track2_score_candidates.py \
        --scores ../data-notes/track2_scores.tsv \
        --candidates ../data-notes/track2_candidates.tsv \
        --out ../data-notes/track2_ranking.tsv

See pipeline/README.md for the full command sequence.
"""
import argparse
import csv
import sys

AXES = ["A", "B", "C", "D", "E"]
COLS = ["rank", "candidate", "tier", "regulatory", "total",
        "A", "B", "C", "D", "E", "gate", "status"]


def read_tsv(path):
    rows = []
    with open(path) as fh:
        lines = [ln for ln in fh if not ln.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        rows.append(row)
    return rows


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scores", required=True)
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--out")
    args = ap.parse_args()

    meta = {r["candidate"]: r for r in read_tsv(args.candidates)}
    scored = read_tsv(args.scores)

    passing, gated = [], []
    for row in scored:
        name = row["candidate"]
        info = meta.get(name)
        if info is None:
            print(f"WARNING: {name!r} scored but absent from the candidate "
                  f"table -- skipped", file=sys.stderr)
            continue
        gate = (row.get("gate") or "").strip()
        rec = {"candidate": name, "tier": info["tier"],
               "regulatory": info["regulatory"], "gate": gate}
        if gate:
            rec.update({ax: "" for ax in AXES})
            rec["total"] = ""
            rec["status"] = f"EXCLUDED by gate {gate}"
            gated.append(rec)
            continue
        vals = {ax: int(row[ax]) for ax in AXES}
        rec.update(vals)
        rec["total"] = sum(vals.values())
        rec["status"] = "ranked"
        passing.append(rec)

    # Rubric-declared ordering: total desc, then B, then D, then A.
    passing.sort(key=lambda r: (-r["total"], -r["B"], -r["D"], -r["A"]))
    for i, rec in enumerate(passing, 1):
        rec["rank"] = i
    for rec in gated:
        rec["rank"] = ""

    out = open(args.out, "w", newline="") if args.out else sys.stdout
    try:
        w = csv.DictWriter(out, fieldnames=COLS, delimiter="\t",
                           extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for rec in passing + gated:
            w.writerow(rec)
    finally:
        if args.out:
            out.close()

    print("\nFULL RANKING", file=sys.stderr)
    for r in passing:
        print(f"  {r['rank']:2d}. {r['candidate']:30} {r['total']:3d}  "
              f"[{r['regulatory']:15}] {r['tier']}", file=sys.stderr)

    approved = [r for r in passing if r["regulatory"] == "approved_drug"]
    print("\nAPPROVED MEDICATIONS ONLY (the brief's literal ask)", file=sys.stderr)
    for i, r in enumerate(approved, 1):
        print(f"  {i}. {r['candidate']:30} {r['total']:3d}  {r['tier']}",
              file=sys.stderr)

    print("\nEXCLUDED BY GATE", file=sys.stderr)
    for r in gated:
        print(f"  {r['candidate']:30} {r['status']}", file=sys.stderr)

    if passing:
        top = passing[0]
        print(f"\nHighest overall: {top['candidate']} ({top['total']}), "
              f"regulatory status: {top['regulatory']}", file=sys.stderr)
        if approved and approved[0]["candidate"] != top["candidate"]:
            print(f"Highest APPROVED DRUG: {approved[0]['candidate']} "
                  f"({approved[0]['total']}) -- these differ, which the report "
                  f"must address rather than conflate", file=sys.stderr)


if __name__ == "__main__":
    main()
