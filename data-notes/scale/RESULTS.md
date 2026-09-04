# Scalability replication — results against the pre-registered prediction

Run 2026-09-04. Prediction: `pipeline/scalability_prediction.md`, committed at `98b9b04`,
**before** any query below was executed. Node sets built by `pipeline/build_node_set.py`
(STRING v12, score ≥ 700, ≤25 per tier); drugs retrieved by the unmodified
`pipeline/track2_target_search.py`; measured by `pipeline/scale_measure.py`.

## The numbers

| Gene | Disease | drugs at d0 | d1 | d2 | Open Targets inhibitory | DGIdb inhibitory | at the defect itself |
|---|---|---|---|---|---|---|---|
| **BUB1B** | MVA (this case) | **0** | 375 | 198 | **129/132 = 97.7%** | 215/216 = 99.5% | no drugs at all |
| **ATM** | Ataxia-telangiectasia | 84 | 791 | 248 | **154/156 = 98.7%** | 196/208 = 94.2% | **10/10 = 100% inhibitory** |
| **NPC1** | Niemann-Pick C | 137 | 81 | 508 | **95/166 = 57.2%** | 217/348 = 62.4% | 137 rows, none typed |
| **CFTR** | Cystic fibrosis | 46 | 285 | 776 | **101/191 = 52.9%** | 166/328 = 50.6% | **11/55 = 20.0%** inhibitory; 31 ACTIVATING, 8 POSITIVE MODULATOR |

## Verdict, against the pre-committed criteria

**P1 — drug count at the defect. FAILS at NPC1.** Predicted "zero or near-zero"; retrieved
**137**. Confirmed at ATM (>0, as predicted) and CFTR (>0 and approved, as predicted).

**P2 — direction of effect. FAILS at NPC1, and this was the pre-committed serious one.**
Predicted ≥80% inhibitory across the neighbourhood; measured **57.2% / 62.4%**.

The pre-registration says, in its own words:

> **P2 failing at NPC1** would be the serious one. It would mean the inhibitor skew is a
> property of the mitotic/senescence neighbourhood rather than of loss-of-function disease,
> and Part 8's generalisation would have to be **withdrawn**, not softened.

**It failed. The generalisation as published is withdrawn.** Track 2 Part 8 claimed the
~95% inhibitor skew "is not a fact about BUB1B — it is a fact about **every
loss-of-function rare disease**, which is most of them." That claim is false as stated, and
this replication is what shows it.

**P3 — monotonic rise with distance. FAILS at three of four, including BUB1B itself.**
Under the mechanical STRING tier rule, drug count does *not* rise monotonically with
distance for BUB1B (0 → 375 → 198), ATM (84 → 791 → 248) or NPC1 (137 → 81 → 508). It
rises only for CFTR (46 → 285 → 776), the one gene for which no prediction was made.

The published monotonicity claim is therefore **an artefact of the curated tier structure**,
not a property of the underlying networks. Curation was the obvious attack on that result
and the attack lands.

**The CFTR falsification test discriminated, exactly as designed.** At the causal gene,
only **20.0%** of typed entries are inhibitory, against 31 ACTIVATING and 8 POSITIVE
MODULATOR — the correctors and potentiators. The test was informative rather than merely
passed.

## What survives, and it is narrower and more useful than what was claimed

Two things survive the replication intact:

1. **BUB1B's zero at the defect is real, not a curation artefact.** It survives a tier rule
   built mechanically from STRING with no human choice in it. Zero drugs, both databases.
2. **The inhibitor skew is real where it applies, and it is extreme.** BUB1B 97.7%, ATM
   98.7% on Open Targets; 99.5% and 94.2% on DGIdb, two independent databases agreeing.

What changes is the *scope* of the claim. The skew does not track loss-of-function. It
tracks **whether the causal gene's neighbourhood is an oncology drug-development target**:

| Neighbourhood | Genes | Inhibitory |
|---|---|---|
| Mitotic checkpoint / DNA damage response — heavily targeted by oncology inhibitor programmes | BUB1B, ATM | **94–99%** |
| Lysosomal transport, ion channel — metabolic and channel biology, where agonists and activators are ordinary | NPC1, CFTR | **51–62%** |

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
worst category available: zero drugs at the defect, and 97.7% of everything nearby pointing
in the direction that makes the disease worse.

**The ATM result is the strongest new finding and is worth stating on its own.** All ten
action-typed compounds at the causal gene are **inhibitors** — AZD0156, AZD1390, AZD7648,
M3541, BAY-8400 — in a disease defined by ATM *deficiency*. The entire ATM-directed
pharmacopeia exists to make ATM-deficient cells, which is what a cancer patient wants and
the exact opposite of what an ataxia-telangiectasia patient needs.

## LIMITS

- **n = 4 genes, chosen by argument, not sampled.** This is a structured probe with one
  adversarial case, not an estimate of any population parameter. No p-value is computed and
  none should be.
- **The two-category split (oncology-targeted vs metabolic) is proposed on four genes and is
  not tested.** It is the hypothesis this replication generates, not a result it establishes.
- **"Action-typed" is a minority of retrieved rows.** NPC1 returned 137 drug rows at the
  defect with no action type at all, so its d0 direction is genuinely unknown rather than
  balanced. Only typed entries are counted, and untyped entries are not assumed inhibitory.
- **STRING confidence mixes experimental and text-mined evidence.** Tier membership is a
  network claim, not a claim of physical interaction.
- **Drug counts are retrieval counts**, subject to the same API caps documented for the
  original search; they are compared across tiers built the same way, not read as totals.
