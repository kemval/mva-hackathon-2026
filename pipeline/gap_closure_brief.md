# Gap-closure brief — MVA Hackathon 2026

**Status: COMPLETE as of 2026-09-04. All six tasks have run.** This began as a task
specification written before the work, in the same spirit as
`pipeline/track2_scoring_rubric.md`, and is retained unedited below so that what was asked
for can be compared against what came back. **What follows the table is the original brief,
not a description of the results.**

| Task | Outcome |
|---|---|
| **1 — Structural analysis of p.Asn1002Lys** | **Ran; result cuts against the thesis.** Q921, the tolerated counterexample, is *more* buried than Asn1002 (RSA 1.1% vs 16.2%) and also H-bonded. Position-based reasoning has a documented failure in this protein. Limitation 1 was **tightened**, not relaxed. ΔΔG attempted across three API shapes and **not obtained** — reported as inspection, never as ΔΔG. |
| **2 — Genotype–phenotype across the published cohort** | **Ran; the question as posed is unanswerable and a better one is answered.** 15 published patients tabulated, every row cited. Exactly one has both the proband's architecture and a tumour outcome, so **no genotype-stratified age-at-first-tumour comparison is possible and none is offered.** What the cohort does show: the birth-to-7y renal-ultrasound window fits Wilms well and is silent on everything else — the two published MVA rhabdomyosarcomas were in the soft palate and the orbit, the one patient with sequential primaries had her second at 12, and one patient's first malignancy was at 34. Also found a third allelic class (truncating + non-coding regulatory) the brief did not anticipate. No p-values. |
| **3 — Japanese and Chinese MVA literature** | **Ran; premise confirmed quantitatively, gap narrowed not closed.** Of 62 PCS-matching PubMed records only **21** are reachable through the "mosaic variegated aneuploidy" string — 41 are invisible to it. Recovered PMID 40555658, a Chinese-language 2025 report of two MVA fetuses. **CiNii, J-STAGE, J-GLOBAL, KAKEN, CNKI, Wanfang, VIP and the native-script terms were NOT queried**, and six full texts hit genuine walls with zero OA locations. Logged as an open acquisition gap, now measured rather than asserted. |
| **4 — Is the nephrocalcinosis a category error?** | **Ran; adjudicated (c), as pre-committed.** Unresolvable — the distinguishing datum is an imaging date that exists in no available file, and recontact is prohibited. Both hypotheses stay live. Task 2's cohort search was expected to cross-check this and **could not**: no published MVA patient with nephrocalcinosis was found, but abstract-level coverage is too thin to carry that negative. |
| **5 — Re-cost the coverage limitation** | **Ran; a standing overclaim withdrawn.** "Cannot be closed by acquiring data" rested on the RAM cost of a *whole-genome* index, which does not apply to the reduced reference anyone would actually use (~30 MB). The real objection is scientific, not resource-based: decoy-free realignment inflates MAPQ. That splits the route — BUB1B has **zero** segdups in its padded region, so it is sound there; CYP2D6 has **six**, so it is not. Corrected in four files. |
| **6 — Surveillance after a first tumour** | **Ran; the finding is a guideline silence.** Both Nakano 2024 and the SIOP-E primary (Hol 2021) are **silent** on post-first-tumour surveillance, and the non-renal exclusion is explicit in the primary. The MVA-specific radiosensitivity claim was re-tiered as a **class generalisation** after a targeted search returned five records, all wrong-product. Not filled by inference. |

**Two things this programme produced that were not asked for**, both recorded because
suppressing them would defeat the point: the scalability generalisation published in Part 8
was pre-registered, tested and **partly refuted by our own test**
(`data-notes/scale/RESULTS.md`), and a fifth identifier/duplicate trap was caught in the
cohort harvest.

---


The Track 2 submission has already survived an adversarial literature review (see
`literature/_contradiction_matrix.md`, C1–C11). Six substantive gaps remain. Three of them
sit directly under load-bearing claims, one is a possible category error, one is an
overclaim of record, and one is an acquisition gap the repository has already named
against itself.

