#!/usr/bin/env bash
# Track 2 pharmacogenomic screen: CPIC-guided PGx from the proband's own WGS.
#
# Runs PharmCAT TWICE and compares the results, which is the point of the script.
# A variants-only VCF has no reference blocks, so a PharmCAT position that is absent
# from the file is UNCALLED, not homozygous reference. PharmCAT offers --missing-to-ref
# to paper over this and labels the flag "DANGEROUS!" in its own CLI help. Running only
# that mode produces a clean-looking pharmacogenomic clearance the data cannot support.
#
# So: run strict, run missing-to-ref, and report the difference. On this proband 16 of
# 23 genes change call between the two.
#
# Outputs land in a gitignored directory: these are derived patient genotype data and
# are excluded from version control per the Data Transfer Agreement.
#
# Prerequisites:
#   - bcftools, bgzip, tabix, samtools, java 17+, python3
#   - PharmCAT v3.4.0 pipeline bundle (pharmcat.jar + pharmcat_vcf_preprocessor)
#   - GRCh38 reference FASTA, bgzip-compressed and faidx-indexed, with chr-prefixed
#     contig names
#
# Usage:
#   ./track2_pgx_screen.sh <pharmcat_dir> <reference.fa.bgz> <input.vcf.gz> <outdir>
set -euo pipefail

PHARMCAT_DIR="${1:?path to the PharmCAT pipeline bundle}"
REF="${2:?path to a bgzipped, faidx-indexed GRCh38 FASTA with chr-prefixed contigs}"
IN_VCF="${3:?path to the proband genome-wide VCF}"
OUTDIR="${4:?output directory (must be gitignored)}"

POSITIONS="${PHARMCAT_DIR}/pharmcat_positions.vcf.bgz"
mkdir -p "${OUTDIR}/strict" "${OUTDIR}/missing_to_ref"

# 1. Contig naming. The provided VCF uses unprefixed contigs (1, 2, ... X); PharmCAT
#    expects GRCh38 chr-prefixed names. Build the map from the VCF's own header rather
#    than assuming a fixed contig list, so decoys and scaffolds are handled too.
echo "==> building contig rename map from the VCF header"
bcftools view -h "${IN_VCF}" \
  | awk -F'[<>,=]' '/^##contig/{
        for (i = 1; i <= NF; i++) if ($i == "ID") { id = $(i+1); break }
        if (id == "MT") print id "\tchrM"; else print id "\tchr" id }' \
  > "${OUTDIR}/rename_chrs.txt"

# 2. Restrict to the PharmCAT positions (+/-50bp) before renaming, so the region file
#    is in the source naming. Restricting first avoids annotating ~2M genome-wide records.
echo "==> restricting to PharmCAT positions"
bcftools view -H "${POSITIONS}" \
  | awk -F'\t' '{ sub(/^chr/, "", $1); print $1 "\t" ($2 > 50 ? $2 - 50 : 1) "\t" $2 + 50 }' \
  | sort -k1,1 -k2,2n > "${OUTDIR}/pgx_regions.bed"

bcftools view -R "${OUTDIR}/pgx_regions.bed" -O u "${IN_VCF}" \
  | bcftools annotate --rename-chrs "${OUTDIR}/rename_chrs.txt" \
      -O z -o "${OUTDIR}/proband_pgx_regions.vcf.gz"
bcftools index -t "${OUTDIR}/proband_pgx_regions.vcf.gz"

echo "    variant calls in PGx regions: $(bcftools view -H "${OUTDIR}/proband_pgx_regions.vcf.gz" | wc -l | tr -d ' ')"
echo "    PharmCAT positions total:     $(bcftools view -H "${POSITIONS}" | wc -l | tr -d ' ')"

# 3. Two preprocessing runs. The -0 run is the one PharmCAT itself calls DANGEROUS.
for mode in strict missing_to_ref; do
  echo "==> preprocessing (${mode})"
  extra=()
  [[ "${mode}" == "missing_to_ref" ]] && extra=(-0)
  "${PHARMCAT_DIR}/pharmcat_vcf_preprocessor" \
      -vcf "${OUTDIR}/proband_pgx_regions.vcf.gz" \
      "${extra[@]}" \
      -refFna "${REF}" \
      -o "${OUTDIR}/${mode}" -bf "proband_${mode}"

  echo "==> PharmCAT (${mode})"
  java -jar "${PHARMCAT_DIR}/pharmcat.jar" \
      -vcf "${OUTDIR}/${mode}/proband_${mode}.preprocessed.vcf.bgz" \
      -o "${OUTDIR}/${mode}" -reporterJson
done

# 4. The comparison is the deliverable.
echo "==> comparing gene calls between the two assumptions"
python3 "$(dirname "$0")/track2_pgx_compare.py" \
    --strict "${OUTDIR}/strict/proband_strict.phenotype.json" \
    --missing-to-ref "${OUTDIR}/missing_to_ref/proband_missing_to_ref.phenotype.json"
