# MVA Hackathon 2026 — Project Workspace

**Team:** Gummietech
Working directory for "Rare Disease, Real Kid: The MVA Hackathon 2026" (SageBio / Hugging Face / MVA Society / BEACON, prizes from AWS + Anthropic). Submissions close **Oct 24, 2026 23:59 UTC**.


## Folder structure

- `literature/` — full text of open-access papers, guideline documents, and official reference material (site captures, journal articles, tool documentation). Start with `00_hackathon_site_full_capture.md` (the complete live-site capture: Overview, FAQ, Official Rules, both Submit tabs, leaderboard snapshot) and `_fetch_log.md` (fetch status and provenance of every source).
- `notes/` — original synthesis documents covering material from copyrighted textbooks (not bulk-reproduced) — mitosis/spindle-checkpoint biology, ACMG variant classification workflow, VCF/BAM/HPO pipeline mechanics, drug repurposing methodology. Orientation material; the primary literature in `literature/` is the citation-grade source.
- `data-notes/` — working analysis notes on the case (gene-panel coordinates, variant candidates, ACMG evidence, phasing analysis). Raw and derived patient genomic data are excluded from version control per the dataset's Data Transfer Agreement — see `data-notes/README.md`.
- `pipeline/` — annotation and filtering scripts, plus `pipeline/README.md` recording the exact end-to-end command sequence (Ensembl REST coordinate lookup → padded BED → `bcftools` region restriction → VEP REST annotation → rare/damaging filter). Both scripts are CLI-parameterised; running them against the annotation output reproduces the submitted candidate list exactly.
- `submissions/` — Track 1 and Track 2 submission materials (predictions CSV, methods reports, pitch script, clinician one-pager).
- `graphify-out/` — knowledge graph built from `literature/` + `notes/` (gitignored, regenerable via `/graphify --update`).

## Knowledge graph

Built from `literature/` + `notes/`: 285 nodes / 359 edges / 15 communities as of the last
update (2026-08-31).

> **Known stale as of 2026-09-04, and not refreshable on this machine.** An incremental
> scan run on 2026-09-04 detected 12 code, 36 doc and 11 paper files changed plus 3 deleted
> — but semantic extraction of the 47 changed doc/paper files needs an LLM backend, and
> none is reachable here: no `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_API_KEY`,
> `OPENAI_API_KEY`, `MOONSHOT_API_KEY` or `DEEPSEEK_API_KEY` is set, and `ollama` is not
> installed. `--code-only` would index the code and **drop the literature nodes**, which are
> the part worth having, so it was not used. The graph therefore does **not** yet include
> `literature/31`–`34`, `data-notes/scale/`, the cohort table, or any of the 2026-09-02
> onward work. Regenerate with `graphify /Users/kiki/mva-hackathon-2026 --update` on a
> machine with a key set. **Nothing in the submission depends on the graph** — it is a
> navigation aid over files that are all present and readable directly. Query with `graphify query "<question>"` or `graphify path "<a>" "<b>"` instead of re-reading raw files. Re-run `/graphify /Users/kiki/mva-hackathon-2026 --update` after adding or editing files in `literature/` or `notes/`.

## Track 1 status (2026-08-31) — analysis complete, submission-ready

A pipeline (region-restriction via `bcftools` → annotation via Ensembl VEP REST → ACMG/AMP-lite filtering) was run against the proband's own VCF and HPO-coded clinical phenotype. Result: a compound-heterozygous candidate in **BUB1B** — a ClinVar-classified pathogenic nonsense variant (p.Leu737Ter) paired with a rare missense variant (p.Asn1002Lys) in the kinase domain — plus a lower-confidence deep-intronic secondary finding.