Your job is to close them, or to establish honestly that they cannot be closed. **An
honest negative is a completed task, not a failed one.** Each task below ends with a
pre-committed acceptable-null outcome; that clause exists so that a null cannot be
quietly reframed as a partial positive when you reach it.

---

# Section A — constraints binding on every task

These carry forward unchanged from the original review brief. They are not stylistic.

## Safety and privacy

- **No recontact.** Do not attempt to contact the family, the clinical team, the
  hackathon organisers, or any patient-organisation contact, by any channel, for any
  reason, including to resolve an ambiguity you find. If a question can only be answered
  by asking someone, the answer is "unanswerable from available data" — write that.
- **Publish no demographic detail about the proband.** Fewer than 50 MVA patients are
  described worldwide. Sex plus age plus tumour type is re-identifying. This constrains
  Task 2 specifically: see the privacy rule inside that block.

## Scientific constraints — these have already caught real errors

- **Chromosomal instability forks into {senescence + SASP} and {cancer predisposition} as
  SIBLINGS, not a chain.** Never write that senescence leads to cancer in this case. A
  senescence-targeting drug is **not** expected to reduce this child's tumour risk.
- **Keep "FDA-approved medication", "dietary supplement" and "investigational" strictly
  distinct, per candidate, every time.** Never blur them, including in passing.
- **This is a protein DEFICIENCY, not defective enzymology.** Direction of effect governs
  everything. Any agent that would further lower BubR1 abundance is contraindicated —
  this is pre-registered gate **G1**, and it is why HSP90 inhibitors are excluded (mutant
  BubR1 is an HSP90 client; Suijkerbuijk 2010). Note that some HSP90 inhibitors are
  themselves senolytics (C1) — "senolytic" is not a safe class label here.
- **Never let a mouse result be described in language that implies human evidence.** Tier
  every claim: human RCT / human phase 1–2 / observational human / mouse in the BubR1
  background specifically / mouse elsewhere / cell line / in silico.
- **Much of the growth deficit is developmentally fixed.** Do not imply reversal.

## Provenance and process

- **Do not edit `pipeline/track2_scoring_rubric.md`.** The pre-registration argument rests
  on commit order being verifiable. Any rubric refinement goes into the report as a dated,
  explicitly-labelled post-registration clarification — never as a silent edit to the
  committed rubric.
- **Fetch full text, not abstracts** — and **exhaust the routes before recording a gap.**
  One failed route is not a gap; it is one failed route. Work this ladder, and record which
  rungs were tried:

  1. **A different API for the same resource.** Europe PMC REST
     (`ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`) is currently the most
     reliable. *The PMC HTML render route recorded in Pass 3 as "5-for-5" is now behind a
     Google reCAPTCHA and no longer works.* BioC and efetch often return abstract-only.
  2. **An OA-location service, to find where a legal copy actually lives.** OpenAlex
     (`api.openalex.org/works/doi:<DOI>`) and Semantic Scholar report `is_oa`, `oa_status`,
     licence, and every OA location. **Do this before believing any "closed access" signal.**
     Europe PMC's `isOpenAccess: N` means "not open access **in Europe PMC**" — deposit
     location, not licence. Misreading it cost this project a wrong Task 6 conclusion that
     reached three files before it was caught.
  3. **Institutional and funder repositories**, from the OA-location results. Note these are
     often browser-rendered **image-only PDFs with no text layer** — extract the pages and
     read them as images. A second repository may hold a text-layer copy, poor for quoting
     but excellent for locating content by page.
  4. **The publisher's own site**, and the primary source behind any summary you are relying
     on — and, when a primary resists, the summaries and reviews that quote it.
  5. **A different identifier for the same object**, verified by title.

  Only after that, record the gap — with the exact barrier named, so it is auditable and
  resumable by someone with different access.

- **Work around access *routes*, never access *controls*.** Do not bypass or complete
  CAPTCHAs, defeat paywalls, or misrepresent identity to obtain a file. A genuine wall is a
  gap and gets recorded as one. This limit is not in tension with the ladder above: the Task 6
  source that looked walled was never walled at all, and the CAPTCHA that was genuinely a wall
  stayed one.
