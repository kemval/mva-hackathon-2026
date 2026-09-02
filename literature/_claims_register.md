# Claims Register

Every load-bearing assertion in the Track 2 evidence base, graded. 2026-09-02.

**Grades.** **Established** — demonstrated directly, in a system that supports the claim as
stated. **Predicted** — follows from established mechanism but has not been measured in
this system. **Untested inference** — joins results across papers, systems or species; no
single source supports it.

**Evidence tiers**, strongest to weakest: `human RCT` · `human phase 1–2` ·
`observational human` · `mouse — BubR1 background` · `mouse — other background` ·
`cell line` · `in silico`.

**Standing rule:** a mouse result is never phrased in language implying human evidence.
Where a row's grade and tier disagree with how a claim reads elsewhere, the row governs.

---

## A. Mechanism — the defect

| # | Claim | Grade | Tier | Source | Note |
|---|---|---|---|---|---|
| A1 | MVA cells with truncating + missense BUB1B have **reduced BubR1 protein abundance**, not defective kinase activity | **Established** | Human patient cells | `15_` Suijkerbuijk 2010 | The load-bearing paper; same genotype architecture as this proband |
| A2 | Forcing BubR1 abundance up **fully restores checkpoint function** | **Established** | Human patient cells | `15_` | Overexpression of kinase-domain missense mutants |
| A3 | A functional threshold sits between **~6% and ~13%** residual BubR1 | **Established** | Human patient cells | `15_` | Quantitative anchor for every dose/decrement argument |
| A4 | Mutant BubR1 is an **HSP90 client** cleared by the proteasome | **Established** | Human patient cells | `15_` | Basis of gate G1 |
| A5 | The therapeutic target in this child is **protein quantity** | **Predicted** | — | Inference from A1–A3 | Directionally well-supported; never measured in this patient |
| A6 | This proband's residual BubR1 level | **UNMEASURED** | — | — | The single highest-value missing datum → **Q1** |
| A7 | Hypothesis is robust to unresolved **phase** (cis or trans → low abundance either way) | **Predicted** | Mouse + human cells | `15_`, `17_` | Wijshake 2012 shows mono-allelic is already deleterious |
| A8 | BubR1 abundance is set by **SIRT2-dependent K668 deacetylation** opposing proteasomal targeting | **Established** | Mouse / cell line | `16_` North 2014 | Mechanism is solid; see C4 for what it does *not* license |

## B. Downstream — the fork

| # | Claim | Grade | Tier | Source | Note |
|---|---|---|---|---|---|
| B1 | CIN forks into **{senescence + SASP}** and **{cancer predisposition}** as **siblings** | **Established** | Review-level | `18_` (abstract only), `23_` | Hard constraint. Senescence does **not** lead to cancer here |
| B2 | Aneuploidy can induce SASP directly or via micronuclei → cGAS-STING | **Established** *in vitro*; **less clear in vivo, per the review itself** | Cell line + review | `18_`, `24_`, `25_` | Review's own wording: "How aneuploidy contributes in vivo… is less clear" |
| B3 | Micronuclei activate cGAS | **Established** | Cell line / mouse | `24_` Mackenzie 2017 | |
| B4 | A senescence-targeting drug **would reduce this child's tumour risk** | **REJECTED — do not assert** | — | — | Violates B1. No source supports it |
| B5 | Senescent-cell clearance helps **p16-dependent** tissues in BubR1 mice, **not** p16-independent ones, and **does not extend survival** | **Established** | **Mouse — BubR1 background** | `04b_` Baker 2011 | Highest-relevance tier for the senolytic arm, and its tightest limit |
| B6 | Cancer risk is managed by **surveillance**, not by a drug | **Established** | Guideline (AACR-endorsed) | `23_` Nakano 2024 | Renal US q3mo birth→7y; avoid radiation |
| B7 | Much of the growth/muscle deficit is **developmentally fixed** | **Established** (clinical constraint) | — | Case + `01_` | No candidate may imply reversal |

## C. Candidate — NAD⁺ precursors (**dietary supplement**, not a medicine)

| # | Claim | Grade | Tier | Source | Note |
|---|---|---|---|---|---|
| C1 | NMN raises BubR1 protein in vivo | **Established** | **Mouse — wild-type**, testes only | `16_` | 500 mg/kg/day **i.p.**, 7 days. Not an oral human dose |
| C2 | "NMN extends lifespan in BubR1 deficiency" | **UNTESTED INFERENCE — do not assert** | — | `16_` | The rescue used **SIRT2 transgenic overexpression**, not NMN. See C4 |
| C3 | Oral NR raises the **human muscle NAD⁺ metabolome** | **Established** | **Human RCT** ×4 | `30_` | Target engagement is settled |
| C4 | Oral NR improves **human muscle function or regeneration** | **REFUTED in the trials designed to test it** | **Human RCT** ×3 | `30_` Stocks 2022, Elhassan 2019; `21_` Shoji 2025 | Three independent nulls |
| C5 | NR reduces **circulating inflammatory cytokines** | **Established** | **Human RCT** | `30_` Elhassan 2019 | The one consistent positive; runs through the SASP arm |
| C6 | NR improved 6-min walk in PAD | **Established but weak for this purpose** | **Human RCT** | `30_` NICE 2024 | One-sided 90% CI; perfusion-limited, not myopathic; authors ask for confirmation |
| C7 | NR raises BubR1 **in a human** | **UNTESTED** | — | — | Never measured, in anyone → **Q2** |
| C8 | Paediatric NR exposure exists | **Established** | **Human phase 1–2** | `22_` Veenhuis 2021 | 17 of 24 participants were children (ataxia telangiectasia) |
| C9 | NR is an **FDA-approved medication** | **FALSE — do not assert** | — | — | Dietary supplement. Category must stay distinct |