A note on what "independent" does and does not claim here, to match the methods report's own scoping rather than overstate it: the **search space** is a literature-defined 9-gene MVA panel, which presupposes MVA as the working diagnosis and so cannot distinguish discovery from confirmation. The **variant call within that space** comes from filtering the proband's own VCF by executable code (`pipeline/`), and every frequency, clinical-classification, domain, and predictor claim was re-verified against primary sources. This repository also contains a capture of the public leaderboard (`literature/00_hackathon_site_full_capture.md`), on which the answer gene is visible, and the analysis lands in a small number of commits — so the artefacts cannot *demonstrate* that the gene was reached blind, and no such claim is made.

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
9. Final pre-submission audit (2026-09-01), run against primary artefacts rather than the previous passes' conclusions. Every figure re-derived from the VCF, the annotated TSVs and the raw VEP JSON matched exactly, all four `pipeline/README.md` commands reproduced their stated output, and every external claim re-queried live (ClinVar `VCV000533901.9`, gnomAD v4, UniProt O60566) matched to the digit. It closed the two loose ends the previous pass had flagged — the SpliceAI threshold attribution, confirmed verbatim against Illumina's documentation, and the phasing claim, confirmed by showing the caller does emit `PGT`/`PID` elsewhere in the region but not for these variants — and found one real overclaim: the PP4 argument that rhabdomyosarcoma rules out CEP57 rested on "malignancy not reported in MVA2," which this repo's own captured JCI paper (Cep57 as a haploinsufficient tumour suppressor) contradicts. That claim is withdrawn and replaced with the stronger, previously unstated variant-level exclusion: the proband has no rare damaging variant in either CEP57 or TRIP13. No variant, coordinate, EPCR or classification changed.
10. Expert-panel remediation pass (2026-09-01), against a blind review that scored the submission 75.0/100. Four of its five findings were accepted and fixed: the phase paragraph still argued from the kinase-domain location and predictor concordance that the PM1 and PP3 sections withdraw (corrected); the karyotype was named as the unassayed discriminating feature and then not recommended (it is now the **first** confirmatory test, ahead of parental Sanger, because it tests the diagnosis rather than the phase); PM3 was retained at the 2015 default Moderate while PM2 followed ClinGen SVI (PM3 now scored on the SVI recessive point scheme, where a single proband of unresolved phase scores 0.25 points and **PM3 drops out entirely** — variant 2 falls to 2 points, still VUS); and the NF1 non-PASS count was wrong (8 records, 7 `MQ40`, not seven and six — re-derived from the VCF). The fifth finding, that the PM2 max-credible-AF derivation misplaced the allelic-contribution term, was checked against the Whiffin/Ware framework's own manuscript source and **declined**: the recessive form is `sqrt(P) x A x sqrt(G) / sqrt(f)`, with the allelic term outside the root exactly as the report had it, and the worked case offered as proof cannot discriminate the two placements since they coincide at A = 1. The derivation is now given in full rather than asserted, and the half of that finding which was valid — that G and A were presented as inputs while only prevalence was flagged unsourced — is fixed. No variant, coordinate, EPCR, candidate set or pipeline code changed.

11. Exhaustive numeric re-audit (2026-09-01), triggered by one defect found while building the visual explainer. Every figure in the report was re-derived from primary artefacts — the region-restricted VCFs, the annotated TSVs, `vep_raw_responses.jsonl` and the genome-wide VCF — and every external claim re-queried live against gnomAD, ClinVar and UniProt. **Roughly sixty independent figures reproduce exactly**, including all 23 Ensembl exon coordinates, all five permissive deletion windows *then listed* and the exons each contains (that pass checked the entries; item 14 below tested the list itself and found a sixth), all 20 gene and flanking call densities, every SpliceAI count, and every population and clinical-classification figure. **Six were wrong and are corrected.** The substantive two: the PM1 section described the BubR1 kinase domain as "marginally denser" in missense than the rest of the protein when its own table shows the opposite (1.12 vs 1.25 per residue — the PM1 rejection is unaffected, because 320 distinct variants across 69.8% of residues is not the absence of benign variation the criterion asks for); and the callability ratio for **CEP57 was 0.17 where the true value is 0.19**, which had directly contradicted the report's own prose that CEP57 yields "5.4x fewer calls than its own flanking sequence" (1/5.4 = 0.185). The prose was right and the table wrong. The remaining four are precision: five further ratio cells moved by one display step once the whole column was recomputed from unrounded densities, the density range is 43-fold rather than 45, per-gene depth medians span 17-51 rather than 17-49, and BUB1B's median depth is 39 rather than 40. One claim was flagged as suspect and then **proved correct** — the 227-indel/365-SNV composition of the 592 unscored SpliceAI rows, which only reads as 173/419 if VEP's `-` allele notation for single-base indels is ignored; that trap is now recorded in the report's Verification table. Separately, the deletion-confirmation email differs between the Official Rules and the dataset card's own gated-access agreement, so both are now cited above. No variant, coordinate, classification, EPCR or candidate-set figure changed.
12. Dataset scope settled against the repository manifest (2026-09-01). The hackathon site describes raw sequencing data as available "optionally in BAM/CRAM"; **the dataset contains neither.** Its 13 files total 79 GB of which 78.9 GB — 99.7% — is raw FASTQ across four lanes, and every non-FASTQ file is already held here. There is consequently no coverage track to download and none to slice out of a remote alignment; the only route to one is aligning the FASTQ. The report therefore keeps its explicitly-labelled call-density proxy. `pipeline/coverage_analysis.py` is retained as a specification of what would settle the question; the fetch script written against the site's BAM/CRAM claim has been removed as unfounded. Details in `pipeline/README.md` section 6. **Superseded in part by item 13.**

