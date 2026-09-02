# Contradiction Matrix

Adversarial cross-examination of the Track 2 evidence base, 2026-09-02. Every pair of
sources making claims about the same object is recorded as **AGREE**, **DISAGREE**, or
**SUPERSET**, with an adjudication and the grounds for it.

Conflicts are ordered by **whether they change a recommendation**, not by how interesting
they are. C1 and C2 change recommendations. C3 changes a rationale. C7 changes provenance.
The rest confirm or bound existing positions.

---

## C1 — "Senolytic" is not a safe class label here — **CHANGES A RECOMMENDATION**

| Source | Claim about HSP90 inhibition |
|---|---|
| Fuhrmann-Stroissnigg 2017, *Nat Commun* (`28_`) | HSP90 inhibitors **are senolytics**; 17-DMAG extended healthspan in `Ercc1−/∆` progeroid mice; ≥7 chemotypes active |
| Suijkerbuijk 2010, *Cancer Res* (`15_`) | MVA missense BubR1 is an **HSP90 client**; geldanamycin depletes it, CHX+GA removes "virtually all mutant BUBR1 protein" |
| Tang 2011, *Cell* (`26_`) | 17-AAG is **aneuploidy-selective at 100 nM** because "aneuploid cells rely on protein quality control pathways for their survival" |

**Relation: AGREE on the biology, and that is precisely the problem.** No source is wrong.
Each is correct in its own frame, and the frames collide only when all three are applied to
one patient.

**Adjudication.** The Track 2 report rejects 17-AAG under gate G1 as an *aneuploidy-drug*
finding, and separately ranks **dasatinib + quercetin** as its highest-scoring approved
medication under a **senolytic** rationale. Fuhrmann-Stroissnigg 2017 shows those are not
two disjoint categories: HSP90 inhibition is a recognised senolytic mechanism, benchmarked
in the same assay as D+Q and navitoclax, and 17-DMAG carries **the strongest progeroid-mouse
in vivo healthspan data of the compounds screened there**. So a clinician or a future search
framed as *"choose the best-evidenced senolytic for a progeroid-like child"* lands on the
one mechanism predicted to destroy the residual BubR1 this child depends on — reaching the
contraindicated agent through the senolytic door, which the report leaves open, rather than
the aneuploidy door, which it closes.

**Why the finding cannot be discounted.** Tchkonia, Kirkland, Niedernhofer and Robbins are
senior authors of the HSP90-senolytic paper **and** of the D+Q programme, Xu 2015, Justice
2019 and Hickson 2019. This is not a rival lab's unreplicated outlier; it comes from inside
the same body of work that supplies the report's senolytic evidence.

**What changes.** Gate G1 must be applied **within** the senolytic class, agent by agent on
molecular target, not at the tier level. The report should state explicitly that HSP90-
inhibitor senolytics (17-DMAG, 17-AAG, ganetespib, NVP-AUY922, BIIB021, PU-H71, AT13387)
are contraindicated in BUB1B deficiency *despite* being senolytics with progeroid in vivo
data — the same inversion as the 17-AAG finding, arriving by a second route.

**Constraint check.** Nothing here implies a senolytic would reduce this child's tumour
risk; the fork constraint is preserved. 17-DMAG and 17-AAG are **investigational**, not
approved.

---

## C2 — Gate G1 is applied inconsistently to quercetin — **CHANGES A RECOMMENDATION (rubric)**

| Source | Claim |
|---|---|
| Aalinkeel 2008, *Prostate* (`29_`) | Quercetin at **50 µM** makes HSP90 the single most down-regulated protein in the PC-3 proteome (−1.75-fold, P<0.001); clients Raf-1 and cdk4 destabilised; siRNA phenocopies |
| Track 2 report, gate G1 | Excludes agents predicted to lower BubR1 abundance — the basis for excluding 17-AAG |
| Track 2 report, §3.3 | Ranks **dasatinib + quercetin** as the highest-scoring approved medication |

