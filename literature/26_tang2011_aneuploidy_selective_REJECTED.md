# Identification of aneuploidy-selective antiproliferation compounds

Authors: Tang YC, Williams BR, Siegel JJ, Amon A
Journal: Cell, 2011 Feb 18;144(4):499-512. doi: 10.1016/j.cell.2011.01.017
Source: PMC3532042 (open access) — PMID 21315436
Captured: 2026-09-02; **upgraded to full text 2026-09-02** via the PMC HTML render route
after the BioC and efetch routes returned abstract-only. This closes fetch-log gap #6.

Relevance: **this paper is in the Track 2 report's rejected tier, and it is there for two
independent reasons.** It is the first thing a naive "drugs for aneuploidy" search
surfaces, which is exactly why the report must address it rather than ignore it.

---

## What it reports

"Compounds that cause lethality in aneuploid but not euploid cells could therefore
provide new cancer therapies. We have identified the energy stress-inducing agent
**AICAR**, the protein folding inhibitor **17-AAG** and the autophagy inhibitor
**chloroquine** as exhibiting this property. AICAR induces p53-mediated apoptosis in
primary mouse embryonic fibroblasts (MEFs) trisomic for either Chromosome 1, 13, 16 or
19."

## Why both hard gates in the pre-registered rubric fire on it

**Gate G2 — mechanism is selective killing of aneuploid cells.** The entire therapeutic
concept is cytotoxicity toward aneuploid cells. That concept was developed for *tumours*,
where aneuploid cells are the disease and euploid cells are the patient. In mosaic
variegated aneuploidy the aneuploid cells **are** the patient — distributed across
tissues throughout the body, by definition of the syndrome. An aneuploidy-selective
cytotoxic is not a therapy in this child; it is a whole-body toxicity with a mechanism.

**Gate G1 — 17-AAG is an HSP90 inhibitor.** This is the sharper and less obvious problem.
Suijkerbuijk et al. 2010 (`literature/15_...`) showed that MVA kinase-domain missense
BubR1 is a misfolding-prone **HSP90 client**: geldanamycin severely decreased mutant but
not wild-type BubR1, and CHX + GA together "removed virtually all mutant BUBR1 protein."
Inhibiting HSP90 in this proband is therefore predicted to **destroy the residual BubR1
the child depends on** — driving the primary defect in the wrong direction.

So the compound that a pathway search would rank highest for "aneuploidy" is, on this
case's own mechanism, among the most clearly contraindicated. That inversion is worth
stating plainly in the report: it is the clearest available demonstration that pathway
proximity is not therapeutic rationale.

## Scope note

Nothing here is a criticism of the paper, which is about cancer therapy and says so. The
error would be transplanting it to a constitutional aneuploidy syndrome — and that error
is available to anyone doing a keyword-driven repurposing search, which is why the
rejection is documented rather than assumed.

---

## What the full text adds beyond the abstract

**The screen's selectivity was mostly negative — an important limit the abstract hides.**
Verbatim: "The majority of compounds **did not exhibit selectivity** towards trisomic MEFs
or did so for only a subset of the trisomies tested (Table S1). However three compounds -
the energy stress inducer AICAR, the Hsp90 inhibitor 17-AAG, and the autophagy inhibitor
chloroquine impaired the accumulation of all four trisomic MEFs to a higher degree than
that of euploid control cells."

**The 17-AAG result, with its concentration and its rationale.** "17-AAG inhibits the
chaperone Hsp90… **17-AAG inhibited proliferation of all aneuploid cells at a
concentration of 100 nM**… cells trisomic for the largest chromosome, Chr1, exhibited
higher sensitivity to the compound than cells harboring an additional copy of the smaller
chromosomes, Chr16 or 19. This finding suggests that **aneuploid cells rely on protein
quality control pathways for their survival**, which is consistent with the finding that
levels of the chaperone Hsp72 are increased in trisomic MEFs."

> This sentence is the mechanistic core of the contraindication, and it is only in the
> full text. The reason 17-AAG works in aneuploid cells is precisely the reason it is
> dangerous here: **chronic aneuploidy creates a chaperone dependency.** In this child the
> aneuploid cells are the patient, and the same chaperone system is separately holding up
> the mutant BubR1 he depends on (Suijkerbuijk 2010). It is a double hit on the same axis.

**An internal inconsistency the paper flags itself.** Metformin, which also activates
AMPK, was much weaker: it "impaired the accumulation of trisomy 13 and 16 cells in
culture, although the effects were not as dramatic," and "**Why AICAR and metformin show
different efficacy in trisomic MEFs, despite both causing AMPK activation, is at present
unclear.**" So the "energy stress via AMPK" mechanism attributed to AICAR is not
established as a class property — metformin is not a back-door substitute for AICAR, and
anyone reasoning "AICAR works, therefore AMPK activation works" is overreading the paper.
(Both are gated out here anyway by G2.)

**AICAR is cytotoxic, not merely cytostatic, in aneuploid cells.** "whereas euploid cells
continued to proliferate in the presence of high concentration of AICAR (0.5 mM), cell
numbers declined in all trisomic cultures, indicating that **AICAR in fact kills trisomic
MEFs**." This sharpens gate G2 rather than softening it.

**Title discrepancy worth recording.** The PMC author-manuscript deposit is titled "The
energy and proteotoxic stress-inducing compounds AICAR and 17-AAG antagonize proliferation
in aneuploid cells"; the final published Cell title is "Identification of aneuploidy-
selective antiproliferation compounds." Same paper, two titles — a citation-matching trap
for anyone searching by title string.

## LIMITS — what this paper does NOT show

- **No BubR1, no MVA, no constitutional aneuploidy.** The models are MEFs trisomic for a
  *single defined* chromosome (1, 13, 16 or 19) and aneuploid human **cancer** cell lines.
  Mosaic variegated aneuploidy — a shifting, mosaic, whole-body mixture of aneuploidies —
  is not modelled anywhere in this paper.
- **No in vivo work.** No animal was treated with any of the three compounds.
- **No human data, no paediatric data, no trial.** AICAR and 17-AAG are **investigational**;
  chloroquine is approved but for other indications and is not proposed here.
- **The therapeutic frame is oncology throughout.** The paper's own conclusion is that
  these compounds "could serve as a new treatment strategy against a broad spectrum of
  human tumors." It makes no claim about constitutional aneuploidy syndromes and should
  not be criticised as if it did.
- **Selectivity is partial and chromosome-dependent** — larger trisomies are more
  sensitive, and most screened compounds showed no selectivity at all.

## Evidence tier

**Cell line only** (primary trisomic MEFs; aneuploid human cancer lines). No in vivo, no
human, no paediatric data. The rejection of this paper's compounds for this child rests on
mechanism, not on a competing clinical result.