- **Verify identifiers against titles.** Two NCBI identifier collisions have already been
  caught in this repository (a PMCID rendering a different paper by overlapping authors,
  and a PMCID belonging to a review that merely cited the intended primary study). Before
  quoting from any fetched record, confirm the fetched title matches the intended one.
- **Log every query — successes and failures with equal prominence** — into
  `literature/_fetch_log.md` as a new "Pass 4" section, with the exact query string and
  the date.
- **Grade every claim** Established / Predicted / Untested inference in
  `literature/_claims_register.md`, and record separately whether **any paediatric data**
  exists, reading structured eligibility fields (`minimumAge`, `stdAges`) rather than free
  text.

## What already exists — read these first, do not redo them

| File | What it holds |
|---|---|
| `literature/_fetch_log.md` | Every acquisition attempt to date, plus an explicit "scope this pass did NOT cover" section. Task 3 is named there as the largest untouched gap. |
| `literature/_contradiction_matrix.md` | Conflicts C1–C11, adjudicated. New conflicts you find are **C12 onward**. |
| `literature/_claims_register.md` | Every assertion, graded and tiered, including explicit "REJECTED — do not assert" rows. |
| `literature/_open_questions.md` | Q1–Q7, ranked by decision value, each with its cheapest experiment. New questions are **Q8 onward**. Note Q1–Q4 are four arms of a single fibroblast western blot. |
| `literature/15_suijkerbuijk2010_bubr1_abundance_mva.md` | The load-bearing mechanism paper: abundance, the ~6–13% functional threshold, and the HSP90-client finding. |
| `submissions/track1/gummietech_track1_report.md` | The ACMG work, the nephrocalcinosis reversal (Task 4), and the callability limitation (Task 5). |

## Deliverables — and one hard limit on them

Produce: new `literature/31_…` files onward (one per source, verbatim quotes, an explicit
**LIMITS** section listing what the paper does *not* show, and an evidence tier);
appends to the contradiction matrix, claims register, open questions and fetch log; and
for Task 5, the corrected wording.

**Do not edit `submissions/track2/gummietech_track2_report.md`,
`submissions/track2/clinician_onepager.md`, or `submissions/track2/pitch_script.md`.**
Instead write `submissions/track2/_pending_edits.md` listing the exact edits each finding
implies — file, section, current text, proposed text, and the finding that motivates it.
The submission text moves only after human review. Task 5 is the one exception and its
scope is stated in its own block.

When all tasks are done, re-run `/graphify /Users/kiki/mva-hackathon-2026 --update` (the
knowledge graph is already stale), and report which of the six tasks could **not** be
completed and why.

---

# Section B — the six tasks

Ordered by decision value. Tasks 1, 2 and 4 are the ones that can change a conclusion.

---

## Task 1 — Structural analysis of p.Asn1002Lys

### The problem

The entire Track 2 thesis is *"this variant lowers BubR1 abundance."* Limitation 1 of the
report concedes this is **probable by analogy, not demonstrated**. The repository holds
AlphaMissense (0.92), CADD (24.5), PolyPhen-2, SIFT and REVEL (0.472, indeterminate) — but
every one of those predicts **pathogenicity**, which is not the thing the mechanism needs.
The mechanism needs **destabilisation**. No structural work on residue 1002 exists
anywhere in this repository. This is the largest unfilled hole under the central claim,
and it is cheap to fill.

### Method

1. **Resolve structures properly.** Query the RCSB search API for entries mapped to
   UniProt **O60566** (human BUB1B). Do *not* trust a recalled PDB ID — verify each hit's
   title and its residue range, and record which entries actually cover the pseudokinase
   domain (residues **766–1050**, per UniProt, as used throughout Track 1).
2. **Pull AlphaFold `AF-O60566-F1`** and record the **pLDDT at residue 1002**. Residue 1002
   is 48 residues from the C-terminus; if pLDDT there is low, say so — it caps how much
   weight any downstream geometry can carry, and that limit belongs in the write-up.
