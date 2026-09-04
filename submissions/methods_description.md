# Methods description — MVA Hackathon 2026

Answers to the organisers' `methods_description_form.xlsx`, for **both tracks**. This
Markdown file is the source of truth and is diffable in the public repository;
`submissions/methods_description_gummietech.xlsx` is generated from it and is the file to
upload alongside each report.

The form's own instructions state that submissions without a methods description "may be
judged less favorably on the Scientific Rigor and Innovation criteria" (Track 2) and "on
the Innovation and Scalability criteria" (Track 1).

---

# Track 1 (Variant Prediction)

**Team name:** Gummietech

**Model number:** 1 of 1. One approach was submitted; no variant sweep across
configurations was run.

### Describe your model/approach in detail

A four-stage pipeline over the proband's own VCF, all code in `pipeline/`, all commands in
`pipeline/README.md`.

1. **Region restriction.** Ensembl REST resolves GRCh38 coordinates for a literature-defined
   9-gene MVA panel and an 11-gene phenotype-driven secondary panel; coordinates are padded
   ±2 kb into BED files; `bcftools view -R` restricts the genome-wide VCF to those regions.
2. **Annotation.** `vep_annotate.py` submits PASS variants to the Ensembl VEP REST API,
   with the SpliceAI plugin enabled. Every raw API response is appended to
   `vep_raw_responses.jsonl` so results can be re-derived offline without re-querying.
3. **Filtering.** `filter_candidates.py` applies a rare-and-damaging filter (gnomAD AF
   threshold across both exome and genome frequencies, plus consequence severity).
4. **ACMG/AMP classification**, applied manually per criterion with every input re-verified
   directly against gnomAD, ClinVar, UniProt and dbNSFP rather than taken from VEP's proxy.

The result is a compound-heterozygous candidate in **BUB1B**: `p.Leu737Ter` (ClinVar
Pathogenic/Likely pathogenic, `VCV000533901.9`) with `p.Asn1002Lys` (gnomAD singleton,
VUS), plus one deep-intronic secondary candidate assessed and downgraded.

**One point of scope honesty that belongs here rather than only in the report.** The search
space is a literature-defined MVA gene panel, which presupposes MVA as the working
diagnosis. The *variant call within that space* is the output of executable code against
the proband's own VCF, but the panel choice is not blind, the answer gene is visible on the
public leaderboard, and this submission makes **no claim** to blind discovery.

### (required) Generative AI disclosure

Anthropic API, Claude — Sonnet 5 for the original analysis and Opus 5 for the subsequent
audit and remediation passes — commercial terms, no training on customer content. Used
for: literature synthesis and knowledge-base construction, pipeline script authoring, ACMG
evidence-code application, independent verification of VEP output against primary sources,
and report drafting. **All bioinformatics results — variant calls, annotations,
frequencies — are outputs of standard third-party tools and public databases (bcftools,
Ensembl VEP REST, gnomAD, ClinVar/NCBI eutils, UniProt REST) queried directly, not
generated or estimated by the model.**

### Automated output, or downstream manual review?

**Both, and the boundary is stated rather than blurred.** The *candidate set* is the
automated output of `filter_candidates.py` — re-running it against the annotation output
reproduces the submitted list exactly. The **ranking (EPCR), the ACMG classification, and
the secondary-finding downgrade are manual** and are not reproducible from code alone.

### Describe downstream manual review

Three things were done by hand. **(1) ACMG/AMP evidence assignment**, criterion by
criterion, including two criteria *rejected* after testing (PS4 dropped as improperly
applied; PM1 rejected because the BubR1 pseudokinase domain is not depleted of benign
variation in gnomAD — 320 distinct missense variants across 69.8% of residues). **(2)
EPCR assignment.** **(3) The secondary candidate's downgrade** from EPCR 0.30 to 0.10 after
SpliceAI returned 0.00 on all four delta scores across all 22 BUB1B transcripts.

### Public or proprietary data?

**Publicly available data only**, plus the hackathon's own gated dataset. No proprietary
database, licensed annotation set, or internal cohort was used.

### Describe the public data used

Ensembl REST (coordinates, VEP annotation, SpliceAI plugin); gnomAD v4 GraphQL
(frequencies); ClinVar via NCBI eutils (clinical classification); UniProt REST (`O60566`,
domain boundaries); dbNSFP via VEP (AlphaMissense, REVEL, CADD, SIFT, PolyPhen-2); HPO for
phenotype coding; UCSC `genomicSuperDups` (segmental-duplication exposure); PubMed/Europe
PMC/OpenAlex for literature. All literature used is captured in `literature/` with fetch
provenance in `literature/_fetch_log.md`.

