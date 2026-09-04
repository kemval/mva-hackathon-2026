# Task 2 — the published MVA cohort, and what it says about the surveillance window

Built 2026-09-04. Table: `data-notes/mva_published_cohort.tsv` (15 published patients or
pedigrees, every row carrying a PMID). Supersedes the INCOMPLETE marker in
`literature/33_bubr1_allelic_effects_genotype_phenotype.md`, which remains the source for
the mouse-model finding.

**Privacy rule observed.** Published patients only. The proband is not a row, is not
compared to any row individually, and no combination of his features is reproduced here.
Fewer than 50 MVA patients are described worldwide; that number is what makes this
analysis tractable and also what makes re-identification possible.

---

## The applied question, and its answer

`literature/23_nakano2024_surveillance_genomic_instability.md` carries the recommendation
Track 2 cites: **renal ultrasound every 3 months from birth to age 7**, oriented to Wilms
tumour. Task 2 asks whether the truncating+missense subgroup's age-at-first-tumour
distribution falls inside that window.

**The honest answer is that the question, as posed, cannot be answered — and that the
window has a different and larger problem that the cohort does answer.**

### Why the genotype-stratified version is unanswerable

Of 15 published patients/pedigrees assembled, **exactly one** has both the proband's
truncating+missense architecture and a stated tumour outcome — He 2018 (PMID 30512160), a
girl of 1 y 11 m with `c.826delG` + `p.Arg814His`, in whom **no tumour is reported at that
age**, which at 23 months is uninformative about lifetime risk. One patient is not a
distribution. **No genotype-stratified age-at-first-tumour comparison is possible from the
published literature, and none is offered here.**

This is a real limit, not a soft one, and it has a specific cause: most case reports
predate routine sequencing (the 1999–2002 cases are cytogenetic diagnoses with no genotype
at all) and most of those that do report a genotype do not report an age at first tumour.

### What the cohort does establish, which matters more

Ages at first tumour, where stated:

| Age | Tumour | Patient |
|---|---|---|
| infant | bilateral Wilms | Kawame 1999 (10429359) |
| 3 | myelodysplasia → ALL | Jacquemont 2002 (11932988) |
| 3 | Wilms | Vempuluru 2026 (42595739) |
| 3.2 (38 mo) | bilateral Wilms | Ochiai 2019 (31081598) |
| 7 | embryonal rhabdomyosarcoma, **soft palate** | Limwongse 1999 (9916837) |
| **12** | embryonal rhabdomyosarcoma, **orbit** — *second* primary | Vempuluru 2026 (42595739) |
| **34** | ampullary adenocarcinoma, then colon + gastric | Rio Frio 2010 (21190457) |

Renal tumours cluster early, inside the window — which is what the window was built for
and is evidence it is well-designed *for Wilms*. **Three findings cut against reading it
as general cancer surveillance:**

1. **The rhabdomyosarcomas are not renal and not detectable by renal ultrasound.** The two
   sites reported are the **soft palate** (Limwongse 1999) and the **orbit** (Vempuluru
   2026). A renal ultrasound protocol, however faithfully executed, would not have found
   either. This is the single most decision-relevant line in the table for any MVA patient
   whose tumour history is rhabdomyosarcoma rather than Wilms.

2. **The only published MVA patient with sequential primaries had the second at age 12** —
   five years after the window closes (Vempuluru 2026). Her first tumour, a Wilms at age
   3, was inside it. A protocol that stops at 7 stops between her two tumours.

3. **Risk does not end in childhood.** Rio Frio 2010 describes a homozygous `BUB1B`
   intronic patient whose first malignancy was an ampullary adenocarcinoma at **34**,
   followed two decades later by multiple primary colon and gastric adenocarcinomas. A
   birth-to-7 protocol does not address the phenotype at all in that patient.

