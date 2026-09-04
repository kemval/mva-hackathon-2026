# Track 2 Report — Drug Repurposing in BUB1B-Related Mosaic Variegated Aneuploidy

**Team:** Gummietech
**Proband:** PROBAND01 (source VCF: `WGS_EX2312012_HGWCNDSX7.vcf.gz`)
**Date:** 2026-09-02, last audited 2026-09-04
**Companion:** Track 1 methods report, `submissions/track1/gummietech_track1_report.md`

---

## Summary

Track 1 identified a compound-heterozygous candidate in **BUB1B**: `p.Leu737Ter`
(Likely Pathogenic, NMD-predicted null) and `p.Asn1002Lys` (VUS, gnomAD singleton, inside
the C-terminal pseudokinase domain). This report asks what, if anything, an existing
medication can do about that.

**The central finding is a correction.** The intuitive reading of this genotype — "the
mitotic checkpoint kinase is broken, so fix or bypass the checkpoint" — is not what the
literature supports, and acting on it would send the drug search in the wrong direction.
In MVA patient-derived cells carrying *exactly* this architecture (a truncating allele
paired with a kinase-domain missense allele), Suijkerbuijk et al. 2010 showed the defect
is **insufficient BubR1 protein**, not defective BubR1 enzymology — and, critically, that
**forcing abundance back up fully restores checkpoint function**. The therapeutic target
is therefore protein *quantity*.

That reframing does four things a keyword-driven search cannot:

1. **It explains why the obvious search returns nothing.** BUB1B has **zero** drugs in
   both Open Targets and DGIdb, independently. So does every other spindle-assembly-
   checkpoint gene. You cannot inhibit your way out of a protein deficiency.
