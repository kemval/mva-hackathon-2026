#!/usr/bin/env python3
"""Measure the two pre-registered quantities on a replication node set.

P2 (direction of effect) is the claim that matters: what fraction of drug entries
around a locus are inhibitory. P1 and P3 concern drug counts at and with distance
from the causal gene.

COUNTING UNIT -- this is the whole point of the file and it is stated rather than
implied. An "entry" is a unique (gene, drug, action_type) triple, which is the unit
the Track 2 report's own 129/142 figure uses. An earlier version of this script
counted raw rows, which inflated every percentage by 1-15 points and, worse, was
placed beside the report's triple-based figure as if the two were comparable. They
were not. Run --selfcheck to confirm this file reproduces the report's own number
before trusting it on anything else.

Two inhibitory tallies are reported because the report reports two: STRICT counts
only INHIBITOR/INHIBITORY (the 129 of 129/142); BROAD adds antisense and RNAi
inhibitors, antagonists and blockers (the report's "~95%").
"""
import argparse
import collections
import csv
import sys

BROAD_EXTRA = ("ANTISENSE INHIBITOR", "RNAI INHIBITOR", "ANTAGONIST", "BLOCKER", "DEGRADER")
STRICT = ("INHIBITOR", "INHIBITORY")


def action_of(row):
    """Open Targets carries action_type; DGIdb carries the same idea in mechanism."""
    return (row.get("action_type") or row.get("mechanism") or "").strip().upper()


def tally(rows):
    """Unique (gene, drug, action) triples -> (n, strict, broad, Counter)."""
    seen = {}
    for r in rows:
        a = action_of(r)
        if a:
            seen[(r["gene"], r["drug"], a)] = a
    c = collections.Counter(seen.values())
    n = len(seen)
    strict = sum(v for k, v in c.items() if k in STRICT)
    broad = strict + sum(v for k, v in c.items()
                         if k not in STRICT and (k in BROAD_EXTRA or "INHIB" in k))
    return n, strict, broad, c


def pct(a, b):
    return f"{100*a/b:.1f}%" if b else "n/a"


def load_tiers(path):
    tiers = {}
    for line in open(path):
        if line.startswith("#"):
            continue
        f = line.rstrip("\n").split("\t")
        if not f or f[0] == "symbol":
            continue
        tiers[f[0]] = f[2]
    return tiers


def selfcheck(path):
    """Reproduce the Track 2 report's own 129/142 before trusting this file elsewhere.

    If this fails, the replication is not measuring what the report measures and no
    percentage it emits should be compared with one in the report.
    """
    rows = [r for r in csv.DictReader(open(path), delimiter="\t")
            if r["source"] == "opentargets"]
    n, strict, broad, c = tally(rows)
    ok = (n == 142 and strict == 129)
    print(f"selfcheck against {path}")
    print(f"  unique (gene,drug,action) triples : {n}   expected 142")
    print(f"  strict INHIBITOR                  : {strict}   expected 129")
    print(f"  broad inhibitory                  : {broad} ({pct(broad, n)})   report says ~95%")
    print(f"  ACTIVATOR={c.get('ACTIVATOR',0)} STABILISER={c.get('STABILISER',0)}"
          f"   report says exactly one of each")
    print("  RESULT:", "PASS — same counting unit as the report" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--drugs")
    ap.add_argument("--nodes")
    ap.add_argument("--gene")
    ap.add_argument("--selfcheck", metavar="TSV",
                    help="reproduce the report's 129/142 from the original search TSV")
    a = ap.parse_args()

    if a.selfcheck:
        sys.exit(selfcheck(a.selfcheck))
    if not (a.drugs and a.nodes and a.gene):
        ap.error("--drugs, --nodes and --gene are required unless --selfcheck is used")

    tiers = load_tiers(a.nodes)
    rows = list(csv.DictReader(open(a.drugs), delimiter="\t"))

    print(f"### {a.gene}")
    uniq = collections.defaultdict(set)
    for r in rows:
        uniq[tiers.get(r["gene"], "?")].add(r["drug"])
    counts = {t: len(uniq[t]) for t in ("d0_defect", "d1_direct", "d2_pathway")}
    print(f"  P1/P3 unique drugs by distance: "
          f"d0={counts['d0_defect']}  d1={counts['d1_direct']}  d2={counts['d2_pathway']}")
    mono = counts["d0_defect"] <= counts["d1_direct"] <= counts["d2_pathway"]
    print(f"  P3 monotonic rise with distance: {'YES' if mono else 'NO'}")

    for src in ("opentargets", "dgidb"):
        n, strict, broad, c = tally([r for r in rows if r["source"] == src])
        if not n:
            print(f"  P2 {src}: no typed entries")
            continue
        print(f"  P2 {src}: {n} unique (gene,drug,action) triples — "
              f"strict {strict} ({pct(strict,n)}), broad {broad} ({pct(broad,n)})")
        for k, v in c.most_common(6):
            print(f"      {v:5d}  {k[:56]}")

    d0 = [r for r in rows if tiers.get(r["gene"]) == "d0_defect"]
    n, strict, broad, c = tally(d0)
    if n:
        print(f"  P2 at the defect itself: {n} typed triples — "
              f"strict {strict} ({pct(strict,n)}), broad {broad} ({pct(broad,n)})"
              f"  {dict(c.most_common(6))}")
    else:
        print(f"  P2 at the defect itself: {len(d0)} drug rows, NONE action-typed "
              f"— direction there is unknown, not favourable")
    print()


if __name__ == "__main__":
    main()
