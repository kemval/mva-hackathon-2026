# Track 2 — 3-minute pitch video: script and storyboard

**Team:** Gummietech · **Target runtime:** 3:00 (hard cap — the brief says 3 minutes)
**Recording note:** the account holder records and uploads to YouTube or Vimeo; the URL
is a required field on the Track 2 submit form.

**Word budget:** at a measured 145 wpm, 3:00 allows ~435 spoken words. The spoken lines
below total **433**, leaving headroom for pauses and visual beats. Do not improvise
additions — it will overrun. If a retake runs long, cut the last sentence of beat 3
first, then the second sentence of beat 4.

*Revised 2026-09-04 (see repo commit history). Beat 2 carries the structural
counterexample; beat 5 marks the NAD⁺ mechanism as an inference; beat 3 carries the
withdrawn generalisation and the replication that withdrew it. The spoken script now
matches Limitation 1, Verification item 1, and Part 8 of the report. Headroom is thin —
re-run the counter after any further edit.*

*(To re-check the count after any edit:*
`awk '/^> /{gsub(/^> /,""); n+=split($0,a," ")} END{print n}' pitch_script.md`*)*

**Tone:** this is about a real child. Calm and precise, not breathless. No "cure"
language anywhere. Never say a drug "works" — say what the evidence does and does not
show.

---

## Beat 1 — The correction (0:00–0:32)

**Visuals:** the two variants on a BubR1 domain diagram — `p.Leu737Ter` truncating before
the pseudokinase domain, `p.Asn1002Lys` inside it. Then a struck-through caption reading
"broken kinase", replaced by "not enough protein".

> "Track 1 found this child's diagnosis: two variants in BUB1B — a nonsense allele, and a
> missense allele in the kinase domain.
>
> The obvious next step is a drug that fixes a broken checkpoint. That step is wrong, and
> it sends the whole search the wrong way.
>
> Suijkerbuijk and colleagues studied MVA patient cells with exactly this genotype. The
> defect isn't broken BubR1. It's not enough BubR1."

## Beat 2 — Why that changes everything (0:32–1:08)

**Visuals:** the rescue experiment as a before/after bar; a two-residue burial comparison
(Q921 at 1.1% RSA vs Asn1002 at 16.2%) as the counterexample beat; then the 6%-vs-13%
threshold as a dial with a marked cliff.

> "Two results carry this submission.
>
> First: forcing two kinase-domain missense mutants back to normal abundance fully
> restored checkpoint function. One sits ten residues from this child's variant — but we
> modelled that, and it cut against us: a *tolerated* variant in the same domain is more
> buried still. Position doesn't prove instability. Hence the assay.
>
> Second: there's a threshold. At six percent of normal BubR1, cells missegregate
> chromosomes. At thirteen percent, segregation is essentially normal. A small gain could
> cross a real line.
>
> So the target isn't the checkpoint. It's protein quantity."

## Beat 3 — The search, and what its shape says (1:08–1:48)

**Visuals:** the six-tier bar chart — 0 drugs at BUB1B rising to 71 at the SASP tier.
Then a stark card: **129 of 142 = INHIBITOR**. Then the four-gene replication table, with
the two failed predictions struck through.

> "We searched twenty-four pathway genes across two drug databases — with the scoring
> rubric committed to git before we ran a single query.
>
> BUB1B returns zero drugs. So does every other checkpoint gene. And of a hundred and
> forty-two drug actions retrieved, a hundred and twenty-nine are inhibitors.
>
> Medicine is built out of inhibitors. This is a disease of too little.
>
> We pre-registered that as a general claim, tested three more diseases, and broke it. It
> isn't true of loss-of-function disease generally — it's true where oncology wants to
> inhibit the pathway. This child's gene is in the worst category."

## Beat 4 — What we would not give him (1:48–2:12)

**Visuals:** a red-bordered card: "17-AAG — top hit for 'aneuploidy' — contraindicated
here". Arrow showing HSP90 inhibition removing the residual protein.

> "Writing the exclusions before the search mattered.
>
> The best-known paper on drugs for aneuploidy proposes 17-AAG, an HSP90 inhibitor. But
> mutant BubR1 is an HSP90 client — block HSP90 and you destroy the little protein this
> child still has. The top hit of a keyword search is among the most contraindicated
> agents available."

## Beat 5 — The ranked answer, honestly labelled (2:12–2:38)

**Visuals:** the ranking table, with the regulatory-status column highlighted.

> "Our highest-scoring candidate is nicotinamide riboside — an NAD-plus precursor
> *inferred*, not shown, to raise BubR1 by slowing its degradation. It has a randomised
> placebo-controlled trial in Werner syndrome, and paediatric use to age one.
>
> But it's a supplement, not an approved medicine, and we don't blur that. The
> highest-scoring approved medicine is dasatinib plus quercetin — where none of twenty-two
> trials ever enrolled a child."

## Beat 6 — What we actually recommend (2:38–3:00)

**Visuals:** a single western blot band, then the two-way decision fork. Close on the line
"measure before treating".

> "But our first recommendation isn't a drug. It's a western blot.
>
> If BubR1 is reduced but present, the hypothesis is live. If it's absent, the whole top
> tier is futile — and we'd want to know before anyone gives a child anything.
>
> These are hypotheses for follow-up, not evidence that a medicine works. Measure first."

---

## Shot list

| # | Asset | Source |
|---|---|---|
| 1 | BubR1 domain diagram with both variants | `viz/track2_explainer.html`, mechanism section |
| 2 | "broken kinase" → "not enough protein" caption swap | title card |
| 3 | Rescue-experiment before/after | Suijkerbuijk 2010 Fig 4D — **redrawn from the reported result, not reproduced** |
| 4 | 6%/13% threshold dial | redrawn from the shRNA titration result |
| 5 | Six-tier drug-count bar chart | `data-notes/track2_target_drugs.tsv` |
| 6 | "129 of 142 INHIBITOR" card | same |
| 7 | HSP90 contraindication card | `literature/26_tang2011_aneuploidy_selective_REJECTED.md` |
| 8 | Ranking table | `data-notes/track2_ranking.tsv` |
| 9 | Western blot + decision fork | `viz/track2_explainer.html`, validation section |

## Recording checklist

- [ ] Read once against a timer before recording; confirm ≤ 3:00
- [ ] No patient-identifying detail on screen — no sex, no age, no location
- [ ] Do not show raw VCF content or genotype tables at any point
- [ ] Figures redrawn from data, not screenshots of copyrighted paper figures
- [ ] State "hypotheses for follow-up" explicitly (beat 6 does this — don't cut it)
- [ ] Upload unlisted or public; paste the URL into the Track 2 submit form
