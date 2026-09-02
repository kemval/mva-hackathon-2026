# Track 2 mechanism characterisation — working notes

Date: 2026-09-02. Status: mechanism settled against primary literature; therapeutic
inference explicitly separated from established finding throughout.

Track 2 asks for "characterization of the variant's mechanism (loss-of-function /
gain-of-function, pathway disrupted, downstream biological consequence) as basis for the
repurposing rationale." This document is that characterisation. The single most important
result of the exercise is that **the mechanism is not what the obvious reading suggests**,
and the correction changes which drugs are worth proposing.

---

## 1. Direction of effect: loss of function, and specifically loss of *quantity*

BUB1B-related MVA1 is autosomal recessive loss-of-function. Complete loss is not the
disease state — `Bub1b` null is embryonic lethal in mouse, and MVA patients survive to
childhood and beyond — so affected individuals are **hypomorphic**: they retain some
BubR1 function, just not enough.

The obvious reading of this proband's genotype is "the checkpoint kinase is broken." That
reading is wrong in a way that matters, and the literature settles it.

## 2. The published mechanism for this exact genotype architecture

Suijkerbuijk et al. 2010 (*Cancer Res* 70:4891, PMID 20516114,
`literature/15_suijkerbuijk2010_bubr1_abundance_mva.md`) studied MVA patient-derived cell
lines carrying precisely this architecture — "In patients with biallelic mutations, **a
missense mutation pairs with a truncating mutation**." Their conclusion is stated as the
paper's model:

> "We propose that chromosomal instability in MVA patients carrying BUB1B mutations is a
> result of **low BUBR1 protein abundance**."

The supporting chain:

| Observation | Detail |
|---|---|
| Patient cells have low BubR1 | Full-length protein decreased **2–6 fold** vs. wild-type across four patient lines |
| The truncating allele contributes nothing | Transcripts absent; NMD. "BUBR1 abundance of truncation mutants is mainly affected on mRNA level" |
| The missense allele is unstable, not inactive | ~2-fold increased protein turnover by cycloheximide chase; HSP90-dependent folding; cleared by the proteasome (MG132 rescues) |
| Kinase-domain position predicts instability | "All mutant proteins with substitution mutations in or near the kinase domain showed a **5–10 fold decrease** in levels." The two substitutions away from the domain (Y155C, R550Q) did not affect levels at all |
| **Restoring abundance restores function** | "Forced overexpression of the poorly expressed substitution mutants I909T and L1012P to levels comparable to wild-type BUBR1 **fully restored** the response to nocodazole ... these mutations do not impose significant constraints on BUBR1 function other than affecting overall BUBR1 protein abundance" |
| Residual protein still works | "The residual protein could be recruited to kinetochores, indicative of at least partial functionality" |
| **There is a threshold** | shRNA titration: ~6% residual BubR1 → missegregation in the majority of cells; **~13% → "virtually no impact on the fidelity of chromosome segregation"** |

So the defect is a **dosage defect in a protein that still works**, not a broken enzyme.

## 3. Where this proband's two variants sit in that framework

- **`p.Leu737Ter`** — truncating. Track 1 established, against the real exon structure,
  that the premature stop lies 747 nt upstream of the final exon-exon junction, far
  outside the ~50–55 nt NMD escape window. This is the "absence of transcripts from
  truncating mutants" class. Contributes **no protein**.
- **`p.Asn1002Lys`** — missense at residue 1002, inside the C-terminal pseudokinase
  domain (UniProt O60566, 766–1050). This is the "high protein turnover of missense
  mutants" class *by position*. The nearest characterised mutant, **L1012P, sits ten
  residues away** and is one of the two whose function was fully restored by forced
  overexpression.

**The inference, stated as an inference.** `p.Asn1002Lys` itself was **not** among the
mutants Suijkerbuijk tested. The prediction that it destabilises BubR1 rests on domain
membership plus the paper's generalisation that "a wide range of mutations in or near the
kinase domain can destabilize BUBR1" and that "this region of BUBR1 is highly sensitive to
amino-acid substitutions."

**And the counterexample must be stated with it: position does not guarantee it.**
`Q921H` lies inside the same domain and was "indistinguishable from wild-type LAP-BUBR1,
both on protein level and functionality." Of the kinase-domain substitutions that paper
examined, most destabilised and one did not. So `p.Asn1002Lys` is *probably* a
destabilising allele and is not *demonstrated* to be one. Track 1 independently classifies
it as a VUS, and nothing here upgrades that.

> This is why the validation plan leads with a BubR1 protein measurement rather than with
> a drug. See §7.

## 4. The therapeutic target follows: abundance, not activity

Three consequences, and they are the reason this report proposes what it proposes:

**(a) BUB1B is undruggable in the conventional sense, and the search confirms it.** DGIdb
returns **zero** drug-gene interactions for BUB1B. That is the correct answer, not a gap:
you cannot inhibit your way out of a protein deficiency, and there is no agonist of a
structural checkpoint scaffold. Any candidate must act on abundance or downstream.

**(b) The relevant pharmacological question is "what raises BubR1 protein?"** Exactly one
published answer exists. North/Sinclair et al. 2014 (*EMBO J*, PMID 24825348,
`literature/16_...`): SIRT2 deacetylates BubR1 at **K668**, and "deacetylation of lysine
668 (K668) of BubR1 **inhibits ubiquitylation and the targeting of BubR1 to the
proteasome**." NAD⁺ availability sets SIRT2 activity; NMN raises NAD⁺ and raises BubR1.

**The two literatures converge on the same control point.** Suijkerbuijk's MVA missense
mutants are lost *via the proteasome* (MG132 prevents it). Sinclair's ageing-related BubR1
decline is *via the proteasome*, gated by K668 acetylation. One pathway, reached from
MVA patient cells and from ageing biology independently. That convergence is the
mechanistic case.

**(c) K668 is intact on the surviving allele.** Residue 668 lies outside the 766–1050
pseudokinase domain, so `p.Asn1002Lys` does not disturb the regulatory site through which
SIRT2 acts. The mechanism is at least *available* on the allele that still makes protein.

**What is not established, and the report must not blur it.** In Sinclair 2014, **NMN was
administered to wild-type mice**, and the BubR1-hypomorph lifespan rescue used **SIRT2
transgenic overexpression**. No experiment in that paper gives an NAD⁺ precursor to a
BubR1-deficient animal. "NMN raises BubR1 abundance" is supported; "NMN helps BubR1
deficiency" is an inference joining two results across two genotypes and two
interventions. Further: the BubR1 rise was measured in **testes**, not muscle, at
500 mg/kg/day **intraperitoneally** — not an oral human dose.

## 5. Why the hypothesis survives the one thing Track 1 could not resolve

Track 1 could not phase the two variants (11 kb apart, beyond short-read range; the caller
emits `PGT`/`PID` elsewhere in the region but not here).

- **In trans** → biallelic hypomorphic MVA1: one silent allele plus one unstable allele.
  Low BubR1.
- **In cis** → functionally a mono-allelic BUB1B nonsense carrier. Wijshake et al. 2012
  (*PLoS Genet*, PMID 23300461, `literature/17_...`) show `BubR1^+/GTTA` mice have
  significantly reduced median *and* maximum lifespan with accelerated cataract,
  lordokyphosis, **skeletal muscle wasting, impaired exercise ability** and fat loss.
  Suijkerbuijk independently found carrier parents' BubR1 levels "consistently in between
  those of patients and unrelated healthy controls." Low BubR1.

**Both branches converge on reduced BubR1 abundance.** An abundance-directed intervention
therefore does not depend on resolving phase. Phase remains decisive for family
counselling and for Track 1's PM3 code — it is simply not load-bearing *here*.

## 6. Downstream: a fork, not a chain

From `notes/01_spindle_assembly_checkpoint_biology.md`, confirmed by graph tracing and not
to be flattened:

```
                                      ┌──> senescence + SASP      (common; most stressed cells)
low BubR1 ──> weakened SAC ──> CIN ───┤
     (§2-3)                           └──> cancer predisposition  (rare; a clone escapes)
```

Senescence and cancer are **siblings off CIN**, not a sequence. The senescence arm now has
a molecular sub-chain: missegregation → **micronuclei** → envelope rupture → cytosolic DNA
→ **cGAS-STING** → interferon/inflammatory signalling → SASP (Mackenzie et al. 2017,
`literature/24_...`; Bakhoum et al. 2018, `literature/25_...`; reviewed for aneuploidy
specifically by Kirsch-Volders & Fenech 2023, `literature/18_...`).

Two consequences the report must hold to:

1. **A senescence-targeting drug is not expected to reduce this child's tumour risk.**
   Conflating the arms would overstate the hypothesis. The cancer arm gets surveillance
   (Nakano et al. 2024, `literature/23_...`), not a prescription.
2. **Suppressing cGAS-STING is not a free good.** Bakhoum 2018 shows this same axis
   *promotes metastatic behaviour*; innate-immune sensing of micronuclei is part of how
   damaged cells are recognised. Blanket suppression in a cancer-predisposed child is a
   substantive risk, which is why the senomorphic tier ranks below the abundance tier.

## 7. Phenotype-to-branch mapping, honestly graded

The proband's eight HPO terms, mapped to what an intervention could and could not touch:

| HPO | Feature | Branch | Could an intervention plausibly touch it? |
|---|---|---|---|
| `HP:0003202` | Skeletal muscle atrophy | senescence/tissue | **The tightest available match.** Baker 2011 rescued muscle fibre diameter and exercise performance in `BubR1^H/H` mice by clearing p16⁺ cells; Wijshake 2012 reports muscle wasting from a *mono-allelic* MVA mutation. Both are mouse. |
| `HP:0001508` | Failure to thrive / low muscle mass | senescence/tissue | Same branch, same caveat |
| `HP:0004322` | Short stature | developmental | **No.** Largely fixed |
| `HP:0001518` | SGA / IUGR | developmental | **No.** Prenatal |
| `HP:0001622` | Premature birth (32 weeks) | perinatal | **No.** Historical |
| `HP:0002859` | Rhabdomyosarcoma | cancer | **Surveillance, not a drug** |
| `HP:0000121` | Nephrocalcinosis, *present since birth* | unexplained | **No** — and it is a *safety constraint*, not a target. Track 1 withdrew two proposed explanations; congenital onset raises rather than lowers the prior for a second monogenic cause |
| `HP:0200067` | Parental recurrent miscarriage | family history | Not this child's pharmacology. Relevant to counselling |

**The uncomfortable convergence, stated because it is the strongest objection to the
lead candidate.** The one phenotype most plausibly drug-approachable is skeletal muscle —
and skeletal muscle is exactly where NAD⁺ supplementation has repeatedly *failed* in
humans. The Werner RCT found no significant change in grip strength, walking speed or
skeletal muscle index (`literature/21_...`); Bohr's review says musculoskeletal conditions
"appear to be less receptive to this intervention" (`literature/14_...`).

The counter-argument is that those trials treated *generic* age-related sarcopenia,
whereas the proposal here is to restore a *specific deficient protein* whose loss is the
proximate cause — a different mechanism with a different prior. That is a genuine
argument. It is also only an argument, and the report labels it as one rather than letting
it quietly neutralise a consistent human negative.

## 8. The decisive experiment, and a bonus it delivers

**Measure BubR1 protein abundance in patient cells** (PBMCs or fibroblasts, western or
flow, against matched controls). It is cheap, standard, and it forks the entire hypothesis:

- **Reduced but present (roughly the 2–6 fold decrease Suijkerbuijk saw)** → the
  hypomorphic state the models represent; abundance restoration is mechanistically
  coherent and the threshold data suggest a modest gain could matter.
- **Near absent** → allele 2 makes no stable protein; there is nothing to stabilise, and
  the abundance tier is futile. Pivot downstream to senolytic/senomorphic.

**The bonus: the same assay speaks to Track 1's open question.** A demonstrated abundance
defect attributable to `p.Asn1002Lys` is functional evidence — the substance of ACMG PS3 —
for a variant currently classified VUS. One inexpensive experiment would both test the
therapeutic hypothesis and potentially resolve the variant classification. That is the
strongest practical recommendation this analysis can make, and it costs far less than any
drug.

---

## Claims register for this document

| # | Claim | Status |
|---|---|---|
| 1 | MVA1 with truncating+missense genotype acts via low BubR1 abundance | **Established** — Suijkerbuijk 2010, patient cells |
| 2 | Restoring abundance restores checkpoint function in kinase-domain missense mutants | **Established** — I909T, L1012P overexpression rescue |
| 3 | A functional threshold lies between ~6% and ~13% residual BubR1 | **Established** — shRNA titration, same paper |
| 4 | `p.Asn1002Lys` destabilises BubR1 | **Predicted, not demonstrated** — by domain analogy; Q921H is a same-domain counterexample |
| 5 | SIRT2/NAD⁺ raises BubR1 via K668 deacetylation blocking proteasomal targeting | **Established** — North/Sinclair 2014 |
| 6 | NMN raises BubR1 abundance in vivo | **Established in wild-type mice, testes, IP dosing** |
| 7 | NMN would raise BubR1 in a BubR1-deficient individual | **Untested inference** — never done in any BubR1-deficient animal |
| 8 | Reduced BubR1 is the shared consequence under either phase | **Established** for the trans case; **supported** for cis by Wijshake 2012 + carrier-parent levels |
| 9 | CIN → micronuclei → cGAS-STING → SASP | **Established in model systems**, not shown in MVA patients |
| 10 | Senescence and cancer are siblings off CIN, not a chain | **Established** — pathway structure |
| 11 | HSP90 inhibitors would deplete residual mutant BubR1 | **Predicted from direct evidence** — geldanamycin removed mutant BubR1 in Suijkerbuijk's own experiments |
