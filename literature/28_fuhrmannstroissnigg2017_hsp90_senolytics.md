# Identification of HSP90 inhibitors as a novel class of senolytics

Authors: Fuhrmann-Stroissnigg H, Ling YY, Zhao J, McGowan SJ, Zhu Y, Brooks RW, Grassi D,
Gregg SQ, Stripay JL, Dorronsoro A, Corbo L, Tang P, Bukata C, Ring N, Giacca M, Li X,
**Tchkonia T, Kirkland JL, Niedernhofer LJ, Robbins PD**
Journal: *Nature Communications*, 2017 Sep 4;8(1):422. doi: 10.1038/s41467-017-00314-z
Source: PMC5583353 (open access) — https://pmc.ncbi.nlm.nih.gov/articles/PMC5583353/
PMID: 28871086
Captured: 2026-09-02 (full text via PMC HTML render)

Relevance: **this paper creates the sharpest contradiction in the Track 2 evidence base,
and it changes a recommendation.** It establishes HSP90 inhibitors as a *member class of
the senolytics* — the drug family the report ranks highest among approved medications —
while this repository's own mechanism paper (Suijkerbuijk 2010) and its rejected-tier
paper (Tang 2011) both make HSP90 inhibition a hard contraindication in this child.
See `literature/_contradiction_matrix.md`, conflict **C1**.

---

## What it establishes

**HSP90 inhibitors are senolytics.** From the abstract: a senescence-associated
β-galactosidase screening platform run on primary `Ercc1−/−` MEFs was used to screen a
compound library, "identifying two inhibitors of the HSP90 chaperone family as having
significant senolytic activity in mouse and human cells."

**The effect reproduces in vivo in a progeroid mouse.** "Treatment of `Ercc1−/∆` mice, a
mouse model of a human progeroid syndrome, with the HSP90 inhibitor **17-DMAG** extended
healthspan, delayed the onset of several age-related symptoms and reduced p16INK4a
expression." Acute treatment gave "more than 50% reduction in expression of p16INK4a in
the kidney, suggesting that 17-DMAG had senolytic activity in vivo."

**It was benchmarked head-to-head against dasatinib + quercetin in the same assay.**
"two established senolytics, a combination of dasatinib plus quercetin (D/Q) and
navitoclax, significantly reduced senescent and total cell counts relative to untreated
cultures." The authors explicitly place their result alongside D+Q: the 17-DMAG in vivo
findings "are consistent with previous results using the combination of dasatinib and
quercetin, which also improved healthspan in `Ercc1−/∆` mice."

**A proposed mechanism that overlaps the D+Q mechanism.** "Treating senescent MEFs with
HSP90 inhibitors results in an almost complete abrogation of the active, phosphorylated
AKT form after only 6 h of treatment… Downregulation of this survival pathway may
contribute to the senolytic activity of HSP90 inhibitors." The paper notes in the same
passage that "quercetin has been reported to affect levels of certain Bcl-2 family
members and to **inhibit AKT activity**" — i.e. the two agents are described as
converging on the same pro-survival node.

**Multiple chemotypes, not one compound.** The HSP90 inhibitors handled include 17-DMAG,
ganetespib, NVP-AUY922, BIIB021, PU-H71, NVP-BEB800 and AT13387 — so the finding is a
class property, not an idiosyncrasy of the geldanamycin scaffold.

## Why this is decisive for this case, and not dismissible

The authorship matters. Tchkonia, Kirkland, Niedernhofer and Robbins are senior authors
here **and** are the same group behind the dasatinib + quercetin senolytic programme,
Xu et al. 2015 (`literature/27_...`), Justice et al. 2019 (`literature/19_...`) and
Hickson et al. 2019 (`literature/20_...`). The HSP90-senolytic result therefore cannot be
set aside as a rival lab's unreplicated outlier: it comes from inside the same body of
work that supplies the report's senolytic evidence, and it is presented there as a
natural extension of it.

The consequence for this proband is a **class-membership problem**, not a data dispute:

- Suijkerbuijk et al. 2010 (`literature/15_...`) show MVA missense BubR1 is a
  misfolding-prone **HSP90 client** that geldanamycin depletes.
- Tang et al. 2011 (`literature/26_...`) show aneuploid cells are *selectively*
  antiproliferated by 17-AAG at 100 nM because they depend on protein quality control.
- This paper shows HSP90 inhibition is a senolytic mechanism with the **strongest
  progeroid-mouse in vivo healthspan data among the compounds it screened.**

So a search framed as "pick the best-evidenced senolytic for a progeroid-like child"
lands directly on the one mechanism that is predicted to destroy the residual BubR1 this
child depends on — arriving at the contraindicated agent through the *senolytic* door
rather than the *aneuploidy* door. The Track 2 report closes only the second door.

**What must change:** gate G1 has to be applied *within* the senolytic class, agent by
agent on the molecular target, rather than at the tier level. "Senolytic" is not a safe
class label in BUB1B deficiency.

## LIMITS — what this paper does NOT show

- **No BubR1 or MVA background anywhere.** The models are `Ercc1−/−` MEFs and `Ercc1−/∆`
  mice — a nucleotide-excision-repair defect, not a spindle-assembly-checkpoint defect.
  Nothing here speaks to BubR1 abundance, and the paper does not measure it.
- **No human data of any kind.** No trial, no human dosing, no paediatric exposure.
  17-DMAG and the other HSP90 inhibitors named are **investigational** agents; none is an
  approved medication, and none may be described as one.
- **Healthspan, not lifespan.** The claim is delayed onset of age-related symptoms and
  reduced p16INK4a, not extended survival.
- **p16INK4a reduction is an inference of senolysis, not a direct measurement of
  senescent-cell killing in vivo** — the paper says "suggesting that 17-DMAG had senolytic
  activity in vivo."
- **It does not test HSP90 inhibitors against aneuploid cells**, so the convergence with
  Tang 2011 is a cross-paper inference drawn here, not a result in either paper.
- The authors themselves expect combination use: "it is likely that HSP90 inhibitors will
  be more effective in combination with other FDA-approved drugs that target other
  anti-apoptotic pathways" — i.e. monotherapy efficacy is not claimed.

## Evidence tier

**Mouse, non-BubR1 background** (Ercc1 progeroid) + **cell line**. No human evidence. No
paediatric data. Under the Track 2 grading scheme this sits below every human tier and
must never be described in language implying human benefit.