13. Coverage limitation re-costed, and an overclaim of this repository's own withdrawn (2026-09-04). Item 12 above stated the callability limitation "cannot be closed by acquiring data," justified on the RAM cost of a human-genome aligner index against 8 GB installed. **That argument does not apply to the route anyone would actually take.** The question concerns a 9-gene panel, not a genome: a reduced reference over the panel and PGx regions indexes in roughly 30 MB, and the RAM objection is nowhere near binding. The real costs, re-measured, are ~79 GB of transfer, mandatory streaming (free disk is now **20 GB**, not the 33 GB stated above), and a multi-day run on 8 cores — machine limits a cloud instance dissolves, not impossibilities. What actually binds is a **scientific** objection the old text never raised: a decoy-free targeted reference inflates MAPQ, because a read from a paralogue elsewhere has nowhere else to map and lands confidently on the only copy present, manufacturing false coverage indistinguishable from real coverage. Queried live against UCSC `genomicSuperDups`, that risk **splits the route in two**: BUB1B has **zero** segmental duplications in its gene body or padded region (nearest is 5.5 kb upstream, outside), so for the callability question the route is sound; CYP2D6 has **six**, including a 9.0 kb ↔ 10.5 kb pair at 97.0% identity, so for the pharmacogenomic question it is not. The limitation is therefore **not closed and differently open** than this repository said: feasible by a route not run, at named costs, with one named failure mode. No variant, coordinate, classification or EPCR changed. Full re-costing in `pipeline/realignment_feasibility.md`; corrected in `pipeline/README.md`, `data-notes/track1_findings.md` and the Track 1 report.

14. Completeness audit of the Track 1 bounds (2026-09-04), asking of each list in the report not whether its entries are right but whether the list is complete. Three defects, one of them substantive. **The permissive multi-exon-deletion window list was short by one window.** The report bounds a hemizygous BUB1B deletion to the intervals between the proband's heterozygous calls and named five; the interval between the deep-intronic call and p.Asn1002Lys — **40,216,470-40,220,612, 4,142 bp, fully containing exons 21 and 22** — is permissive on identical reasoning and was never listed. The two previous audits both verified that each listed window contained the exons claimed, which was true, and neither asked whether one was missing; `pipeline/coverage_analysis.py` carried the same five hardcoded, copied from the report's prose, so the code inherited the omission rather than catching it. The list is now **derived** by `pipeline/deletion_windows.py` from the het calls and the Ensembl exon structure, and `WINDOWS` is regenerated from it. The same derivation produced a second finding the prose had no column for: **three of the six windows delete in-frame** (402, 477 and 279 nt), so the allelic-architecture prior — which disfavours a deletion in trans because it would make a truncating/truncating genotype, and which was one of the two things pushing the EPCR *up* — applies to only half the windows and is correspondingly weakened. The other two defects are stale text that survived its own correction: the section on the two out-of-spectrum features still closed by asserting nephrocalcinosis had "a probable acquired cause," four paragraphs after withdrawing exactly that conclusion, and the Verification table still credited the Aziz *JCI* authors with *recommending* cancer surveillance — the precise overclaim the body text retracts. Both removed. **No variant, coordinate, classification, candidate-set figure or EPCR changed**; the deletion bound is wider than stated and the argument narrowing it is weaker.