**Relation: DISAGREE — internal, between the report's rule and the report's own conclusion.**

**Adjudication — the concern is real but concentration-limited, and it is graded down
accordingly.** 50 µM in vitro is one to two orders of magnitude above the free aglycone
plasma concentration achievable from oral quercetin, including the 1000 mg/day used in
senolytic trials. The mechanism is down-regulated *expression*, not ATP-site inhibition;
quercetin is a promiscuous flavonoid; and the effect was cancer-cell-selective, sparing
normal prostate epithelium. **This is not grounds to reject dasatinib + quercetin.**

It is grounds to fix the rule. As written, G1 excludes on mechanism alone; applied
uniformly it would also flag quercetin. It needs an **exposure qualifier** — *"excluded
where the agent is predicted to lower BubR1 abundance at concentrations achievable in
vivo"* — after which 17-AAG stays excluded (100 nM, target-directed) and quercetin does not
(~50 µM, expression-level). Without that qualifier the rubric is inconsistent, and the
inconsistency happens to favour the candidate the report already preferred — the direction
of bias most worth guarding against.

**The residual worry, stated rather than dismissed.** Checkpoint function here sits near a
threshold of **~6–13%** of normal BubR1 (Suijkerbuijk 2010), so a proportionally small
decrement matters more than in a healthy adult, and **no one has measured BubR1 in the
presence of quercetin at any concentration.** → open question **Q3**.

---

## C3 — NAD⁺ precursors: target engagement replicates, muscle benefit does not — **CHANGES A RATIONALE**

| Source | Tier | Result |
|---|---|---|
| North 2014, *EMBO J* (`16_`) | Mouse, **wild-type** | NMN 500 mg/kg/day i.p. raised BubR1 in **testes** |
| Shoji 2025, *Aging Cell* (`21_`) | **Human RCT**, Werner syndrome | Sarcopenia indicators **unchanged** |
| Stocks 2022, *JCI Insight* (`30_`) | **Human RCT**, n=32 elderly | Muscle stem-cell recruitment and regeneration histology: **"no NRPT supplementation effect"** |
| Elhassan 2019, *Cell Rep* (`30_`) | **Human RCT**, n=12 aged | Muscle NAD⁺ metabolome ↑, **"without altering mitochondrial bioenergetics"**; circulating inflammatory cytokines ↓ |
| Dollerup 2018, *Am J Clin Nutr* (`30_`) | **Human RCT**, n=40 | Insulin sensitivity "**not improved**" |
| Remie 2020, *Am J Clin Nutr* (`30_`) | **Human RCT**, n=13 | Fat-free mass ↑ 1.34%; primary metabolic endpoints not improved |
| McDermott 2024 NICE, *Nat Commun* (`30_`) | **Human RCT**, n=90 PAD | 6-min walk **improved** (+17.6 m, one-sided 90% CI) |

**Relation: SUPERSET then DISAGREE.** The human trials collectively supersede the mouse
result on the question of *human functional benefit*, and they disagree with each other on
direction.

**Adjudication.** Target engagement is settled — four independent trials show the muscle or
blood NAD⁺ metabolome rises on oral NR. **Muscle functional benefit is null in every trial
designed to detect it**: Stocks 2022 (regeneration — the mechanism nearest this child's
`HP:0003202`), Elhassan 2019 (bioenergetics), and Shoji 2025 (sarcopenia in a monogenic
progeroid disease). Three independent nulls on the endpoint class that matters most.

The single positive, NICE, is the weakest design **for this purpose**: peripheral artery
disease is a perfusion-limited walking impairment rather than a myopathy, the primary
analysis uses an unusual one-sided 90% CI, and the authors themselves write that "a larger
clinical trial to confirm these findings is needed." It does not license a muscle claim.