2. **It selects a different drug class** — agents that raise BubR1 abundance (the
   NAD⁺/SIRT2 axis, which controls BubR1's proteasomal turnover) rather than agents that
   clear the downstream damage (senolytics), which is where the available literature
   otherwise points every team.
3. **It survives the one question Track 1 could not answer.** Whether the two variants
   are in *cis* or *trans*, the shared consequence is reduced BubR1 abundance. The
   hypothesis does not depend on unresolved phase.
4. **It generates contraindications no pathway search would surface** — including that
   **HSP90 inhibitors are predicted to make this child worse**, because the mutant BubR1
   is an HSP90 client. One such agent is simultaneously the top hit of the best-known
   "drugs for aneuploidy" paper. An adversarial review pass found that the same
   contraindication is reachable by a *second, less obvious route*: **HSP90 inhibitors are
   also a recognised senolytic class**, which means "senolytic" cannot be used as a
   class-level safety label in this child and the gate must be applied agent by agent
   (§3.3, §3.4).

**Ranked answer.** Against a scoring rubric pre-registered before any query was run, the
highest-scoring candidate overall is **nicotinamide riboside** (13/17) — which is a
*dietary supplement, not an approved medication*. The highest-scoring **approved
medication** is **dasatinib plus quercetin** (10/17). This report presents both and does
not blur them, because the brief asks for approved medications and the science points
first at something that is not one.

**What we actually recommend doing first is not a drug.** It is a **western blot for
BubR1 in patient cells**. If BubR1 is reduced-but-present, the abundance hypothesis is
live and the threshold data suggest a modest gain could matter. If it is absent, the
entire top tier is futile and the ranking should be re-read from the senolytic tier down.
The same inexpensive assay would also generate functional evidence bearing on Track 1's
unresolved VUS. Measure before treating.

**A patient-specific layer.** Because this child has a cancer-predisposition syndrome,
has already had rhabdomyosarcoma, and may face chemotherapy again, we also ran a
CPIC-guided pharmacogenomic analysis of the proband's own genome. This is actionable
whether or not any repurposing candidate is ever used — and it is reported with the same
blank-versus-zero honesty Track 1 applied to coverage.

> **Framing, per the track's own instruction.** These are hypotheses for follow-up, not
> evidence that any medicine works. Nothing here is medical advice, no MVA patient has
> ever received any of these agents for this indication, and no contact with the family,
> their clinicians, or the MVA Society has been made or should be inferred.

---

## Part 1 — Mechanism characterisation

### 1.1 Direction of effect

BUB1B-related MVA1 is autosomal-recessive **loss of function**. Complete loss is not the
disease state: `Bub1b`-null is embryonic lethal in mouse, and MVA patients survive into
childhood and beyond. Affected individuals are therefore **hypomorphic** — they retain
BubR1 function, but not enough of it.

### 1.2 The published mechanism for this genotype architecture

Suijkerbuijk et al. 2010 (*Cancer Res* 70:4891, PMID 20516114) is the load-bearing
citation for this report, and it is not an analogy: its subject is patients whose
genotype is built the same way as this proband's. Its opening premise — "In patients with
biallelic mutations, **a missense mutation pairs with a truncating mutation**" — is a
description of this case.

Its conclusion is stated as the paper's model:

> "We propose that chromosomal instability in MVA patients carrying BUB1B mutations is a
> result of **low BUBR1 protein abundance**."

The evidence chain, measured in patient-derived cell lines:

| Observation | Detail |
|---|---|
| Patient cells have low BubR1 | Full-length protein down **2–6 fold** vs. wild-type across four patient lines |
| The truncating allele contributes nothing | Transcripts absent (NMD); "BUBR1 abundance of truncation mutants is mainly affected on mRNA level" |
| The missense allele is **unstable, not inactive** | ~2-fold increased turnover on cycloheximide chase; HSP90-dependent folding; cleared by the proteasome (MG132 rescues) |
| Kinase-domain position predicts instability | Substitutions in or near the domain showed a **5–10 fold decrease**; the two substitutions *outside* it (Y155C, R550Q) did not affect levels at all |
| **Restoring abundance restores function** | "Forced overexpression of the poorly expressed substitution mutants I909T and L1012P to levels comparable to wild-type BUBR1 **fully restored** the response to nocodazole ... these mutations do not impose significant constraints on BUBR1 function other than affecting overall BUBR1 protein abundance" |
| Residual protein is competent | "The residual protein could be recruited to kinetochores, indicative of at least partial functionality" |
| **A threshold exists** | shRNA titration: ~6% residual BubR1 → missegregation in most cells; **~13% → "virtually no impact on the fidelity of chromosome segregation"** |

Two of these deserve emphasis. The **rescue experiment** is a direct human-cell
demonstration that the therapeutic principle works: raise the abundance of a
kinase-domain missense BubR1 mutant, and checkpoint function comes back. The
**threshold** is what makes a modest pharmacological effect potentially meaningful rather
than cosmetic — the difference between failing and functioning sits within a few
percentage points of normal protein.

### 1.3 Where this proband's variants sit

- **`p.Leu737Ter`** — truncating. Track 1 established, against the real exon structure,
  that the stop lies 747 nt upstream of the final exon-exon junction, far outside the
  ~50–55 nt NMD-escape window. This is the "absent transcript" class: **no protein**.
- **`p.Asn1002Lys`** — missense at residue 1002, inside the pseudokinase domain
  (UniProt O60566, 766–1050). This is the "high turnover" class *by position*. The
  nearest characterised mutant, **L1012P, lies ten residues away**, and is one of the two
  whose function was fully restored by forced overexpression.

**Stated as the inference it is.** `p.Asn1002Lys` was not among the mutants Suijkerbuijk
tested. The prediction rests on domain membership plus that paper's generalisation that
"a wide range of mutations in or near the kinase domain can destabilize BUBR1" and that
the region shows "a strong tendency ... to misfolding."

**And the counterexample belongs in the same paragraph.** `Q921H` lies inside the same
domain and was "indistinguishable from wild-type LAP-BUBR1, both on protein level and
functionality." Position does not guarantee destabilisation. Most kinase-domain
substitutions in that series destabilised; one did not.

Structural modelling sharpens rather than dissolves this counterexample
(`data-notes/structural_analysis_n1002k.md`, AlphaFold `AF-O60566-F1`): **Q921 is *more*
deeply buried than Asn1002 — RSA 1.1% against 16.2% — and is itself hydrogen-bonded**, so
its tolerance cannot be explained away as a surface position. The distinction that
survives is chemical rather than positional: Gln→His preserves both hydrogen-bond donor
and acceptor capability, whereas Asn→Lys preserves neither and buries a positive charge in
an aromatic pocket. That distinction is in turn weakened by `R814H`, a conservative
Arg→His substitution that *was* destabilising. Position-based reasoning has a documented
failure in this protein, and this report does not lean on it.

So the mechanism for this child is **probable, not demonstrated** — which is exactly why
§5 leads with an assay rather than a prescription. Track 1 classifies `p.Asn1002Lys` as a
VUS and nothing here changes that.

### 1.4 Why the therapeutic target is abundance

**BUB1B is not druggable in the conventional sense, and this is a measured result rather
than an assumption.** Both Open Targets and DGIdb return **zero** drugs or clinical
candidates for BUB1B. Open Targets nonetheless flags it as small-molecule tractable
("High-Quality Ligand", "Druggable Family") — which sharpens rather than softens the
point: a small molecule against BubR1 would be an *inhibitor*, and the defect is a
deficiency. Chemical tractability is not therapeutic relevance.

**Exactly one published mechanism raises BubR1 protein.** North/Sinclair et al. 2014
(*EMBO J* 33:1438, PMID 24825348): SIRT2 deacetylates BubR1 at **K668**, and
"deacetylation of lysine 668 (K668) of BubR1 **inhibits ubiquitylation and the targeting
of BubR1 to the proteasome**." SIRT2's activity depends on NAD⁺; NMN raises NAD⁺ and
raises BubR1.

**The two literatures converge on one control point.** Suijkerbuijk's MVA missense
mutants are cleared *by the proteasome*. Sinclair's age-related BubR1 decline is *by the
proteasome*, gated by K668 acetylation. Two independent research programmes — one from
MVA patient cells, one from ageing biology — arrive at the same node. That convergence,
not either paper alone, is the mechanistic argument.

**K668 is intact here.** Residue 668 lies outside 766–1050, so `p.Asn1002Lys` does not
disturb the regulatory site through which SIRT2 acts. The mechanism is at least
*available* on the allele that still makes protein.

**What Sinclair 2014 does not show, stated plainly because it is routinely
over-cited.** NMN was administered to **wild-type** mice. The `BubR1^H/H` lifespan rescue
used **SIRT2 transgenic overexpression**. No experiment in that paper gives an NAD⁺
precursor to a BubR1-deficient animal. Further: the BubR1 rise was measured in **testes**
(BubR1 was "difficult to determine" in heart), at 500 mg/kg/day **intraperitoneally** —
not an oral human dose. "NMN raises BubR1" is supported; "NMN helps BubR1 deficiency" is
an inference across two genotypes and two interventions, and is labelled as one
throughout this report.

### 1.5 The hypothesis is robust to unresolved phase

Track 1 could not resolve *cis* vs *trans* (the variants are ~11 kb apart, beyond
short-read phasing; the caller emits `PGT`/`PID` elsewhere in the region but not here).

- **In trans** → biallelic hypomorphic MVA1: one silent allele, one unstable allele.
- **In cis** → functionally a mono-allelic BUB1B nonsense carrier. Wijshake et al. 2012
  (*PLoS Genet*, PMID 23300461) show `BubR1^+/GTTA` mice — one MVA allele — have
  significantly reduced median *and* maximum lifespan, with accelerated cataract,
  lordokyphosis, **skeletal muscle wasting, impaired exercise ability** and fat loss.
  Suijkerbuijk independently found carrier parents' BubR1 "consistently in between those
  of patients and unrelated healthy controls."

**Both branches end at reduced BubR1 abundance.** Phase remains decisive for family
counselling and for Track 1's PM3 evidence code. It is not load-bearing for the
therapeutic hypothesis, and that is a genuine strength rather than a hedge.

### 1.6 Downstream: a fork, not a chain

```
                                      ┌──> senescence + SASP      (common; most stressed cells)
low BubR1 ──> weakened SAC ──> CIN ───┤
                                      └──> cancer predisposition  (rare; a clone escapes)
```

Senescence and cancer predisposition are **siblings off chromosomal instability**, not a
sequence. The senescence arm has a molecular sub-chain: missegregation → **micronuclei**
→ envelope rupture → cytosolic DNA → **cGAS-STING** → inflammatory signalling → SASP
(Mackenzie 2017; Bakhoum 2018; reviewed for aneuploidy by Kirsch-Volders & Fenech 2023).

Two consequences this report holds to:

1. **A senescence-directed drug is not expected to reduce this child's tumour risk.** The
   cancer arm gets surveillance (Part 6), not a prescription. Claiming otherwise would
   overstate the hypothesis beyond what the pathway structure supports.
2. **Suppressing cGAS-STING is not a free good.** Bakhoum 2018 shows this same axis
   *drives metastatic behaviour*; micronucleus sensing is part of how damaged cells are
   recognised. Blanket suppression in a cancer-predisposed child is a real risk, and it
   is why the senomorphic tier ranks below the abundance tier.

### 1.7 Phenotype mapping, graded honestly

| HPO | Feature | Branch | Plausibly addressable? |
|---|---|---|---|
| `HP:0003202` | Skeletal muscle atrophy | senescence/tissue | **Tightest available match.** Baker 2011 rescued muscle fibre diameter and exercise performance in `BubR1^H/H` mice; Wijshake 2012 reports muscle wasting from a *single* MVA allele. Both mouse |
| `HP:0001508` | Failure to thrive / low muscle mass | senescence/tissue | Same branch, same caveat |
| `HP:0004322` | Short stature | developmental | **No** — largely fixed |
| `HP:0001518` | SGA / IUGR | developmental | **No** — prenatal |
| `HP:0001622` | Premature birth (32 weeks) | perinatal | **No** — historical |
| `HP:0002859` | Rhabdomyosarcoma | cancer | **Surveillance, not a drug** |
| `HP:0000121` | Nephrocalcinosis, *present since birth* | unexplained | **No** — and it is a *safety constraint*. Track 1 withdrew two proposed acquired explanations, then withdrew the correction's own inference as well: onset timing is undated in the source file and the paediatric evidence puts the *higher* monogenic yield in full-term children without risk factors, which is the opposite of this proband's profile. Both readings stay live and neither carries a conclusion (Track 1, matrix C13) |
| `HP:0200067` | Parental recurrent miscarriage | family history | Counselling, not this child's pharmacology |

**The strongest objection to our own lead candidate, stated here rather than buried.**
The one phenotype most plausibly drug-approachable is skeletal muscle — and skeletal
muscle is precisely where NAD⁺ supplementation has repeatedly **failed** in humans. The
Werner syndrome RCT found no significant change in grip strength (p = 0.563), walking
speed (p = 0.584) or skeletal muscle index (p = 0.671). Bohr's review independently
concludes musculoskeletal conditions "appear to be less receptive to this intervention."

The counter-argument is that those trials treated *generic* age-related sarcopenia,
whereas this proposal restores a *specific deficient protein* whose loss is the proximate
cause — a different mechanism with a different prior. That is a real argument. It is also
only an argument, and it does not cancel a consistent human negative.

**A second honest limit on scope.** Much of this child's phenotype was set before birth.
IUGR, 32-week delivery and established short stature are not reversible by any agent
here. The realistic goal is slowing ongoing tissue attrition, not reversal, and any
proposal implying otherwise is overselling.

---

## Part 2 — The search, and what its shape reveals

### 2.1 Method

The scoring rubric was **written and committed before any query was run**
(`pipeline/track2_scoring_rubric.md`, commit `20eda20`). The commit order is verifiable
in the repository history and is the reason the rubric cannot have been reverse-engineered
around a favoured answer.

Twenty-four pathway nodes were fixed from the mechanism characterisation
(`data-notes/regions/track2_pathway_nodes.tsv`; every Ensembl ID verified live against
Ensembl REST), spanning six tiers: the defect itself, the checkpoint, the abundance
machinery, micronucleus sensing, senescence, and SASP. Each was queried against **two
independent drug-target databases** — Open Targets and DGIdb — because agreement between
sources drawing on different underlying data is the only cheap check available on either.
Both GraphQL schemas were verified live; Open Targets has renamed its drug collection from
`knownDrugs` to `drugAndClinicalCandidates`, and the old name now returns a hard error
rather than an empty result, so a naive script would silently report zero drugs for
everything.

### 2.2 Drug availability rises with distance from the defect — in this curated node set

> **Superseded in scope by Part 8.** The monotonic pattern below is a real property of
> *this* 24-gene curated pathway set. It does **not** survive when the tiers are rebuilt
> mechanically from STRING network distance — it fails for BUB1B itself under that rule
> (0 → 375 → 198). The pattern is an artefact of the curation, and Part 8 reports the
> replication that shows it. What survives is the zero at the defect, which holds under
> both constructions.

Unique drugs and clinical candidates per node, Open Targets:

| Tier | Genes | Unique OT drugs |
|---|---|---|
| **the defect** | BUB1B | **0** |
| checkpoint (SAC) | BUB1, BUB3, CDC20, MAD1L1, MAD2L1, TTK | 2 |
| micronucleus sensing | CGAS, STING1 | 1 |
| senescence | BCL2, BCL2L1, CDKN1A, CDKN2A, TP53 | 16 |
| abundance machinery | CD38, HSP90AA1, NAMPT, NMNAT1, PARP1, SIRT2 | 30 |
| SASP | IL6, JAK1, JAK2, MTOR | 71 |

**BUB1B returns zero in both databases independently** — as do BUB3, CDC20, MAD2L1 and
NMNAT1. Six further genes return zero in Open Targets but *not* in DGIdb (BUB1 6, MAD1L1
2, CGAS 3, SIRT2 12, CDKN2A 29, CDKN1A 30 interaction records), and the distinction is
worth keeping: DGIdb aggregates interaction *claims* of mixed confidence, and states
plainly that its records are "not presented in ranked order of potential or predicted
efficacy".

**SIRT2 deserves a line of its own.** Every SIRT2 compound in either database is an
inhibitor or an unranked low-confidence claim; **there is no SIRT2 activator anywhere in
the searched space.** That is precisely why the abundance mechanism has to be reached
through substrate supply — an NAD⁺ precursor — rather than through a drug against the
enzyme itself.

The abundance tier's 30 is misleading and worth unpacking, because 23 of those drugs are
in the two genes this report *excludes*: HSP90AA1 (10, gated) and PARP1 (13, gated).
Subtract them and the abundance tier has **four** usable drugs, all anti-CD38 antibodies,
plus three NAMPT inhibitors that push NAD⁺ in the wrong direction.

### 2.3 The structural finding: the pharmacopeia is built of inhibitors

Across all 24 genes, of 142 action-typed Open Targets entries, **129 are `INHIBITOR`**.
Adding antisense inhibitors, RNAi inhibitors and antagonists brings it to 135, or ~95%
inhibitory. There is exactly **one `ACTIVATOR`** and **one `STABILISER`** in the entire set.

> **What an "entry" is**, because the figure is not reproducible without knowing: a unique
> **`(gene, drug, action_type)` triple**. One drug acting on two genes counts twice; the
> same drug–gene pair reported under two action types counts twice. Reproduce with
> `python3 pipeline/scale_measure.py --selfcheck data-notes/track2_target_drugs.tsv`,
> which asserts 142 and 129 and fails loudly otherwise. Every percentage in Part 8 uses
> this same unit, so the two sections are directly comparable.

DGIdb agrees independently: among its approved-drug interactions across these genes,
**62 are `INHIBITORY` and 1 is `ACTIVATING`** — and that one is *granisetron against
TP53*, an antiemetic, which is a spurious annotation of exactly the kind DGIdb's own
disclaimer warns about ("not presented in ranked order of potential or predicted
efficacy").

> **This is the report's central structural finding.** Modern drug development produces
> inhibitors, because inhibiting a protein is chemically tractable and most common
> diseases involve too much of something. **MVA is a disease of too little of something.**
> The mismatch between an inhibitor-shaped pharmacopeia and a deficiency-shaped disease is
> not incidental to this case — it is why repurposing for loss-of-function rare disease is
> hard, and it generalises far beyond BUB1B.

> **Narrowed by Part 8, on our own pre-registered test.** The last clause is too strong and
> is corrected there. On the same counting unit as the 129/142 above, the inhibitor skew does
> **not** hold for loss-of-function disease generally — strict inhibitory measures **54.5%
> for NPC1** and **37.5% for CFTR**. It holds where the causal gene sits in a pathway
> oncology has invested in inhibiting: **95.8% for BUB1B**, **93.4% for ATM**. The corrected
> claim is narrower, diagnostic, and still bad news for this child, whose gene is in the
> worst category.

It also explains why the honest answer to "which approved medication targets this
mechanism?" is *none directly*, and why the highest-scoring candidate is a metabolic
substrate (an NAD⁺ precursor) rather than a drug: substrate supply is one of the few ways
to push a system *up* using something that already exists.

### 2.4 Trial evidence, with paediatric eligibility read from structured fields

ClinicalTrials.gov API v2, with paediatric eligibility taken from each trial's own
eligibility module (`minimumAge`, `stdAges`) rather than from free text, because "children
were included" is easy to assert and hard to check.

The API returns at most 100 records per query, so where a candidate has more than 100
trials the paediatric figure is a **floor over the first 100 retrieved**, not a total.
Rows marked ✓ were retrieved completely and their counts are exhaustive.

| Candidate | Trials (total) | Retrieved | Paediatric-eligible |
|---|---|---|---|
| metformin | 3112 | 100 | ≥11 |
| sirolimus | 2377 | 100 | ≥13 |
| ruxolitinib | 485 | 100 | ≥24 |
| baricitinib | 194 | 100 | ≥16 |
| **nicotinamide riboside** | 123 | 100 | **≥8** (minimum ages down to **1 year**; several in ataxia telangiectasia) |
| navitoclax | 45 | 45 ✓ | 6 |
| fisetin | 36 | 36 ✓ | 2 |
| nicotinamide mononucleotide | 32 | 32 ✓ | 1 |
| **dasatinib + quercetin** | 22 | 22 ✓ | **0** |

The load-bearing row is the complete one: **all 22** dasatinib+quercetin trials were
retrieved, so the zero is exhaustive rather than a sampling artefact.

**Not one of the 22 dasatinib+quercetin trials has enrolled anyone under 18** — and since
all 22 were retrieved, that is a complete count, not a floor. This matters because
dasatinib *itself* is FDA-approved from age 1 — so the tempting sentence "dasatinib is
approved in children" is true of the drug and false of the regimen.

> **A wider version of that sentence was in this report and is withdrawn.** It read "the
> lowest minimum age across the entire senolytic trial landscape is 18," and the table
> directly above it refutes it: **navitoclax has six paediatric-eligible trials with
> minimum ages down to 1 year**, and fisetin two. Inspected individually, all six navitoclax
> trials are paediatric *leukaemia* protocols — navitoclax as a BCL-2/BCL-xL cytotoxic, at
> continuous oncologic dosing — and fisetin's two are breast-cancer-survivor trials tagged
> `CHILD` in `stdAges` with no `minimumAge` stated at all. So the defensible claim is
> narrower and is the one that was already load-bearing: **no trial of any of these agents
> as a senolytic, at intermittent senolytic dosing, has enrolled a child.** The retained
> fields cannot separate indication from agent, so that narrower claim rests on reading the
> twelve trial titles, not on a structured field, and is labelled accordingly. The general
> claim was the same error as verification row 12 — a property of one exhaustively retrieved
> row asserted across rows that were not checked. The paediatric safety data are for continuous oncologic dosing, not intermittent
senolytic dosing, and this report does not let the two borrow credibility from each other.

---

## Part 3 — Candidates

### 3.1 Two rankings, because the brief and the science point different ways

Scored on the pre-registered rubric: **A** mechanistic directness (0–5), **B** evidence
tier (0–5), **C** paediatric data (0–4), **D** case-specific safety burden (−5–0),
**E** feasibility (0–3). Regulatory status is recorded but **deliberately not scored**, so
that an approved drug with a weak mechanism cannot outrank a better-evidenced supplement.

| # | Candidate | Total | A | B | C | D | E | Status | Tier |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **nicotinamide riboside** | **13** | 4 | 5 | 2 | −1 | 3 | supplement | abundance |
| 2 | nicotinamide mononucleotide | 11 | 5 | 2 | 2 | −1 | 3 | supplement | abundance |
| 3 | **dasatinib + quercetin** | **10** | 3 | 4 | 4 | −3 | 2 | **approved** | senolytic |
| 4 | metformin | 10 | 2 | 2 | 4 | −1 | 3 | approved | senomorphic |
| 5 | fisetin | 9 | 3 | 2 | 2 | −1 | 3 | supplement | senolytic |
| 6 | ruxolitinib | 7 | 3 | 2 | 3 | −3 | 2 | approved | senomorphic |
| 7 | sirolimus | 6 | 2 | 2 | 3 | −3 | 2 | approved | senomorphic |
| 8 | baricitinib | 6 | 3 | 1 | 3 | −3 | 2 | approved | senomorphic |
| 9 | daratumumab | 4 | 4 | 1 | 3 | −4 | 0 | approved | abundance |
| 10 | navitoclax | 3 | 3 | 2 | 1 | −3 | 0 | investigational | senolytic |

Ranks 3 and 4 tie at 10 and are separated by the rubric's declared tie-break (axis B
first): dasatinib+quercetin has genuine human biomarker trials, metformin does not.

**Approved medications only — the brief's literal ask:** dasatinib + quercetin (10),
metformin (10), ruxolitinib (7), sirolimus (6), baricitinib (6), daratumumab (4).

**A caution about metformin's rank.** It reaches 10 almost entirely on safety, paediatric
familiarity and cost (C = 4, E = 3), with the weakest mechanism score in the top half
(A = 2). The rubric is working as designed — it refuses to let mechanism alone dominate —
but a reader should not mistake metformin's position for mechanistic support. It is the
*safest* thing on the list, not the most *targeted*.

**Scores are not measurements.** Two candidates one point apart are not meaningfully
distinguishable, and every score carries a written justification with its citation in
`data-notes/track2_scores.tsv`. Disagree with any single cell and the ranking recomputes;
that is the point of keeping judgement in a reviewable table and arithmetic in code.

### 3.2 Lead candidate — NAD⁺ precursors (nicotinamide riboside; nicotinamide mononucleotide)

**Regulatory status: dietary supplement. Not an approved medication.** NMN's lawful
supplement status was restored by FDA in September 2025 after the 2022 exclusion; neither
compound is a licensed drug for any indication.

**Why it leads.** It is the only candidate acting on the *defect* rather than its
consequences. The mechanism is specific and published: SIRT2 deacetylates BubR1 K668,
blocking its ubiquitylation and proteasomal degradation; NAD⁺ availability sets SIRT2
activity. K668 is intact on this proband's surviving allele. And the degradation route it
acts on is the *same route* by which MVA missense mutants are lost in patient cells.

NR and NMN split the two axes in an instructive way. **NMN scores higher on mechanism**
(5): it is the compound actually shown to raise BubR1 in vivo. **NR scores higher on
evidence** (5): it has a double-blind randomised placebo-controlled crossover trial in
Werner syndrome, a monogenic progeroid disease, plus paediatric exposure in ataxia
telangiectasia — a genome-instability, cancer-predisposition disorder that is the closest
available disease analogue. NR wins on total because human trial evidence and paediatric
data outweigh a one-step-closer rodent mechanism.

**The three limits that must travel with any citation of this candidate:**

1. **NMN was never given to a BubR1-deficient animal, and the animal in question does not
   carry this disease's genotype.** The rescue in `BubR1^H/H` mice used genetic SIRT2
   overexpression, so the bridge from "NMN raises BubR1 in wild-type mice" to "NMN would
   help this child" is an inference, not a result. A second gap sits underneath it:
   `BubR1^H/H` is a hypomorph **no MVA patient has**, and the mouse built with the human
   architecture instead — `BubR1^X753/L1002P`, truncating plus kinase-domain missense — is
   **embryonic lethal**, none of 39 embryos surviving to E13.5 (Sieben et al. 2020, *JCI*),
   while the human carrying the analogous genotype lived. The species discordance is
   itself the finding. Every mouse result cited anywhere in this report therefore comes
   from a background that models the *direction* of the defect, not the genotype
   (`literature/33_...`, claims K2–K6). One numbering trap is worth naming because it
   invites exactly the wrong inference: mouse `L1002P` is **human L1012P**, not this
   proband's residue 1002.
2. **Muscle is where NAD⁺ supplementation has consistently failed in humans** — and muscle
   is this child's most drug-approachable phenotype (§1.7). This is not one awkward trial
   but a consistent pattern across independent RCTs, assembled by deliberately searching
   for null results (`literature/30_...`): Stocks et al. 2022 found **"no NRPT
   supplementation effect"** on muscle regeneration or stem-cell recruitment after
   experimental injury; Elhassan et al. 2019 raised the muscle NAD⁺ metabolome
   **"without altering mitochondrial bioenergetics"**; and Shoji et al. 2025 found
   sarcopenia indicators unchanged in Werner syndrome. Target engagement is settled —
   oral NR demonstrably reaches muscle — and functional benefit is not.
   **The one endpoint that does move consistently is inflammatory**: Elhassan reports
   depressed circulating cytokines. So the defensible rationale for NR in this child runs
   through the SASP arm of the fork, **not** through reversing muscle atrophy — which is
   also the arm least likely to be confused with reversing a developmentally fixed deficit
   (Limitation 8).
3. **Raising NAD⁺ in a cancer-predisposition syndrome carries a theoretical oncologic
   concern**, since proliferating tumour cells also depend on NAD⁺. This is the −1 on
   axis D and it is not resolved by any data we found.

**Also: not all NAD⁺ precursors are equivalent here.** Nicotinamide (plain vitamin B3
amide) is a **sirtuin inhibitor** at high concentration. Since this mechanism runs
*through* SIRT2, nicotinamide is a poor substitute for NR or NMN and should not be
swapped in on the assumption that any B3 vitamer will do.

### 3.3 Highest-scoring approved medication — dasatinib + quercetin

**Regimen, as published:** dasatinib 100 mg/day + quercetin 1250 mg/day, three days per
week for three weeks (Justice et al. 2019, IPF, n = 14, open-label); or D 100 mg +
Q 1000 mg for 3 days (Hickson et al. 2019, diabetic kidney disease, n = 11).

**Human evidence, cited as corrected.** Hickson 2019 carries a **2020 corrigendum** whose
substance is in a supplementary appendix invisible to PubMed and the PMC record. A
re-analysis using the pre-planned paired tests on untransformed data **withdrew** the skin
senescence-marker result and the individual IL-1α / IL-6 / MMP-9 claims. What survives:
adipose p16INK4A⁺ cells down (p = 0.017), macrophages (p = 0.007), crown-like structures
(p = 0.004), a six-measure joint analysis (p = 0.020), and a composite blood-SASP score
(p = 0.003), with MMP-12 alone at p = 0.034. The primary hypothesis held; the peripheral
claims did not. Anyone citing this trial from its abstract is citing withdrawn text.

**Mechanistic fit to this case.** Baker et al. 2011 cleared p16⁺ senescent cells in
`BubR1^H/H` mice and rescued muscle fibre diameter and exercise performance — the tightest
match to `HP:0003202`. But that was a **genetic transgene (INK-ATTAC), not these drugs**;
D+Q has never been tested in a BubR1 model. Baker 2011 also explicitly did **not** rescue
cardiac phenotypes or extend survival.

**A within-class gate that must travel with any senolytic recommendation.** Ranking a
senolytic top among approved medications creates a hazard the tier label hides:
**HSP90 inhibitors are themselves a senolytic class.** Fuhrmann-Stroissnigg et al. 2017
identified them as such — seven chemotypes active, benchmarked in the same assay as
dasatinib + quercetin and navitoclax, with 17-DMAG extending healthspan in `Ercc1−/∆`
progeroid mice. That paper's senior authors (Tchkonia, Kirkland, Niedernhofer, Robbins)
are the same investigators behind the D+Q programme, Justice 2019 and Hickson 2019, so
this is not a rival result that can be set aside.

The consequence is specific. Anyone extending this report's logic — *"a senolytic scored
highest, and this child is progeroid-like, so choose the senolytic with the best in vivo
progeroid data"* — would arrive at **17-DMAG, which gate G1 forbids** (§3.4). The
contraindication is reachable through the senolytic door as well as the aneuploidy door,
and only the second is obvious. **"Senolytic" is therefore not a safe class label here.**
Any agent in this tier must be checked individually against its molecular target before
use, and HSP90-directed senolytics are excluded.

**A consistency correction to gate G1's wording** *(post-registration clarification,
2026-09-02 — the rubric in `pipeline/track2_scoring_rubric.md` is deliberately left as
committed, so the pre-registration remains verifiable from commit order; this is an
amendment recorded here, not a silent edit).* As written, G1 excludes agents "predicted to
lower BubR1 abundance" **on mechanism alone**. Applied uniformly, that wording also flags
**quercetin**: Aalinkeel et al. 2008 found quercetin makes HSP90 the single
most-down-regulated protein in the PC-3 proteome (−1.75-fold, p < 0.001), destabilising the
HSP90 clients Raf-1 and cdk4, with siRNA knockdown phenocopying the effect.

