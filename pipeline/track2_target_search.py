#!/usr/bin/env python3
"""Query Open Targets and DGIdb for drugs acting on a set of pathway nodes.

Track 2's search step. Takes the pathway node table (symbol, Ensembl ID, tier,
rationale) fixed in data-notes/regions/track2_pathway_nodes.tsv and, for each
node, asks two independent drug-target databases what approved or clinical-stage
compounds act on it. Emits one row per (gene, drug, source) pair.

Two databases are queried rather than one because they draw on different
underlying sources; agreement between them is the only cheap check available on
either. Where they disagree, the report says so rather than silently merging.

Open Targets also returns a `tractability` assessment per target, which is
recorded because a target with zero drugs is a different finding depending on
whether it is chemically tractable (nobody has made one) or intractable (nobody
can). For BUB1B specifically, this distinction is the point: it is flagged
small-molecule tractable, but any small molecule would be an INHIBITOR, and the
defect is a protein deficiency -- so tractability here does not imply a therapy.

Every raw API response is appended to --raw-log so that results can be re-derived
offline without re-querying, in the same spirit as the Track 1 VEP response log.

Usage:
    python3 track2_target_search.py \
        --nodes ../data-notes/regions/track2_pathway_nodes.tsv \
        --out ../data-notes/track2_target_drugs.tsv \
        --raw-log ../data-notes/track2_search_raw.jsonl

See pipeline/README.md for the full command sequence.
"""
import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request

OPENTARGETS = "https://api.platform.opentargets.org/api/v4/graphql"
DGIDB = "https://dgidb.org/api/graphql"

# Field names verified live against each schema on 2026-09-02. Open Targets
# renamed the drug collection from `knownDrugs` to `drugAndClinicalCandidates`;
# querying the old name returns a hard GraphQL error, so a failure here means
# the schema moved again rather than that a target has no drugs.
OT_QUERY = """
query($ensemblId: String!) {
  target(ensemblId: $ensemblId) {
    approvedSymbol
    tractability { label modality value }
    drugAndClinicalCandidates {
      count
      rows { drug { id name drugType maximumClinicalStage
                    mechanismsOfAction { rows { mechanismOfAction actionType } } } }
    }
  }
}
"""

DGIDB_QUERY = """
query($names: [String!]!) {
  genes(names: $names) {
    nodes {
      name
      interactions {
        drug { name conceptId approved }
        interactionScore
        interactionTypes { type directionality }
      }
    }
  }
}
"""

COLS = ["gene", "tier", "source", "drug", "drug_id", "drug_type",
        "max_clinical_stage", "approved", "mechanism", "action_type"]


def post(url, payload, retries=4, pause=3.0):
    """POST JSON with backoff. Raises on final failure rather than returning
    an empty result, so a network problem is never mistaken for 'no drugs'."""
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=body,
        headers={"Content-Type": "application/json",
                 "User-Agent": "mva-hackathon-2026 track2 search"})
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as fh:
                return json.loads(fh.read().decode())
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(pause * (attempt + 1))
    raise RuntimeError(f"{url} failed after {retries} attempts: {last}")


def read_nodes(path):
    nodes = []
    with open(path) as fh:
        for line in fh:
            if not line.strip() or line.startswith("#") or line.startswith("symbol\t"):
                continue
            symbol, ensembl_id, tier, rationale = line.rstrip("\n").split("\t")
            nodes.append({"symbol": symbol, "ensembl_id": ensembl_id,
                          "tier": tier, "rationale": rationale})
    return nodes


def log_raw(fh, source, key, payload):
    if fh:
        fh.write(json.dumps({"source": source, "key": key, "response": payload}) + "\n")


def query_open_targets(node, raw_fh):
    """Returns (rows, tractability_labels, drug_count)."""
    data = post(OPENTARGETS, {"query": OT_QUERY,
                              "variables": {"ensemblId": node["ensembl_id"]}})
    log_raw(raw_fh, "opentargets", node["symbol"], data)
    if "errors" in data:
        raise RuntimeError(f"Open Targets rejected the query for "
                           f"{node['symbol']}: {data['errors']}")
    target = (data.get("data") or {}).get("target")
    if target is None:
        raise RuntimeError(f"Open Targets returned no target for "
                           f"{node['symbol']} ({node['ensembl_id']})")

    tract = [f"{t['modality']}:{t['label']}"
             for t in (target.get("tractability") or []) if t.get("value")]

    candidates = target.get("drugAndClinicalCandidates") or {}
    rows = []
    for row in candidates.get("rows") or []:
        drug = row.get("drug") or {}
        moas = ((drug.get("mechanismsOfAction") or {}).get("rows")) or [{}]
        for moa in moas:
            rows.append({
                "gene": node["symbol"], "tier": node["tier"],
                "source": "opentargets",
                "drug": drug.get("name", ""), "drug_id": drug.get("id", ""),
                "drug_type": drug.get("drugType", ""),
                "max_clinical_stage": drug.get("maximumClinicalStage", ""),
                "approved": "",  # Open Targets exposes stage, not an approval flag
                "mechanism": moa.get("mechanismOfAction", ""),
                "action_type": moa.get("actionType", ""),
            })
    return rows, tract, candidates.get("count", 0)