**What changes.** NR's rank need not fall on the report's own rubric — the rubric rewards
safety, availability and paediatric exposure, where NR still scores well. But its
**rationale must be re-scoped**: the consistent human signal is anti-inflammatory
(Elhassan: depressed circulating cytokines), not myogenic. If NR is defensible here it is
through the SASP/inflammation arm of the fork, **not** through reversing muscle atrophy —
which is also the arm least likely to be confused with reversing a developmentally fixed
deficit.

**What the nulls do *not* refute.** None of these trials studied BUB1B deficiency,
aneuploidy, or a child, and none measured BubR1. They disconfirm the *generic* muscle
claim; the genotype-specific BubR1-abundance hypothesis remains **untested in humans
altogether**.

---

## C4 — Citation drift on North/Sinclair 2014 — CONFIRMED, previously caught

**Claim in the citing literature:** "NMN rescued BubR1 mice."
**What the paper did** (`16_`): NMN was administered to **wild-type** mice; the
`BubR1^H/H` lifespan rescue used **genetic SIRT2 overexpression**. Two experiments, two
genotypes, two interventions.

**Relation: DISAGREE — secondary literature vs. primary record. Primary wins.**
**Adjudication:** upheld. Re-verified against the full text this pass. "NMN raises BubR1
abundance" is supported; "NMN extends lifespan in BubR1 deficiency" is an inference joining
two separate results and must be labelled as one. C3 adds the further constraint that even
the supported half has not translated to human muscle function.

---

## C5 — PharmCAT vs ClinGen on RYR1 rs35364374 — CONFIRMED, previously caught

| Source | Call |
|---|---|
| PharmCAT (automated) | "Uncertain Susceptibility" to malignant hyperthermia |
| ClinGen expert panel, VCV000093279 (3-star) | **Benign** |

**Relation: DISAGREE.** **Adjudication: the expert panel wins**, on the standing rule that a
human expert panel review outranks automated tool output. The discrepancy is itself worth
reporting — an unreviewed PharmCAT report would put a false malignant-hyperthermia flag in
the chart of a child likely to need anaesthesia for tumour surveillance and biopsies, which
is a live clinical harm, not a bookkeeping error.

---

## C6 — Hickson 2019 corrigendum — CONFIRMED, and the corpus-wide sweep is otherwise clean

Hickson 2019 (`20_`) withdrew its skin-senescence and individual IL-1α/IL-6/MMP-9 findings
in a re-analysis living in **Appendix 1 of the corrigendum's supplementary bundle**, not in
PMC or PubMed.

**New this pass — a systematic negative worth recording as prominently as a positive.** All
18 PMC-deposited sources in the corpus were queried through PubMed's
`CommentsCorrections` fields for `ErratumIn`, `RetractionIn`, `ExpressionOfConcernIn`,
`CorrectedandRepublishedIn` and `UpdateIn`. **Exactly one hit: Hickson 2019 → PMID
31982828.** No retractions, no expressions of concern, nothing else. The corpus is clean
apart from the corrigendum already handled.

**Caveat on the negative:** this sweep detects only corrections *indexed by PubMed*. The
Hickson case is itself the proof that substantive withdrawals can live in supplementary
files invisible to that index, so a clean sweep is necessary, not sufficient.

---

## C7 — NCBI identifier collisions corrupted two source captures — **CHANGES PROVENANCE**

**Instance 1.** `elink` maps PMID 37866738 (Kirsch-Volders & Fenech 2023, *Mutat Res Rev*,
"Towards prevention of aneuploidy-associated cellular senescence and aging") → PMC13019530.
**PMC13019530 renders a different paper**: Kirsch-Volders, Mišík & Fenech 2026,
*Mutagenesis*, "Aneuploidy in exfoliated buccal cells" — different journal, three years
later, shared first and last authors. File `18_` had appended the wrong body text (62
occurrences of "buccal", 3 of "SASP", 0 of "senolytic").

