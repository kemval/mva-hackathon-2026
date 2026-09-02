# Surveillance after a first tumour in MVA — what the guidelines say, and where they stop

Captured 2026-09-02 for **Task 6** of `pipeline/gap_closure_brief.md`.

**Headline: the guideline is silent on this case, and the silence is the finding.** The
AACR/SIOP-E recommendation this project cites is a *Wilms* surveillance protocol running
birth→7 years. This child has already had a rhabdomyosarcoma. Nothing in the MVA
recommendation says what changes after a first tumour, and no MVA-specific evidence
underwrites its radiation-avoidance advice.

---

## 1. What the MVA recommendation actually contains

From `literature/23_nakano2024_surveillance_genomic_instability.md` (Nakano et al., *Clin
Cancer Res* 2024, PMID 39264246), the complete MVA section, read end to end:

> "This group recommended renal ultrasound surveillance every 3 months from birth until age
> 7, for all MVA conditions including those with an unknown genetic cause. **Radiation
> exposure should be avoided.** This AACR study group supports these recommendations."

> "We recommend regular clinical assessment including review of systems to identify signs of
> rhabdomyosarcoma and other malignancies."

> "Whereas cancer risk is clearly increased in MVA, **the rarity of the syndrome hampers
> establishment of an accurate risk assessment**, particularly when considering the different
> MVA subtypes. Therefore, we recommend increased awareness in MVA families for early signs
> of potential tumor development."

**Read against Task 6's question, four things are absent.** There is no statement about
surveillance *after* a first malignancy; no imaging modality for the rhabdomyosarcoma risk it
names (only "clinical assessment"); no whole-body MRI recommendation for MVA, though the same
paper does recommend WBMRI for other syndromes it covers; and no rationale given for stopping
renal ultrasound at 7, nor any guidance for the years beyond it.

## 2. The primary source is paywalled — and NCBI mis-links it

The brief directed me to the SIOP-E recommendation itself rather than Nakano's summary of it.
That is **Hol JA, Jewell R, Chowdhury T, Duncan C, Nakata K, Oue T, et al., "Wilms tumour
surveillance in at-risk children: Literature review and recommendations from the SIOP-Europe
Host Genome Working Group and SIOP Renal Tumour Study Group," *Eur J Cancer* 2021, PMID
34134020, DOI 10.1016/j.ejca.2021.05.014.**

**It could not be obtained.** Europe PMC's authoritative record returns `pmcid: None`,
`isOpenAccess: N`, `inPMC: N` — Elsevier, closed, no open deposit anywhere.

> ⚠️ **Identifier caution — the fourth collision found in this repository.** NCBI `elink`
> returned **PMC13164404** for PMID 34134020. That PMCID is a **different paper**:
> *"Genetic and Epigenetic Drivers of Wilms Tumor Predisposition in Russian Pediatric
> Patients: A Multicenter Study," Int J Mol Sci* **2026**. It is on the same topic — Wilms
> predisposition — so its content would have read as plausible corroboration. Caught by the
> mechanical title check before a single word was quoted. Logged as **C15**.

**Consequence, stated plainly:** the surveillance protocol this project recommends to a family
is cited **second-hand**, through a summary in another paper, and cannot be verified against
its primary text. That limit belongs in the report.

## 3. Is radiation sensitivity documented *for MVA*?

**No.** A targeted PubMed search — `(mosaic variegated aneuploidy OR BUB1B OR premature
chromatid separation) AND (radiosensitiv* OR "radiation sensitiv*" OR irradiat*)` — returned
**five records, all wrong-product matches**: radiation inducing chromatid separation in
carcinoma cells, BUB1B in breast-cancer homologous recombination, a mouse *Apc* QTL study,
phototherapy on fibroblasts, and visceral obesity. **None concerns MVA patients.**

The recommendation instead descends from Nakano's opening class statement:

> "**Many** of these genomic instability disorders also present with exquisite sensitivity to
> anticancer treatments such as ionizing radiation and chemotherapy, which may further
> increase the risk of second cancers."