**Outstanding (does not block submission):**
- Actual upload via the hackathon's "Submit – Track 1" tab, which requires the account holder's own Hugging Face session.

## Track 2 status (2026-09-02; audited 2026-09-04) — analysis complete, every figure re-derived

A mechanism characterisation, a pre-registered drug search, a patient-specific
pharmacogenomic screen, and a ranked candidate list with an explicit rejected tier.

**The central finding is a correction to the obvious reading of the genotype.** The
intuitive move — "the mitotic checkpoint kinase is broken, so target the checkpoint" — is
wrong, and it sends the drug search the wrong way. Suijkerbuijk et al. 2010 studied MVA
patient cells carrying exactly this architecture (a truncating allele paired with a
kinase-domain missense allele) and showed the defect is **insufficient BubR1 protein**,
not defective enzymology — and that **forcing abundance back up fully restores checkpoint
function**, with a threshold between ~6% and ~13% of normal. The therapeutic target is
protein quantity. That reframing explains why BUB1B has zero drugs, selects a different
candidate class from the crowd answer, survives Track 1's unresolved phase (cis or trans,
the shared consequence is low abundance), and generates contraindications no pathway
search would surface.

**The search's structural finding.** Across 24 pathway genes and two independent
databases, **129 of 142 action-typed Open Targets entries are inhibitors** — ~95%
inhibitory against a disease of deficiency. (Drug availability also rose with distance from
the defect across this curated node set, 0 at BUB1B to 71 at the SASP tier, but that pattern
did **not** survive a mechanical tier rule and is reported below as an artefact of the
curation.) The only approved drug
annotated as activating anything is an antiemetic against TP53, a spurious annotation.
**That generalisation was pre-registered as a falsifiable prediction, tested on three
further diseases, and partly refuted by our own test** (`data-notes/scale/RESULTS.md`). The
skew does not track loss-of-function: NPC1 measures 54.5% strictly inhibitory and CFTR
37.5%. It tracks whether the causal gene sits in a pathway oncology has invested in
inhibiting — BUB1B 95.8%, ATM 93.4%. All figures use the same counting unit as the report's
own 129/142 (unique gene-drug-action triples), which `scale_measure.py --selfcheck`
re-derives before emitting anything else. The corrected rule is narrower and diagnostic: it says in advance
which rare diseases face this problem, and BUB1B is in the worst category. The monotonicity
claim did not survive a mechanical tier rule either, and is reported as an artefact of the
original curation.

**Ranked answer.** Highest overall: **nicotinamide riboside** (13/17) — a dietary
supplement, not an approved medicine, and the report does not blur that. Highest approved
medication: **dasatinib + quercetin** (10/17), where none of 22 trials ever enrolled a
child. Three agents excluded by hard gates fixed before the search, including HSP90
inhibitors — predicted to destroy the residual BubR1 this child depends on, and
simultaneously the lead compound of the best-known "drugs for aneuploidy" paper.

**What is actually recommended first is not a drug** but a western blot for BubR1, which
forks the whole hypothesis and would additionally generate PS3-grade functional evidence
on Track 1's unresolved VUS.

**Patient-specific layer.** A CPIC-guided PharmCAT screen of the proband's own genome.
Its headline is an honest negative: only 22 of 1,226 positions carry a call, and **16 of
23 genes change call** when absent positions are assumed reference — an assumption
PharmCAT's own CLI labels "DANGEROUS!". It also caught a false alarm worth catching:
PharmCAT reports RYR1 rs35364374 as "Uncertain Susceptibility" to malignant hyperthermia,
while ClinGen's expert panel classifies that exact variant **Benign**.

Materials: `submissions/track2/gummietech_track2_report.md` (report),
`pitch_script.md` (3-minute video script, 433 spoken words against a 435 budget, timed),
`clinician_onepager.md` (plain-language summary), and
`viz/track2_explainer.html` (visual explainer, companion to the Track 1 atlas). Working notes in
`data-notes/track2_mechanism.md`; scripts and commands in `pipeline/README.md`.