**Instance 2, found by the check written in response to instance 1.** `elink` maps PMID
32638319 (Kıyga 2020, *Mol Biol Rep*) → PMC13212844. **PMC13212844 renders** Shahid et al.
2026, *Discover Oncology*, a systematic review that merely *tabulates* the Kıyga study as
its reference [25]. Citing it as the primary source would have been an attribution error;
file `29_` now cites the review as a review and marks the primary study unread.

**Relation: DISAGREE — database cross-reference vs. rendered content. Rendered content
wins.**

**Adjudication and blast radius.** **No claim in this repository is affected.** Every
load-bearing quotation attributed to Kirsch-Volders & Fenech was written from the genuine
2023 abstract and all four were re-verified verbatim against PubMed for PMID 37866738,
including both quotes used in the Track 2 report. The defect is provenance, not conclusions
— but it is the kind that no amount of careful *reading* catches, because the fetched text
is internally coherent and by the same authors.

**What changes.** A corpus-wide **title-vs-identifier verification** was written and run
across all 18 PMC-sourced files: resolve each cited PMC ID back to its PubMed title and
compare it to the title the file claims. Two genuine mismatches (both above), six benign
flags (multi-source or thematically-titled files). This check is now a required step and is
recorded in `_fetch_log.md`. **Generalisable trap:** both collisions involve recent,
high-numbered PMC deposits (PMC130–132 million) whose forward and reverse `elink` mappings
are mutually inconsistent.

---

## C8 — Tang 2011's AMPK mechanism is not a class property — BOUNDS A MECHANISM

Metformin activates AMPK like AICAR, but was much weaker and hit only trisomy 13 and 16.
The paper states: "**Why AICAR and metformin show different efficacy in trisomic MEFs,
despite both causing AMPK activation, is at present unclear.**"

**Relation: DISAGREE — internal to one paper, and flagged by its own authors.**
**Adjudication:** the "energy stress via AMPK" mechanism is under-determined. Anyone
reasoning "AICAR works, therefore AMPK activation works, therefore metformin is a safe
approved substitute" is overreading. Metformin is not a back-door route into this tier.
(Both agents are excluded by gate G2 regardless — see C9.)

---

## C9 — Tang 2011's selectivity is partial, and the aneuploidy is the wrong kind — BOUNDS A REJECTION

"**The majority of compounds did not exhibit selectivity** towards trisomic MEFs or did so
for only a subset of the trisomies tested." Sensitivity also scaled with chromosome size.

**Relation: SUPERSET** — the full text supersedes the abstract, which conveys a cleaner
result than the data support.

**Adjudication:** strengthens the rejection rather than weakening it. The models are MEFs
trisomic for a *single defined* chromosome; MVA is a shifting, mosaic, whole-body mixture
of aneuploidies. The screen's own selectivity is chromosome-dependent, so even its
therapeutic logic does not transfer cleanly. Gate G2 stands: in MVA the aneuploid cells
**are** the patient, so an aneuploidy-selective cytotoxic is whole-body toxicity with a
mechanism — and Tang's full text confirms AICAR is frankly cytotoxic, not cytostatic
("AICAR in fact kills trisomic MEFs").

---

## C10 — "JAK inhibition suppresses the SASP" overstates Xu 2015 — BOUNDS A CLAIM

Full text: suppression is "by up to 60%", plateaus at 0.6 µM, and in recipient cells
"**IL-1α, IL-1β, and IL-8 expression did not change**… suggesting that the SASP is
**segmentally suppressed**."

**Relation: SUPERSET** — full text over abstract.
**Adjudication:** the senomorphic tier's claim must be "partial, segmental damping", not
"SASP suppression". Xu 2015 is also **not** interchangeable with the senolytic evidence: it
silences secretion, it does not remove cells. A ranked list containing both must keep the
mechanisms distinct. Safety, from the paper itself: ruxolitinib causes anaemia and
thrombocytopenia in humans, and platelet counts "tended to be reduced" in treated mice.

---

## C11 — Baker 2011's rescue is tissue-restricted — BOUNDS THE SENOLYTIC HYPOTHESIS