Note "**many**", not all. Where the paper documents hypersensitivity it names the syndrome —
ataxia-telangiectasia, and Nijmegen breakage syndrome, whose patients "typically show
hypersensitivity to radiation." **MVA is not among them.** Its section carries the
recommendation with no supporting sensitivity data.

The general principle the paper invokes is precautionary rather than syndrome-specific:

> "major national and international organizations responsible for evaluating radiation risks
> agree that there probably is no low-dose radiation 'threshold' for inducing cancers. In
> other words, **no amount of radiation should be considered absolutely safe.**"

**This does not make the advice wrong.** Avoiding radiation in a child with constitutional
chromosomal instability and a cancer predisposition is prudent on first principles. But the
report must not imply that MVA-specific radiosensitivity evidence exists, because it does not.

## 4. The worked precedent in an adjacent syndrome — cited as precedent, not transplanted

Li-Fraumeni is the syndrome where the field has actually solved this bind. **Frebourg T et al.,
"Guidelines for the Li-Fraumeni and heritable TP53-related cancer syndromes," *Eur J Hum
Genet* 2020, PMID 32457520:**

> "in cancer patients with germline disease-causing TP53 variants, **radiotherapy, and
> conventional genotoxic chemotherapy contribute to the development of subsequent primary
> tumours.** It is critical to perform TP53 testing **before the initiation of treatment** in
> order to avoid in carriers, if possible, radiotherapy and genotoxic chemotherapies."

> "In children, the recommendations are to perform clinical examination and abdominal
> ultrasound **every 6 months**, annual **WBMRI and brain MRI from the first year of life**."

Every modality there is **non-ionising** — which is how a surveillance programme is built for a
patient who must avoid radiation. And **Kratz CP et al., *Clin Cancer Res* 2017 (PMID 28572266)**
records the AACR panel adopting "a modified version of the 'Toronto protocol'."

**This is a precedent for the shape of a solution, not evidence about MVA.** LFS is a
dominant single-gene tumour-suppressor syndrome with a large evidence base; MVA is a recessive
chromosomal-instability syndrome with under 50 described patients. Nothing here may be
represented as an MVA recommendation.

## 5. Where post-first-tumour guidance would live, if it exists

**Bhatia S et al., "The Children's Oncology Group Long-Term Follow-Up Guidelines…", *JAMA
Oncol* 2025, PMID 39976936.** Version 6.0 (October 2023), 165 sections, applies to those "who
survived 2 or more years from completion of… cancer-directed therapy":

> "Major changes include the addition of **recommendations regarding surveillance for genetic
> cancer predisposition**, surveillance following the use of novel cancer treatment
> modalities, and routine vaccination practices during long-term follow-up."

This is the correct framework for a survivor with a predisposition syndrome, and the child is
one. **What it says about MVA specifically was not obtained** — the guideline is a separate
document at survivorshipguidelines.org, not fetched here. Recorded as a named gap, not as an
answer.

---

## LIMITS — what this file does NOT show

- **It does not establish that the protocol should change after a first tumour.** It
  establishes that the guideline does not address the question.
- **The primary SIOP-E recommendation was never read.** Everything about it here is Nakano's
  summary.
- **COG LTFU v6.0's actual content was not retrieved.** Whether it names MVA is unknown.
- **The absence of MVA radiosensitivity literature is from one targeted search**, in English,
  on PubMed. Task 3's non-English literature is untouched and could hold Japanese PCS-era
  radiosensitivity work — plausible, given that chromosomal breakage studies were that
  field's core method.
- **No MVA-specific RMS surveillance recommendation was found anywhere**, which is consistent
  with none existing, but is not proof of it.
- Nothing here is a treatment recommendation, and no source addresses this child.

## Evidence tier

**Expert-consensus guideline** (AACR workshop, SIOP-E) for the MVA protocol — the strongest
tier available in this project, and still consensus rather than trial evidence, in a syndrome
whose own guideline says the rarity "hampers establishment of an accurate risk assessment."
The LFS material is **guideline evidence about a different syndrome**. The radiation-avoidance
advice is **precautionary class generalisation**, not MVA-specific data.
