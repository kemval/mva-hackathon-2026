# Scalability replication — results against the pre-registered prediction

Run 2026-09-04. Prediction: `pipeline/scalability_prediction.md`, committed at `98b9b04`,
**before** any query below was executed. Node sets built by `pipeline/build_node_set.py`
(STRING v12, score ≥ 700, ≤25 per tier); drugs retrieved by the unmodified
`pipeline/track2_target_search.py`; measured by `pipeline/scale_measure.py`.

> **Counting unit, stated because an earlier version of this file got it wrong.** An
> "entry" is a unique **`(gene, drug, action_type)` triple** — the same unit the Track 2
> report's own `129/142` figure uses. The first version of these results counted raw rows,
> which inflated every percentage and, worse, was printed beside the report's triple-based
> figure as though the two were comparable. They were not. `scale_measure.py --selfcheck`
> now re-derives the report's `129 / 142` exactly before any other number here is trusted:
>
> ```
> $ python3 pipeline/scale_measure.py --selfcheck data-notes/track2_target_drugs.tsv
>   unique (gene,drug,action) triples : 142   expected 142
>   strict INHIBITOR                  : 129   expected 129
>   RESULT: PASS — same counting unit as the report
> ```
>
> **STRICT** counts only `INHIBITOR`/`INHIBITORY` (the 129). **BROAD** adds antisense and
> RNAi inhibitors, antagonists and blockers (the report's "~95%"). Both are given, because
> the report gives both.

## The numbers

**Open Targets**

| Gene | Disease | drugs at d0 | d1 | d2 | triples | strict inhibitory | broad |
|---|---|---|---|---|---|---|---|
| **BUB1B** | MVA (this case) | **0** | 375 | 198 | 72 | **69 (95.8%)** | 70 (97.2%) |
| **ATM** | Ataxia-telangiectasia | 84 | 791 | 248 | 76 | **71 (93.4%)** | 74 (97.4%) |
| **NPC1** | Niemann-Pick C | 137 | 81 | 508 | 121 | **66 (54.5%)** | 68 (56.2%) |
| **CFTR** | Cystic fibrosis | 46 | 285 | 776 | 160 | **60 (37.5%)** | 70 (43.8%) |

**DGIdb, independently**

| Gene | triples | strict inhibitory |
|---|---|---|
| BUB1B | 181 | **180 (99.4%)** |
| ATM | 182 | **170 (93.4%)** |
| NPC1 | 308 | **187 (60.7%)** |
| CFTR | 268 | **133 (49.6%)** |

**At the causal gene itself**

| Gene | typed triples | direction |
|---|---|---|
| BUB1B | 0 | **no drugs at all**, in either database |
| **ATM** | 10 | **10/10 = 100% inhibitory** — every one points the wrong way for a deficiency |
| NPC1 | 0 | 137 drug rows, **none action-typed** — see the caveat below |
| CFTR | 49 | **strict 18.4%, broad 20.4%** inhibitory — against **26 `ACTIVATING`** and **8 `POSITIVE MODULATOR`** |

### Caveat on NPC1's 137, because "137 drugs" overstates what those records are

All 137 come from **DGIdb only** — Open Targets returns none — and **not one carries an
action type**. Many are raw ChEMBL binding-assay entries (`CHEMBL:CHEMBL114544`,
`CHEMBL:CHEMBL1243244`) rather than drugs in any clinical sense, alongside a few real
candidates such as **arimoclomol** and the NPC1 ligand **25-hydroxycholesterol**.

So P1 fails at NPC1 on *record count*, which is the metric it was written against, and the
comparison with BUB1B is sound because BUB1B returns zero from both databases. But **the
direction of effect at NPC1's own defect is genuinely unknown, not favourable**, and no
part of the conclusion below rests on it.

## Verdict, against the pre-committed criteria

**P1 — drug count at the defect. FAILS at NPC1.** Predicted "zero or near-zero"; retrieved
**137** records (with the caveat above). Confirmed at ATM (>0, as predicted) and CFTR (>0
and approved, as predicted).

**P2 — direction of effect. FAILS at NPC1, and this was the pre-committed serious one.**
Predicted ≥80% inhibitory across the neighbourhood; measured **54.5% strict / 56.2% broad**
on Open Targets and **60.7%** on DGIdb. Every reading is far below the threshold.

The pre-registration says, in its own words:

> **P2 failing at NPC1** would be the serious one. It would mean the inhibitor skew is a
> property of the mitotic/senescence neighbourhood rather than of loss-of-function disease,
> and Part 8's generalisation would have to be **withdrawn**, not softened.

**It failed. The generalisation as published is withdrawn.** Track 2 Part 8 claimed the
inhibitor skew "is not a fact about BUB1B — it is a fact about **every loss-of-function
rare disease**, which is most of them." That claim is false as stated.

**P3 — monotonic rise with distance. FAILS at three of four, including BUB1B itself.**
Under the mechanical STRING tier rule, drug count does *not* rise monotonically with
distance for BUB1B (0 → 375 → 198), ATM (84 → 791 → 248) or NPC1 (137 → 81 → 508). It
rises only for CFTR (46 → 285 → 776), the one gene for which no prediction was made.

The published monotonicity claim is therefore **an artefact of the curated tier structure**,
not a property of the underlying networks. Curation was the obvious attack on that result
and the attack lands.

**The CFTR falsification test discriminated, exactly as designed** — and more sharply than
the first (row-based) pass suggested. At the causal gene only **18.4% strict / 20.4% broad**
of typed entries are inhibitory, against **26 `ACTIVATING`** and **8 `POSITIVE MODULATOR`**
— the correctors and potentiators. Across the whole CFTR neighbourhood, strict inhibitory is
**37.5%**, the lowest of the four genes. The test was informative rather than merely passed.

## What survives, and it is narrower and more useful than what was claimed

Two things survive the replication intact:

1. **BUB1B's zero at the defect is real, not a curation artefact.** It survives a tier rule
   built mechanically from STRING with no human choice in it. Zero drugs, both databases.
2. **The inhibitor skew is real where it applies, and it is extreme.** BUB1B 95.8%, ATM
   93.4% strict on Open Targets; 99.4% and 93.4% on DGIdb — two independent databases
   agreeing closely.

What changes is the *scope* of the claim. The skew does not track loss-of-function. It
tracks **whether the causal gene's neighbourhood is an oncology drug-development target**:

| Neighbourhood | Genes | Strict inhibitory (OT) |
|---|---|---|
| Mitotic checkpoint / DNA damage response — heavily targeted by oncology inhibitor programmes | BUB1B, ATM | **93–96%** |
| Lysosomal transport, ion channel — metabolic and channel biology, where agonists and activators are ordinary | NPC1, CFTR | **38–55%** |

**The corrected generalisation, stated as a testable claim rather than a slogan:** a
deficiency patient faces a pharmacopeia pointing the wrong way **when the causal gene sits
in a pathway that oncology has invested in inhibiting** — because those programmes exist to
kill dividing cells, and every tool they produce lowers activity. Where the pathway is
metabolic or transport biology, activators and agonists are plentiful and repurposing has
somewhere to start.

That is a **more** useful rule than the one it replaces, because it is diagnostic: it tells
you in advance which rare diseases have this problem. MVA and ataxia-telangiectasia have
it. Niemann-Pick C and cystic fibrosis do not.

**And it sharpens the point for this child rather than weakening it.** BUB1B sits in the
worst category available: zero drugs at the defect, and 95.8% of everything nearby pointing
in the direction that makes the disease worse.

**The ATM result is the strongest new finding and is worth stating on its own.** All ten
action-typed compounds at the causal gene are **inhibitors** — AZD0156, AZD1390, AZD7648,
M3541, BAY-8400 — in a disease defined by ATM *deficiency*. The entire ATM-directed
pharmacopeia exists to make cells ATM-deficient, which is what a cancer patient wants and
the exact opposite of what an ataxia-telangiectasia patient needs.

## LIMITS

- **n = 4 genes, chosen by argument, not sampled.** This is a structured probe with one
  adversarial case, not an estimate of any population parameter. No p-value is computed and
  none should be.
- **The two-category split (oncology-targeted vs metabolic) is proposed on four genes and is
  not tested.** It is the hypothesis this replication generates, not a result it establishes.
- **"Action-typed" is a minority of retrieved rows**, and at NPC1's defect it is none at all
  (see the caveat above). Untyped entries are never assumed inhibitory.
- **STRING confidence mixes experimental and text-mined evidence.** Tier membership is a
  network claim, not a claim of physical interaction.
- **Drug counts are retrieval counts**, subject to the same API caps documented for the
  original search; they are compared across tiers built the same way, not read as totals.
- **The first version of this file reported row-based percentages** (BUB1B 97.7%, ATM 98.7%,
  NPC1 57.2%, CFTR 52.9%). Those are superseded by the figures above. No verdict changed —
  the corrected numbers widen the split rather than narrowing it.