### Describe proprietary data used

None.

### Can the approach output compound-heterozygous pairs?

**Yes.** The submission format is used as designed: one row carries both variants of the
pair in the `chrom_1/pos_1/ref_1/alt_1` and `chrom_2/pos_2/ref_2/alt_2` fields.

**With an explicit limitation.** The pipeline proposes the *pair*; it does not establish
*phase*. The two variants are ~11 kb apart, beyond short-read fragment span, and the
caller emits no `PGT`/`PID` linking them — though it does emit them elsewhere in the same
region, which is how we confirmed the absence is physical rather than a caller artefact.
Compound heterozygosity is therefore **presumed and labelled as presumed**, and the first
recommended confirmatory test is a karyotype (which tests the diagnosis), with parental
Sanger second (which tests the phase).

### How were secondary/incidental findings handled?

One secondary finding is submitted, at EPCR 0.10, with the `notes` column carrying its
full rationale. It is a deep-intronic BUB1B variant (`c.2679-1026A>G`) that sits physically
between the two primary candidates and was raised as a possible alternative second allele
on rarity, gene and position — then **tested and downgraded** rather than left as a
suggestive observation. It is reported as a candidate that was assessed and excluded, not
as a competing causal hypothesis.

### Run time and cost

The full pipeline runs in **under 10 minutes end to end** on a 2019-class laptop (8 GB RAM,
8 cores), dominated by Ensembl VEP REST latency, not compute. Standard library Python only,
no cluster, no paid compute. **The analysis time is the cost**: the work spans 2026-08-31
to 2026-09-04 across 41 commits, the large majority of it verification and audit rather
than the initial pipeline, which was the smaller part of the effort.

### Method abstract (≤500 words)

We recover a compound-heterozygous BUB1B candidate — `p.Leu737Ter` (ClinVar
Pathogenic/Likely pathogenic) plus `p.Asn1002Lys` (gnomAD singleton, VUS) — from the
proband's own VCF using a four-stage pipeline: Ensembl-REST coordinate resolution into a
padded BED, `bcftools` region restriction, VEP REST annotation with the SpliceAI plugin,
and a rare/damaging filter. All code is CLI-parameterised and standard-library only.

The submission's distinguishing feature is not the variant call, which the public
leaderboard shows the field has converged on. It is the **verification discipline applied
to it.** Every population-frequency, clinical-classification, domain and predictor claim
was re-derived from its primary source rather than taken from the annotation tool, and
that process repeatedly found real errors — including a rarity filter that silently
excluded gnomAD exome frequencies (proved harmless by replaying the corrected filter
against saved raw responses: identical candidate set), a callability ratio that
contradicted the report's own prose, and a PP4 argument resting on a claim this
repository's own captured literature disproves. Roughly sixty figures were re-derived from
primary artefacts; six were wrong and are corrected in place, with the corrections
recorded rather than quietly absorbed.

**Strengths.** Reproducible from code and documented commands. Evidence codes tested and
*rejected* where unsupported — PM1 is rejected on gnomAD missense density in the very
domain that would otherwise support it, and PS4 was dropped as improperly applied.
Negative results are reported as negatives. The phasing limitation is stated, not
assumed away.

**Limitations, and they are load-bearing.** The search space is a literature-defined MVA
panel, so this cannot distinguish discovery from confirmation, and no such claim is made.
The input is a **sites-only VCF**: absence of a call and absence of coverage are
indistinguishable, and every negative in the report rests on that undifferentiated absence.
A call-density-against-flanking-sequence proxy is offered and explicitly labelled a proxy.
That limitation is *open, not unclosable* — a reduced-reference realignment would close it
at named costs, and BUB1B carries zero segmental duplications, so the route is sound for
this gene specifically. CNVs are not called at all; a multi-exon deletion remains possible
in six named windows, three of them in-frame. Phase is unresolved. `p.Asn1002Lys` remains a VUS and this
submission does not upgrade it.

---

# Track 2 (Drug Repurposing)

**Team name:** Gummietech

### Describe your approach in detail

