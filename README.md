# MVA Hackathon 2026 — Project Workspace

**Team:** Gummietech
Working directory for "Rare Disease, Real Kid: The MVA Hackathon 2026" (SageBio / Hugging Face / MVA Society / BEACON, prizes from AWS + Anthropic). Submissions close **Oct 24, 2026 23:59 UTC**.


## Folder structure

- `literature/` — full text of open-access papers, guideline documents, and official reference material (site captures, journal articles, tool documentation). Start with `00_hackathon_site_full_capture.md` (the complete live-site capture: Overview, FAQ, Official Rules, both Submit tabs, leaderboard snapshot) and `_fetch_log.md` (fetch status and provenance of every source).
- `notes/` — original synthesis documents covering material from copyrighted textbooks (not bulk-reproduced) — mitosis/spindle-checkpoint biology, ACMG variant classification workflow, VCF/BAM/HPO pipeline mechanics, drug repurposing methodology. Orientation material; the primary literature in `literature/` is the citation-grade source.
- `data-notes/` — working analysis notes on the case (gene-panel coordinates, variant candidates, ACMG evidence, phasing analysis). Raw and derived patient genomic data are excluded from version control per the dataset's Data Transfer Agreement — see `data-notes/README.md`.
- `pipeline/` — annotation and filtering scripts, plus `pipeline/README.md` recording the exact end-to-end command sequence (Ensembl REST coordinate lookup → padded BED → `bcftools` region restriction → VEP REST annotation → rare/damaging filter). Both scripts are CLI-parameterised; running them against the annotation output reproduces the submitted candidate list exactly.
- `submissions/` — Track 1 and Track 2 submission materials (predictions CSV, methods report).
- `graphify-out/` — knowledge graph built from `literature/` + `notes/` (gitignored, regenerable via `/graphify --update`).

## Knowledge graph

Built from `literature/` + `notes/`: 285 nodes / 359 edges / 15 communities as of the last update (2026-08-31). Query with `graphify query "<question>"` or `graphify path "<a>" "<b>"` instead of re-reading raw files. Re-run `/graphify /Users/kiki/mva-hackathon-2026 --update` after adding or editing files in `literature/` or `notes/`.

## Track 1 status (2026-08-31) — analysis complete, submission-ready

An independently derived pipeline (region-restriction via `bcftools` → annotation via Ensembl VEP REST → ACMG/AMP-lite filtering) was run against the proband's own VCF and HPO-coded clinical phenotype — not inferred from the public leaderboard. Result: a compound-heterozygous candidate in **BUB1B** — a ClinVar-classified pathogenic nonsense variant (p.Leu737Ter) paired with a rare missense variant (p.Asn1002Lys) inside the kinase domain — plus a lower-confidence deep-intronic secondary finding.

Every population-frequency, clinical-classification, protein-domain, and in-silico-predictor claim underlying the ACMG evidence was independently re-verified directly against its primary source (gnomAD, ClinVar, UniProt, dbNSFP) rather than taken from an intermediate annotation tool; this process caught and corrected two factual errors along the way (documented in the report's Verification section and `data-notes/track1_findings.md`).

Full analysis: `data-notes/track1_findings.md`. Final submission materials: `submissions/track1/gummietech_track1_report.md` and `submissions/track1/gummietech_vep-acmg-compound-het.csv`.

**Completed:**
1. Independent variant discovery, ACMG/AMP evidence classification, and phenotype correlation.
2. Compound-heterozygosity presumed with an explicitly documented phasing limitation (variants ~11kb apart, beyond short-read phasing range — stated as a limitation, not silently assumed).
3. Phenotype-driven 11-gene secondary panel search for two unexplained clinical features, grounded in cited differential-diagnosis literature; result is negative and reported as such.
4. Formal in-silico missense scoring (AlphaMissense, REVEL, CADD, SIFT, PolyPhen-2) for the missense candidate, reporting a discordant result (REVEL) rather than omitting it.
5. Full trust-audit verification pass against primary sources, plus a final proofread that re-confirmed every figure a second time.
6. Code-level audit checking the pipeline against what the report claims it does. This found one real defect — the rarity filter had silently excluded gnomAD exome frequencies — proved it harmless by replaying the corrected filter offline against the saved raw API responses (identical candidate set: primary 2/2, secondary 0/0), corrected the code, and recorded both the defect and the check in the report's Verification table. The same pass closed the repo's reproducibility gaps (the filtering step had no code; the two annotation scripts were duplicates with hardcoded paths; the `bcftools` step was undocumented) and tightened two ACMG evidence codes (PS4 dropped as improperly applied, PM2 downgraded to PM2_Supporting per ClinGen SVI) without changing the classification.
7. GitHub repository created (public at hackathon close, per the rules) and submission files named per the required convention.
8. SpliceAI splice-impact assessment, via Ensembl VEP's own `&SpliceAI=1` plugin after the Broad's standalone Lookup API proved unreachable across three attempts. Both panels were re-annotated from scratch, adding a `spliceai_max_ds` column (blank, not 0.00, where SpliceAI has no data). The deep-intronic secondary candidate scores 0.00 on all four delta scores across all 22 BUB1B transcripts, so its EPCR was lowered 0.30 → 0.10. A panel-wide screen of all 2,346 PASS variants found none reaching the 0.2 high-recall threshold.

**Outstanding (does not block submission):**
- Actual upload via the hackathon's "Submit – Track 1" tab, which requires the account holder's own Hugging Face session.

## Next actions

1. Submit Track 1 via the hackathon site (account-holder action).
2. Begin the Track 2 mechanism deep-dive: build the causal chain from the confirmed BUB1B variant through spindle-checkpoint dysfunction to the proband's HPO-coded phenotype, then into the drug-repurposing hypotheses (senolytics vs. NAD+/NMN supplementation) already grounded in `literature/`.

## Standing obligations

- **Data deletion.** Per the Official Rules, all dataset copies must be deleted from every environment (local machines, cloud instances, notebooks, private repos, intermediate and derived datasets) within **30 days of hackathon close**, and deletion must be confirmed by email to `RarediseaserealkidMVAhackathon2026@synapse.org`. This covers `data-notes/raw/`, `data-notes/annotated/`, and the region-restricted VCFs — all gitignored, so none of it is in git history, but all of it is on disk.
- **Repository visibility.** The repo may stay private during the hackathon but must be made public once it closes so the expert panel can review the code.
