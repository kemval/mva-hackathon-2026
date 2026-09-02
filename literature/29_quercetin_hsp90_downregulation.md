# Quercetin down-regulates HSP90 — the dose-limited version of the same contradiction

Primary source: Aalinkeel R, Bindukumar B, Reynolds JL, Sykes DE, Mahajan SD, Chadha KC,
Schwartz SA. "The dietary bioflavonoid, quercetin, selectively induces apoptosis of
prostate cancer cells by down-regulating the expression of heat shock protein 90."
*The Prostate*, 2008 Dec 1;68(16):1773-89. doi: 10.1002/pros.20845
Source: PMC2826114 (open access) — PMID 18726985
Captured: 2026-09-02 (full text via PMC HTML render)

Supporting (**secondary — read as a review, not as primary data**): Shahid B, Sultan MT,
Noman AM, et al., "Systematic review on anticancer potential of Kaempferol and quercetin
against lung, breast, and colorectal cancers," *Discover Oncology*, 2026 Apr 15
(PMID 41986570, PMC13212844). Its Table 1, row 11, tabulates quercetin 10–100 µM / 48 h in
MCF-7 and MDA-MB-231 with the entry "↓ Hsp27/70/90", citing as its reference [25] the
primary study Kıyga E, Şengelen A, Adıgüzel Z, Önay Uçar E, *Mol Biol Rep* 2020;47(7)
(PMID 32638319). **That primary study has not been read here** — only the review's
tabulation of it — and no claim in this repository may be sourced past that boundary.

> ⚠ **Identifier caution.** NCBI's `elink` maps PMID 32638319 → PMC13212844, but
> PMC13212844 in fact renders the 2026 Shahid systematic review, not the 2020 Kıyga
> primary study. Following that link and citing it as the primary paper would have been an
> attribution error; the citation above reflects what was actually fetched and read. This
> is the **second** instance of this NCBI linkage defect found in this corpus — see the
> PROVENANCE CORRECTION in `literature/18_kirschvolders2023_aneuploidy_senescence.md` and
> conflict **C7** in `literature/_contradiction_matrix.md`.

Relevance: **quercetin is half of the Track 2 report's highest-scoring approved-medication
candidate (dasatinib + quercetin), and it has published HSP90-lowering activity.** Gate G1
of the report's own rubric excludes agents predicted to lower BubR1 abundance, and it
excludes 17-AAG on exactly that mechanism. This file exists so the gate is applied
consistently rather than only to the agents it was written for. See
`literature/_contradiction_matrix.md`, conflict **C2**.

---

## What it establishes

**HSP90 was the single most down-regulated protein in the quercetin-treated proteome.**
Unbiased 2D-DIGE with LC-MS/MS on PC-3 cells treated with **50 µM quercetin for 24 h**:
"Spot # 191 was subsequently identified as Hsp90… Of all proteins, spot # 191 showed the
greatest change (−1.75-fold) after treatment with quercetin" (P < 0.001). The next
largest changes were smaller — tumour protein D52 (−1.69), tropomyosin 3 (−1.66).

**Client proteins were used as the read-out of functional HSP90 inhibition.** "Raf-1 and
cyclin-dependent kinase (cdk) 4 are destabilized by Hsp90 inhibition and are used in this
study as Hsp90 client proteins" — the same surrogate-marker logic used in clinical trials
of dedicated HSP90 inhibitors, which the paper cites.

**Knockdown phenocopies the drug.** "Knockdown of Hsp90 by short interfering RNA also
resulted in induction apoptosis similar to quercetin in cancer cells."

**Abstract conclusion, verbatim:** "quercetin down-regulates the expression of Hsp90
which, in turn, induces inhibition of growth and cell death in prostate cancer cells."

## Adjudication — the concern is real but concentration-limited

This does **not** carry the same weight as the 17-AAG finding, and the review says so
plainly rather than inflating it:

- **The effective concentration is ~50 µM in vitro.** Oral quercetin in humans, including
  at the 1000 mg/day used in senolytic trials, produces free aglycone plasma
  concentrations in roughly the low-micromolar-to-submicromolar range — one to two orders
  of magnitude below the exposure used here. On potency grounds alone, whole-body HSP90
  suppression from oral quercetin is unlikely.
- **The mechanism is down-regulated *expression*, not active-site inhibition.** It is a
  weaker and slower perturbation than a geldanamycin-class ATP-site inhibitor.
- **Quercetin is a promiscuous flavonoid.** A single most-changed spot in one proteome of
  one cancer cell line is a lead, not an established pharmacology.
- **Selectivity cuts the other way too:** apoptosis was induced "in cancer cells but not
  in normal prostate epithelial cells," so the effect may not generalise to a
  non-malignant fibroblast.

**Net position:** this is *not* grounds to reject dasatinib + quercetin. It is grounds to
fix an inconsistency in how the gate is written. Gate G1 currently excludes on mechanism
alone; applied literally and uniformly it would also flag quercetin. It therefore needs an
explicit **exposure qualifier** — something of the form *"excluded where the agent is
predicted to lower BubR1 abundance at concentrations achievable in vivo"* — after which
17-AAG remains excluded (100 nM, target-directed) and quercetin does not (~50 µM,
expression-level, above achievable exposure). Without that qualifier the rubric is applied
inconsistently, and the inconsistency favours the candidate the report already preferred,
which is the direction of bias worth guarding against.

The residual worry that survives the potency argument is narrow and should be stated
rather than dismissed: this child's checkpoint function sits near a threshold between
**~6% and ~13%** of normal BubR1 (Suijkerbuijk 2010), so a proportionally small decrement
matters more here than in a healthy adult — and **no one has measured BubR1 in the
presence of quercetin at any concentration.** That is a cheap experiment, listed in
`literature/_open_questions.md` as **Q3**.

## LIMITS — what this paper does NOT show

- **No BubR1 measurement, no aneuploid cells, no MVA context.** The clients assayed are
  Raf-1 and cdk4. BubR1 is never mentioned.
- **No in vivo work.** Cell lines only (PC-3, LNCaP, DU-145, normal prostate epithelium).
- **No pharmacokinetic bridge.** The paper makes no claim that 50 µM is achievable in a
  human, and it should not be read as making one.
- **It is not a senolytic study** and does not connect its HSP90 result to quercetin's use
  in dasatinib + quercetin. That connection is drawn here, across papers, and is graded as
  an untested inference.
- Nothing here bears on **dasatinib**, which has no HSP90 activity at issue.

## Evidence tier

**Cell line only.** In silico/PK reasoning about human exposure is inference, not
measurement. Under the Track 2 grading scheme this is the weakest tier that can still
support a flagged concern, and it supports a *rubric correction*, not a candidate
rejection.