3. **Characterise the position.** Compute or measure: relative solvent accessibility
   (burial vs surface), heavy-atom contact count within 5 Å, secondary-structure context
   within the pseudokinase fold, and the specific hydrogen bonds or salt bridges the Asn
   side chain makes. Note whether the residue sits at a known interaction interface
   (BUB3, KNL1, CDC20, or the intramolecular pseudokinase–TPR contacts).
4. **Reason about the substitution itself.** Asn→Lys introduces a positive charge and a
   longer side chain. Buried, that is a strong destabilisation argument. Surface-exposed
   and unpartnered, it is a weak one. State which case obtains, and do not soften a weak
   result into a strong one.
5. **Attempt a stability-specific ΔΔG** via a public predictor (DDMut, DynaMut2, MAESTRO
   or equivalent). If none is reachable, **report structural inspection as inspection, not
   as ΔΔG.** A prediction you did not run is not a prediction you have.
6. **The high-value sub-analysis.** Take the MVA missense alleles Suijkerbuijk 2010
   actually tested and map them onto the same structure. Ask whether they cluster near
   1002 **in three dimensions**, even where they are distant in sequence. If they do, the
   analogy that Limitation 1 rests on stops being positional hand-waving and becomes a
   structural argument. If they do not, that is a real weakening of the thesis and must be
   reported as one.

### Acceptance criteria

A `literature/`-style analysis file stating, with numbers: where N1002 sits, what it
contacts, what Asn→Lys does there, whether a ΔΔG was obtained and from what, and whether
the Suijkerbuijk alleles co-localise. Plus a claims-register row and, if the finding
conflicts with anything already asserted, a contradiction-matrix entry.

### Pre-committed outcome

**This is in-silico work and stays tiered as in-silico.** At best it moves Limitation 1
from "analogy" to "analogy plus structural prediction". It **cannot** reach "demonstrated"
— only the BubR1 western blot (Q1) can do that, and the report must continue to say so.
If N1002 turns out to be surface-exposed and unremarkable, write that plainly: it would
mean the central claim rests more heavily on the western blot than the report currently
concedes, which is a finding worth more than a comfortable one.

---

## Task 2 — Genotype–phenotype correlation across the published MVA cohort

### The problem

Fewer than 50 MVA patients are described worldwide, which makes the case literature small
enough to tabulate **exhaustively** — a comparison the literature can actually support and
which, as far as this repository can tell, has not been done. The proband's architecture is
**truncating + missense**. Whether that architecture behaves differently from biallelic
missense is directly case-relevant, and it determines whether the surveillance protocol
Track 2 cites is genotype-appropriate here.

### Method

1. **Assemble the case set.** Start from `literature/04_mva_society_bibliography.md` and
   Hanks 2004 (PMID 15475955, five families), then traverse citations in both directions —
   cited-by and reference lists. Known names to chase: Matsuura, Suijkerbuijk 2010,
   García-Castillo, Jacquemont, Lane, Kajii, Izumi, Plaja, Callier, Putoux 2017 (two
   brothers). Fold in anything Task 3 recovers.
2. **One row per published patient.** Columns: source PMID; allelic architecture
   (truncating/truncating, truncating/missense, missense/missense); the specific variants;
   domain position of each missense; tumour Y/N; tumour type; **age at first tumour**;
   microcephaly; growth parameters; **renal findings** *(this column feeds Task 4)*;
   PCS/aneuploidy rate; survival or age at last report.
3. **Then compare architectures** on tumour spectrum, age at first tumour, and survival.
4. **Answer the applied question:** does the truncating+missense subgroup's age-at-first-
   tumour distribution fall inside the birth→7y renal-ultrasound window Nakano 2024
   recommends, or outside it?

### Privacy rule — read this before building the table

The table covers **published patients only**. Each row must be traceable to a citation.
**The proband is never added as a row**, and the table must not be used to triangulate him
— no "our patient resembles case 7" narrowing, and no combination of his features
reproduced alongside it. The <50-patient count that makes this analysis tractable is the
same count that makes re-identification possible.

### Acceptance criteria

