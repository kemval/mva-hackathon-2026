# Pre-registered prediction: does the loss-of-function/inhibitor mismatch generalise?

**Committed before any query in this analysis was run.** The commit order is verifiable in
`git log`, in the same spirit as `pipeline/track2_scoring_rubric.md` — which is **not**
edited by this work, because its own pre-registration argument depends on it not being.

## What is being tested

Track 2 Part 8 currently *asserts* that its central structural finding generalises:

> ~95% of drugs around this pathway are inhibitors; the disease is a deficiency. That is
> not a fact about BUB1B — it is a fact about **every loss-of-function rare disease**.

That is an untested claim in a section the panel weights at 15%. This task converts it
into a measurement, on diseases chosen before the numbers were seen, with one case picked
specifically because **the prediction should fail there**.

## The tier rule — fixed here, so it cannot be tuned to the answer

The BUB1B node set was hand-curated from the mechanism document. Curation is the obvious
attack on any generalisation drawn from it: the tiers could have been arranged to produce
the monotone result. So this replication does **not** curate. Tiers are assigned by a
mechanical rule against a public network:

- **Distance 0** — the causal gene itself.
- **Distance 1** — its direct interaction partners in STRING v12 (*Homo sapiens*, combined
  score ≥ 700, the STRING "high confidence" cutoff), capped at the 25 highest-scoring
  partners.
- **Distance 2** — partners of those partners under the same cutoff, excluding anything
  already at distance 0 or 1, capped at 25 by summed score.

The cap exists so a hub gene cannot swamp the tier; it is stated now rather than chosen
later. Ensembl IDs resolve via Ensembl REST, as in the original search.

**The same rule is re-applied to BUB1B**, so the original result is re-derived under the
mechanical rule and not only under its own curation. If the BUB1B monotonicity survives
the rule change, that is evidence it was not an artefact of curation. If it does not, that
is a finding about this submission and will be reported as one.

## The three replication diseases, and why each

| Gene | Disease | Why chosen |
|---|---|---|
| **NPC1** | Niemann-Pick type C | Ultra-rare, LoF, lysosomal. No dedicated NPC1-directed programme. The mismatch should hold cleanly. |
| **ATM** | Ataxia-telangiectasia | LoF, but with a large oncology interest in **inhibiting** ATM. Tests whether "drugs exist" and "drugs point the right way" come apart. |
| **CFTR** | Cystic fibrosis | **The falsification test.** Correctors and potentiators exist and are approved. The prediction should break here. |

## The predictions

Stated numerically so they cannot be reinterpreted after the fact.

**P1 — Drug count at the defect.**
- NPC1: **zero or near-zero.** Nobody has drugged the transporter itself.
- ATM: **greater than zero**, because ATM inhibitors are in oncology development.
- CFTR: **greater than zero**, and approved.

**P2 — Direction of effect, which is the claim that actually matters.**
- NPC1 and ATM: of action-typed entries across the whole neighbourhood, **≥ 80% inhibitory.**
- ATM specifically: of entries at distance 0, **essentially all inhibitory** — meaning
  drugs against the causal gene exist and every one of them pushes the *wrong way* for a
  deficiency. This is the sharper version of the Track 2 finding and the one worth having.
- CFTR: **substantially below 80%** inhibitory at distance 0, because potentiators and
  correctors are not inhibitors.

**P3 — Monotonicity.** Unique drug count rises with distance (0 → 1 → 2) for NPC1 and ATM.
No prediction is made for CFTR, where distance 0 is already drugged.

## What counts as the prediction failing

Pre-committed, so that a miss cannot be re-described as a partial hit:

- **P2 failing at NPC1** would be the serious one. It would mean the inhibitor skew is a
  property of the mitotic/senescence neighbourhood rather than of loss-of-function disease,
  and Part 8's generalisation would have to be **withdrawn**, not softened.
- **P1 or P3 failing** weakens the "expect zero at the causal gene" advice to a tendency,
  and the report must say so.
- **CFTR failing to break the prediction** would mean the falsification test did not
  discriminate — the test would be uninformative, not passed, and must be reported that way.

## What this cannot show

Three diseases is not a survey. Genes were chosen by argument, not sampled, so this is a
**structured probe with one adversarial case, not an estimate of a population parameter.**
No p-value will be computed and no claim about "most rare diseases" will be made from n=3.
STRING confidence scores mix experimental and text-mined evidence, so distance-1 membership
is a network claim, not a claim of physical interaction.

Whatever comes back is reported, including the case where the generalisation this
submission already published turns out to be narrower than stated.