**The approach begins by rejecting the obvious reading of the genotype**, and that
correction is the submission's central contribution. The intuitive move — the mitotic
checkpoint kinase is broken, therefore target the checkpoint — is not what the literature
supports. Suijkerbuijk et al. 2010 studied MVA patient cells carrying *exactly* this
allelic architecture (truncating allele plus kinase-domain missense allele) and showed the
defect is **insufficient BubR1 protein, not defective enzymology** — and that forcing
abundance back up fully restores checkpoint function, with a threshold between ~6% and
~13% of normal. The therapeutic target is protein **quantity**.

From there: (1) a 24-gene pathway node set built from that mechanism; (2) a scoring rubric
with four hard exclusion gates, **committed to git before any drug query was run** — the
commit order is publicly verifiable; (3) queries against Open Targets and DGIdb
independently; (4) trial evidence from ClinicalTrials.gov, with paediatric eligibility read
from the **structured** `minimumAge`/`stdAges` fields rather than free text; (5) label
verification via openFDA; (6) scoring, and a ranked list with an explicit rejected tier.

### (required) Generative AI disclosure

Anthropic API, Claude — Sonnet 5 for the original analysis and Opus 5 for the audit,
adversarial-review and gap-closure passes — commercial terms, no training on customer
content. Used to fetch and summarise primary literature, write the pipeline scripts,
execute API queries, run PharmCAT, and draft the report. **Every factual claim was verified
against a primary source rather than taken from the model's recall**, and that process
caught real errors, including three citation misattributions, a withdrawn set of
conclusions in a widely-cited trial's corrigendum, and a false-positive malignant-
hyperthermia signal. **No patient data was transmitted to any third-party service:** all
API queries concerned public gene, drug, trial and variant identifiers, and PharmCAT ran
locally.

### Automated or manual candidate identification?

**Automated search, manual mechanism and manual adjudication** — and the interesting
result is that the automated half would have been actively harmful on its own. The drug
retrieval is scripted and reproducible. But the *mechanism reframing* that makes the search
point the right way is manual literature work, and the **exclusion gates are manual and
mechanism-derived**. Without them, the top-ranked hit of a keyword search for "drugs for
aneuploidy" is an HSP90 inhibitor — which is predicted to **destroy the residual BubR1 this
child depends on**, because mutant BubR1 is an HSP90 client.

### Describe manual literature review and expert curation

**31 source files** in `literature/` — 24 of them primary literature, the remainder site
captures, tool documentation, clinical guidelines and a bibliography — each captured with
verbatim quotes and its acquisition provenance logged. Most are full text; those obtainable
only as abstracts are **labelled abstract-only** rather than presented as full text, and the
fetch log records which.

The **LIMITS** convention (an explicit section stating what a paper does *not* show) and the
evidence tier (human RCT / human phase 1–2 / observational human / mouse in the BubR1
background / mouse elsewhere / cell line / in silico) were introduced with the adversarial
review pass and apply to the **10 files added under it**, not retroactively to the earlier
corpus. Stated precisely because an earlier draft of this form claimed all of them carried
it — which is not true, and is checkable in one command. Supporting registers: a **claims register** grading
every assertion, a **contradiction matrix** adjudicating 19 conflicts with grounds, an
**open-questions file** ranking what the literature cannot answer by decision value, and a
**fetch log** recording every acquisition attempt including failures.

An adversarial review pass was run against the submission's own thesis. It found, among
other things, that HSP90 inhibitors are *also* a recognised senolytic class — meaning the
top approved-medication tier contained its own hard contraindication, reachable without
ever mentioning aneuploidy, and that "senolytic" cannot be used as a class-level safety
label in this child.

### Public or proprietary data sources?

**Publicly available sources only.**

### Describe the public data sources used

Open Targets Platform GraphQL (drug/target associations, action types, tractability);
DGIdb GraphQL (independent second database); ClinicalTrials.gov API v2 (trial evidence,
structured paediatric eligibility); openFDA (label verification); Ensembl REST (gene ID
resolution); PubMed / Europe PMC / OpenAlex / Semantic Scholar (literature and open-access
location); ClinVar, gnomAD, UniProt, AlphaFold (`AF-O60566-F1`), RCSB, STRING v12, UCSC.
PharmCAT was run locally against the proband's own VCF under the Data Transfer Agreement.

### Describe proprietary data sources used

None.

### How was the variant's mechanism characterised?

**Loss of function, and specifically loss of protein *abundance* rather than loss of
catalytic activity** — a distinction that governs the entire search, because it sets the
required direction of drug effect.

- **Direction:** `p.Leu737Ter` is NMD-predicted null. `p.Asn1002Lys` sits in the C-terminal
  pseudokinase domain; the published mechanism for this architecture is protein instability.