## D. Candidate — senolytics / senomorphics

| # | Claim | Grade | Tier | Source | Note |
|---|---|---|---|---|---|
| D1 | D+Q reduces senescent-cell burden in humans | **Established (preliminary)** | **Human phase 1**, n=9 | `20_` Hickson 2019 | **Read with the corrigendum**: skin-senescence and individual IL-1α/IL-6/MMP-9 results **withdrawn** |
| D2 | D+Q improves physical function in IPF | **Established (open-label, uncontrolled)** | **Human phase 1** | `19_` Justice 2019 | First-in-human D+Q; no control arm |
| D3 | **No D+Q trial has ever enrolled a child** | **Established** | Trial registry, structured `minimumAge`/`stdAges` fields | `data-notes/track2_trials.tsv` | 0 of 22 |
| D4 | **HSP90 inhibitors are senolytics** | **Established** | **Mouse — Ercc1 background** + cell line | `28_` Fuhrmann-Stroissnigg 2017 | ≥7 chemotypes; 17-DMAG healthspan in progeroid mice |
| D5 | HSP90-inhibitor senolytics are **contraindicated here** | **Predicted — high confidence** | Inference from A4 + `26_` | `15_`, `26_`, `28_` | Double hit: depletes mutant BubR1 **and** aneuploid cells depend on chaperone capacity |
| D6 | "Senolytic" is a **safe class label** for this child | **FALSE — do not assert** | — | C1 in matrix | The class contains D4/D5. Gate per agent, not per tier |
| D7 | Quercetin lowers HSP90 at **50 µM** in a cancer cell line | **Established (in that system)** | **Cell line** | `29_` Aalinkeel 2008 | Largest single proteome change; clients destabilised |
| D8 | Oral quercetin lowers HSP90 or BubR1 **in a human** | **UNTESTED — and unlikely on potency grounds** | — | — | ~50 µM is far above achievable free plasma levels → **Q3** |
| D9 | JAK inhibition **suppresses the SASP** | **Overstated — it damps it partially and segmentally** | **Mouse — aged WT** + human primary cells | `27_` Xu 2015 | ≤60%, plateaus at 0.6 µM; IL-1α/IL-1β/IL-8 unchanged in recipients |
| D10 | Senomorphic and senolytic evidence are **interchangeable** | **FALSE — do not assert** | — | `27_` vs `19_`/`20_` | One silences secretion, the other removes cells |
| D11 | Ruxolitinib is **safe in a child with cancer predisposition** | **UNTESTED** | — | `27_` | Anaemia/thrombocytopenia in humans; immunosurveillance unaddressed → **Q5** |

## E. Rejected tier

| # | Claim | Grade | Tier | Source | Note |
|---|---|---|---|---|---|
| E1 | 17-AAG is aneuploidy-selective at **100 nM** | **Established** | **Cell line** | `26_` Tang 2011 | |
| E2 | It works *because* aneuploid cells depend on protein quality control | **Established (as the authors' interpretation)** | **Cell line** | `26_` | The mechanistic core of the contraindication |
| E3 | Aneuploidy-selective cytotoxics are **not therapies in MVA** | **Predicted — high confidence** | Inference | `26_` + case definition | In MVA the aneuploid cells **are** the patient (gate G2) |
| E4 | AICAR **kills** trisomic cells (not merely cytostatic) | **Established** | **Cell line** | `26_` | Sharpens E3 |
| E5 | Metformin is a safe approved substitute for AICAR | **FALSE — do not assert** | — | `26_` | Authors: differing efficacy "at present unclear". Gated by G2 anyway |
| E6 | Tang's screen was broadly selective | **Overstated** | **Cell line** | `26_` | "The majority of compounds did not exhibit selectivity" |

## F. Patient-specific pharmacogenomics

| # | Claim | Grade | Tier | Source | Note |
|---|---|---|---|---|---|
| F1 | Only **22 of 1,226** PGx positions carry a call | **Established** | Patient VCF | `data-notes/pgx/` | |
| F2 | **16 of 23** genes change call under the reference assumption | **Established** | Patient VCF | | PharmCAT's own CLI labels this "DANGEROUS!" |
| F3 | RYR1 rs35364374 confers malignant-hyperthermia susceptibility | **REFUTED by expert panel** | ClinGen VCV000093279, 3-star | C5 in matrix | PharmCAT says "Uncertain Susceptibility"; panel says **Benign** |
| F4 | The PGx layer yields an actionable prescribing change | **No — the result is an honest negative** | — | | Reported as such |

## G. Provenance

| # | Claim | Grade | Note |
|---|---|---|---|
| G1 | Every quotation attributed to Kirsch-Volders & Fenech 2023 is **verbatim correct** | **Established** | Re-verified against PubMed PMID 37866738, 2026-09-02 |
| G2 | That source's **full text was never obtained**; a misfetched body has been removed | **Established** | NCBI identifier collision — matrix C7 |
| G3 | The corpus contains **exactly one** indexed erratum (Hickson 2019) and no retractions | **Established (with caveat)** | Sweep of 18 PMC sources; detects only PubMed-indexed corrections |
| G4 | Title-vs-identifier verification has been run across all PMC-sourced files | **Established** | 2 genuine mismatches, both corrected |