We do **not** reject dasatinib + quercetin on this basis, and the reasoning is stated so it
can be checked rather than trusted. The effect is demonstrated at **~50 µM in vitro**, one
to two orders of magnitude above the free plasma concentrations achievable from oral
quercetin including the 1000–1250 mg/day used in senolytic trials; the mechanism is
reduced *expression* rather than active-site inhibition; quercetin is a promiscuous
flavonoid, so one most-changed spot in one cancer cell line is a lead, not an established
pharmacology; and the apoptotic effect spared normal epithelium. **G1 should therefore read
"…at concentrations achievable in vivo."** With that qualifier, 17-AAG remains excluded
(100 nM, target-directed) and quercetin does not.

What survives the potency argument is narrow and is recorded rather than dismissed: this
child's checkpoint function sits near a threshold of **~6–13%** of normal BubR1, so a
proportionally small decrement matters more here than in a healthy adult, and **no one has
measured BubR1 under quercetin at any concentration.** That is a cheap experiment and it is
added to §5.2 as an arm of the assay already recommended.

**Case-specific safety (axis D = −3):**
- **Growth.** Tyrosine kinase inhibitors are documented to impair growth in children
  treated for CML. This child is already growth-restricted (`HP:0004322`). This is the
  most specific and serious objection.
- **Chemotherapy interaction.** Dasatinib is a CYP3A4 substrate; interaction with future
  cytotoxic regimens is foreseeable, and Nakano et al. 2024 note that genomic-instability
  disorders show "exquisite sensitivity to anticancer treatments."
