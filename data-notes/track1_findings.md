# Track 1 Findings — Working Notes

Generated: 2026-08-31, from independent analysis of the proband's own VCF + HPO phenotype (not copied from the Track 1 leaderboard).

## Pipeline run

1. Downloaded VCF only (`data-notes/raw/WGS_EX2312012_HGWCNDSX7.vcf.gz`, 315MB, GRCh38, single-sample proband-only).
2. Looked up exact GRCh38 coordinates for a 9-gene MVA panel (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, BUB1, BUB3) via Ensembl REST — see `data-notes/regions/mva_gene_panel_grch38.tsv`.
3. Region-restricted the VCF to these 9 genes ± 2kb padding via `bcftools view -R` — 1288 variants total, 1281 PASS (`data-notes/mva_panel_variants.vcf.gz`).
4. Annotated all 1281 PASS variants via Ensembl VEP REST (consequence, canonical HGVS, max gnomAD population AF, ClinVar significance) — `data-notes/annotated/vep_panel_annotated.tsv`, raw API responses in `vep_raw_responses.jsonl`.
5. Filtered to gnomAD AF < 0.001 + MODERATE/HIGH impact.

## Result: two strong candidates, both in BUB1B, both heterozygous

| Position (GRCh38) | Change | Consequence | Impact | HGVS | gnomAD max AF (VEP proxy, initial pass) | ClinVar | Genotype |
|---|---|---|---|---|---|---|---|
| 15:40209701 | T>G | stop_gained | HIGH | c.2210T>G, p.Leu737Ter | 0.000073 (rs759242053) | **likely_pathogenic;pathogenic** | 0/1 |
| 15:40220612 | T>G | missense_variant | MODERATE | c.3006T>G, p.Asn1002Lys | 0.000000 (absent from gnomAD) | none on record | 0/1 |

**These are the initial VEP-proxy figures from the first pipeline pass, kept here unedited for an honest audit trail.** They were superseded by direct gnomAD API re-verification during the trust audit (see below): p.Leu737Ter is genome AF 3.29e-5 (5/152,174) / exome AF 7.87e-5 (115/1,461,846) — close to VEP's 0.000073 but not identical, likely a different population-subset breakdown; p.Asn1002Lys is **not** absent — it's a gnomAD exome singleton (AC=1/1,461,878, AF≈6.84e-7), the error the trust audit caught. Use the corrected figures in `submissions/track1/gummietech_track1_report.md`, not this table, for anything downstream.

A third, lower-priority candidate in the same gene: 15:40216470 A>G, deep intronic (c.2679-1026A>G, 1026bp from nearest splice site), gnomAD AF 0.000000 per VEP, MODIFIER impact — not flagged as splice-altering by VEP's basic consequence call; would need SpliceAI to properly assess. Sits physically between the two exonic candidates. **Independently re-verified 2026-08-31** (final proofread pass): unlike p.Asn1002Lys, this one's absence checks out — a direct gnomAD v4 GraphQL query (bypassing VEP entirely) for `15-40216470-A-G` returns "Variant not found," confirming genuine absence rather than an under-indexed VEP proxy gap.

**No other gene in the 9-gene panel produced any rare (AF<0.001) + moderate/high-impact PASS variant.** (CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, BUB1, BUB3 all came back empty on this filter — see full table in `vep_panel_annotated.tsv` for the handful of rare-but-intronic/MODIFIER hits in MAD1L1/BUB1/SLF2/BUB3, none exonic.)

## Interpretation (independently derived, not copied from the leaderboard)

This is a textbook compound-heterozygous loss-of-function pattern in **BUB1B** — a nonsense variant that's *already ClinVar-classified pathogenic* (truncates the protein at residue 737, before the C-terminal pseudokinase domain per `notes/01_spindle_assembly_checkpoint_biology.md` domain notes — strong PVS1 territory) paired with a second, novel (gnomAD-absent) missense variant in the same gene (PM2, needs PP3 in-silico scoring + PM1 domain-hotspot check once exact domain boundaries are confirmed). Both are heterozygous, consistent with recessive compound-het inheritance. This independently confirms the crowd's BUB1B convergence — but via the case's own data + a real ACMG evidence trail, which is what the judged write-up actually needs.