The table as a committed file, every row cited; a written comparison; and an explicit
statement of the surveillance-window answer.

### Pre-committed outcome

**Cases are published because they had tumours.** Ascertainment bias is not a caveat here,
it is the dominant feature of the dataset — a genotype–tumour association could be entirely
manufactured by which families got written up. If the comparison is underpowered or
confounded, say so and report descriptively. **Do not compute p-values on an
ascertainment-biased case-report series**, and if you compute anything inferential,
label it as descriptive and explain why it cannot be read as a test.

---

## Task 3 — Japanese and Chinese MVA literature

### The problem

`literature/_fetch_log.md` names this, in its own words, as the largest untouched
acquisition gap in the repository. It is not a minor one: much of the early
characterisation of this condition ran through the Japanese **premature chromatid
separation (PCS)** literature. With a world total near 50 patients, missing a national
cohort could mean missing a real fraction of all described cases.

### The key insight — state it before searching

**"Mosaic variegated aneuploidy" as a search string misses this literature structurally.**
The same entity was described as **PCS syndrome** by Kajii, Matsuura and Ikeuchi. Search
the phenotype's other name, not just its current one.

### Method

Search, logging **every** query verbatim with its date:

- **PubMed** with `[la]jpn` and `[la]chi` language limits; author-name searches for Kajii T,
  Matsuura S, Ikeuchi T, Izumi H; and "premature chromatid separation", "PCS syndrome",
  "constitutional aneuploidy".
- **CiNii Research** (`cir.nii.ac.jp`), **J-STAGE** (`jstage.jst.go.jp`), **J-GLOBAL**,
  and **KAKEN** (grant records often name cohort-building work that never reached a
  journal).
- *Journal of Human Genetics* and *Congenital Anomalies* — English-language venues that
  carry Japanese cohorts.
- **CNKI, Wanfang, VIP** for Chinese-language reports.
- Search terms in all three languages, including 早期染色体分離 and PCS症候群.

Any patient recovered here flows into **Task 2's table**.

### Acceptance criteria

A Pass 4 fetch-log section listing every query and its outcome; new `literature/` files for
anything obtained in full text; and new rows in Task 2's table.

### Pre-committed outcome

**Much of this is paywalled, un-indexed, or both.** "Attempted, blocked, here is the exact
query and what it returned" is a **fully acceptable result** and must be logged as
prominently as a hit — that is the standing discipline in this repository and it applies
here more than anywhere. What is *not* acceptable is leaving the gap undescribed, or
implying coverage that was not achieved.

---

## Task 4 — Is the nephrocalcinosis a category error?

### The problem

Track 1 originally offered acquired explanations for the nephrocalcinosis — prematurity,
loop diuretics, the calcium and phosphate load of parenteral nutrition, immature tubular
handling — and then **withdrew both**, on the grounds that the phenotype document says the
finding is *"present since birth"* and every acquired mechanism is postnatal. It now
argues congenital onset **raises** the prior for a second monogenic cause, and reports the
negative 6-gene renal panel as a materially weaker negative because of it.

That reversal may itself be the error. Nephrocalcinosis is **common** in preterm infants —
loop diuretics, PN mineral load, and the neonatal course alone are sufficient. This is
exactly the kind of thing a clinician catches instantly and a variant pipeline never does.
The repository currently contains **no preterm-nephrocalcinosis literature at all**.

### What the source actually says — verified, quote it

`data-notes/raw/Challenge_Clinical_Phenotype_1.docx` is **2,750 characters in total**. The
entire basis for the reversal is one table cell:

> "Nephrocalcinosis | Nephrocalcinosis | HP:0000121 | Calcium deposits in kidney tissue;
> **present since birth**"

There is **no imaging date and no onset detail anywhere in the document**. Note also its
provenance: this is a phenotype summary table written for a hackathon, not a clinical
record. A preterm infant first imaged at four weeks in NICU could plausibly be summarised
as "present since birth" by someone compressing a chart into a table cell.

### Method

