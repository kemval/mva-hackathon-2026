#!/usr/bin/env python3
"""Build a distance-tiered pathway node table for any causal gene.

Implements the tier rule pre-registered in pipeline/scalability_prediction.md:
distance 0 is the causal gene, distance 1 its STRING high-confidence partners,
distance 2 the partners of those. Emits the same four-column schema
track2_target_search.py already consumes, so the replication runs through the
identical code path as the original BUB1B search.

Tiers are assigned by rule rather than curated, because curation is the obvious
objection to a generalisation drawn from a hand-picked gene set.

Usage:
    python3 build_node_set.py --gene NPC1 --out ../data-notes/regions/scale_npc1_nodes.tsv
"""
import argparse
import csv
import json
import sys
import time
import urllib.parse
import urllib.request

STRING = "https://string-db.org/api/json/interaction_partners"
ENSEMBL = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/"
SCORE_CUTOFF = 700          # STRING "high confidence", pre-registered
TIER_CAP = 25               # pre-registered, so a hub cannot swamp a tier


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mva-hackathon-2026"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def partners(symbols):
    """STRING high-confidence partners of a set of symbols, as {symbol: summed score}."""
    q = urllib.parse.urlencode({
        "identifiers": "%0d".join(symbols),
        "species": 9606,
        "required_score": SCORE_CUTOFF,
        # STRING's interaction_partners endpoint silently defaults to 10 partners per
        # protein. Left implicit, that would have capped tier 1 at 10 and quietly broken
        # the 25-per-tier rule pre-registered in scalability_prediction.md, so it is set
        # explicitly. Caught by noticing every tier 1 came back at exactly 10.
        "limit": TIER_CAP,
        "caller_identity": "mva-hackathon-2026",
    })
    out = {}
    for row in get(f"{STRING}?{q}"):
        for key in ("preferredName_A", "preferredName_B"):
            name = row[key]
            if name not in symbols:
                out[name] = out.get(name, 0.0) + float(row["score"])
    return out


def ensembl_id(symbol):
    """Resolve a gene symbol to an Ensembl gene ID.

    STRING's preferred names lag HGNC, so the direct symbol lookup misses renamed
    genes (GBA -> GBA1, SLC9A3R1 -> NHERF1). Falling back to the xrefs endpoint,
    which resolves synonyms, keeps those nodes in the search space instead of
    silently dropping them. Caught when the drug search raised on GBA and
    SLC9A3R1 rather than reporting them as zero-drug targets.
    """
    try:
        return get(f"{ENSEMBL}{symbol}?content-type=application/json")["id"]
    except Exception:
        pass
    for attempt in range(3):
        try:
            xr = get(f"https://rest.ensembl.org/xrefs/symbol/homo_sapiens/"
                     f"{symbol}?content-type=application/json")
            genes = [x["id"] for x in xr if x.get("type") == "gene"]
            if genes:
                return genes[0]
            return ""
        except Exception:
            time.sleep(2)
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gene", required=True, help="causal gene symbol (distance 0)")
    ap.add_argument("--out", help="write the node TSV here (default: stdout)")
    ap.add_argument("--pause", type=float, default=1.0)
    a = ap.parse_args()

    d1 = partners([a.gene])
    d1_syms = [s for s, _ in sorted(d1.items(), key=lambda kv: -kv[1])[:TIER_CAP]]
    time.sleep(a.pause)

    d2 = partners([a.gene] + d1_syms) if d1_syms else {}
    seen = set([a.gene]) | set(d1_syms)
    d2_syms = [s for s, _ in sorted(d2.items(), key=lambda kv: -kv[1])
               if s not in seen][:TIER_CAP]

    rows = [(a.gene, "d0_defect", "the deficient protein; searched first to establish the negative")]
    rows += [(s, "d1_direct", f"STRING high-confidence partner of {a.gene}") for s in d1_syms]
    rows += [(s, "d2_pathway", f"STRING partner-of-partner, distance 2 from {a.gene}") for s in d2_syms]

    fh = open(a.out, "w", newline="") if a.out else sys.stdout
    fh.write(f"# Distance-tiered node set for {a.gene}, built by pipeline/build_node_set.py\n")
    fh.write(f"# Rule pre-registered in pipeline/scalability_prediction.md: STRING v12,\n")
    fh.write(f"# Homo sapiens, combined score >= {SCORE_CUTOFF}, {TIER_CAP} per tier by score.\n")
    fh.write(f"# Built {time.strftime('%Y-%m-%d')}. Not curated.\n")
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["symbol", "ensembl_id", "tier", "rationale"])
    for sym, tier, why in rows:
        w.writerow([sym, ensembl_id(sym), tier, why])
        time.sleep(0.1)
    if a.out:
        fh.close()
        print(f"{a.gene}: {len(rows)} nodes -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