**HPO phenotype cross-check** (`Challenge_Clinical_Phenotype_1.docx`, see plan's Progress section): rhabdomyosarcoma, short stature, failure to thrive, IUGR/very low birth weight all sit squarely in the BUB1B-MVA spectrum (matches Hanks et al. 2004's own discovery cohort, which included rhabdomyosarcoma cases) — phenotype match supports PP4.

**Unresolved: nephrocalcinosis and parental recurrent miscarriage** are not on the standard BUB1B/MVA feature lists reviewed so far (`literature/01_wikipedia_mva_syndrome.md`). Still need dedicated investigation — either under-documented BUB1B features, or a lead toward a secondary finding elsewhere in the genome. Not yet addressed.

## Open question: phase (cis vs. trans) — NOT YET RESOLVED

The two candidate variants are ~11kb apart (40209701 → 40220612). GATK/Sentieon's local read-based phasing (`PGT`/`PID` tags) found **no** phase-informative reads connecting either variant to anything nearby — meaning short-read local phasing already came up empty at the variant-calling stage. This is expected: standard Illumina paired-end fragments (typically ~300-500bp) physically cannot span an 11kb gap, so WhatsHap read-backed phasing on the BAM is **very unlikely to resolve phase for this specific pair either**, for the same physical reason — it isn't a tooling limitation, it's a fragment-length limitation inherent to short-read sequencing at this variant separation.

**Options considered:**
1. **Download a region-subsetted BAM/CRAM and run WhatsHap anyway** — technically possible, but per the physical-distance reasoning above, expected to also come back uninformative for this pair specifically. Also requires the user's own authenticated HF session (gated dataset) — not something I can do without their token, which I should not request or handle directly.
2. **Statistical/population-based phasing** (e.g. Eagle2/Beagle against a haplotype reference panel) — possible but low-confidence for a variant this rare (may not be well-represented in reference panels), and adds real setup complexity/time for likely low information gain.
3. **Report as "presumed compound heterozygous, phase not directly resolvable from proband-only short-read WGS at this variant separation"** — scientifically honest, standard practice in real clinical genetics when parental samples aren't available, and arguably a *stronger* rigor signal for the write-up than silently assuming trans configuration (which is what a from-memory "it's BUB1B" submission would implicitly do).

**Recommendation**: go with option 3 for the Track 1 submission, explicitly caveated, unless the user wants to attempt option 1 or 2 despite the low expected yield. This doesn't weaken the submission — the automated score only needs the correct variant(s) identified (partial credit is even given for recovering just one of a compound-het pair per the FAQ), and the *write-up* gets credit for correctly identifying and being transparent about a real methodological limitation rather than glossing over it.

## Phasing decision (user input, 2026-08-31)