1. Quote the clause verbatim and state its provenance as above.
2. Establish from the literature what "present since birth" can and cannot distinguish:
   the **incidence and especially the timing** of nephrocalcinosis in preterm/VLBW infants;
   the furosemide association; PN calcium/phosphate load; and whether antenatal-onset
   nephrocalcinosis is detectable at all, and by what.
3. Cross-check **Task 2**: do any published BUB1B-MVA patients have nephrocalcinosis? If
   several do, it may be an under-documented feature of the syndrome and neither acquired
   nor a second diagnosis — a third possibility the current text does not consider.
4. **Adjudicate into exactly one of:**
   - **(a)** Track 1's withdrawal was correct — congenital onset does raise the monogenic
     prior, and the reasoning stands.
   - **(b)** Track 1 **over-corrected** on a four-word clause in a summary table, and the
     acquired explanation should be restored as at least co-equal.
   - **(c)** The source cannot resolve it, the distinguishing datum is an imaging date that
     does not exist in any available file, and **recontact is prohibited** — so the
     question is unanswerable and both hypotheses stay live.

### Acceptance criteria

A literature file on preterm nephrocalcinosis with verbatim quotes and a LIMITS section; a
contradiction-matrix entry (C12+) recording the adjudication and its grounds; and, in
`_pending_edits.md`, the exact Track 1 report text that would change under each outcome.

### Pre-committed outcome

**(c) is a likely and fully acceptable answer** and must be stated prominently rather than
resolved by picking whichever side reads better. If the honest finding is that a published
reversal rests on four words in a hackathon summary table with no imaging date behind them,
that is the finding — write it that way.

---

## Task 5 — Re-cost the coverage limitation and correct the overclaim

### The problem

`pipeline/README.md` and `data-notes/track1_findings.md` state that the callability
limitation **"cannot be closed by acquiring data,"** justified by the RAM cost of a
human-genome aligner index (BWA ~6–7 GB, minimap2 ~11 GB, bwa-mem2 ~40 GB) against 8 GB
installed. But **you do not need the whole genome.** A reduced reference containing only
BUB1B plus the PGx regions has a trivially small index. The RAM argument, as written, does
not apply to the approach that would actually be used. The claim is stronger than the
situation warrants.

### Scope — decided, do not exceed it

**No alignment is run in this task.** The deliverable is an honest re-costing and a
corrected claim, not a coverage track. Do not download the FASTQ.

### Method

1. **Re-verify the machine's constraints.** Measured 2026-09-02: **8 GB RAM, 8 cores,
   30 GB free disk** — note the repository says 33 GB, which is now stale — **`samtools`
   is installed** at `/opt/homebrew/bin/samtools`, and **no aligner is present** (bwa,
   bwa-mem2, minimap2, bowtie2, hisat2 all absent). Re-check before writing.
2. **Cost the reduced-reference route honestly.** State the actual index size for a
   ~200 kb region; state that the RAM objection does not survive it; then state what the
   real costs are: ~79 GB of FASTQ streamed through the aligner (network and CPU time, not
   memory), and the runtime on 8 cores.
3. **Name the real scientific objection, which is not resource-based.** Decoy-free
   targeted realignment attracts reads from paralogous and repetitive regions genome-wide,
   because reads that belong elsewhere have nowhere else to go — producing false coverage
   that looks like real coverage. This is **genuinely fatal for CYP2D6/CYP2D7** and merely
   **noisy** elsewhere. Check BUB1B specifically for segmental-duplication, pseudogene or
   readthrough exposure (note the BUB1B-PAK6 readthrough locus) and say which category
   BUB1B falls into.
4. **Rewrite the claim** in `pipeline/README.md`, `data-notes/track1_findings.md`, and the
   corresponding Track 1 report limitation, to what is actually true — something closer to
   *"feasible by a route this analysis did not run, at these named costs and with these
   named failure modes"* than *"cannot be closed."*

### Preserve what is correct

Two things in the current text are right and must survive the correction:

- **Short reads cannot resolve phase across ~11 kb.** The two variants are beyond fragment
  span; read-backed phasing faces the same physical limit. This is not weakened by
  anything in this task.
