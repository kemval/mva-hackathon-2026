# Track 2 candidate scoring rubric — PRE-REGISTERED

**Written and committed 2026-09-02, before any drug-search query was run.**
The commit order is the point: `git log --follow pipeline/track2_scoring_rubric.md`
should show this file committed strictly before `data-notes/track2_candidates.csv`
and before `pipeline/track2_target_search.py` was ever executed against a live API.
Fixing the scoring criteria before seeing the candidate list is what stops the rubric
from being reverse-engineered to justify a favoured answer.

If a criterion below turns out to be unworkable once real candidates exist, it is to be
**amended in a subsequent commit with the reason recorded**, not silently edited. Any
such amendment is disclosed in the report.

---

## What is being scored

Candidate interventions for the **senescence / tissue-dysfunction branch** of
BUB1B-related MVA in this proband. Two things are explicitly *out of scope* for this
rubric and are handled elsewhere in the report:

- the **cancer-predisposition branch**, which takes a surveillance argument rather than
  a drug (the two branches are siblings off chromosomal instability, not a chain —
  see `notes/01_spindle_assembly_checkpoint_biology.md`);
- **developmentally fixed features** (IUGR, prematurity, established short stature),
  which no post-hoc intervention reverses.

## The defect being targeted

Per Suijkerbuijk et al. 2010 (`literature/15_...`), MVA caused by a truncating +
kinase-domain-missense BUB1B genotype acts through **low BubR1 protein abundance**, not
through a catalytically dead enzyme. The intervention target is therefore *abundance and
its downstream consequences*, and the rubric's mechanistic axis is anchored to that.

---

## Hard gates (excluded regardless of score)

A candidate failing any gate is reported in the **rejected tier with the reason**, not
silently dropped. Rejections are part of the deliverable.

| Gate | Rationale |
|---|---|
| **G1 — Predicted to lower BubR1 abundance further** | e.g. HSP90 inhibitors: Suijkerbuijk 2010 shows mutant BubR1 is an HSP90 client cleared by the proteasome when HSP90 is inhibited. Depleting the residual protein the patient depends on is the wrong direction. |
| **G2 — Mechanism is selective killing of aneuploid cells** | This child is *constitutionally, mosaically* aneuploid in tissues throughout the body. Aneuploidy-selective cytotoxicity is not a therapy here; it is a whole-body toxicity. |
| **G3 — Target absent or not engaged in this patient** | A drug whose target is not present, or not implicated by this genotype, is pathway decoration. |
| **G4 — Evidence is a signature/correlation with no mechanistic path** | Connectivity-map style hits with no causal account are hypotheses about a database, not about a child. |

## Scoring axes

Applied independently; the total is a **sum**, and every sub-score must carry a
one-line written justification with a citation. No axis is weighted, because there is no
principled basis for a weighting and inventing one would be false precision.

### A. Mechanistic directness (0–5)
| Score | Definition |
|---|---|
| 5 | Demonstrated to raise BubR1 protein abundance |
| 4 | Acts on the proximal node governing BubR1 abundance (NAD⁺/SIRT2 axis; proteostasis) |
| 3 | Acts on the first downstream consequence — senescent-cell burden, or SASP output |
| 2 | Acts on a distal consequence (systemic inflammation generally) |
| 1 | Pathway-adjacent; no causal path demonstrated to any node in this chain |
| 0 | No mechanistic path |

### B. Evidence tier for *that* mechanism (0–5)
Scored for the mechanism as it would be used here — not for the drug's unrelated
approved indication.
| Score | Definition |
|---|---|
| 5 | Randomised controlled trial in humans, in a mechanism-related disease |
| 4 | Open-label / phase 1–2 human trial with a mechanism biomarker endpoint |
| 3 | In vivo rodent evidence **in a BubR1 model specifically** |
| 2 | In vivo rodent evidence in another model |
| 1 | Human or animal cell culture only |
| 0 | Computational or associative only |

### C. Paediatric data and safety (0–4)
| Score | Definition |
|---|---|
| 4 | Approved **with a paediatric indication**, with long-term paediatric safety data |
| 3 | Approved in adults; documented paediatric off-label use with published safety data |
| 2 | Food-derived or supplement, with human paediatric exposure data |
| 1 | Adult human data only |
| 0 | No human data, or a known paediatric contraindication |

### D. Case-specific safety burden (−5 to 0, subtractive)
Assessed against *this* proband's documented features. One point deducted per applicable
concern, to a floor of −5, each stated explicitly:
- oncologic risk in a cancer-predisposition syndrome (genotoxicity, immune escape);
- renal burden, given nephrocalcinosis **present since birth** (`HP:0000121`);
- growth, puberty or developmental effects in a child already growth-restricted;
- interaction with cytotoxic chemotherapy the patient may plausibly receive again;
- immunosuppression.

### E. Feasibility (0–3)
Formulation available for a child; cost and access; monitoring burden on a family
already managing a rare disease; whether a treating team could act on it without a
bespoke trial infrastructure.

**Total = A + B + C + D + E.** Range −5 to 17.

## Reported alongside the score, never folded into it

**Regulatory status** is recorded as a categorical attribute — `FDA/EMA-approved drug`,
`dietary supplement`, or `investigational` — and is **not scored**. Reason: the task asks
for "existing, market-approved medications", so approval status determines *which
shortlist a candidate appears on*, but letting it add points would let an approved drug
with a weak mechanism outrank a better-evidenced one, which is precisely the error the
mechanistic axis exists to prevent.

The report therefore presents **two lists from one ranking**:
1. **Approved medications only** — the literal answer to the brief.
2. **The full ranking**, including supplements and investigational agents, so the
   strongest-evidenced option is visible even where it is not a licensed drug.

Nothing is described as "approved" that is not approved. NMN's status as a lawful
dietary supplement (restored by FDA in September 2025 after the 2022 exclusion) makes it
a supplement, not a medication, and it is labelled as such wherever it appears.

## Tie-breaking

Ties are broken by axis **B (evidence tier)**, then **D (case-specific safety)**, then
**A**. Declared here so it is not chosen after the fact.

## What a score is not

A total is a structured summary of a reasoned argument, not a measurement. Two
candidates one point apart are not meaningfully distinguishable, and the report says so
rather than presenting the ordering as finer-grained than the evidence supports. Every
candidate carries a prose dossier; the number never travels without it.
