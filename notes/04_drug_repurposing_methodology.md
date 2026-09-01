# Synthesis Notes: Drug Repurposing Methodology (Practical Guide)

*Original synthesis by Claude for this project, summarizing the general methodology described in reviews like Pushpakom et al. 2019 (see `literature/12_pushpakom2019_drug_repurposing_review.md` once fetched). Use alongside the primary paper for the Track 2 report.*

Captured: 2026-08-31

## The general drug repurposing logic

Drug repurposing (a.k.a. repositioning) identifies new therapeutic uses for existing, already-approved (or already clinically-tested) compounds — the appeal being that safety/pharmacokinetic data already exist, which can dramatically shorten the path from hypothesis to clinical testing versus a novel drug.

Three broad discovery strategies, roughly from most to least "mechanism-first":

1. **Target-based / mechanism-driven**: start from the disrupted biological pathway (as characterized from the variant), then search for approved drugs known to modulate a node in that pathway. This is the primary approach for this project, since the task explicitly asks to reason from "biological mechanisms disrupted in this case."
2. **Signature-based / expression-driven**: compare disease-associated gene-expression signatures against large databases of drug-induced expression signatures (e.g. Connectivity Map / LINCS L1000) to find compounds that reverse the disease signature. Harder to apply directly here since there's likely no disease-specific expression dataset for this single patient — more useful as a supplementary/exploratory method if time allows.
3. **Phenotype/screening-based**: empirical drug screens in a relevant model system. Out of scope for a hackathon report (no lab access), but worth citing as the natural "next step" a repurposing hypothesis would need before real clinical use — this framing directly satisfies the task's own instruction that "submissions are hypotheses for follow-up, not evidence that a medicine works."

## Practical workflow for this project

1. **List every disrupted pathway node** from the mechanism deep-dive (see `notes/01_mitosis_spindle_checkpoint_synthesis.md`): BUB1B/BubR1 itself, the broader spindle assembly checkpoint, downstream chromosomal instability, cellular senescence/SASP, DNA damage response, apoptosis regulation.
2. **Query each node systematically** in:
   - **Open Targets Platform** — genetics-driven evidence connecting a target gene to diseases and to known/investigational drugs; good starting point for "what drugs already exist that touch this gene or pathway."
   - **DGIdb** — aggregates drug-gene interaction claims across many source databases; useful for a broad first pass.
   - **DrugBank / ChEMBL** — detailed mechanism-of-action, approval status, and indication data per compound, needed to assess feasibility (is it actually approved? for what population? any pediatric data?).
3. **Score/filter each candidate** on:
   - **Mechanistic plausibility** — how directly does the drug's known mechanism connect to the disrupted pathway? (Direct target modulation > pathway-adjacent > speculative.)
   - **Approval/regulatory status** — approved > investigational/late-stage trial > preclinical only. The task specifically asks for "existing, approved medications."
   - **Safety in the relevant population** — this patient is a child; flag any candidate lacking pediatric safety data as a real feasibility caveat rather than ignoring it.
   - **Existing evidence in an adjacent condition** — has the drug shown benefit (even in an unrelated disease) via a mechanism that plausibly generalizes here? (This is exactly the shape of the Baker et al. 2011 senescence-clearance → senolytic-drug argument.)
4. **Present candidates as a ranked, reasoned shortlist**, not a single guess — Track 2's "Scientific Rigor" and "Innovation" criteria reward showing the systematic search process, not just landing on one answer.
5. **Explicitly separate "primary hypothesis" from "candidates for further investigation"** — mirrors how Track 1 separates primary vs. secondary findings, and keeps appropriate scientific humility (matches the track's own framing: "hypotheses for follow-up, not evidence that a medicine works").

## The flagship hypothesis lead for this case (to develop further in Weeks 5-6)

BubR1/BUB1B insufficiency is mechanistically linked (in mouse models) to accumulation of senescent cells and a progeroid phenotype (Baker et al. 2011). **Senolytic drugs** (compounds that selectively clear senescent cells) are a real, actively-studied approved-drug class:
- **Dasatinib** (approved tyrosine kinase inhibitor, leukemia indication) + **quercetin** (dietary supplement) — the most-studied senolytic combination, with human Phase 1 data in other conditions (e.g. idiopathic pulmonary fibrosis, diabetic kidney disease) as of recent literature.
- This needs to be evaluated carefully and honestly in the actual report: it comes from a *mouse model of BubR1 hypomorphism*, not a proven treatment for human MVA, and pediatric senolytic safety data is thin — the write-up should present this as a well-reasoned, mechanism-grounded hypothesis worth investigating, explicitly flag the translational gap (mouse model ≠ this child's exact variant/mechanism, and dasatinib carries real pediatric oncology-context safety considerations that need honest discussion), and pair it with 3-5 alternative/complementary candidates from the systematic pathway search rather than presenting it as a standalone answer.

## What to actually read for full depth
- Pushpakom S et al. 2019, *Nature Reviews Drug Discovery* — primary methodology reference; fetch into `literature/12_pushpakom2019_drug_repurposing_review.md`.
- Open Targets Platform docs — `literature/10_open_targets_overview.md`.
- DGIdb docs — `literature/11_dgidb_overview.md`.
- Fresh literature search (Weeks 5-6) on "dasatinib quercetin senolytic clinical trial" and "senolytic pediatric safety" — pull current results, don't rely solely on this synthesis note, since trial landscape moves fast.
