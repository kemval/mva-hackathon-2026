#!/usr/bin/env python3
"""Measure the two pre-registered quantities on a replication node set.

P2 (direction of effect) is the claim that matters: what fraction of action-typed
drug entries around a locus are inhibitory. P1 and P3 concern drug counts at and
with distance from the causal gene.

Reports Open Targets action types and DGIdb interaction types separately, because
they are different vocabularies and merging them would hide disagreement.
"""
import argparse
import collections
import csv


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--drugs", required=True)
    ap.add_argument("--nodes", required=True)
    ap.add_argument("--gene", required=True)
    a = ap.parse_args()

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

    for src, field in (("opentargets", "action_type"), ("dgidb", "mechanism")):
        typed = [r for r in rows if r["source"] == src and (r.get(field) or "").strip()]
        if not typed:
            print(f"  {src}: no typed entries")
            continue
        c = collections.Counter((r[field] or "").upper() for r in typed)
        inh = sum(v for k, v in c.items() if "INHIB" in k or "ANTAGONIST" in k
                  or "BLOCKER" in k or "DEGRADER" in k)
        print(f"  P2 {src}: {inh}/{len(typed)} inhibitory ({100*inh/len(typed):.1f}%)")
        for k, v in c.most_common(6):
            print(f"      {v:5d}  {k[:60]}")

    d0 = [r for r in rows if tiers.get(r["gene"]) == "d0_defect"]
    d0t = [r for r in d0 if (r.get("action_type") or r.get("mechanism") or "").strip()]
    if d0t:
        c = collections.Counter((r.get("action_type") or r.get("mechanism") or "").upper()
                                for r in d0t)
        inh = sum(v for k, v in c.items() if "INHIB" in k or "ANTAGONIST" in k or "BLOCKER" in k)
        print(f"  P2 at the defect itself: {inh}/{len(d0t)} inhibitory "
              f"({100*inh/len(d0t):.1f}%) — {dict(c.most_common(6))}")
    else:
        print(f"  P2 at the defect itself: {len(d0)} drug rows, none action-typed")
    print()


if __name__ == "__main__":
    main()
