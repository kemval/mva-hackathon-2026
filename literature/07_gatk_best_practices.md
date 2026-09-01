# GATK Best Practices Workflows (overview)

Source: https://gatk.broadinstitute.org/hc/en-us/sections/360007226651-Best-Practices-Workflows
Captured: 2026-08-31

## Available workflows (index page)
- **Getting started with GATK4** — orientation ("GATK — properly pronounced 'Gee-ay-tee-kay'...")
- **About the GATK Best Practices** — context document on how the Best Practices are structured
- **GATK Best Practices for Structural Variation Discovery on Single Samples** — GATK-SV, structural variation discovery pipeline for Illumina short-read data
- **Mitochondrial short variant discovery (SNVs + Indels)** — handles challenges specific to the mitochondrial genome
- **Somatic short variant discovery (SNVs + Indels)** — somatic (tumor) variant calling — not the relevant workflow for this germline rare-disease case
- **Germline short variant discovery (SNPs + Indels)** — "Identify germline short variants (SNPs and Indels) in one or more individuals" — **this is the directly relevant workflow for Track 1**
- **Data pre-processing for variant discovery** — "the obligatory first phase that must precede variant discovery" (alignment, duplicate marking, base quality score recalibration) — relevant only if working from BAM/CRAM/FASTQ rather than the pre-provided VCF
- **Somatic copy number variant discovery (CNVs)** — tumor CNV calling, not directly relevant
- **RNAseq short variant discovery (SNPs + Indels)** — not relevant (this is DNA WGS data)

## Use in this project
Given the dataset already provides a called VCF (per `literature/00_hackathon_site_full_capture.md`), the **Germline short variant discovery** workflow is the reference standard to cite when describing/validating the existing calls, and the **Data pre-processing** workflow only becomes relevant if re-calling from BAM/CRAM is deemed necessary (see `notes/03_vcf_bam_pipeline_mechanics.md` — likely unnecessary for this project; the existing VCF should be trustworthy enough to build on). If deeper pipeline detail is needed later, fetch the individual "Germline short variant discovery" and "About the GATK Best Practices" sub-pages directly (this index page only lists them, doesn't contain their full content).