- **Zero paediatric senolytic exposure** (§2.4).

### 3.4 Explicitly rejected, with reasons

Rejections are part of the deliverable, not omissions. Three candidates were excluded by
hard gates fixed before the search:

**HSP90 inhibitors (tanespimycin/17-AAG, ganetespib, luminespib, and seven other names the
search returned) — gate G1, and this is the finding we would most want a clinician to
see.** *(Ten unique drug names on HSP90AA1 in Open Targets, which is nine compounds once
retaspimycin's free base and hydrochloride are merged, and eight once `CD24FC` — a CD24-Fc
fusion protein annotated `INHIBITOR` against HSP90AA1 — is set aside as an annotation
artefact rather than an HSP90 inhibitor. An earlier version of this sentence said "eight
others," implying eleven.)* Suijkerbuijk 2010 showed mutant BubR1 is an **HSP90 client**: geldanamycin severely
reduced mutant but not wild-type BubR1, and cycloheximide plus geldanamycin "removed
virtually all mutant BUBR1 protein." Inhibiting HSP90 in this child is predicted to
**destroy the residual BubR1 this child depends on**.

The inversion is worth stating plainly: **17-AAG is the lead compound of Tang et al.
2011, the best-known "aneuploidy-selective" paper** — the single most likely hit for
anyone searching "drugs for aneuploidy." On this case's own mechanism it is among the most
clearly contraindicated agents available. Pathway proximity is not therapeutic rationale.

Tang's full text sharpens *why*, in a sentence available only in the body: 17-AAG inhibited
all four trisomic lines at 100 nM, and the authors read this as evidence that **"aneuploid
cells rely on protein quality control pathways for their survival."** That is the same
chaperone dependency, approached from the other side — so in this child HSP90 inhibition is
a **double hit on one axis**: it depletes the mutant BubR1 directly, and it strikes the
quality-control capacity that constitutionally aneuploid cells depend on.

**The same gate excludes HSP90-inhibitor *senolytics* — a route the tier structure hides.**
Fuhrmann-Stroissnigg et al. 2017 established HSP90 inhibitors as a senolytic class
(17-DMAG, ganetespib, NVP-AUY922, BIIB021, PU-H71, NVP-BEB800, AT13387), with 17-DMAG
improving healthspan in progeroid mice — **the strongest in vivo progeroid data among the
senolytics screened there.** So the best-evidenced senolytic for a progeroid-like child is
precisely the one this case forbids. G1 is therefore a **within-class** gate on the
senolytic tier as well as a cross-tier one (§3.3), and no senolytic may be selected by
class label alone. Note the categories: 17-AAG and 17-DMAG are **investigational**, not
approved medications.

**Aneuploidy-selective cytotoxics (AICAR, chloroquine, 17-AAG) — gate G2.** The concept
was built for tumours, where aneuploid cells are the disease and euploid cells are the
patient. In mosaic variegated aneuploidy the aneuploid cells **are** the patient,
distributed across tissues by definition of the syndrome. This is not a therapy; it is a
whole-body toxicity with a mechanism.

**NAMPT inhibitors (daporinad, teglarinad) — gate G1.** They lower NAD⁺, the exact
opposite of the intended direction, and would be predicted to lower BubR1. The search
returned them under the abundance tier, which is precisely why the gates were written
before the search.

**PARP inhibitors (olaparib and 12 others) — gate G1, on the harm limb.** Mechanistically
these are *NAD⁺-sparing* (PARP1 is a major NAD⁺ consumer), so they genuinely reach the
abundance node — this is the most interesting rejection of the four. But PARP inhibitors
are associated with secondary MDS/AML, and administering a genotoxic agent to a child with
a constitutional chromosomal-instability and cancer-predisposition syndrome inverts the
risk calculus. Rejected on harm, not on mechanism, and flagged as the candidate most
worth revisiting if a non-genotoxic NAD⁺-sparing agent ever emerges.

**Not gated but ranked low, and why:** daratumumab (4) is mechanistically apt — anti-CD38
blockade raises NAD⁺ by removing its principal consumer, and it was the *only approved
drug the search found acting on the abundance tier* — but it carries profound
immunosuppression and infection risk in a cancer-predisposed child, requires IV infusion,
and has no paediatric approval. Navitoclax (3) is investigational with dose-limiting
thrombocytopenia.

---

## Part 4 — A patient-specific pharmacogenomic layer, and an honest negative

### 4.1 Why this is here

Everything above is disease-level. This part is about **this child**, who has a
cancer-predisposition syndrome, has already had rhabdomyosarcoma, and — per Nakano et al.
2024 — belongs to a class of disorders showing "exquisite sensitivity to anticancer
treatments such as ionizing radiation and chemotherapy, which may further increase the
risk of second cancers." Drug-metabolism genotype is therefore actionable for this child
**whether or not any repurposing candidate is ever used**, and it is derivable at zero
marginal cost from the genome already sequenced for Track 1.

**Method.** PharmCAT v3.4.0 (CPIC-guided) against the proband's own genome-wide VCF,
restricted to the 1,226 PharmCAT positions with contigs renamed (`1` → `chr1`) to match
the tool's GRCh38 expectation. Fully scripted in `pipeline/track2_pgx_screen.sh`.

### 4.2 The result is mostly a negative, and the negative is the useful part

**Only 22 of 1,226 PharmCAT positions carry an interpretable variant call in this VCF.**
The other 1,204 are simply absent — and this is a variants-only VCF with no reference
blocks, so **absence is not evidence of a reference genotype**. (Twenty-*three* positions
carry a call; the 23rd is the undocumented RYR1 record at `chr19:38499696` that PharmCAT
discarded, §4.3. The three numbers reconcile as 22 + 1,204 = 1,226 only because that one is
excluded, and this report states which side of the ledger it falls on rather than letting
the arithmetic imply it.) It is the same invariant Track 1 enforced on
gnomAD frequencies, SpliceAI scores and call density, carried into a new domain.

PharmCAT provides a `--missing-to-ref` flag for exactly this situation, and its own CLI
labels it **"DANGEROUS!"**. We ran the analysis **both ways** and compared:

**16 of 23 genes change their call when absent positions are assumed to be reference.**
Seven of the sixteen are shown below — the ones whose flip manufactures a *reassuring*
label, which is the failure mode that matters clinically. The other nine are ABCG2,
CACNA1S, CFTR, CYP2B6, CYP2C19, CYP4F2, IFNL3, NAT2 and VKORC1; two of those are worth a
line of their own, because they show the assumption does not only invent normality.
**NAT2** goes `Unknown/Unknown` → `*5/*5`, a *slow-acetylator* call conjured out of absent
positions, and **CYP2B6** collapses from 30 candidate diplotypes to the single `*2/*6`.
Both are re-derivable from the two committed PharmCAT reports in `data-notes/pgx/`.

| Gene | Strict (no assumption) | With `--missing-to-ref` |
|---|---|---|
| TPMT | Unknown/Unknown | *1/*1 → "Normal Metabolizer" |
| NUDT15 | Unknown/Unknown | *1/*1 → "Normal Metabolizer" |
| UGT1A1 | Unknown/Unknown | *1/*1 → "Normal Metabolizer" |
| CYP2C9 | Unknown/Unknown | *1/*1 → "Normal Metabolizer" |
| SLCO1B1 | Unknown/Unknown | *1/*1 → "Normal Function" |
| G6PD | Unknown | B/B → "Normal" |
| CYP3A4 | Unknown/Unknown | *1/*1 → "Normal Metabolizer" |

> **Every one of those reassuring "Normal Metabolizer" calls is an artefact of the
> assumption, not a measurement.** A pipeline that ran PharmCAT with `-0` and printed the
> table would hand a clinician a clean-looking pharmacogenomic clearance for thiopurines,
> irinotecan and fluoropyrimidines that **this data cannot support**. That is the single
> most important output of this section.

**A subtlety that survives even the strict run.** PharmCAT's own messages note that "the
DPYD Reference allele assignment is characterized by the absence of variants at the
positions that are included in the underlying allele definition." So even the conservative
run's *positive* diplotype labels embed an absence-equals-reference assumption at the
other positions in each allele definition. The only fully-supported facts here are the
**observed variant genotypes themselves**.

### 4.3 What is genuinely supported, verified variant by variant

Three observed calls, each verified against ClinVar with genomic coordinates matched to
the VCF:

| Variant | Call | Depth/GQ | ClinVar | Interpretation |
|---|---|---|---|---|
| `CYP3A5` rs776746 (c.219-237A>G) | **hom** T>C | DP 48, GQ 99 | VCV000005066, drug response | **CYP3A5 \*3/\*3 — poor metaboliser (non-expressor)**. The common genotype in European ancestry |
| `DPYD` rs1801160 (c.2194G>A, \*6) | het C>T | DP 32, GQ 99 | VCV000100080, drug response, **expert panel** | CPIC assigns \*6 normal function; activity score unchanged |
| `RYR1` rs35364374 (c.6178G>T, p.Gly2060Cys) | het G>T | DP 54, GQ 99 | **VCV000093279 — Benign, reviewed by expert panel** | See below |

**The RYR1 finding is a false alarm, and catching it matters.** PharmCAT reports this
diplotype with the CPIC phenotype **"Uncertain Susceptibility"** to malignant hyperthermia
— an alarming label for a child facing repeated procedures under general anaesthesia.
Checked against the primary source, **ClinGen's expert panel classifies this exact variant
Benign** for malignant hyperthermia susceptibility 1 (3-star review). The tool's
conservative-by-design label is more alarming than the expert classification warrants.

Reporting "possible malignant hyperthermia susceptibility" from the tool output alone
would have been a clinically consequential error — the kind that changes anaesthetic
planning for no reason. **A pharmacogenomic phenotype label is not a variant
classification, and must be checked against one.**

Separately, PharmCAT flagged an **undocumented variant at chr19:38499696** in RYR1 (VCF
shows C>T; the allele definition expects G) which it silently "replaced with reference."
That variant is uninterpreted, not absent.

### 4.4 What this section actually recommends

Not a drug. Three concrete asks a clinical team could act on:

1. **Do not treat this analysis, or any WGS-derived PGx run on a variants-only VCF, as
   pharmacogenomic clearance.** TPMT, NUDT15, UGT1A1, DPYD and CYP2C9 are **not
   established** in this data.
2. **If thiopurines, irinotecan or fluoropyrimidines are ever contemplated** — all
   plausible in rhabdomyosarcoma and in the leukaemias reported in MVA1 — **order a
   targeted clinical pharmacogenomic assay first.** Irinotecan in particular is used in
   relapsed rhabdomyosarcoma regimens, and UGT1A1 status is unresolved here.
3. **The RYR1 result should not change anaesthetic planning.** It is expert-panel Benign.

---

## Part 5 — What to do first: the decisive experiment

The track's own framing is that these are "hypotheses for follow-up, not evidence that a
medicine works." Made concrete, the first step is not a prescription.

### 5.1 Measure BubR1 protein

**A western blot (or quantitative flow) for BubR1 in patient PBMCs or fibroblasts against
matched controls.** It is cheap, standard, and it forks the entire report:

| Result | Interpretation | Consequence |
|---|---|---|
| **Reduced but present** (Suijkerbuijk saw 2–6 fold decreases) | The hypomorphic state the models represent | Abundance restoration is coherent; the ~6%-to-~13% threshold suggests a modest gain could matter |
| **Absent / near-zero** | Allele 2 makes no stable protein | Nothing to stabilise. **The entire top tier is futile**; re-read the ranking from the senolytic tier down |

**It also answers a Track 1 question.** A demonstrated abundance defect attributable to
`p.Asn1002Lys` is functional evidence — the substance of ACMG **PS3** — for a variant
currently classified VUS. One inexpensive experiment tests the therapeutic hypothesis and
may resolve the variant classification. Nothing else in this report costs so little and
decides so much.

**The structural analysis raises the value of this assay rather than substituting for
it.** Modelling gave the mechanism a specific, falsifiable form — Asn1002 makes three
side-chain hydrogen bonds cross-linking the Trp978 and Val998 backbone, and Asn→Lys loses
the acceptor outright — but it also found that the report's own counterexample is
structurally indistinguishable from the candidate (§1.3). No computational route can
settle which way this residue behaves. A single abundance measurement can.

### 5.2 Supporting assays, cheapest first

| Assay | What it establishes | Note |
|---|---|---|
| **Cytokinesis-block micronucleus assay** | Direct read-out of the mechanism (missegregation rate) | Standard, inexpensive, and it measures the actual defect rather than a proxy |
| **Karyotype on non-malignant metaphases** | Confirms the MVA diagnosis | Already Track 1's first recommended test, and independently the diagnostic Nakano 2024 lists for MVA |
| Senescence markers (p16, SA-β-gal) | Whether the senescence arm is engaged | Kirsch-Volders & Fenech: "no biomarker or biomarker combination characteristic for all types of senescent cells" — a panel of imperfect proxies |
| SASP cytokine panel | Whether inflammation is measurable | Same caveat |
| Blood NAD⁺ / NADH | Whether there is a deficit to correct | Bohr: assessing individual NAD⁺ status is "challenging" and not standardised |
| **BubR1 western ± NR, ± quercetin, ± an HSP90 inhibitor** | Whether the lead candidate raises BubR1, whether quercetin lowers it at achievable exposures, and whether the G1 prediction is real | **These are three extra arms on the plate already required by §5.1** — same cells, same assay, marginal cost only. Concentrations must be matched to achievable human plasma levels, *not* to the mouse intraperitoneal exposure in North 2014 |

### 5.3 What would falsify each candidate

- **NAD⁺ precursors** — BubR1 absent on western; or NAD⁺ normal at baseline with no rise
  on supplementation; or BubR1 unchanged despite a documented NAD⁺ rise.
- **Senolytics** — no senescent-cell burden detectable; or muscle phenotype unchanged
  after clearance in a model carrying this genotype. **Separately disqualifying, per agent:**
  any senolytic whose mechanism runs through HSP90 (§3.3, §3.4).
- **Dasatinib + quercetin specifically** — a non-flat BubR1 dose-response to quercetin
  across achievable plasma concentrations would demote it; a flat one would clear the
  question raised in §3.3.
- **Senomorphics** — no measurable SASP/inflammatory signature to suppress.

**The ordering principle is measure before treating**, and no recommendation in this
report is contingent on an unmeasured assumption without saying so.

---

## Part 6 — The cancer branch: surveillance, not a prescription

Per §1.6, senescence and cancer predisposition are siblings off chromosomal instability,
not a chain. **No agent in this report should be expected to reduce this child's tumour
risk**, and claiming otherwise would be the single easiest overreach available.

The intervention with actual evidence behind this branch is surveillance. The primary
recommendation is Hol et al. 2021 (*Eur J Cancer* 153:51–63, SIOP-Europe Host Genome
Working Group / SIOP Renal Tumour Study Group), read here as the version of record rather
than through a summary; Nakano et al. 2024 (*Clin Cancer Res*, 2nd AACR Childhood Cancer
Predisposition Workshop) endorses it — "This AACR study group supports these
recommendations". The MVA-specific protocol is:

- **Renal ultrasound every 3 months from birth until age 7**, for all MVA conditions
  including those of unknown genetic cause. The 3-month interval is justified by tumour
  growth rate — the shortest reported Wilms doubling time is 11 days, and an interval of
  4 months or more "risks higher tumour stage at diagnosis".
- **"Radiation exposure should be avoided."**
- **Regular clinical assessment including review of systems** for signs of
  rhabdomyosarcoma and other malignancies.
- Family-facing warning signs, named explicitly: "abnormal mass or swelling, hematuria,
  hypertension, pain, and discomfort."

**The risk that justifies this protocol is quantified in the primary, and the figure is
striking.** Wilms tumour has been reported in **approximately 50% of patients with *BUB1B*
variants** (Hol 2021), against ~20% for *TRIP13* and none reported for *CEP57* — the
highest Wilms risk in the guideline's "other syndromes" section. Three caveats travel with
it and must not be dropped: the estimate rests on small early case series (Jacquemont
2002, Hanks 2004), no denominator is given, and in a literature where patients are
published *because* they developed tumours, ascertainment bias runs toward overestimation.
The guideline's own framing is "because of the limited number of reported patients." Note
also that the recommendation is anchored to **cytogenetically confirmed** MVA — which
independently corroborates this project's decision to lead with karyotype as the
confirmatory test.

**The age-7 endpoint is borrowed, not MVA-derived.** The guideline gives a rationale — by
age 7, 90% of sporadic Wilms tumours, 94% in Beckwith-Wiedemann and >95% in *WT1*-related
syndromes have been diagnosed — but is explicit that "for other CPS, the number of
reported patients with WT was too small to determine this percentage," and MVA is an
"other CPS". The endpoint applied to this child is therefore a harmonised convention
carried over from syndromes with larger case counts. The guideline is transparent about
that; this report should be too.

**The radiation-avoidance advice is precautionary rather than MVA-specific, and it is
independent of the modality choice.** A targeted search found **no study of
radiosensitivity in MVA, *BUB1B*-deficient or PCS-syndrome patients**; the supporting
sentence is a class statement — "**many** of these genomic instability disorders also
present with exquisite sensitivity" — naming ataxia-telangiectasia and Nijmegen breakage
syndrome, not MVA. It remains sound as precaution, and on the general position that no
amount of radiation is considered absolutely safe. But a class generalisation applied to a
specific syndrome is exactly the move this report flags elsewhere, so its tier is stated
rather than inherited. **Separately, ultrasound is not a compromise forced by
radiosensitivity:** the guideline judges ultrasonography "equally effective for initial WT
detection" against CT or MRI. Modality and radiation advice are independent arguments.

**One limit has to travel with this protocol.** It is a *Wilms* surveillance programme,
and this child has already had a rhabdomyosarcoma. The guideline does not address what
surveillance becomes after a first malignancy; where it considers a prior tumour at all,
it is a prior *renal* tumour, formerly a reason to prolong surveillance in *WT1*-related
syndromes and since superseded by harmonising every syndrome to the 7th birthday. And the
omission of non-renal surveillance is **explicit, not accidental** — the guideline states
that "cancer surveillance for other tumour types is warranted in some of these conditions
(but outside the scope of this guideline)." Nakano 2024 then adds only "regular clinical
assessment including review of systems," with no modality, interval or endpoint. For this
child the position across both sources is a well-specified renal protocol and, for
everything else, clinical review with no protocol attached. **That is a documented gap in
the evidence base, not a reason to depart from the protocol** — and it is a reasonable
thing for the treating team to know it is a gap.

Nakano 2024 also confirms the genotype-specific risk profile Track 1 reasoned to
independently: "A convincing increased cancer risk particularly during childhood has been
described only for **MVA1 and MVA3**", with MVA1 tumours "predominantly Wilms tumor and
rhabdomyosarcoma", plus MDS, AML and ALL.

This is where real-world benefit for this family most plausibly lies, and it requires no
new science — only that the protocol is known, followed, and understood for what it does
and does not cover.

---

## Part 7 — Limitations

Stated as a list because burying them in prose would defeat the purpose.

1. **`p.Asn1002Lys` is not proven to destabilise BubR1, and structural analysis makes the
   analogy weaker rather than stronger.** It was not among the mutants Suijkerbuijk tested,
   and `Q921H` is a same-domain counterexample that behaves like wild-type. Modelling both
   residues on AlphaFold `AF-O60566-F1` (`data-notes/structural_analysis_n1002k.md`) shows
   **Q921 is *more* buried than Asn1002 (RSA 1.1% vs 16.2%) and also makes buried
   side-chain hydrogen bonds** — so every structural feature that would mark residue 1002
   as critical is also present at a position where substitution demonstrably did nothing to
   protein level. Position-based reasoning has a documented failure in this protein. What
   the modelling does supply is a *specific and falsifiable* mechanism: Asn1002 makes three
   side-chain hydrogen bonds cross-linking the Trp978 and Val998 backbone, and Asn→Lys
   loses the acceptor outright while introducing a buried positive charge into an aromatic
   pocket. That is a hypothesis to test, not evidence for the conclusion. The mechanism for
   *this child* is probable by analogy, not demonstrated. Track 1 classifies the variant as
   a VUS and this report does not upgrade it.
2. **No NAD⁺ precursor has ever been given to a BubR1-deficient animal**, let alone a
   person with MVA. The lead candidate's central inference is untested. **And the mouse
   models this report draws on do not carry the human MVA genotype** — `BubR1^H/H` is a
   hypomorph no patient has, while the mouse built with the patient architecture is
   embryonic lethal where the equivalent human lived (§3.2; `literature/33_...`). A rescue
   in a BubR1 mouse does not license a human expectation here, and this report's mouse
   tiers should be read at that reduced weight throughout.
3. **Muscle is the wrong tissue for the lead candidate's track record.** Human NAD⁺
   trials have consistently failed on musculoskeletal endpoints — three independent RCT
   nulls on the endpoint class that matters most (§3.2) — and muscle is this child's most
   drug-approachable phenotype. The nulls disconfirm the *generic* muscle claim; they do
   not test the genotype-specific BubR1-abundance hypothesis, which remains untested in
   humans altogether.
4. **No MVA patient has received any agent in this report for this indication.** There is
   no clinical precedent, anywhere, for any of it.
5. **n = 1.** Nothing here is generalisable to other MVA patients without their own
   genotype and mechanism assessment — a different variant class (for example the
   `Y155C`/`R550Q` stable mutants, which impair function *without* lowering abundance)
   would point at a different tier of this same ranking.
6. **The hyperPARylation/NAD⁺-depletion framework is imported.** Bohr's review concerns
   DNA-*repair* disorders; MVA is a chromosome-*segregation* disorder in which DNA damage
   is secondary. Whether MVA cells actually show NAD⁺ depletion is **untested** and is a
   measurable question, listed in §5.2.
7. **The cGAS-STING → SASP chain is model-system biology**, not shown in MVA patients.
8. **Developmentally fixed features will not respond.** IUGR, prematurity and established
   short stature are historical.
9. **The pharmacogenomic layer establishes very little**, by design and by honest
   reporting — 1,204 of 1,226 positions are uncalled (§4.2).
10. **Scores are structured arguments, not measurements.** The rubric strained in one
    place worth naming: axis C assumes a drug/supplement dichotomy that does not cleanly
    cover "approved adult drug with paediatric trial exposure but no paediatric
    indication." Baricitinib and daratumumab were both scored 3 under that reading, and a
    reader who scores them differently should recompute rather than accept ours.
11. **A cited source's full text was never obtained, and a database cross-reference was
    wrong.** Kirsch-Volders & Fenech 2023 is held here as **abstract only**: NCBI's own
    `elink` maps its PMID to a PMC record that renders a *different* paper by overlapping
    authors, and no correct open deposit exists. Both quotations this report draws from it
    were re-verified verbatim against the primary PubMed record, so no claim is affected —
    but nothing beyond that abstract may be attributed to it. A second instance of the same
    NCBI linkage defect was found in the same pass. Both are recorded in
    `literature/_fetch_log.md`, and a title-vs-identifier check now runs across the corpus.
12. **Database coverage is a real limit.** Open Targets and DGIdb do not index dietary
    supplements as drugs, so the lead candidate could never have been *found* by the
    search — it came from the mechanism literature. A purely database-driven pipeline
    would have missed it entirely, which is itself a finding about this class of method.

---

## Part 8 — Scalability

The criterion asks whether the approach generalises. An earlier version of this section
*asserted* that it does. That assertion has since been pre-registered as a falsifiable
prediction, tested on three further diseases, and **partly refuted by our own test.** What
follows is the corrected version, because a generalisation that has survived an honest
attempt to break it is worth more than one that was never tried.

**1. The method is a parameterised pipeline, not a one-off.** `track2_target_search.py`
takes any gene set; `track2_trial_evidence.py` takes any intervention list;
`track2_score_candidates.py` applies any rubric. `build_node_set.py` now builds the gene
set itself, mechanically, from STRING network distance. For a new disease the only input is
a gene symbol. Nothing is hardcoded to BUB1B — demonstrated, not claimed, by running the
identical code path on NPC1, ATM and CFTR (`data-notes/scale/`, `pipeline/scale_measure.py`).

### 2. What we predicted, and what actually happened

Pre-registered in `pipeline/scalability_prediction.md` at commit `98b9b04`, before any
query ran. Tiers were assigned **mechanically** by STRING distance rather than curated,
precisely because curation was the obvious attack on the original result.

All percentages below use the **same counting unit as §2.3** — unique
`(gene, drug, action_type)` triples, strict `INHIBITOR`. `scale_measure.py --selfcheck`
re-derives §2.3's own 129/142 before emitting any of these, so the two sections compare
like with like.

| Gene | Disease | drugs at the defect | Open Targets inhibitory | DGIdb inhibitory |
|---|---|---|---|---|
| **BUB1B** | MVA (this case) | **0**, both databases | **95.8%** (69/72) | 99.4% (180/181) |
| **ATM** | Ataxia-telangiectasia | 84 | **93.4%** (71/76) | 93.4% (170/182) |
| **NPC1** | Niemann-Pick C | 137 † | **54.5%** (66/121) | 60.7% (187/308) |
| **CFTR** | Cystic fibrosis | 46 | **37.5%** (60/160) | 49.6% (133/268) |

† NPC1's 137 are **DGIdb-only and none is action-typed**; many are raw ChEMBL binding-assay
entries rather than drugs. P1 fails there on record count — the metric it was written
against — but the *direction* at NPC1's own defect is genuinely unknown, not favourable, and
nothing below rests on it.

**Two of our three predictions failed, and one of them was the important one.**

- **The claim that the inhibitor skew is "a fact about every loss-of-function rare disease"
  is withdrawn.** We predicted ≥80% inhibitory at NPC1 and measured **54.5%**. The
  pre-registration committed us, in writing and in advance, to withdrawing rather than
  softening the claim if exactly this happened. It happened.
- **The monotonic rise of drug availability with distance does not survive a mechanical tier
  rule** — it fails for BUB1B itself (0 → 375 → 198), for ATM and for NPC1. That pattern was
  an artefact of how the original 24-gene pathway set was curated, and we report it as one.
- **The CFTR falsification test worked as designed.** At the causal gene only **18.4%** of
  typed triples are strictly inhibitory (20.4% broad), against **26 `ACTIVATING`** and
  **8 `POSITIVE MODULATOR`** — the correctors and potentiators. Across the whole CFTR
  neighbourhood strict inhibitory is **37.5%**, the lowest of the four. The prediction broke
  where we said it should break.

### 3. What survives is narrower, and more useful

Two findings came through the replication intact. **BUB1B's zero at the defect is real and
not a curation artefact** — it survives a tier rule with no human choice in it, in both
databases. And **the inhibitor skew is real where it applies, and extreme**: 93–99% across
two independent databases for BUB1B and ATM.

What changes is the scope. The skew does not track loss-of-function. It tracks **whether
the causal gene sits in a pathway oncology has invested in inhibiting**:

| Neighbourhood | Genes | Inhibitory |
|---|---|---|
| Mitotic checkpoint / DNA-damage response — heavy oncology inhibitor investment | BUB1B, ATM | **93–96%** |
| Lysosomal transport, ion channel — metabolic biology, where agonists are ordinary | NPC1, CFTR | **38–55%** |

**The corrected rule is diagnostic rather than rhetorical: it tells you in advance which
rare diseases have this problem.** A deficiency patient faces a pharmacopeia pointing the
wrong way when the causal gene's pathway is an oncology target — because those programmes
exist to kill dividing cells, and every tool they produce lowers activity. MVA and
ataxia-telangiectasia are in that category. Niemann-Pick C and cystic fibrosis are not.

**This sharpens the finding for this child rather than weakening it.** BUB1B sits in the
worst category available: zero drugs at the defect, and 95.8% of everything nearby pointing
in the direction that makes the disease worse.

**The ATM result stands on its own.** All ten action-typed compounds at the causal gene are
inhibitors — AZD0156, AZD1390, AZD7648, M3541, BAY-8400 — in a disease defined by ATM
*deficiency*. That entire pharmacopeia exists to make cells ATM-deficient, which is what an
oncologist wants and the precise opposite of what an ataxia-telangiectasia patient needs.
The same trap this report identified for MVA is sitting, unremarked, in another rare disease.

### 4. The transferable practice

- Query the causal gene first and **expect zero** — treat it as information, not failure.
- Ask "what raises this protein?" rather than "what binds it?"
- **Write the exclusion gates before the search**, because the highest-ranked pathway hit
  can be the most harmful agent available (here, HSP90 inhibitors).
- **Check which neighbourhood you are in before assuming the pharmacopeia is against you** —
  that is the correction this replication forced, and it is the difference between a slogan
  and a usable rule.
- **Pre-register, then publish the failures.** Two of three predictions here failed, and the
  resulting claim is narrower, testable, and true.

**5. The patient-specific safety layer generalises to any sequenced patient.** Any child
with a rare disease who has had WGS already has the data for a CPIC-guided PGx analysis.
The transferable lesson is the negative one: on a variants-only VCF, **absence is not
reference**, and a pipeline that assumes otherwise produces a confident, clean, wrong
table. We measured that: 16 of 23 genes flip.

**Limits.** Four genes, chosen by argument rather than sampled — a structured probe with one
adversarial case, not a population estimate, and no p-value is computed. The two-category
split is the hypothesis this replication generates, not a result it establishes. Action-typed
entries are a minority of retrieved rows; NPC1's 137 drug rows at the defect carry no action
type at all, so its direction there is genuinely unknown rather than balanced. Full numbers,
verdicts and limits in `data-notes/scale/RESULTS.md`.

## Part 9 — Data handling, ethics, and scope

- **No demographic inference is published.** Fewer than 50 people worldwide are known to
  have MVA. Sex and age were deliberately **not** inferred from the VCF and are not
  reported, because demographic detail plus tumour type is re-identifying in a cohort that
  small, and the phenotype document restricts publication to what the family has already
  made public.
- **Pharmacogenomic disclosure is limited to actionable phenotype for gene-drug pairs
  bearing on a stated recommendation.** No full star-allele profile is published. The
  method and code are published in full so the analysis is reproducible by anyone with
  their own authorised data access.
- **No patient data is in this repository.** Raw, derived and PGx working files are
  gitignored per the Data Transfer Agreement; `data-notes/pgx/` was added to `.gitignore`
  before the analysis was run.
- **No recontact.** No contact has been made or attempted with the family, their
  clinicians, or the MVA Society, per the Official Rules.
- **This is not medical advice.** It is a research hypothesis submitted to a hackathon.
  Every candidate here would require functional validation (§5), then formal safety and
  regulatory review, before anyone could responsibly give any of it to a child.
- **Data deletion.** All dataset copies will be deleted within 30 days of hackathon close,
  with confirmation emailed to both addresses that appear in the source material
  (`RarediseaserealkidMVAhackathon2026@synapse.org` in the Official Rules, and
  `MVAHackathon2026@synapse.org` in the dataset card's own gated-access agreement).

---

## Part 10 — AI-assistant usage disclosure

This analysis was performed with Claude (Anthropic) as an interactive assistant, per the
hackathon's 28 Aug 2026 disclosure requirement. The model was used to: fetch and summarise
primary literature; write the pipeline scripts; execute API queries against Open Targets,
DGIdb, ClinicalTrials.gov, openFDA, Ensembl, PubMed/PMC, ClinVar and gnomAD; run PharmCAT;
and draft this report.

Every factual claim was verified against a primary source rather than taken from the
model's recall, and that process caught real errors — including three citation
misattributions, a withdrawn set of claims in a widely-cited trial, and a false-positive
malignant-hyperthermia signal (§11). No patient data was transmitted to any third-party
service: all API queries concerned public gene, drug, trial and variant identifiers, and
PharmCAT was run locally.

---

## Part 11 — Verification

Every external claim was re-queried against its primary source. This pass found and
corrected the following, each of which would have been an error in the submission.

**Rows 36–41 are the 2026-09-04 numeric audit of Track 2**, run as the counterpart to the
Track 1 audit at commit `ea393d5`. Its result is worth stating up front because it is the
useful part: **every number in this report reproduces from the committed artefacts, and
every defect it found was a sentence or a downstream file that had drifted away from a
number.** Three of the six are the same failure — a correction this report made to itself
never reached the files that quote it.

| # | Finding | Resolution |
|---|---|---|
| 1 | **North/Sinclair 2014 does not show what it is usually cited for.** NMN was given to *wild-type* mice; the `BubR1^H/H` rescue used SIRT2 transgenic overexpression | Report states the inference as an inference throughout (§1.4, §3.2, Limitation 2) |
| 2 | **Hickson 2019's corrigendum withdrew conclusions.** Re-analysis with pre-planned paired tests on untransformed data removed the skin-senescence result and the individual IL-1α/IL-6/MMP-9 claims. The substance is in a supplementary appendix invisible to PubMed and the PMC record | Retrieved from the Europe PMC supplementary bundle; report cites only corrected figures (§3.3) |
| 3 | **PharmCAT reports "Uncertain Susceptibility" to malignant hyperthermia for RYR1 rs35364374; ClinGen's expert panel classifies that variant Benign** (VCV000093279, 3-star) | Reported as a false alarm, with the general lesson that a PGx phenotype label is not a variant classification (§4.3) |
| 4 | **16 of 23 PGx genes change call under `--missing-to-ref`** | Both runs reported; no "Normal Metabolizer" call is presented as established (§4.2) |
| 5 | **Open Targets renamed `knownDrugs` → `drugAndClinicalCandidates`**; the old field now returns a hard error | Schema verified live; script raises rather than silently reporting zero drugs |
| 6 | **Three MVA Society bibliography citations credited the senior author.** Wijshake T (not van Deursen JM); Nakano Y (not Walsh MF); North BJ (not Sinclair DA) | All corrected; the bibliography is now flagged as systematically senior-author-attributed (`literature/04_...`) |
| 7 | **openFDA returns misleading labels on generic-name search** — a topical ruxolitinib cream, a metformin *combination* product, and a homeopathic quercetin preparation | Re-queried by brand (JAKAFI, Olumiant, metformin single-agent); paediatric claims corrected. Baricitinib's US label states paediatric use **not** established, contrary to our initial assumption |
| 8 | **`csv.DictWriter` defaults to CRLF**, appending `\r` to the final column and silently breaking field comparisons in the output TSV | Fixed with explicit `lineterminator="\n"`; search re-run |
| 9 | All 24 Ensembl gene IDs verified live against Ensembl REST | 24/24 correct |
| 10 | All three observed PGx variants verified against ClinVar with SPDI coordinates matched to the VCF calls | 3/3 match to the digit |
| 11 | **This row raised a misattribution against Track 1 that does not hold, and the correction runs against this table rather than for it.** It read: Suijkerbuijk 2010 is cited in the Track 1 report for the claim that the kinase domain is "dispensable", whereas the paper shows kinase-domain *missense mutants* fail because they are **unstable** and argues the domain is structurally *important*. Re-checked against the full text captured in this repository, the paper states the cited claim verbatim: *"neither the kinase activity nor the 265 amino-acid kinase domain are required for establishing mitotic checkpoint activity or stable microtubule attachments"* (`literature/15_...`, the LAP-731X truncation experiment, Fig. 5) | **The accusation is withdrawn; Track 1's citation is correct.** The paper makes both claims and they are compatible: the domain is dispensable for *checkpoint function* when the protein that lacks it is stable (731X), and required for the *stability* of the full-length protein. Track 1 cites the first, for PM1's "active site of an enzyme" archetype; Track 2 §1.2–1.3 relies on the second. Both stand. Two things did need fixing and are fixed: the "Precision note" in `literature/15_...` mischaracterised its own captured text, and Track 1 quoted the paper's **265**-aa domain beside UniProt's **285**-aa (766–1050) boundary without saying they are different definitions. Catalytic dispensability is separately attributable to Kops et al. 2012. No Track 1 evidence code moves — the PM1 rejection rests on gnomAD missense density, not on this sentence |
| 12 | **Audit pass, 2026-09-02: the trial table conflated total trials with the API's 100-record retrieval cap.** Paediatric counts for ruxolitinib, baricitinib, sirolimus, metformin and NR were floors over the retrieved 100, presented as totals | Table now separates total / retrieved / paediatric and marks complete retrievals. The load-bearing row (D+Q, 22 of 22) was already exhaustive, so the zero-paediatric claim is unaffected |
| 13 | **Audit pass: "returns zero in both databases" over-reached.** Only BUB1B, BUB3, CDC20, MAD2L1 and NMNAT1 are zero in both. CDKN1A and CDKN2A have 30 and 29 DGIdb interaction records; SIRT2 has 12 | Corrected, with the DGIdb confidence caveat stated and the SIRT2 point sharpened — every SIRT2 compound found is an inhibitor or unranked claim, and no activator exists in the searched space |
| 14 | All other report figures re-derived from the artefacts: OT action-type tally (129/142), all six tier counts (0/2/1/16/30/71), DGIdb approved directionality (62 inhibitory / 1 activating), the ranking totals and every axis score | Reproduce exactly |
| 15 | **Adversarial review pass, 2026-09-02: HSP90 inhibitors are a recognised senolytic class** (Fuhrmann-Stroissnigg et al. 2017), from the same investigator group as the D+Q programme — so the report's top approved-medication *tier* contains its own hard contraindication, reachable without ever mentioning aneuploidy | Gate G1 restated as a **within-class** gate; §3.3 and §3.4 now exclude HSP90-directed senolytics explicitly and state that "senolytic" is not a safe class label here |
| 16 | **Gate G1 was applied inconsistently.** As pre-registered it excludes on mechanism alone, which would also flag quercetin (Aalinkeel 2008: HSP90 is the most down-regulated protein in the proteome at 50 µM) | G1 amended **in the report, not in the committed rubric**, to "…at concentrations achievable in vivo," with the potency reasoning shown. D+Q is **not** rejected; the residual question becomes an assay arm in §5.2 |
| 17 | **NCBI `elink` mis-maps PMID 37866738 to a PMC record containing a different paper** by overlapping authors; `literature/18_` had captured the wrong full text. A second, independent instance of the same defect was found by the check written in response to the first | Both quotations re-verified verbatim against the primary PubMed record — **no claim affected**. Source downgraded to abstract-only, misfetched text removed, and a title-vs-identifier check now runs corpus-wide (Limitation 11) |
| 18 | **Rows 26 and 27 of the fetch log were wrongly closed as "abstract only."** Both were recoverable via the PMC HTML render route | Tang 2011 and Xu 2015 upgraded to full text. Both changed the report: Tang supplied the chaperone-dependency rationale now in §3.4, and Xu showed SASP suppression is ≤60% and **segmental** (IL-1α/IL-1β/IL-8 unchanged), so no senomorphic claim of "SASP suppression" is made |
| 19 | **Corrigendum/retraction sweep across all 18 PMC-deposited sources** via PubMed `CommentsCorrections` | Exactly one hit — the Hickson 2019 erratum already handled. No retractions, no expressions of concern. Reported as an honest negative, with the caveat that the sweep detects only PubMed-indexed corrections and Hickson is itself proof that withdrawals can hide in supplements |
| 20 | **AlphaFold-based structural characterisation** of N1002 and of the Suijkerbuijk comparator alleles, on `AF-O60566-F1` | Reported in full (`data-notes/structural_analysis_n1002k.md`). The result runs **against** the report's central claim and is stated that way: Q921 — the tolerated counterexample — is more buried and also H-bonded (§1.3, Limitation 1) |
| 21 | **No experimental structure covers residue 1002.** UniProt's PDB cross-reference declaring "1-1050" for 5KHU/6TLJ is **entity length, not modelled range** | Structural work is reported as AlphaFold modelling only, with the pLDDT limit stated; no claim rests on an experimental structure at this residue (matrix C12) |
| 22 | **ΔΔG attempted and not obtained** — the DDMut retrieval endpoint failed across three API shapes | Reported as structural *inspection*, never as a ΔΔG. A prediction not run is not a prediction held |
| 23 | **Hol et al. 2021 primary obtained and read** as the version of record, via OpenAlex → Cambridge/Utrecht repository deposits | An earlier pass recorded this source as closed access. That was wrong: Europe PMC's `isOpenAccess: N` means "not open access *in Europe PMC*" — deposit location, not licence. The paper is CC-BY. Matrix **C15** |
| 24 | MVA sections of Hol 2021 and Nakano 2024 read end to end for **post-first-tumour surveillance** | **Silent in both**, and the non-renal exclusion is explicit in the primary. Reported as a guideline gap, not filled by inference (§6, Q9) |
| 25 | **MVA-specific radiosensitivity search** | Five records returned, **all wrong-product**. No study of radiosensitivity in MVA, *BUB1B*-deficient or PCS patients exists. The claim is re-tiered as a class generalisation (§6, matrix C16) |
| 26 | **NCBI `elink` returns a false PMCID for Hol 2021** | Fourth identifier trap caught in this repository. Verified by title before any quotation, per the standing check (Limitation 11) |

| 27 | **Scalability replication, 2026-09-04: two of three pre-registered predictions FAILED.** The published claim that the inhibitor skew "is a fact about every loss-of-function rare disease" measured **54.5%** at NPC1 against a predicted ≥80%; the monotonic rise with distance did not survive a mechanical STRING tier rule, failing even for BUB1B itself (0 → 375 → 198) | Generalisation **withdrawn**, per the pre-registration's own instruction to withdraw rather than soften. Part 8 rewritten around the corrected, narrower rule; §2.2 and §2.3 carry supersession notes (`data-notes/scale/RESULTS.md`) |
| 28 | **STRING's `interaction_partners` endpoint silently defaults to 10 partners per protein**, which would have capped tier 1 at 10 and broken the pre-registered 25-per-tier rule | Caught by noticing every tier 1 returned exactly 10. `limit` now set explicitly and all four node sets rebuilt |
| 29 | **STRING preferred names lag HGNC** — `GBA`, `SLC9A3R1` and `SLC9A3R2` failed Ensembl symbol lookup, and the search correctly *raised* rather than reporting them as zero-drug targets | Synonym fallback via the Ensembl `xrefs` endpoint; node sets rebuilt with zero unresolved IDs |
| 30 | **Fifth identifier trap: PMIDs 19373780 and 19856400 are one patient plus a comment on it**, not two patients, and carry near-identical titles | Caught by the standing title-verification check before either entered the cohort table. Counting both would have inflated the cohort and triple-counted three tumours |
| 31 | **Task 5: a standing overclaim of this repository's own.** "The callability limitation cannot be closed by acquiring data" rested on whole-genome-index RAM against a route nobody would take | Withdrawn in four files. The binding objection is scientific — decoy-free realignment inflates MAPQ — and splits by locus: BUB1B has **zero** segdups in its padded region, CYP2D6 has **six** (`pipeline/realignment_feasibility.md`) |
| 32 | **The pitch script had fallen out of sync with the report three times** — the withdrawn positional analogy, the NAD⁺ mechanism stated as fact, and the withdrawn generalisation | All three corrected; script re-verified at 433 spoken words against its 435 budget. The required organiser acknowledgement is now matched verbatim against the site capture by a check that fails loudly |

| 33 | **Self-audit of the 2026-09-04 pass found a methodology mismatch in our own replication.** `scale_measure.py` counted raw rows while §2.3's `129/142` counts unique `(gene, drug, action_type)` triples — and the two were printed side by side as if comparable, inflating every replication percentage by 1–15 points | Counting unit unified on the report's. `--selfcheck` now re-derives §2.3's own 129/142 and **fails loudly** before any other figure is emitted. All figures restated; **no verdict changed** — the corrected numbers *widen* the BUB1B/ATM vs NPC1/CFTR split (93–96% vs 38–55%) rather than narrowing it, and CFTR's falsification is sharper at 37.5% than the 52.9% first reported |
| 34 | **§2.3 never defined what an "entry" was**, making its headline figure irreproducible without guessing the dedup rule — three attempts were needed to recover it, and it was briefly suspected of being wrong when it was correct all along | Denominator now defined in §2.3 with a one-line reproducer. The figure itself was **right**: 142 triples, 129 `INHIBITOR`, exactly one `ACTIVATOR` and one `STABILISER`, matching the prose at every dedup level |
| 35 | **The self-audit also found an overclaim in the methods description** ("thirty-four sources captured in full text… each with an explicit LIMITS section and an evidence tier") and a transposed tier chart in the pitch deck (`abundance`/`senescence` swapped against §2.2) | Both corrected. Source counts restated against `ls literature/[0-9]*.md`; deck re-verified in-browser rather than by inspection |

| 36 | **Track 2 numeric audit, 2026-09-04: every figure in this report re-derived from the committed artefacts.** OT action-type tally (142 triples / 129 `INHIBITOR` / 135 broad / one `ACTIVATOR` / one `STABILISER`), all six tier counts (0/2/1/16/30/71), the abundance-tier unpacking (HSP90AA1 10 + PARP1 13 = 23; remainder 4 anti-CD38 + 3 NAMPT), the five genes zero in both databases, the six zero-in-OT-only counts (BUB1B 6 / MAD1L1 2 / CGAS 3 / SIRT2 12 / CDKN2A 29 / CDKN1A 30), DGIdb approved directionality (62/1, granisetron–TP53), every trial row, all ten ranking totals and all fifty axis scores, the PGx 1,204 absent and 16-of-23 flip, and all sixteen Part 8 figures | **All reproduce exactly.** No figure changed. The defects this pass found are prose claims that outran the artefacts, and downstream files that never took a correction the report had already made — rows 37–40 |
| 37 | **A claim in §2.4 was refuted by the table printed directly above it.** "The lowest minimum age across the entire senolytic trial landscape is 18" — while our own trial file records **six paediatric-eligible navitoclax trials with minimum ages down to 1 year** and two for fisetin | Withdrawn and replaced with the narrower claim the argument actually needed (no *senolytic-indication* trial of these agents has enrolled a child), with the twelve trials inspected individually and the basis of the narrower claim — trial titles, not a structured field — labelled. Same failure mode as row 12 |
| 38 | **A withdrawn Track 1 inference survived in Track 2 §1.7 and in `data-notes/track2_mechanism.md`.** Both still read "congenital onset raises the prior for a second monogenic cause" — the exact clause Track 1 withdrew when the gestational-age-stratified evidence was read (matrix C13) | Both corrected to Track 1's current position: onset undated, monogenic yield ~10× higher in full-term children *without* risk factors, both readings live and neither concluding. The `_pending_edits` note "Task 4 touches Track 1 only" was wrong — Task 4 touched Track 2 as well, and nothing checked |
| 39 | **The two withdrawn Part 8 claims were still live in three downstream artefacts** — `submissions/methods_description.md` (the *submitted* form) asserted monotonicity and presented the loss-of-function generalisation as the finding, describing the falsification test without reporting that it failed; `README.md` led with monotonicity; `viz/track2_explainer.html` carried both, in a section heading and in a callout, with no scalability section at all | All three corrected to the post-replication position. The report, deck, pitch script and judges' note were already right, which is why this went unnoticed: **the correction propagated to everything a reader sees first and stalled in the files a judge opens next** |
| 40 | **Four stale counts, each in a file that quotes a number from another file.** Verification findings "32" and "twenty-six" against an actual 35; pitch script "394 spoken words" in the README against an actual 433; "32 commits" against 39 | All four corrected against their sources. The underlying fault is that these are hand-copied cross-file figures with no check; the ones that *are* checked by a script (129/142, the word counter in `pitch_script.md`) were all correct |
| 41 | **`§4.2`'s "22 of 1,226" was right but unreconcilable from the artefacts.** Twenty-three PharmCAT positions carry a call; 22 are interpretable, and 22 + 1,204 absent = 1,226 only because the undocumented RYR1 record at `chr19:38499696` is excluded — which §4.3 describes but §4.2 did not credit | Wording changed to "interpretable variant call" with the reconciliation stated. Same class as row 34: a correct figure that could not be reproduced without guessing the rule |

| 42 | **The root cause of rows 37–40 was that nothing checked prose.** Every figure under a script (`scale_measure.py --selfcheck`, the pitch script's own word counter) was correct; every figure copied by hand between files had gone stale, and every withdrawn claim that survived did so in a file no script read | `pipeline/check_consistency.py` now enforces both classes and **fails loudly**: no withdrawn claim may be *asserted* in any of ten reader-facing files (it may appear only inside the paragraph retracting it, and the verification table and `_pending_edits.md` are exempt by design), and each cross-file figure — verification-row count, pitch word count, commit count, the 500-word form limit, the 129/142 selfcheck — must equal the source it names |

**Reproducibility.** All scripts are in `pipeline/`, CLI-parameterised, standard library
only, with the exact command sequence in `pipeline/README.md`. The pre-registration is
verifiable from commit order. No patient data is committed; reproducing the
pharmacogenomic section requires independently authorised access to the hackathon dataset.

---

## Sources

Primary literature captured in full in `literature/` (see `_fetch_log.md` for provenance
and for every source that remains abstract-only — the count changed in the 2026-09-02 pass,
which recovered two full texts and downgraded one):

Suijkerbuijk et al. 2010, *Cancer Res* 70:4891 (PMID 20516114) · North/Sinclair et al.
2014, *EMBO J* 33:1438 (PMID 24825348) · Wijshake et al. 2012, *PLoS Genet* 8:e1003138
(PMID 23300461) · Baker et al. 2011, *Nature* 479:232 · Hol JA, Jewell R, Chowdhury T,
Duncan C, Nakata K, Oue T, et al. 2021, *Eur J Cancer* 153:51–63 (PMID 34134020, CC-BY) —
the SIOP-Europe surveillance recommendation, read as the primary; Nakano 2024 remains
cited as the AACR endorsement · Sieben et al. 2020, *J Clin Invest* — the
`BubR1^X753/L1002P` mouse · Kirsch-Volders & Fenech 2023,
*Mutat Res Rev* 792:108474 (PMID 37866738) · Justice et al. 2019, *EBioMedicine* 40:554
(PMID 30616998) · Hickson et al. 2019, *EBioMedicine* 47:446 **and its 2020 corrigendum**,
*EBioMedicine* 52:102595 (PMIDs 31542391, 31982828) · Shoji et al. 2025, *Aging Cell*
(PMID 40459998) · Veenhuis et al. 2021, *Mov Disord* (PMID 34515380) · Nakano et al. 2024,
*Clin Cancer Res* 30:5009 (PMID 39264246) · Mackenzie et al. 2017, *Nature* 548:461
(PMID 28738408) · Bakhoum et al. 2018, *Nature* 553:467 (PMID 29342134) · Tang et al.
2011, *Cell* 144:499 (PMID 21315436) · Xu et al. 2015, *PNAS* 112:E6301 (PMID 26578790) ·
Bohr 2025, *Aging Cell* 25:e70319 (PMID 41436848) · Kops et al. 2012, *Dev Cell*
(PMID 22698286) · Hanks et al. 2004, *Nat Genet* 36:1159 (PMID 15475955).

Added by the adversarial review pass, 2026-09-02 — Fuhrmann-Stroissnigg et al. 2017,
*Nat Commun* 8:422 (PMID 28871086) · Aalinkeel et al. 2008, *Prostate* 68:1773
(PMID 18726985) · Stocks et al. 2022, *JCI Insight* 7:e156925 (PMID 35998039) ·
Elhassan et al. 2019, *Cell Rep* 28:1717 (PMID 31412242) · Dollerup et al. 2018,
*Am J Clin Nutr* 108:343 (PMID 29992272) · Remie et al. 2020, *Am J Clin Nutr* 112:413
(PMID 32320006) · McDermott et al. 2024, *Nat Commun* 15:5046 (PMID 38871717).

The adjudication of every conflict between these sources is recorded in
`literature/_contradiction_matrix.md`; each assertion in this report is graded
Established / Predicted / Untested inference in `literature/_claims_register.md`; and what
the literature **cannot** answer, with the cheapest experiment for each, is in
`literature/_open_questions.md`.

Databases queried live: Open Targets Platform (GraphQL v4), DGIdb v5, ClinicalTrials.gov
API v2, openFDA drug labels, Ensembl REST, NCBI eutils/PMC, ClinVar, gnomAD v4, UniProt,
CPIC via PharmCAT v3.4.0.