def query_dgidb(nodes, raw_fh):
    names = [n["symbol"] for n in nodes]
    tier_of = {n["symbol"]: n["tier"] for n in nodes}
    data = post(DGIDB, {"query": DGIDB_QUERY, "variables": {"names": names}})
    log_raw(raw_fh, "dgidb", ",".join(names), data)
    if "errors" in data:
        raise RuntimeError(f"DGIdb rejected the query: {data['errors']}")

    rows = []
    seen_genes = set()
    for gene in ((data.get("data") or {}).get("genes") or {}).get("nodes") or []:
        seen_genes.add(gene["name"])
        for inter in gene.get("interactions") or []:
            drug = inter.get("drug") or {}
            types = inter.get("interactionTypes") or [{}]
            for t in types:
                rows.append({
                    "gene": gene["name"], "tier": tier_of.get(gene["name"], ""),
                    "source": "dgidb",
                    "drug": drug.get("name", ""),
                    "drug_id": drug.get("conceptId", ""),
                    "drug_type": "",
                    "max_clinical_stage": "",
                    "approved": str(drug.get("approved", "")),
                    "mechanism": t.get("type") or "",
                    "action_type": t.get("directionality") or "",
                })
    missing = sorted(set(names) - seen_genes)
    return rows, missing


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--nodes", required=True, help="pathway node TSV")
    ap.add_argument("--out", help="write the drug table here (default: stdout)")
    ap.add_argument("--raw-log", help="append every raw API response here (JSONL)")
    ap.add_argument("--pause", type=float, default=1.0,
                    help="seconds between Open Targets calls (default: 1.0)")
    args = ap.parse_args()

    nodes = read_nodes(args.nodes)
    raw_fh = open(args.raw_log, "a") if args.raw_log else None

    all_rows = []
    tractability = {}
    zero_drug_genes = []
    try:
        for node in nodes:
            rows, tract, count = query_open_targets(node, raw_fh)
            all_rows.extend(rows)
            tractability[node["symbol"]] = tract
            if count == 0:
                zero_drug_genes.append(node["symbol"])
            print(f"  opentargets {node['symbol']:9} {count:4d} candidates  "
                  f"tractability: {', '.join(tract) or 'none'}", file=sys.stderr)
            time.sleep(args.pause)

        dg_rows, missing = query_dgidb(nodes, raw_fh)
        all_rows.extend(dg_rows)
        print(f"  dgidb        {len(dg_rows)} interaction rows across "
              f"{len(nodes) - len(missing)} genes", file=sys.stderr)
        if missing:
            print(f"  dgidb        no record for: {', '.join(missing)}", file=sys.stderr)
    finally:
        if raw_fh:
            raw_fh.close()

    out = open(args.out, "w", newline="") if args.out else sys.stdout
    try:
        # lineterminator is explicit: csv defaults to \r\n, which silently
        # appends a carriage return to the final column and breaks downstream
        # field comparisons (an awk `$10=="ACTIVATING"` test matched nothing
        # until this was found). Unix endings, always.
        w = csv.DictWriter(out, fieldnames=COLS, delimiter="\t",
                           extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in sorted(all_rows, key=lambda r: (r["gene"], r["source"], r["drug"])):
            w.writerow(row)
    finally:
        if args.out:
            out.close()

    print(f"\n{len(all_rows)} gene-drug rows written", file=sys.stderr)
    if zero_drug_genes:
        print(f"Open Targets returned ZERO drugs for: "
              f"{', '.join(zero_drug_genes)}", file=sys.stderr)
        for g in zero_drug_genes:
            print(f"    {g}: tractability = "
                  f"{', '.join(tractability[g]) or 'none'}", file=sys.stderr)


if __name__ == "__main__":
    main()