**Consequence, stated without inference beyond the data:** the birth-to-7y renal
ultrasound recommendation is well matched to Wilms risk and is **silent on**
non-renal tumours, on post-first-tumour surveillance, and on adult-onset risk. That is
consistent with — and now empirically supported by — the guideline-silence finding already
recorded from the primary sources (Q9; `literature/32_surveillance_after_first_tumour.md`).
It remains a **gap in the guideline**, not a recommendation this repository is entitled to
fill.

---

## A genotype–phenotype signal worth recording, and its ascertainment problem

Two observations survive from the table:

- **Tumour risk may be gene-dependent, not uniform across "MVA".** All six biallelic
  `TRIP13` patients developed Wilms tumour (Yost 2017, PMID 28553959) — a strikingly
  complete penetrance for that one tumour. Meanwhile Pinson 2014 (PMID 24259107) proposes
  that **absence of tumour development**, together with conserved head circumference, is a
  feature distinguishing `CEP57`-related MVA2 from `BUB1B`-related MVA1. If that holds,
  "MVA" is not one surveillance population, and a protocol derived from mixed cohorts is
  applied to genes with different risks.
- **A third allelic class exists that this task was not specified to expect.** Two
  independent pedigrees carry a **non-coding regulatory** allele — a promoter `G>A`
  (Yamaguchi 2018, PMID 29673003) and an upstream regulatory element variant
  `ss804270619 G>A` (Qu 2025, PMID 40555658), each paired with a truncating allele. This
  matters mechanistically rather than just taxonomically: **a regulatory variant can only
  reduce the amount of protein made, not alter the enzymology of the protein made.** Two
  independent human pedigrees reaching the MVA phenotype through a purely quantitative
  route is convergent support for Track 2's central claim that the therapeutic target is
  protein quantity — support that does not depend on Suijkerbuijk's cell work.

### Why no statistic is computed on any of this

**Pre-committed in the brief, and it binds.** Cases are published *because* they had
tumours. The 21% malignancy figure Jacquemont 2002 reports (3 of 14) is a proportion among
*published* patients, and publication is conditioned on the outcome being measured.
Ascertainment bias is not a caveat on this dataset, it is its dominant feature. **No
p-value is computed, no test is performed, and the TRIP13 6-of-6 figure must not be read
as a penetrance estimate** — it is six patients ascertained through a study that found them
by sequencing children who had Wilms tumour.

---

## LIMITS — what this table does not show

- **It is not exhaustive.** It is what a systematic PubMed harvest (582 records across 14
  query strings, triaged to 65 patient-level candidates) yielded at abstract level. Older
  cases enumerated only inside review articles are not separately represented.
- **Almost every row is abstract-grade.** Six sources were pursued to full text and
  **blocked** (see `_fetch_log.md` Pass 4). Blank cells mean "not stated in the abstract",
  never "absent in the patient". The renal column in particular is badly served by
  abstracts and cannot support the Task 4 cross-check it was built for — **one** patient
  (He 2018) has a renal finding stated, which is far too thin to say whether renal
  involvement is an under-documented MVA feature. Task 4's adjudication is unaffected and
  stays at (c), unresolvable.
- **One row is probably not MVA at all.** Sari 2009 (PMID 19373780) is attributed by its
  own authors to **Fanconi anaemia** presenting with PCS, and its three tumours should not
  be read as an MVA tumour spectrum. It is retained, flagged, because excluding it
  silently would be the more misleading choice.
- **A double-counting trap was caught.** PMID **19856400** (Alter & Olson 2010) carries an
  almost identical title to PMID 19373780 and is a **comment on that case, not a second
  patient**. Counting both would have inflated the cohort and duplicated three tumours.
  This is the fifth identifier/duplicate trap recorded in this repository; the standing
  title-verification check is what caught it.
- **Diagnoses are not uniform.** Rows span pure cytogenetic diagnoses (1999–2002),
  gene-confirmed MVA1/MVA2/MVA3, and prenatal diagnoses where the outcome is a
  termination. They are not a like-for-like population and are not treated as one.