Senescent-cell clearance in BubR1 progeroid mice helps **p16Ink4a-dependent** tissues
(muscle, fat, eye) but explicitly **does not** help p16-independent phenotypes (cardiac
arrhythmia, arterial stiffening) and **does not extend overall survival**.

**Relation: DISAGREE** with any generalised "senolytics help BubR1 mice" reading.
**Adjudication:** upheld. This is the only senescence-clearance evidence in the **BubR1
background specifically**, which makes it the highest-relevance tier available for the
senolytic arm — and it is simultaneously the source of that arm's tightest limit. Cited
correctly in the report; recorded here so the limit travels with the claim.

---

## C12 — A PDB cross-reference's declared chain range vs. the residues actually modelled

**CHANGES PROVENANCE.**

**Side A — UniProt O60566's PDB cross-references.** Two cryo-EM entries are listed against
BubR1 with chains spanning the full protein: **5KHU** `Q=1-1050` and **6TLJ** `S=1-1050`.
Read at face value, these say the pseudokinase domain — and residue 1002 specifically — has
experimental structural coverage.

**Side B — PDBe's observed-residue records for the same two entries.** 6TLJ chain S models
**19-345**; 5KHU chain P models **26-479**. Neither reaches residue 766, let alone 1002. The
declared range is the *entity* length taken from the deposited sequence, not the residues
resolved in the map.

**Relation: DISAGREE**, and only one side is a measurement.

**Adjudication: the observed-residue record wins, decisively.** The cross-reference field is
metadata about what the construct was; the coverage record is what the experiment resolved.
Checked across all nine PDB entries mapped to O60566: the X-ray structures cover 57-220,
647-720, 663-681 and 20-42, and **no experimental structure covers the BubR1 pseudokinase
domain at all.**

**Grounds.** Direct measurement supersedes declarative metadata; the two sources are not
independent (the cross-reference is derived from the deposition, not from the map).

**Effect.** The structural analysis in `data-notes/structural_analysis_n1002k.md` rests
entirely on a **predicted** model (AlphaFold AF-O60566-F1 v6) and must say so wherever it is
used. Had the cross-reference been trusted, the report would have claimed experimental
structural support for its central mechanism that does not exist — an overclaim of exactly
the kind this matrix exists to catch.

**Pattern note.** This is the **third** identifier/metadata trap found in this repository,
after the two PMID↔PMCID collisions in C7. All three share a signature: a database field that
is internally coherent, plausible, and wrong, where careful reading of the content would
never have caught it. The defence is mechanical verification against a second source, not
attentiveness.

---

## Summary of adjudications

| # | Conflict | Winner / resolution | Effect |
|---|---|---|---|
| C1 | HSP90 inhibitors are senolytics **and** contraindicated | Both true; class label unsafe | **Recommendation** |
| C2 | Quercetin's HSP90 activity vs. gate G1 | Concern real, dose-limited; rule needs exposure qualifier | **Recommendation (rubric)** |
| C3 | NR target engagement vs. muscle benefit | Human RCTs supersede mouse; nulls dominate | **Rationale** |
| C4 | "NMN rescued BubR1 mice" | Primary record wins — it did not | Confirms prior catch |
| C5 | PharmCAT vs ClinGen (RYR1) | Expert panel wins — Benign | Confirms prior catch |
| C6 | Hickson corrigendum | Upheld; corpus sweep otherwise clean | Honest negative |
| C7 | NCBI identifier collisions ×2 | Rendered content wins | **Provenance** |
| C8 | AICAR vs metformin | Mechanism under-determined | Bounds mechanism |
| C9 | Tang selectivity | Full text supersedes abstract | Bounds rejection |
| C10 | JAK/SASP suppression | Full text supersedes abstract | Bounds claim |
| C11 | Baker tissue restriction | Upheld | Bounds hypothesis |
| C12 | PDB declared chain range vs. observed residues | Observed record wins — **no experimental structure covers residue 1002** | **Provenance** |