- **The dataset genuinely contains no BAM or CRAM** — 13 files, 79.1 GB, 78.9 GB of it
  FASTQ. The hackathon site's "optionally in BAM/CRAM" claim is wrong and the manifest
  wins. That correction stands.

### Acceptance criteria

Corrected wording in all three locations, with the numbers stated; and a short feasibility
note recording the re-costing so the reasoning is auditable rather than asserted.

### Pre-committed outcome

Do not overcorrect in the other direction. The honest position is *"feasible with named
costs and named failure modes, not attempted"* — **not** *"the limitation is closed."*
It is not closed. It is differently open than the repository currently says.

---

## Task 6 — Surveillance after a first tumour

### The problem

The surveillance protocol Track 2 cites — `literature/23_nakano2024_surveillance_genomic_instability.md`,
AACR 2024, endorsing the SIOP-Europe recommendation — is **renal ultrasound every 3 months
from birth to age 7**, and it is oriented to Wilms tumour. **This child has already had a
rhabdomyosarcoma.** Whether the protocol changes after a first tumour is unaddressed
anywhere in the submission. So is the practical bind: the same guideline says *"radiation
exposure should be avoided"*, which constrains how you do imaging surveillance at all.

### Method

1. **Go to the primary recommendation, not the summary of it.** Nakano 2024 reports the
   SIOP-Europe Host Genome Working Group / SIOP Renal Tumour Study Group recommendation and
   says the AACR group "supports" it. Fetch the SIOP-E source itself and check whether it
   addresses post-first-tumour surveillance, which Nakano's summary does not.
2. **Check the AACR workshop series** for survivorship and post-first-tumour guidance
   across the cancer-predisposition syndromes, and the whole-body-MRI protocols developed
   for Li-Fraumeni (the Toronto protocol precedent) as the model for
   non-ionising-modality surveillance in a radiation-sensitive patient.
3. **Check COG survivorship guidelines** and rhabdomyosarcoma survivor follow-up guidance
   for what applies to a survivor with an underlying predisposition syndrome.
4. **Separately establish the tier of the radiation-sensitivity claim.** Is radiation
   sensitivity documented **for MVA / BUB1B specifically**, or is it inherited from
   Nakano's general statement about the genomic-instability disorder class ("many of these
   genomic instability disorders also present with exquisite sensitivity…")? These are
   different evidentiary claims and the report currently does not distinguish them. If it
   is the class statement, say so — a class generalisation applied to a specific syndrome
   is exactly the kind of move this repository flags elsewhere.

### Acceptance criteria

A new literature file per source obtained, with verbatim quotes and LIMITS; a claims-
register row for the radiation-sensitivity tier specifically; and `_pending_edits.md`
entries for the surveillance section of the report and the one-pager.

### Pre-committed outcome

**"The guideline is silent on the post-first-tumour case" is itself a real and reportable
finding**, and a useful one for a family — it tells them the protocol they have been given
was written for a different situation than the one they are in. Do not fill a guideline
silence with inference and present the result as guidance. If the literature does not
answer it, add it to `_open_questions.md` as Q8+ with the cheapest way to resolve it.

---

# Section C — how to finish

1. Every source obtained → `literature/31_…` onward, one file each, verbatim quotes,
   **LIMITS**, evidence tier.
2. Every conflict found → `_contradiction_matrix.md` as C12+, with adjudication **and
   grounds** (sample size, model system, primary vs incidental, replication, corrigendum).
3. Every assertion → `_claims_register.md`, graded and tiered.
4. Every unanswerable question → `_open_questions.md` as Q8+, with its cheapest experiment.
5. Every query → `_fetch_log.md`, Pass 4, failures as prominent as successes.
6. Every implied submission edit → `submissions/track2/_pending_edits.md`, **written but
   not applied** (Task 5 excepted, per its own block).
7. Re-run `/graphify /Users/kiki/mva-hackathon-2026 --update`.
8. **Report which of the six tasks could not be completed, and why.** A task you could not
   finish, described accurately, is worth more than a task you finished by lowering the
   standard.

Where the evidence is thin, say it is thin. An honest negative finding is worth more to
this child than an overstated positive one.
