#!/usr/bin/env bash
# Retrieve only the regions of interest from the hackathon's alignment file.
#
# WHY A SLICE. The full dataset is ~85 GB across 11 files and Hugging Face
# recommends 100-150 GB of working space. Almost none of that bulk answers a
# question this analysis is actually asking: FASTQ adds nothing over an
# alignment unless you intend to re-align. What IS worth having is the
# CRAM/BAM, because a coverage track converts the report's single largest
# limitation -- "absence of a call and absence of coverage are
# indistinguishable" -- from a disclaimer into a measurement.
#
# samtools is built here with libcurl, so it can read a remote CRAM/BAM over
# HTTPS given the index and pull out one region. That is tens of MB instead of
# 15-30 GB. Everything written lands in data-notes/raw/, which is gitignored,
# and falls under the same 30-day deletion obligation as the rest of the data.
#
# PREREQUISITE -- run these yourself; this script never handles credentials:
#     pip install -U huggingface_hub
#     hf auth login
#
# Usage:
#     ./fetch_alignment_slice.sh --list
#     ./fetch_alignment_slice.sh --file <NAME.cram>
#     ./fetch_alignment_slice.sh --file <NAME.cram> --regions 15:40158984-40223137
set -euo pipefail

REPO="SageBio/mva-hackathon-2026-data"
OUT="$(cd "$(dirname "$0")/.." && pwd)/data-notes/raw"
# BUB1B padded, plus the two genes whose negative results are least well supported.
REGIONS="15:40158984-40223137,11:95787965-95839070,5:890849-921357"
REF=""
FILE=""
LIST=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --list)    LIST=1; shift ;;
    --file)    FILE="$2"; shift 2 ;;
    --regions) REGIONS="$2"; shift 2 ;;
    --ref)     REF="$2"; shift 2 ;;
    --repo)    REPO="$2"; shift 2 ;;
    --out)     OUT="$2"; shift 2 ;;
    -h|--help) sed -n '2,25p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

command -v samtools >/dev/null || { echo "samtools not found" >&2; exit 1; }
samtools --version | grep -q 'libcurl=yes' \
  || echo "WARNING: samtools lacks libcurl; remote slicing will fail, use --file with a local path" >&2

if [[ $LIST -eq 1 || -z "$FILE" ]]; then
  echo "Files in ${REPO}:"
  python3 - "$REPO" <<'PY'
import sys
try:
    from huggingface_hub import HfApi
except ImportError:
    sys.exit("huggingface_hub not installed -- run: pip install -U huggingface_hub")
try:
    info = HfApi().repo_info(sys.argv[1], repo_type="dataset", files_metadata=True)
except Exception as exc:                       # gated repo, not logged in, etc.
    sys.exit(f"could not list repo: {exc}\nRun `hf auth login` first.")
for s in sorted(info.siblings, key=lambda s: -(s.size or 0)):
    size = f"{(s.size or 0)/2**30:7.2f} GB" if s.size else "        ?"
    print(f"  {size}  {s.rfilename}")
print("\nPick the .cram or .bam and re-run with --file <name>.")
PY
  exit 0
fi

TOKEN="$(python3 -c 'from huggingface_hub import HfFolder; print(HfFolder.get_token() or "")' 2>/dev/null || true)"
[[ -n "$TOKEN" ]] || { echo "No HF token found. Run: hf auth login" >&2; exit 1; }

URL="https://huggingface.co/datasets/${REPO}/resolve/main/${FILE}"
mkdir -p "$OUT"
export HTS_AUTH_LOCATION="${HTS_AUTH_LOCATION:-}"
CURL_HDR="Authorization: Bearer ${TOKEN}"

# The index is small; fetch it so samtools can seek instead of streaming the file.
for ext in crai bai; do
  if curl -fsSL -H "$CURL_HDR" -o "${OUT}/$(basename "$FILE").${ext}" "${URL}.${ext}" 2>/dev/null; then
    echo "fetched index: $(basename "$FILE").${ext}"; break
  fi
  rm -f "${OUT}/$(basename "$FILE").${ext}"
done

REF_ARG=()
[[ -n "$REF" ]] && REF_ARG=(--reference "$REF")

BASE="$(basename "${FILE%.*}")"
IFS=',' read -ra RS <<< "$REGIONS"
echo "slicing ${#RS[@]} region(s) from ${FILE}"
samtools view -b "${REF_ARG[@]}" \
  --input-fmt-option "nthreads=2" \
  -o "${OUT}/${BASE}.slice.bam" \
  "$URL" "${RS[@]}" \
  || { echo "Remote slicing failed. The server may not honour range requests;" >&2
       echo "fall back to: hf download ${REPO} ${FILE} --repo-type dataset --local-dir ${OUT}" >&2
       exit 1; }

samtools index "${OUT}/${BASE}.slice.bam"
echo "wrote ${OUT}/${BASE}.slice.bam ($(du -h "${OUT}/${BASE}.slice.bam" | cut -f1))"
echo "next: python3 pipeline/coverage_analysis.py --bam ${OUT}/${BASE}.slice.bam"