User chose: report as **presumed compound heterozygous, phase not directly resolvable from proband-only short-read WGS at this variant separation** — no BAM/CRAM download attempted (would require the user's own HF credentials, and the 11kb distance makes short-read WhatsHap phasing unlikely to succeed regardless). This will be stated explicitly and honestly in the Track 1 methods report as a named limitation, not glossed over.

## Secondary/phenotype-driven panel search (nephrocalcinosis + rhabdomyosarcoma predisposition genes)

Ran the same pipeline (region-restrict → VEP annotate → rare+damaging filter) against an 11-gene secondary panel chosen to explain the two HPO features not on the standard BUB1B/MVA list: **TP53, DICER1, NF1, PTCH1, HRAS** (rhabdomyosarcoma-predisposition syndromes) and **CASR, CLDN16, CLDN19, AGXT, SLC34A1, CYP24A1** (nephrocalcinosis-associated genes). Coordinates in `data-notes/regions/secondary_panel_grch38.tsv`, annotated results in `data-notes/annotated/vep_secondary_annotated.tsv`.

**Result: clean — no rare (gnomAD AF<0.001) + moderate/high-impact variant in any of these 11 genes.** The only "ClinVar pathogenic" hits (TP53 p.Pro72Arg, AGXT p.Pro11Leu, SLC34A1 p.Ala133Val) are all common polymorphisms (AF 0.01–0.75) with conflicting ClinVar interpretations — well-known benign/low-penetrance variants, not credible causal candidates for an ultra-rare phenotype.

**Conclusion**: nephrocalcinosis is most likely either an under-documented feature of BUB1B-MVA specifically (renal involvement is described in some case reports even where general overviews don't foreground it) or a secondary/comorbid consequence of the mosaic-aneuploidy phenotype rather than a separate genetic cause — this framing (not a confirmed answer) belongs in the Track 1 report's limitations/discussion. The parental recurrent-miscarriage history is family history, not resolvable from the proband's own sequencing at all — noted as an open question, not something this analysis can or should claim to explain.

**Panel grounding (added 2026-08-31, closes improvement-pass item #6)**: the 11-gene panel was originally chosen from general clinical knowledge, not a cited source — checked against real literature directly:
- **RMS-predisposition side (TP53, DICER1, NF1, PTCH1)**: confirmed as the standard RMS-predisposition gene set by Schneider et al., "Germline predisposition to genitourinary rhabdomyosarcoma," *Translational Andrology and Urology* (PMC7658107) — TP53 (Li-Fraumeni), NF1, DICER1, and PTCH1/SUFU (Gorlin) are explicitly named as the major RMS-associated predisposition genes. HRAS (Costello syndrome) is named alongside them as a broader RMS-predisposition consideration in the same literature, supporting its inclusion too.
- **Nephrocalcinosis side (CASR, CLDN16, CLDN19, AGXT, SLC34A1, CYP24A1)**: confirmed against "Genetic evaluation of paediatric nephrocalcinosis: phenotype-driven genetic panels reveal a rare diagnosis," *Clinical Kidney Journal* (academic.oup.com/ckj/article/15/4/812/6468760) and "Genetic causes of nephrolithiasis and nephrocalcinosis in a pediatric population," *Pediatric Nephrology* (Springer, PMC12852217) — all six genes appear in real pediatric nephrocalcinosis genetic-testing panels cited in both papers (CLDN16/CLDN19 for FHHNC, AGXT for primary hyperoxaluria type 1, CYP24A1 for infantile hypercalcemia, CASR, SLC34A1). The panel is a reasonable, literature-grounded subset of the ~30-gene commercial panels these reviews describe — not exhaustive (the full panels include ~20+ additional genes: ATP6V0A4, ATP6V1B1, CLCNKB, HNF4A, HOGA1, SLC12A1, SLC9A3R1, VDR, and others), and that non-exhaustiveness should stay explicit in the write-up rather than implying full coverage.

## Status: Track 1 analysis complete, submission ready (2026-08-31)
- [x] Independent variant discovery from proband's own VCF + phenotype (not copied from leaderboard)
- [x] Rare + damaging filter across 9-gene MVA panel → 2 BUB1B candidates
- [x] Secondary 11-gene phenotype-driven panel → clean, no candidates; panel grounded in cited differential-diagnosis literature
- [x] Phasing limitation identified and honestly documented
- [x] ACMG evidence-code write-up (see `submissions/track1/gummietech_track1_report.md`)
- [x] Final Track 1 CSV + methods report, named per hackathon convention (`gummietech_vep-acmg-compound-het.csv`, `gummietech_track1_report.md`)
- [x] Trust audit / verification pass against primary sources (2026-08-31, see below)
- [x] Formal AlphaMissense/REVEL/CADD/SIFT/PolyPhen2 scoring for PP3 (2026-08-31, see below)
- [x] Final proofread: every gnomAD/ClinVar/UniProt/genotype figure independently re-verified a second time against live primary sources
- [x] GitHub repository created (private; public at hackathon close), patient genomic data excluded per the Data Transfer Agreement
- [x] Code-level audit of the pipeline against the report's claims (2026-08-31, see below) — one real defect found in the AF filter, proven harmless, corrected
- [x] Pipeline consolidated into one CLI-parameterised annotation script + a filter script; full command sequence documented in `pipeline/README.md`
- [x] SpliceAI on secondary intronic finding — **resolved 2026-08-31** via Ensembl VEP's own SpliceAI plugin after three failed attempts against the Broad's standalone Lookup API (see "SpliceAI resolved" section at the end of this file). The two "unreachable" entries below are kept as written for the audit trail.
- [ ] Actual upload via the hackathon's "Submit – Track 1" tab — requires the account holder's own Hugging Face session

## Trust audit — verification against primary sources (2026-08-31)

Prompted by the user asking whether this analysis is actually grounded in trustworthy sources. Ran direct queries against gnomAD, ClinVar, and UniProt (not just VEP's proxy annotation) and found two real errors, now fixed in the draft submission files:

1. **Error found**: the draft claimed p.Asn1002Lys is "absent from gnomAD." **Wrong** — direct gnomAD API query shows it's a singleton (AC=1 of 1,461,878 exome alleles, AF≈6.84e-7). VEP's REST proxy simply hadn't indexed this ultra-rare variant (its `colocated_variants` field was empty for this position) — a real gap in Ensembl's bundled gnomAD annotation, not a script bug. **Fixed** in the CSV and methods report — now correctly states "gnomAD singleton" rather than "absent."
2. **Evidence undersold**: direct ClinVar query (via NCBI eutils) shows the stop_gained variant's classification is stronger than originally reported — VCV000533901.9, "criteria provided, multiple submitters, no conflicts" (2-star), specifically for "Mosaic variegated aneuploidy syndrome 1" (OMIM 257300). **Fixed** — now cited with full accession/review-status detail.
3. **Evidence undersold**: direct UniProt query (O60566) confirms the kinase domain spans residues 766-1050 (protein is 1050 aa total). This means: (a) the stop_gained at 737 removes the *entire* kinase domain (confirmed, not "likely"), and (b) p.Asn1002Lys falls *directly inside* the kinase domain, not just "near" it. **Fixed** — PM1 evidence code now cited with confirmed domain overlap.
4. **Log error found and fixed**: `literature/_fetch_log.md` incorrectly stated Baker et al. 2011 had no available PMC copy. It does — PMC3468323 — now fetched in full, see `literature/04b_baker2011_senescence_clearance_fulltext.md`.
5. **Open item, not yet resolved**: `notes/01_spindle_assembly_checkpoint_biology.md` claims BubR1 has a "KEN-box motif." UniProt's O60566 feature table only lists a D-box (224-232), no KEN-box. Checked the Kops 2012 "unusual pseudokinase" paper abstract directly — see below.
6. **Baker 2011 and Sinclair 2014 core claims re-verified** directly against their actual PubMed abstracts (not WebSearch's paraphrase) — both confirmed accurate, no corrections needed to the strategic Track 2 hypotheses built on them.

This kind of check — querying the primary database directly instead of trusting an intermediate tool's cached/proxied version of it — should be repeated before finalizing any submission, and especially before the Track 2 report leans on any "novel"/"absent from X" style claim.

## Formal in-silico missense predictors for p.Asn1002Lys (2026-08-31)

Direct query against MyVariant.info's dbNSFP aggregation (`chr15:g.40220612T>G`, GRCh38) — a real multi-tool database, not a single proxy — returned:

| Tool | Result | Deleterious? |
|---|---|---|
| **AlphaMissense** | score 0.92 / 0.88 (two transcript annotations), pred "likely pathogenic" both | Yes |
| **CADD** (phred) | 24.5 (top ~0.4% most deleterious genome-wide) | Yes |
| **PolyPhen-2** (HDIV) | 1.0, "probably damaging" | Yes |
| **PolyPhen-2** (HVAR) | 0.997, "probably damaging" | Yes |
| **SIFT** | 0.0, "deleterious" | Yes |
| **REVEL** | 0.472 | **Ambiguous** — below the commonly-used ≥0.5 supporting threshold (and well below the ≥0.7 strong-support threshold some ACMG implementations use) |

**Honest read, not overclaimed**: 5 of 6 individual predictors call this deleterious/damaging, including AlphaMissense (widely regarded as the best-calibrated single tool currently available). But REVEL — the meta-predictor ClinGen's SVI working group specifically recommends over ad-hoc tool-counting for ACMG PP3/BP4 — sits at 0.472, just under its own commonly-cited "supporting" cutoff. **PP3 is invoked as weak/supporting evidence, not strong evidence** — stating this precisely rather than citing only the tools that agree. This doesn't change the overall classification (PVS1 on the first variant already carries most of the weight), but it's the correct, non-cherry-picked way to report it.

## SpliceAI attempt on the secondary deep-intronic finding (2026-08-31)

Attempted a direct query against the SpliceAI Lookup API (`spliceailookup-api.broadinstitute.org`) for `chr15-40216470-A-G` (GRCh38). **Result: connection timeout** — repeated attempts (~75s each) failed at the TCP handshake stage, while the same machine reached `gnomad.broadinstitute.org`, the SpliceAI Lookup *frontend* (`spliceailookup.broadinstitute.org`, HTTP 200), and general internet hosts without issue. This points to the SpliceAI backend API specifically being unreachable/down at time of attempt, not a network-level block on this environment. Not re-attempted further to avoid burning time on a transient external outage.

**Status**: genuinely not resolved, reported honestly as such rather than silently skipped or faked. This is the lowest-priority of the three findings (a secondary/tertiary row, VEP's basic consequence call already doesn't flag it as splice-altering, gnomAD-absent) — retry later (transient outages on public bioinformatics APIs are common) if time allows before final submission; not a blocker.

## Code-level audit of the pipeline (2026-08-31)

The earlier trust audit checked the *claims* against primary databases. This pass checked the *code* against the claims — i.e. does the pipeline actually do what the methods report says it does.

**Defect found: the rarity filter never included gnomAD exomes.** `max_gnomad_af()` accumulated only keys matching `k.startswith("gnomadg")` or `k == "af"`. In the VEP REST response the exome keys are `gnomade`, `gnomade_nfe`, … — and `"gnomade".startswith("gnomadg")` is `False`, so every gnomAD exome frequency was silently dropped, even though the request URL asks for them (`af_gnomade=1`). Worse for the field's name: the bare `af` key it *did* include is the **1000 Genomes** global AF, not gnomAD at all. So the column labelled `gnomad_max_af` was gnomAD-genomes subpopulation maxima mixed with a 1000G figure.

**Why the result still stands — verified, not assumed.** The error is permissive, not exclusionary: excluding a frequency source can only let a variant *through* the AF<0.001 filter, never remove one. So no candidate could have been missed. Rather than reason it out and move on, the corrected computation was replayed offline against the saved raw VEP responses (`vep_raw_responses.jsonl`, `vep_secondary_raw_responses.jsonl` — no live API re-run needed, the audit trail was already on disk):

| Panel | Records | As-run filter | Exome-inclusive filter | Added | Dropped |
|---|---|---|---|---|---|
| Primary (9-gene) | 1281 | 2 candidates | 2 candidates | 0 | 0 |
| Secondary (11-gene) | 1065 | 0 candidates | 0 candidates | 0 | 0 |

p.Leu737Ter's max AF rises from 7.35e-5 to 9.982e-5 (a gnomAD exome subpopulation) — still an order of magnitude below the 0.001 threshold. p.Asn1002Lys stays 0.0 in VEP, which is the under-indexing gap the earlier trust audit already caught and corrected via direct gnomAD query.

**Fixed**: `pipeline/vep_annotate.py` now matches both `gnomadg*` and `gnomade*` and drops the 1000G `af` key. The defect and the offline check are both recorded in the submission's Verification table rather than quietly patched — a reviewer reading the repo would otherwise find the discrepancy themselves.

**Reproducibility gaps closed in the same pass:**
- The filtering step (AF<0.001 + MODERATE/HIGH) had **no code at all** — the candidate list came from inspection. Now `pipeline/filter_candidates.py`, which reproduces the submitted candidate list exactly from the annotated TSVs (2 rows primary, 0 secondary). The hackathon rules require "all scripts/configs needed to reproduce results."
- The two annotation scripts were byte-identical except for three path constants (and the secondary's docstring still said "MVA gene panel" / `Usage: python3 vep_annotate_panel.py`). Merged into one `vep_annotate.py` taking `--vcf`/`--out-tsv`/`--out-raw`, which also removes the hardcoded `/Users/kiki/...` paths the report previously had to apologise for.
- The `bcftools view -R` region-restriction step was described in the methods but recorded nowhere. Now in `pipeline/README.md` with the actual commands for both panels.
- Latent bug fixed while in there: the genotype lookup matched on `(chrom, pos)` only, ignoring ref/alt, so a multi-allelic site could have attached the wrong genotype to a row. Now matches the full key with a single-record positional fallback for VEP-normalised indels. Never affected a reported variant — all three matched exactly — and the genotypes in the submission were independently confirmed by direct `bcftools` query anyway.

**ACMG evidence codes tightened** (classification unchanged — PVS1 carries the weight):
- **PS4 dropped.** It was cited for the ClinVar classification, but PS4 is the case-control prevalence code and no case-control data was generated here. The code that formally covers a reputable-source classification is PP5 — which ClinGen's SVI working group has recommended against since 2018 as double-counting. The ClinVar concordance is now reported as corroboration, explicitly not scored.
- **PM2 → PM2_Supporting** on both variants, following the ClinGen SVI recommendation adopted by most VCEP specifications rather than the 2015 guidelines' default Moderate.
- **PVS1 strengthened**: added the NMD assessment (stop at codon 737 of 1050, well upstream of the final exon-exon junction → NMD-predicted), which is the first branch of the ClinGen PVS1 decision tree and was conspicuous by its absence.

**SpliceAI retried** for `chr15-40216470-A-G`: still a hard timeout (HTTP 000 after 45s). Now documented as a persistent outage across two independent attempts rather than a single transient failure.

## Second audit pass (2026-08-31) — auditing the audit

Re-audited Track 1 after the first remediation pass, deliberately targeting the material written *during* that pass, since that is the least-reviewed content in the submission. All prior figures re-confirmed against live APIs; three real problems found, all introduced by the previous pass.

**Live re-verification (all exact):** gnomAD v4 GraphQL returns p.Leu737Ter exome AC=115/1,461,846 AF=7.867e-5, genome AC=5/152,174 AF=3.286e-5; p.Asn1002Lys exome AC=1/1,461,878 AF=6.841e-7 with no genome record (singleton confirmed); the secondary intronic variant "Variant not found" (genuinely absent). ClinVar esummary returns VCV000533901.9, Pathogenic/Likely pathogenic, "criteria provided, multiple submitters, no conflicts", trait "Mosaic variegated aneuploidy syndrome 1", NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter), last evaluated 2024-10-09. Variant counts re-derived by direct `bcftools`: primary panel 1288 records / 1281 PASS, secondary 1085 / 1065 PASS. Genotypes exact: 0/1, AD 21,25 DP 46 GQ 99 and AD 15,13 DP 28 GQ 99.

**Problem 1 — the NMD claim was right but the stated reasoning was not.** The previous pass justified NMD with "roughly 70% through the coding sequence and well upstream of the final exon-exon junction." Position within the CDS does not establish where the last exon-exon junction is; that was an assertion dressed as an argument. Checked properly against the Ensembl transcript structure for ENST00000287598 (23 exons, CDS 3153 nt): c.2210 is in **exon 17 of 23**, the final exon-exon junction is at **CDS 2957**, so the premature stop is **747 nt upstream** of it — far outside the ~50-55 nt escape window. Conclusion unchanged, reasoning now actually verified.

**Problem 2 — variant 2's classification was banking the tentative PM3.** The report scored variant 2 at PM1+PM2_Supporting+PM3(tentative)+PP3(weak) = 6 points and called it "also Likely Pathogenic" — while the Limitation section simultaneously said phase was unresolved. PM3 *is* the phase-dependent code. Withhold its 2 points and variant 2 is 4 points, a VUS; withhold the weak PP3 too and it is 3. This was the report contradicting itself: treating phase as unresolved in one section and spending its evidence in another. Now stated plainly — in isolation variant 2 is a **VUS pending phase confirmation**, and the compound-het call rests on variant 1 reaching LP on its own (9 points) plus PP4 plus the Limitation-section reasoning, not on variant 2 classifying independently.

**Problem 3 — the REVEL threshold citation was imprecise in a way that flattered the result.** The report cited 0.472 as "just under its commonly-used ≥0.5 supporting threshold." But the ClinGen SVI calibration (Pejaver et al. 2022) — the same work that grounds the report's own "use a calibrated predictor, don't count tools" claim in the very same sentence — sets PP3_Supporting at REVEL ≥0.644 and BP4_Supporting at ≤0.290. 0.472 is not "just under" anything; it is in the **indeterminate band**, supporting neither direction. Strictly applied, REVEL yields no PP3 at all here. Now stated that way, which weakens PP3 slightly and is the honest reading.

**Added:** a Verification row recording that all three HGVS coding positions were reconstructed independently from Ensembl exon coordinates rather than trusting VEP's own HGVS output — 40209701 → 66 nt into exon 17 (CDS 2144-2284) → c.2210; 40220612 → 48 nt into exon 23 (CDS 2958-3153) → c.3006; 40216470 → 1026 nt before the exon 21 acceptor at 40217496 → c.2679-1026. All three match exactly. Also clarified the working directory assumed by the commands in `pipeline/README.md`.

**Net effect on the submission:** no variant, coordinate, or CSV row changes. The overall classification stays Likely Pathogenic (compound heterozygous). What changes is that two overclaims are removed and one unsupported inference is replaced with a verified one.

## SpliceAI resolved via the VEP plugin (2026-08-31, third pass)

Supersedes the two "SpliceAI unreachable" entries above, which are left unedited as an
audit trail of what was tried and when.

**What was wrong with the earlier conclusion.** Both previous attempts hit the Broad's
standalone SpliceAI Lookup API (`spliceailookup-api.broadinstitute.org`) and both timed
out, and the analysis concluded the question was unanswerable. It was not. Ensembl VEP
serves SpliceAI through its own plugin, behind a single `&SpliceAI=1` query parameter on
the REST endpoint **this pipeline was already calling for every variant**. A third attempt
against the Broad API also failed; the plugin route worked first try. The failure was one
of not asking the tool already in hand, not of external availability.

**What was done.** `pipeline/vep_annotate.py` gained `&SpliceAI=1` and a `max_spliceai_ds()`
function; both panels were re-annotated from scratch (which also regenerated them with the
already-corrected `max_gnomad_af`, so the exome-frequency defect is no longer a replay
argument). The new `spliceai_max_ds` column is the max of DS_AG/DS_AL/DS_DG/DS_DL across
transcripts, and is **blank rather than 0.00** where SpliceAI has no data — 592 of 2,346
rows (227 indels, 365 SNVs, predominantly intronic/downstream/upstream). Blank is never
counted as zero: `filter_candidates.py` does not read the column, and the screen guards on
`$11!=""`.

**Results.**

- Deep-intronic secondary candidate `15:40216470 A>G`: **0.00 on all four delta scores,
  across all 22 BUB1B transcripts.** The pseudoexon/cryptic-splice hypothesis is not
  supported. EPCR lowered 0.30 → 0.10 in the submission CSV.
- p.Leu737Ter: 0.03 (acceptor gain) on all 22 BUB1B transcripts — no cryptic-splice rescue
  of the premature stop, so PVS1 rests on NMD as claimed.
- p.Asn1002Lys: 0.00 on all 22 BUB1B transcripts. The 0.02 recorded in `spliceai_max_ds`
  comes from two overlapping *PAK6* transcripts, not from BUB1B.
- Panel-wide screen of all 2,346 PASS variants: **none** reaches the 0.2 high-recall
  threshold. Primary panel 1,007/1,281 scored (78.6%), max 0.18; secondary 747/1,065
  (70.1%), max 0.13. The 0.18 is a common MAD1L1 intronic polymorphism at gnomAD AF 0.771.
  Among the 14 rare (AF<0.001) scored variants the max is 0.03.

**Net effect on the submission:** the primary finding, its coordinates, and its EPCR are
unchanged (still 2 candidates primary / 0 secondary). The secondary row's EPCR drops to
0.10 on a negative result that was obtained rather than assumed, and a disclosed blind spot
(splice-altering variants hiding below the MODIFIER filter) is now closed and negative
rather than merely disclosed.

## Third audit pass (2026-08-31) — auditing the SpliceAI re-annotation

An independent correctness-and-consistency audit of the five files the SpliceAI work
touched. Code, arithmetic, and reproducibility came back clean: `max_spliceai_ds()` does
what all three documents say, every figure re-derived from the TSVs matched exactly, and
all four commands in `pipeline/README.md` reproduce their stated output. Fixed:

1. **The report's "Submitted predictions" section still said the secondary row was at
   EPCR 0.30** — the one sentence whose job is to describe the submitted CSV, contradicting
   both the CSV (0.10) and two other passages in the report. Corrected.
2. **"Every PASS variant now carries a SpliceAI score"** — false, and contradicted twelve
   lines later by the report's own coverage figure. Reworded to the real number (1,754 of
   2,346).
3. **The 0.02 on p.Asn1002Lys was described as coming from "two non-canonical transcripts"**
   — they are *PAK6* transcripts, a different gene. The true result (0.00 on all 22 BUB1B
   transcripts) is cleaner than what was claimed; the text now says so.
4. **"The deep-intronic variant reported below"** — it is reported above; the section
   reorder inverted the reference.
5. **"Mostly indels and upstream positions"** for the 592 blanks — only just true (52%),
   and silently omitting the two next-largest categories. Replaced with the actual
   composition, in the report, `pipeline/README.md`, and the `max_spliceai_ds` docstring.
6. **Three clinical claims introduced in the rewrite were asserted from general knowledge
   with no traceable source** — nephrocalcinosis of prematurity/VLBW, ifosfamide/platinum
   nephrotoxicity, and the embryonic-lethality premise behind the recurrent-miscarriage
   reasoning. All three are very likely correct, but in a report that cites a source for
   every comparable claim, an uncited one reads as verified when it is not. They are now
   explicitly marked as unsourced background, and the miscarriage argument is stated as the
   conditional it actually is. Note this partly reverses this log's earlier position (line
   55) that the miscarriage history was "not something this analysis can or should claim to
   explain" — the report now offers a framing, hedged, and says it carries no PP4 weight.
   **If anything here gets sourced before submission, these are the three to source.**
7. **SpliceAI's 0.2/0.5/0.8 thresholds** were attributed only to "SpliceAI's own
   thresholds" while the comparable REVEL thresholds cite Pejaver et al. 2022. Now
   attributed to Jaganathan et al. 2019 and the tool's documentation — **added from general
   knowledge during this pass, so worth a confirming glance.**
8. Cosmetic: a docstring cross-reference pointing "below" at a function defined above; a
   Verification-table source cell still describing the offline replay after the live
   re-annotation superseded it; "across all nine panel genes" for 10 variants that span
   five of the nine.

Also brought two files outside the SpliceAI diff back into line: the root `README.md` still
listed SpliceAI as outstanding and unreachable, and this log's own checkbox was unticked.

**Net effect on the submission:** one real correction to a submitted-artefact description
(the EPCR 0.30/0.10 mismatch). No variant, coordinate, CSV value, or classification changes.