- **Pathway:** the spindle assembly checkpoint. BubR1 is an MCC component; insufficient
  BubR1 means a weakened checkpoint and chromosome missegregation.
- **Downstream, and this is treated as a fork rather than a chain:** aneuploidy branches
  into {senescence + SASP} and {cancer predisposition} as **siblings**. A senescence-
  targeting drug is therefore *not* expected to reduce this child's tumour risk, and the
  report never claims it is.
- **Robust to unresolved phase:** in *cis* or in *trans*, the shared consequence is low
  BubR1 abundance.
- **Independently supported by allele class:** two published pedigrees reach MVA through a
  **non-coding regulatory** allele, which can only reduce how much protein is made.
- **And tested against itself.** AlphaFold modelling of residue 1002 was run to shore up
  this claim and **weakened it**: `Q921`, a tolerated same-domain counterexample, is *more*
  buried than Asn1002. That is reported as the result it is, and the report's Limitation 1
  is tightened rather than relaxed.

### Time or effort

2026-08-31 to 2026-09-04, 41 commits. The mechanism characterisation and the verification
passes consumed substantially more effort than the drug search itself, which is the correct
ratio for this problem: the search is cheap and the reframing is what makes it point
anywhere useful.

### Method abstract (≤500 words)

BUB1B has **zero** drugs in Open Targets and DGIdb independently, as does every other
spindle-assembly-checkpoint gene. Rather than treat that as failure we treat it as
information, and ask what the surrounding pharmacopeia's shape reveals.

Across 24 pathway genes and two databases, **129 of 142 action-typed Open Targets entries
are strict `INHIBITOR`s** (135, ~95%, counting antagonists/antisense) against a deficiency. We pre-registered a
falsifiable version of that mismatch, with its withdrawal criterion, and tested it on three
further genes including one (CFTR) chosen because it should *fail* there. **Two of three
predictions failed and the generalisation is withdrawn.** The skew does not track
loss-of-function (NPC1 **54.5%**, CFTR **37.5%**) but whether the causal gene sits in a
pathway oncology has invested in inhibiting (BUB1B **95.8%**, ATM **93.4%**) — narrower, and
diagnostic: it says in advance which rare diseases face this problem, and BUB1B is in the
worst category. Our monotonic-rise-with-distance claim likewise failed under a mechanical
STRING tier rule, for BUB1B itself (0 → 375 → 198), and is reported as an artefact of our
own curation. What survives both tests is **the zero at the defect**.

**Ranked answer, with regulatory status never blurred.** Highest overall: nicotinamide
riboside (13/17) — a **dietary supplement, not an approved medicine**. Highest approved
medication: dasatinib + quercetin (10/17), where **none of 22 trials ever enrolled a
child**. Gates fixed before the search exclude HSP90 inhibitors — simultaneously the lead
compound of the best-known "drugs for aneuploidy" paper and, here, predicted to destroy the
residual protein the child depends on.

**What we recommend first is not a drug.** It is a western blot for BubR1, which forks the
entire hypothesis and would additionally generate PS3-grade functional evidence on Track 1's
unresolved VUS. Measure before treating.

**A patient-specific layer.** A CPIC-guided PharmCAT screen of the proband's own genome,
whose headline is an honest negative: only 22 of 1,226 positions carry an interpretable
call, and **16 of 23 genes change call** when absent positions are assumed reference — an
assumption PharmCAT's own CLI labels "DANGEROUS!". It also caught a false alarm: PharmCAT
reports RYR1 `rs35364374` as "Uncertain Susceptibility" to malignant hyperthermia; ClinGen's
expert panel classifies that variant **Benign**.

**Strengths.** Pre-registration verifiable from commit order. Two independent drug
databases. Mechanism-derived gates catching a contraindication no pathway search surfaces.
**Forty-two verification findings that each *changed* the submission**, several against its
own thesis. A closing audit re-derived every figure above from the artefacts; all reproduce.

**Limitations.** No NAD⁺ precursor has been given to a BubR1-deficient animal, let alone a
person with MVA; the lead candidate's central inference is untested. The mouse models **do
not carry the human MVA genotype** — the mouse built with the patient architecture is
embryonic lethal where the equivalent human lived. Human NAD⁺ trials have failed on
musculoskeletal endpoints. `p.Asn1002Lys` is not proven to destabilise BubR1, and structural
analysis made that analogy weaker, not stronger. n = 1. No MVA patient has ever received any
of these agents for this indication, and nothing here is medical advice.
