#!/usr/bin/env python3
"""Fail loudly when the submission's cross-file claims drift out of sync.

Written because the 2026-09-04 Track 2 audit found that *every number* in the
report reproduced from the artefacts, while six prose claims had gone stale --
three of them because a correction the report made to itself never reached the
files that quote it (the methods-description form, the README, the explainer).

The figures that were already checked by a script (the 129/142 selfcheck, the
pitch script's own word counter) were all correct. So the fix is not another
hand-copied number: it is to put the hand-copied ones under a check too.

Two classes are enforced:

  WITHDRAWN  a claim this project has withdrawn must not be stated as live in
             any reader-facing file. It may still appear inside the paragraph
             that retracts it -- that is how a withdrawal is written -- so a
             match is a failure only when its own block carries no retraction
             marker. The verification table and _pending_edits.md are exempt
             entirely: quoting withdrawn text is what they are for.

  DERIVED    a number quoted in one file must equal the source it names.

Usage:  python3 pipeline/check_consistency.py [--root .]
Exit 0 if everything agrees, 1 otherwise.
"""
import argparse
import pathlib
import re
import subprocess
import sys

# Files a judge, clinician or family actually reads. Records of past error
# (Part 11 of the report, _pending_edits.md) are deliberately not here.
READER_FACING = [
    "README.md",
    "submissions/methods_description.md",
    "submissions/track2/gummietech_track2_report.md",
    "submissions/track2/clinician_onepager.md",
    "submissions/track2/pitch_script.md",
    "submissions/track2/notes_for_judges.md",
    "submissions/track1/gummietech_track1_report.md",
    "data-notes/track2_mechanism.md",
    "viz/track2_explainer.html",
    "viz/pitch_deck.html",
]

# (regex, what was withdrawn and where the current position lives)
WITHDRAWN = [
    (r"congenital onset raises",
     "Track 1 withdrew the inference that congenital onset raises the monogenic "
     "prior; both readings are live (matrix C13)"),
    (r"rises monotonically with distance",
     "P3 failed: monotonic rise did not survive a mechanical STRING tier rule, "
     "failing for BUB1B itself (data-notes/scale/RESULTS.md)"),
    (r"fact about every loss-of-function",
     "P2 failed at NPC1 (54.5% vs a predicted >=80%); the generalisation is "
     "withdrawn (data-notes/scale/RESULTS.md)"),
    (r"lowest minimum age",
     "refuted by our own trial table: navitoclax has six paediatric-eligible "
     "trials with minimum ages down to 1 year (data-notes/track2_trials.tsv)"),
]


# A block that contains one of these is retracting the claim, not asserting it.
RETRACTION = re.compile(
    r"withdraw|withdrawn|superseded|refut|is false|not true|no longer|"
    r"an artefact of|corrected|failed|overclaim|too strong",
    re.I,
)


def blocks(text):
    """Split into paragraph-sized units, so a retraction is judged in context."""
    return [b for b in re.split(r"\n\s*\n|</p>|</div>", text) if b.strip()]


def strip_records(path, text):
    """Drop the sections whose job is to quote withdrawn text."""
    if path.name == "gummietech_track2_report.md":
        return text.split("## Part 11")[0]
    if path.name == "gummietech_track1_report.md":
        # Track 1's own audit trail quotes its withdrawn wording the same way.
        return re.sub(r"(?ms)^\|.*?\|$", "", text)
    return text


def check_withdrawn(root, fails):
    for rel in READER_FACING:
        path = root / rel
        if not path.exists():
            continue
        body = strip_records(path, path.read_text())
        for block in blocks(body):
            if RETRACTION.search(block):
                continue
            for pattern, why in WITHDRAWN:
                if re.search(pattern, block):
                    fails.append(
                        f"{rel}: withdrawn claim /{pattern}/ is asserted, with no "
                        f"retraction in its own paragraph -- {why}")


def check_derived(root, fails):
    report = (root / "submissions/track2/gummietech_track2_report.md").read_text()
    judges = (root / "submissions/track2/notes_for_judges.md").read_text()
    methods = (root / "submissions/methods_description.md").read_text()
    readme = (root / "README.md").read_text()
    script = root / "submissions/track2/pitch_script.md"

    rows = len(re.findall(r"(?m)^\| \d+ \|", report.split("## Part 11")[1]))
    m = re.search(r"verification table lists (\d+) findings", judges)
    if not m:
        fails.append("notes_for_judges.md: verification-count sentence not found")
    elif int(m.group(1)) != rows:
        fails.append(f"notes_for_judges.md: says {m.group(1)} findings, "
                     f"Part 11 has {rows}")

    spoken = sum(len(line[2:].split())
                 for line in script.read_text().splitlines()
                 if line.startswith("> "))
    if f"{spoken} spoken words" not in readme:
        fails.append(f"README.md: pitch script is {spoken} spoken words; "
                     "the README quotes a different figure")

    commits = subprocess.run(["git", "-C", str(root), "rev-list", "--count", "HEAD"],
                             capture_output=True, text=True).stdout.strip()
    if commits and f"{commits} commits" not in methods:
        fails.append(f"methods_description.md: repository has {commits} commits; "
                     "the form quotes a different figure")

    for i, m in enumerate(re.finditer(r"^### Method abstract.*?\n(.*?)(?=^### |^# |\Z)",
                                      methods, re.S | re.M), start=1):
        n = len(m.group(1).split())
        if n > 500:
            fails.append(f"methods_description.md: abstract {i} is {n} words "
                         "against the form's 500-word limit")

    out = subprocess.run([sys.executable, str(root / "pipeline/scale_measure.py"),
                          "--selfcheck", str(root / "data-notes/track2_target_drugs.tsv")],
                         capture_output=True, text=True)
    if "PASS" not in out.stdout:
        fails.append("scale_measure.py --selfcheck did not pass: the report's "
                     "129/142 no longer re-derives from the artefacts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=pathlib.Path(__file__).resolve().parent.parent)
    args = ap.parse_args()
    root = pathlib.Path(args.root)

    fails = []
    check_withdrawn(root, fails)
    check_derived(root, fails)

    if fails:
        print(f"FAIL — {len(fails)} inconsistenc"
              f"{'y' if len(fails) == 1 else 'ies'}:")
        for f in fails:
            print(f"  - {f}")
        return 1
    print(f"PASS — {len(READER_FACING)} reader-facing files carry no withdrawn "
          "claim, and every cross-file figure matches its source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