**Outstanding (account-holder actions):** record and upload the pitch video (deck ready at
`viz/pitch_deck.html`, script at `submissions/track2/pitch_script.md`); submit via the
"Submit – Track 2" tab.

## Gap-closure programme (2026-09-02 to 2026-09-04) — all six tasks complete

`pipeline/gap_closure_brief.md` pre-specified six gaps and a pre-committed acceptable-null
outcome for each. All six have now run; the per-task outcome table is at the head of that
file. Three of the six returned **honest negatives**, which the brief counts as completed
tasks:

- **Task 2** established that the genotype-stratified question it asked **cannot be
  answered** — exactly one published patient shares the proband's architecture *and* has a
  tumour outcome. What the 15-patient cohort does show is that the birth-to-7y renal
  ultrasound window fits Wilms and is silent on everything else: the two published MVA
  rhabdomyosarcomas were in the **soft palate** and the **orbit**, the only patient with
  sequential primaries had her second at **12**, and one patient's first malignancy was at
  **34**. It also found a third allelic class the brief did not anticipate — truncating
  plus **non-coding regulatory**, in two independent pedigrees, which can only reduce
  protein quantity.
- **Task 3** confirmed its own premise quantitatively — of 62 "premature chromatid
  separation" records, only **21** are reachable through the "mosaic variegated aneuploidy"
  string — and then **did not close the gap**: seven national databases and the
  native-script terms were not queried, and six full texts hit genuine walls. The blind
  spot is now measured rather than asserted.
- **Task 5** withdrew a standing overclaim of this repository's own (see item 13 above).

**And one result was not asked for and cuts against the submission.** The Part 8
generalisation — that the loss-of-function/inhibitor mismatch holds for rare disease
broadly — was pre-registered as a falsifiable prediction, tested on NPC1, ATM and CFTR, and
**partly refuted**. Two of three predictions failed. The claim is withdrawn and replaced
with a narrower, diagnostic one: the skew tracks whether the causal gene sits in a pathway
oncology has invested in inhibiting (BUB1B **95.8%**, ATM **93.4%** strict inhibitory), not
whether the disease is loss-of-function (NPC1 **54.5%**, CFTR **37.5%**). BUB1B is in the
worst category. Details in `data-notes/scale/RESULTS.md`.

## Submission checklist

| Item | Track 1 | Track 2 |
|---|---|---|
| Report | `submissions/track1/gummietech_track1_report.md` | `submissions/track2/gummietech_track2_report.md` |
| Predictions CSV | `submissions/track1/gummietech_vep-acmg-compound-het.csv` | n/a |
| **Methods description** | `submissions/methods_description_gummietech.xlsx` (+ Markdown mirror) | same file, Track 2 sheet |
| GitHub repo URL | https://github.com/kemval/mva-hackathon-2026 | same |
| Pitch video URL | n/a | **outstanding** — record from `viz/pitch_deck.html` |
| Notes for judges (optional) | n/a | `submissions/track2/notes_for_judges.md` |

## Next actions

1. Submit Track 1 via the hackathon site (account-holder action).
2. Record the 3-minute Track 2 pitch video from `submissions/track2/pitch_script.md` and
   submit Track 2 (one team member submits on the team's behalf; the panel reviews only
   the latest of up to 3 entries).

## Standing obligations

- **Data deletion.** Per the Official Rules, all dataset copies must be deleted from every environment (local machines, cloud instances, notebooks, private repos, intermediate and derived datasets) within **30 days of hackathon close**, and deletion must be confirmed by email. **Two different addresses appear in the source material and the confirmation should go to both:** the Official Rules give `RarediseaserealkidMVAhackathon2026@synapse.org`, while the gated-access agreement on the dataset card itself — the text actually agreed to at download — gives `MVAHackathon2026@synapse.org`. This covers `data-notes/raw/`, `data-notes/annotated/`, and the region-restricted VCFs — all gitignored, so none of it is in git history, but all of it is on disk.
- **Repository visibility.** The repo may stay private during the hackathon but must be made public once it closes so the expert panel can review the code.
