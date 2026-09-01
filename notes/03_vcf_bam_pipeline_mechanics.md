# Synthesis Notes: VCF/BAM/CRAM Mechanics & a Practical Pipeline for This Case

*Synthesized from general bioinformatics knowledge (equivalent territory to Genomics in the Cloud by Van der Auwera & O'Connor, and Bioinformatics Data Skills by Buffalo). Treat as a practical how-to for this specific task, not a citation-grade reference — those books go much deeper on the "why" of each GATK Best Practices step.*

## File formats, briefly

- **FASTQ**: raw sequencer reads + quality scores. Almost certainly not needed for this project — see below.
- **BAM/CRAM**: aligned reads (CRAM = compressed BAM, needs a reference genome to decompress). Official Rules say this is provided *optionally* — useful for phasing and manual inspection, not required for the core variant list.
- **VCF (Variant Call Format)**: the actual list of variant calls (SNVs, indels, sometimes structural variants) already produced by an upstream variant-calling pipeline, with per-site metadata (quality, depth, filters) and per-sample genotypes. **This is almost certainly the primary file to start from** — someone (the data providers) has already run alignment + variant calling; redoing that from FASTQ would burn enormous compute for no analytical benefit unless there's a specific reason to suspect the existing calls are wrong in the region of interest.

## Recommended pipeline order (matches the plan's Week 2)

1. **Download and inspect the VCF only** (`bcftools stats`, `bcftools view` on a few records) to understand what caller produced it, what filters are already applied, and what the sample/proband ID structure looks like.
2. **Annotate** with Ensembl VEP (or ANNOVAR) to get gene/transcript/consequence (missense, nonsense, frameshift, splice-region, etc.), plus population frequency (gnomAD) and ClinVar annotations as VEP plugins/custom annotations — this collapses steps 1-2 of the ACMG workflow into one annotation pass.
3. **Filter** to a manageable candidate list:
   - Restrict to genes on a curated "MVA-relevant" panel (BUB1B, CEP57, TRIP13 at minimum; consider a broader chromosomal-instability/mitotic-checkpoint gene panel via PanelApp for secondary-finding potential) — but don't *only* do this; also run an unbiased genome-wide rare-variant filter to make sure nothing outside the obvious candidate genes is missed (this is where a real secondary finding would surface).
   - Apply population frequency threshold (e.g. gnomAD AF < 0.001 or absent, appropriate for a rare recessive disease).
   - Apply consequence severity filter (prioritize LOF and predicted-damaging missense over synonymous/intronic, but don't discard splice-region variants — SpliceAI-flagged deep intronic variants are a classic "everyone else missed it" finding in real rare-disease diagnostics).
4. **Phenotype-driven ranking**: feed the case's HPO terms + the annotated/filtered VCF into **Exomiser**, which combines variant-level pathogenicity scores with phenotype-similarity scores (comparing the case's HPO terms against known gene-phenotype associations, e.g. via HPO/OMIM/Orphanet mappings) to produce a single ranked candidate list. This directly mirrors the hackathon's own framing ("using their clinical symptoms and genomic data") and is a defensible, standard-of-care-adjacent methodology to cite.
5. **Phase check** for any compound-het candidate (see `notes/02_acmg_variant_classification_workflow.md`) — subset the BAM/CRAM to just the candidate gene's coordinates with `samtools view -b input.cram chr15:XX,XXX,XXX-XX,XXX,XXX region.bam` (use actual BUB1B/CEP57/TRIP13 GRCh38 coordinates once confirmed), then run WhatsHap read-backed phasing on that small subset — this avoids ever needing to process the full 85GB.
6. **Manual sanity check in IGV**: load the small regional BAM/CRAM subset + VCF into IGV to visually confirm read support, mapping quality, and absence of obvious artifacts (e.g. the variant sitting in a low-complexity/repeat region that commonly produces false positives) — a cheap, high-credibility step for the write-up.
7. **ACMG scoring** per `notes/02_acmg_variant_classification_workflow.md` for the top candidate(s).
8. **Write the ranked CSV** per the exact schema in `literature/00_hackathon_site_full_capture.md` (GRCh38 coordinates, EPCR column, finding_type).

## Compute-sizing reality check

- VCF-only work (steps 1-4, 7-8): comfortably runs on a laptop or a small/free cloud instance — VCFs for a single genome, even unfiltered, are typically low-single-digit GB compressed, far smaller than the 85GB full dataset (which is dominated by BAM/CRAM/FASTQ).
- Region-subsetted BAM/CRAM work (steps 5-6): trivial once subsetted — a single gene locus is a few hundred KB to a few MB of alignment data, not gigabytes.
- **There is very likely no need to ever download the full 85GB, and no need for a full re-alignment from FASTQ.** If you find yourself tempted to do a full realignment "to be thorough," that effort is much better spent on the Track 2 mechanism/drug-repurposing research, per the plan's Track-2-weighted strategy.

## Key tools referenced above (all free/open-source)
- `bcftools`/`vcftools` — VCF manipulation and stats
- Ensembl VEP or ANNOVAR — variant annotation
- Exomiser — phenotype-driven variant prioritization (uses HPO terms directly)
- `samtools` — BAM/CRAM manipulation, including region subsetting
- WhatsHap — read-backed phasing
- IGV (Integrative Genomics Viewer) — manual visual inspection
- gnomAD, ClinVar — reference population-frequency and known-pathogenicity databases (queryable via web UI or as VEP annotation sources)
