# MVA (BUB1B) — what this analysis found, in plain language

**One page for a treating team or family. Not medical advice.** This is a research
hypothesis submitted to a public hackathon. Nothing here has been tested in anyone with
MVA. No one involved has contacted, or may contact, the family or their clinicians.

---

## The finding, in one paragraph

In this child's form of MVA, the problem is most likely **not enough BubR1 protein**,
rather than a BubR1 protein that doesn't work. One gene copy is switched off entirely
(the nonsense variant produces no protein). The other makes a protein that is probably
unstable and gets broken down too fast — the published pattern for MVA variants sitting
where this one sits. In patient cells with this same genotype pattern, **putting the
protein level back up restored normal chromosome segregation.** That is why we think
"protein quantity" is the thing worth aiming at.

## The single most useful next step is a lab test, not a medicine

**Measure BubR1 protein in the child's own cells** — a western blot or quantitative flow
on blood cells or skin fibroblasts, compared against controls.

| If BubR1 is… | What it means |
|---|---|
| **Reduced but present** | The hypothesis is live. There is protein there to stabilise, and published work suggests the gap between "cells missegregate" and "cells are fine" is only a few percent of normal. |
| **Absent** | There is nothing to stabilise. The whole top of our candidate list is pointless, and that is worth knowing **before** anyone tries anything. |

This test is inexpensive and standard. It may also help resolve the second variant, which
current genetic criteria leave classified as "uncertain".

Two other cheap tests would help: a **karyotype** on non-cancerous cells (confirms the
diagnosis, and is the test the international guideline lists for MVA), and a
**micronucleus assay**, which measures the actual chromosome-segregation problem directly.

## What we would consider, and what we would not

**Most promising on mechanism:** NAD⁺ precursors — nicotinamide riboside or nicotinamide
mononucleotide. These raise the level of a molecule the cell uses to protect BubR1 from
being degraded. There is a randomised placebo-controlled trial in Werner syndrome and
paediatric use in ataxia-telangiectasia down to age one.
**Be clear: these are dietary supplements, not licensed medicines**, and no one with MVA
has ever taken them for this reason. Honest caveats: the key mouse experiment was never
done in a BubR1-deficient animal, and in human trials NAD⁺ supplements have repeatedly
**failed** to improve muscle — which is one of this child's main problems.

**Best-scoring licensed medicine:** dasatinib plus quercetin, a "senolytic" combination
that clears worn-out cells. Dasatinib is licensed in children from age 1 for leukaemia —
but **none of the 22 trials of this senolytic combination has ever included a child**, and
dasatinib is known to slow growth in children, which matters for a child already small for
age.

**We would actively avoid HSP90 inhibitors.** This is the most concrete warning we can
offer. The unstable BubR1 in MVA depends on a cellular chaperone called HSP90 to stay
folded. Drugs that block HSP90 — a real class in cancer trials — would be expected to
**destroy the small amount of BubR1 this child still has**. Awkwardly, one such drug is the
top result of the best-known paper on "drugs for aneuploidy", so it is exactly what a
quick search would suggest.

We would also avoid drugs designed to kill cells with the wrong number of chromosomes. In
MVA those cells are spread throughout the body — that is the condition, not a tumour.

## Cancer surveillance is separate — and it is where the real evidence is

The chromosome problem leads to two separate consequences: worn-out cells, and raised
cancer risk. **A medicine aimed at the first should not be expected to reduce the
second.** For cancer risk, an international expert group (AACR, 2024) recommends for MVA:

- **Renal ultrasound every 3 months from birth to age 7**
- **Avoid radiation exposure where possible**
- Regular clinical review for signs of rhabdomyosarcoma and other tumours
- Watch for: an unexplained lump or swelling, blood in the urine, high blood pressure,
  pain or persistent discomfort

## One practical caution about genetic drug-dosing reports

We ran a pharmacogenomic analysis on the existing sequencing data. **It came back mostly
uninformative, and that is the honest result.** Only 22 of 1,226 relevant positions were
actually measured. If a report of this kind says "normal metaboliser" for thiopurines,
irinotecan or fluorouracil based on whole-genome data alone, that may be an assumption
rather than a measurement — in our run, 16 of 23 genes changed answer depending on which
assumption was used. **If any of those chemotherapies is ever being considered, ask for a
dedicated pharmacogenomic test first.**

One finding is worth stating plainly because the software flags it alarmingly: a variant
in the *RYR1* gene was labelled "uncertain susceptibility" to malignant hyperthermia (a
serious anaesthetic reaction). **Checked against the expert-panel classification, that
variant is Benign.** It should not change anaesthetic planning.

---

*Full reasoning, sources and code: `submissions/track2/gummietech_track2_report.md` and
the repository it sits in. Every claim above is traceable to a named primary source.*
