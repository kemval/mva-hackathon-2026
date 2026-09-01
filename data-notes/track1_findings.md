# Track 1 Findings — Working Notes

Generated: 2026-08-31, from independent analysis of the proband's own VCF + HPO phenotype (not copied from the Track 1 leaderboard).

## Pipeline run

1. Downloaded VCF only (`data-notes/raw/WGS_EX2312012_HGWCNDSX7.vcf.gz`, 315MB, GRCh38, single-sample proband-only).
2. Looked up exact GRCh38 coordinates for a 9-gene MVA panel (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, BUB1, BUB3) via Ensembl REST — see `data-notes/regions/mva_gene_panel_grch38.tsv`.
3. Region-restricted the VCF to these 9 genes ± 2kb padding via `bcftools view -R` — 1288 variants total, 1281 PASS (`data-notes/mva_panel_variants.vcf.gz`).
4. Annotated all 1281 PASS variants via Ensembl VEP REST (consequence, canonical HGVS, max gnomAD population AF, ClinVar significance) — `data-notes/annotated/vep_panel_annotated.tsv`, raw API responses in `vep_raw_responses.jsonl`.
5. Filtered to gnomAD AF < 0.001 + MODERATE/HIGH impact.

## Result: two strong candidates, both in BUB1B, both heterozygous

| Position (GRCh38) | Change | Consequence | Impact | HGVS | gnomAD max AF | ClinVar | Genotype |
|---|---|---|---|---|---|---|---|
| 15:40209701 | T>G | stop_gained | HIGH | c.2210T>G, p.Leu737Ter | 0.000073 (rs759242053) | **likely_pathogenic;pathogenic** | 0/1 |
| 15:40220612 | T>G | missense_variant | MODERATE | c.3006T>G, p.Asn1002Lys | 0.000000 (absent from gnomAD) | none on record | 0/1 |

A third, lower-priority candidate in the same gene: 15:40216470 A>G, deep intronic (c.2679-1026A>G, 1026bp from nearest splice site), gnomAD AF 0.000000, MODIFIER impact — not flagged as splice-altering by VEP's basic consequence call; would need SpliceAI to properly assess. Sits physically between the two exonic candidates.

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

## Status: Track 1 analysis substantively complete
- [x] Independent variant discovery from proband's own VCF + phenotype (not copied from leaderboard)
- [x] Rare + damaging filter across 9-gene MVA panel → 2 BUB1B candidates
- [x] Secondary 11-gene phenotype-driven panel → clean, no candidates
- [x] Phasing limitation identified and honestly documented
- [x] ACMG evidence-code write-up (done, see `submissions/track1/DRAFT_methods_report_v1.md`)
- [x] Draft Track 1 CSV + methods report (done, v1)
- [x] Trust audit / verification pass against primary sources (2026-08-31, see below)
- [x] Formal AlphaMissense/REVEL/CADD/SIFT/PolyPhen2 scoring for PP3 (2026-08-31, see below)
- [ ] SpliceAI on secondary intronic finding — attempted, service unreachable (see below); not blocking, low-priority secondary row

## Trust audit — verification against primary sources (2026-08-31)

Prompted by the user asking whether this analysis is actually grounded in trustworthy sources. Ran direct queries against gnomAD, ClinVar, and UniProt (not just VEP's proxy annotation) and found two real errors, now fixed in the draft submission files:

1. **Error found**: the draft claimed p.Asn1002Lys is "absent from gnomAD." **Wrong** — direct gnomAD API query shows it's a singleton (AC=1 of 1,461,878 exome alleles, AF≈6.84e-7). VEP's REST proxy simply hadn't indexed this ultra-rare variant (its `colocated_variants` field was empty for this position) — a real gap in Ensembl's bundled gnomAD annotation, not a script bug. **Fixed** in the CSV and methods report — now correctly states "gnomAD singleton" rather than "absent."
2. **Evidence undersold**: direct ClinVar query (via NCBI eutils) shows the stop_gained variant's classification is stronger than originally reported — VCV000533901.9, "criteria provided, multiple submitters, no conflicts" (2-star), specifically for "Mosaic variegated aneuploidy syndrome 1" (OMIM 257300). **Fixed** — now cited with full accession/review-status detail.
3. **Evidence undersold**: direct UniProt query (O60566) confirms the kinase domain spans residues 766-1050 (protein is 1050 aa total). This means: (a) the stop_gained at 737 removes the *entire* kinase domain (confirmed, not "likely"), and (b) p.Asn1002Lys falls *directly inside* the kinase domain, not just "near" it. **Fixed** — PM1 evidence code now cited with confirmed domain overlap.
4. **Log error found and fixed**: `literature/_fetch_log.md` incorrectly stated Baker et al. 2011 had no available PMC copy. It does — PMC3468323 — now fetched in full, see `literature/04b_baker2011_senescence_clearance_FULLTEXT.md`.
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
