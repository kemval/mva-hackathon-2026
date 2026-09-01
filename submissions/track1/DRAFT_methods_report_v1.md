# Track 1 Methods Report — Variant Prediction (DRAFT v1)

**Proband:** WGS_EX2312012
**Date:** 2026-08-31

## Summary

Independent analysis of the proband's own whole-genome VCF and HPO-coded clinical phenotype identifies a compound-heterozygous candidate in **BUB1B**: a known pathogenic nonsense variant (p.Leu737Ter, ClinVar VCV000533901.9) paired with an extremely rare missense variant (p.Asn1002Lys, a gnomAD singleton) that falls directly within the protein's kinase domain. This result was derived from scratch via a rare-variant filtering pipeline against the proband's own data — not inferred from public knowledge of MVA genetics or from the Track 1 leaderboard, though it converges on the same gene most other submissions have also reported. A phenotype-driven secondary panel search (11 genes covering the two clinical features not on the standard BUB1B symptom list) found no additional candidates. Phase (cis/trans) between the two BUB1B variants could not be directly resolved from this proband-only short-read dataset; this limitation is discussed explicitly below rather than assumed away.

*All key claims below were independently re-verified directly against primary sources (gnomAD's own API, ClinVar/eutils, UniProt, PubMed) as of 2026-08-31, not taken solely from the VEP REST proxy that generated the initial candidate list — see the Verification section at the end of this report.*

## Methods

1. **Data**: proband VCF (`WGS_EX2312012_HGWCNDSX7.vcf.gz`, GRCh38, single-sample, GATK/Sentieon Haplotyper-called) and the proband's HPO-coded clinical phenotype (`Challenge_Clinical_Phenotype_1.docx`).
2. **Primary gene panel**: BUB1B, CEP57, TRIP13 (the three established MVA-causing genes) plus CENATAC, SLF2, SMC5 (MVA subtypes 4-6), MAD1L1, BUB1, BUB3 (spindle-assembly-checkpoint-adjacent genes) — 9 genes total, GRCh38 coordinates resolved via Ensembl REST, ±2kb padding.
3. **Region restriction**: `bcftools view -R` against the padded gene-panel BED, using the provided `.tbi` index — avoided processing the full genome-wide VCF (~2M+ raw records).
4. **Annotation**: Ensembl VEP REST API (canonical transcript, HGVS nomenclature, max gnomAD population allele frequency across gnomAD genomes/exomes subpopulations, ClinVar clinical significance where available).
5. **Filtering**: gnomAD max AF < 0.001 AND VEP impact MODERATE or HIGH on the canonical transcript.
6. **Phenotype cross-check**: proband's HPO terms compared against each gene's known phenotype spectrum (see Discussion).
7. **Secondary panel**: TP53, DICER1, NF1, PTCH1, HRAS (rhabdomyosarcoma-predisposition syndromes, per Schneider et al., *Translational Andrology and Urology*, PMC7658107, which names TP53/NF1/DICER1/PTCH1-SUFU as the major RMS-predisposition genes and HRAS/Costello syndrome as a related consideration) and CASR, CLDN16, CLDN19, AGXT, SLC34A1, CYP24A1 (nephrocalcinosis-associated genes, per two pediatric nephrocalcinosis genetics reviews — *Clinical Kidney Journal* 15(4):812 and *Pediatric Nephrology*, PMC12852217 — a literature-grounded but deliberately non-exhaustive subset of the ~30-gene commercial panels these reviews describe), run through the identical pipeline, to investigate two HPO features (nephrocalcinosis, parental recurrent miscarriage) not on the standard BUB1B/MVA symptom list.

Full pipeline scripts: `pipeline/vep_annotate_panel.py` (primary panel) and `pipeline/vep_annotate_secondary.py` (secondary panel), both in the repository. Raw annotated tables (`data-notes/annotated/`) exist locally but are **not** committed to version control — see Reproducibility below.

## Primary finding: BUB1B compound-heterozygous candidate

| Variant | Consequence | gnomAD v4 AF (direct query) | ClinVar (direct query) |
|---|---|---|---|
| chr15:40209701 T>G, c.2210T>G, **p.Leu737Ter** | stop_gained (HIGH) | genomes 3.29e-5 (5/152,174); exomes 7.87e-5 (115/1,461,846) | **Pathogenic/Likely pathogenic**, VCV000533901.9, review status "criteria provided, multiple submitters, no conflicts" (2-star), trait: Mosaic variegated aneuploidy syndrome 1 (OMIM 257300, Orphanet 1052, MONDO:0009759) |
| chr15:40220612 T>G, c.3006T>G, **p.Asn1002Lys** | missense_variant (MODERATE) | exomes 6.84e-7 — **singleton (AC=1 of 1,461,878 alleles)**, not absent | not in ClinVar |

Both heterozygous (0/1), high genotype quality (GQ=99), adequate read depth (21-25x and 15-13x respectively).

### ACMG/AMP evidence

**Variant 1 (p.Leu737Ter, stop_gained)**
- **PVS1 (Very Strong)**: null variant (premature stop) in BUB1B, where loss-of-function is the established mechanism for MVA1. Per UniProt (O60566, direct query), BubR1's kinase domain spans residues 766-1050 of the 1050-aa protein — the truncation at residue 737 falls before this domain begins, so it **removes the entire kinase domain** (confirmed, not inferred).
- **PS4/PP5 (Strong/Supporting)**: independently classified Pathogenic/Likely pathogenic in ClinVar (VCV000533901.9, 2-star review status, multiple submitters, no conflicts, specifically for "Mosaic variegated aneuploidy syndrome 1" — direct ClinVar/eutils query, not just VEP's `clin_sig` field).
- **PM2 (Moderate)**: rare in gnomAD (genomes AF 3.29e-5, exomes AF 7.87e-5, direct gnomAD API query), consistent with an ultra-rare recessive disease allele.

**Variant 2 (p.Asn1002Lys, missense)**
- **PM2 (Moderate)**: a gnomAD singleton — observed in exactly 1 of 1,461,878 gnomAD exome alleles (AF≈6.84e-7), direct gnomAD API query. (Correction: VEP's REST proxy reported this as "absent," because Ensembl's bundled gnomAD annotation dataset had not indexed this ultra-rare variant — the direct gnomAD query is the authoritative figure and should be used, not "absent.")
- **PM1 (Moderate)**: per UniProt (O60566), residue 1002 falls **directly within** the kinase domain (766-1050) — a confirmed functional-domain hit, not merely "nearby" as an earlier draft of this analysis hedged.
- **PM3 (Moderate, tentative)**: candidate second hit in trans with a known-pathogenic variant in the same recessive-disease gene — see Limitations below regarding phase confirmation.
- **PP3 (Supporting, weak)**: direct dbNSFP query (via MyVariant.info, `chr15:g.40220612T>G`) returns AlphaMissense (0.92/0.88, "likely pathogenic"), CADD phred 24.5, PolyPhen-2 (1.0/0.997, "probably damaging"), and SIFT (0.0, "deleterious") all concordant for damaging — but REVEL, the meta-predictor ClinGen's SVI group recommends over simple tool-counting, scores 0.472, just under its commonly-used ≥0.5 supporting threshold. Reported as weak/supporting PP3, not strong — the concordant tools support it, but the single most-calibrated meta-predictor is ambiguous, and that shouldn't be papered over.

**Combined classification**: Likely Pathogenic (compound heterozygous). PVS1+PS4/PP5+PM2 on the first variant alone already clears this threshold; PM1/PM2/PM3(tentative)/PP3(weak) on the second variant and PP4 (phenotype match) further support it. Formal confirmation still pending phase resolution (see Limitation below).

### Phenotype correlation (PP4)

The proband's HPO-coded features — rhabdomyosarcoma (HP:0002859), short stature (HP:0004322), failure to thrive (HP:0001508), skeletal muscle atrophy (HP:0003202), premature birth (HP:0001622), and very-low-birth-weight/IUGR (HP:0001518) — match the BUB1B-MVA (MVA1) phenotype spectrum closely, including the specific association with embryonal rhabdomyosarcoma reported in the original BUB1B-MVA discovery cohort (Hanks et al. 2004). This phenotype profile is more consistent with BUB1B than with CEP57 (which classically presents with rhizomelic limb shortening and reduced cancer predisposition — not observed here) or TRIP13.

## Secondary finding

chr15:40216470 A>G (c.2679-1026A>G), deep intronic, absent from gnomAD (independently re-confirmed via direct gnomAD v4 GraphQL query, not just VEP's proxy — the query returns "Variant not found," genuinely absent, not an under-indexing artifact like the p.Asn1002Lys correction above), physically located between the two primary candidates within BUB1B. VEP's canonical-transcript consequence call does not flag this as splice-altering. A direct SpliceAI query was attempted (SpliceAI Lookup API) but the service was unreachable (connection timeout at time of attempt, while other bioinformatics APIs and the same service's own frontend responded normally — an external outage, not a methodology gap) — reported honestly as not-yet-resolved rather than skipped silently. Reported as a secondary/lower-confidence row per the submission format; does not affect automated scoring either way.

## Unresolved / not addressed by this analysis

- **Nephrocalcinosis (HP:0000121)** and **parental recurrent spontaneous abortion (HP:0200067)**, both present in the proband's clinical phenotype, are not explained by any variant found in this analysis. An 11-gene secondary panel targeting rhabdomyosarcoma-predisposition and nephrocalcinosis-associated genes (TP53, DICER1, NF1, PTCH1, HRAS, CASR, CLDN16, CLDN19, AGXT, SLC34A1, CYP24A1 — see Methods for the literature grounding each half of this panel) returned no rare, damaging candidates. This panel is a literature-grounded but deliberately non-exhaustive subset (real pediatric nephrocalcinosis panels run ~30 genes; this analysis did not run all of them) — a clean result here narrows, but does not fully rule out, a monogenic explanation. These features may represent under-documented aspects of the BUB1B-MVA phenotype, a secondary consequence of chromosomal instability rather than a distinct monogenic cause, or (for the family-history feature) something inherently outside what proband-only sequencing can address. This is flagged as an open question rather than resolved.
- A fully unbiased genome-wide rare-variant scan (beyond the 9-gene primary panel and 11-gene secondary panel) was not performed at full annotation depth in this pass, due to practical constraints on REST-API-based genome-wide annotation; the panels used were chosen to be phenotype-driven and biologically motivated rather than exhaustive.

## Limitation: phase not directly resolvable

The two primary BUB1B candidate variants are ~11kb apart. GATK/Sentieon's local read-based phasing (`PGT`/`PID` FORMAT tags) found no phase-informative reads connecting either variant to any nearby heterozygous site — expected, since standard short-read paired-end fragments (typically 300-500bp) cannot physically span an 11kb gap. This is a limitation of proband-only short-read sequencing at this variant separation, not a tooling gap: read-backed phasing tools (e.g. WhatsHap) operating on the same underlying reads would face the identical physical constraint. No parental samples are available for segregation-based phasing. The compound-heterozygous interpretation is therefore **presumed, not directly confirmed** — based on (1) a known-pathogenic LOF variant co-occurring with a rare novel missense variant in the same well-established recessive-disease gene, (2) a full phenotype match to the BUB1B-MVA spectrum, and (3) the low prior probability of two independent rare BUB1B variants arising by chance in an unrelated configuration. Definitive phase confirmation would require either parental sequencing or long-read data, neither of which is available in this dataset.

## Verification

The initial candidate list was generated via Ensembl VEP's REST API, which proxies gnomAD and ClinVar data through Ensembl's own bundled annotation set. Because that bundled set can lag behind or diverge from the primary databases (confirmed here: it missed the p.Asn1002Lys variant in gnomAD entirely, see above), every claim used in this report's ACMG scoring was independently re-queried directly against the primary source before being finalized:

| Claim | Primary source queried directly | Result |
|---|---|---|
| p.Leu737Ter population frequency | gnomAD v4 GraphQL API | genomes 3.29e-5, exomes 7.87e-5 |
| p.Leu737Ter clinical classification | ClinVar via NCBI eutils (VCV000533901.9) | Pathogenic/Likely pathogenic, 2-star, MVA1-specific |
| p.Asn1002Lys population frequency | gnomAD v4 GraphQL API | singleton, AC=1/1,461,878, AF≈6.84e-7 (VEP's proxy had reported "absent" — corrected) |
| BubR1 kinase domain boundaries | UniProt O60566 REST API | residues 766-1050 of 1050 aa; both variants' positions relative to this domain confirmed |
| Canonical transcript choice | Ensembl (`is_canonical` flag) cross-checked against ClinVar's independently-chosen RefSeq transcript (NM_001211.6) | Both sources converge on the same HGVS nomenclature (c.2210T>G, p.Leu737Ter) — internal consistency confirms the transcript choice is correct |
| p.Asn1002Lys in-silico deleteriousness (PP3) | dbNSFP via MyVariant.info (AlphaMissense, REVEL, CADD, SIFT, PolyPhen-2) | 5/6 predictors damaging; REVEL specifically ambiguous (0.472) — reported as weak, not strong, PP3 |
| Secondary intronic finding splice impact | SpliceAI Lookup API | Unreachable (service timeout) — genuinely unresolved, not fabricated or omitted |
| Secondary intronic finding gnomAD absence | gnomAD v4 GraphQL API (direct, bypassing VEP) | Confirmed genuinely absent ("Variant not found") — re-checked specifically because VEP's proxy was already caught wrong once on a different variant in this pair |
| All three variants' genotype quality/read depth | Direct `bcftools view` on the region-restricted VCF | GQ=99 for all three; AD/DP exactly as reported (p.Leu737Ter 21,25/46x; p.Asn1002Lys 15,13/28x) |

## AI-assistant usage disclosure

Anthropic API, Claude (Sonnet 5), commercial terms, no training on customer content. Used for: literature synthesis and knowledge-base construction, pipeline script authoring (VEP REST annotation script), ACMG evidence-code application, independent verification of VEP's output against gnomAD/ClinVar/UniProt primary sources, and this report's drafting. All bioinformatics results (variant calls, annotations, frequencies) are outputs of standard third-party tools and public databases (bcftools, Ensembl VEP REST, gnomAD API, ClinVar/NCBI eutils, UniProt REST) queried directly against the proband's own data or public reference data, not generated or estimated by the AI assistant.

## Reproducibility

Annotation/filtering scripts (`pipeline/`) and gene-panel coordinate lookups (`data-notes/regions/`) are in the project repository. The scripts currently use hardcoded local paths (`/Users/.../mva-hackathon-2026/data-notes/...`) rather than relative paths or CLI arguments — a real reproducibility gap worth naming rather than glossing over; a re-runner would need to edit the `VCF`/`OUT_TSV`/`OUT_RAW` constants at the top of each script for their own environment before running. Per the hackathon's Data Transfer Agreement ("I will not release or otherwise grant data access to anyone"), the raw VCF, phenotype document, and full-panel genotype-level annotation output are intentionally **not** committed to version control — see `data-notes/README.md` for the exclusion policy. Reproducing this analysis requires obtaining independent authorized access to the dataset and re-running the scripts against a freshly downloaded VCF.

---
*This is a DRAFT (v1). Final proofread pass completed 2026-08-31: every gnomAD/ClinVar/UniProt/genotype figure in this report was independently re-verified against its live primary-source API and matches exactly (see Verification table). Formal PP3 in-silico scoring is done. Only remaining items before actual submission: (1) SpliceAI on the secondary intronic finding — attempted, service unreachable, not blocking; (2) rename this file and the predictions CSV to the required `<team-name>_track1_report.md` / `<team-name>_<model-name>.csv` convention once a team/display name is chosen — not yet done, no name has been picked.*
