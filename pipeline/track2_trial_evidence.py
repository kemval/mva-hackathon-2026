#!/usr/bin/env python3
"""Query ClinicalTrials.gov (API v2) for human trial evidence per candidate.

Track 2's evidence step. For each candidate intervention, retrieves the trials
that have actually been run, and -- the question that matters most for this case
-- whether any of them enrolled children.

The paediatric question is answered from the structured eligibility fields
(minimumAge / stdAges) rather than from free text, because "children were
included" is exactly the kind of claim that is easy to assert and hard to check.
A trial counts as paediatric here only if its own eligibility module says so.

Output is one row per trial, plus a per-candidate summary on stderr.

Usage:
    python3 track2_trial_evidence.py \
        --candidates ../data-notes/track2_candidates.tsv \
        --out ../data-notes/track2_trials.tsv

See pipeline/README.md for the full command sequence.
"""
import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CTGOV = "https://clinicaltrials.gov/api/v2/studies"

FIELDS = ",".join([
    "NCTId", "BriefTitle", "OverallStatus", "Phase", "EnrollmentCount",
    "Condition", "InterventionName", "MinimumAge", "MaximumAge", "StdAge",
    "StartDate", "PrimaryCompletionDate",
])

COLS = ["candidate", "nct_id", "status", "phase", "enrollment", "min_age",
        "max_age", "std_ages", "paediatric", "conditions", "title"]


def fetch(query, page_size=100, retries=4, pause=3.0):
    params = urllib.parse.urlencode({
        "query.intr": query, "fields": FIELDS,
        "pageSize": str(page_size), "countTotal": "true",
    })
    url = f"{CTGOV}?{params}"
    req = urllib.request.Request(
        url, headers={"User-Agent": "mva-hackathon-2026 track2 trials"})
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as fh:
                return json.loads(fh.read().decode())
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            time.sleep(pause * (attempt + 1))
    raise RuntimeError(f"ClinicalTrials.gov failed for {query!r}: {last}")


def is_paediatric(elig):
    """True only if the trial's own eligibility module says children are eligible.

    Two independent signals are accepted: the CT.gov standard age bucket CHILD,
    or a minimum age stated in days/weeks/months, or in years below 18. Anything
    else -- including a missing minimumAge -- is treated as NOT paediatric,
    because absence of a stated minimum is not evidence that children were
    enrolled.
    """
    if "CHILD" in (elig.get("stdAges") or []):
        return True
    raw = (elig.get("minimumAge") or "").strip().lower()
    if not raw:
        return False
    parts = raw.split()
    if len(parts) != 2:
        return False
    try:
        value = float(parts[0])
    except ValueError:
        return False
    unit = parts[1].rstrip("s")
    if unit in ("day", "week", "month"):
        return True
    return unit == "year" and value < 18


def read_candidates(path):
    out = []
    with open(path) as fh:
        for line in fh:
            if not line.strip() or line.startswith("#"):
                continue
            if line.startswith("candidate\t"):
                continue
            out.append(line.rstrip("\n").split("\t")[0])
    return out


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--candidates", required=True,
                    help="TSV whose first column is the intervention name")
    ap.add_argument("--out", help="write the trial table here (default: stdout)")
    ap.add_argument("--pause", type=float, default=1.0)
    args = ap.parse_args()

    rows = []
    for cand in read_candidates(args.candidates):
        data = fetch(cand)
        total = data.get("totalCount", 0)
        studies = data.get("studies") or []
        n_paed = 0
        for st in studies:
            ps = st.get("protocolSection") or {}
            ident = ps.get("identificationModule") or {}
            status = ps.get("statusModule") or {}
            design = ps.get("designModule") or {}
            elig = ps.get("eligibilityModule") or {}
            cond = ps.get("conditionsModule") or {}
            paed = is_paediatric(elig)
            n_paed += bool(paed)
            rows.append({
                "candidate": cand,
                "nct_id": ident.get("nctId", ""),
                "status": status.get("overallStatus", ""),
                "phase": "/".join(design.get("phases") or []),
                "enrollment": (design.get("enrollmentInfo") or {}).get("count", ""),
                "min_age": elig.get("minimumAge", ""),
                "max_age": elig.get("maximumAge", ""),
                "std_ages": "/".join(elig.get("stdAges") or []),
                "paediatric": "yes" if paed else "no",
                "conditions": "; ".join((cond.get("conditions") or [])[:4]),
                "title": ident.get("briefTitle", ""),
            })
        print(f"  {cand:34} {total:5d} trials total, {len(studies):3d} retrieved, "
              f"{n_paed:3d} paediatric-eligible", file=sys.stderr)
        time.sleep(args.pause)

    out = open(args.out, "w", newline="") if args.out else sys.stdout
    try:
        w = csv.DictWriter(out, fieldnames=COLS, delimiter="\t",
                           extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)
    finally:
        if args.out:
            out.close()
    print(f"\n{len(rows)} trial rows written", file=sys.stderr)


if __name__ == "__main__":
    main()
