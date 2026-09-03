# Pending submission edits — written, not applied

Findings from `pipeline/gap_closure_brief.md` imply the edits below.

Status: **Tasks 1, 4 and 6 complete. Tasks 2, 3 and 5 not started.**

**APPLIED 2026-09-02.** Edits 1–8 and 10–16 are now in the submission text, reviewed and
applied together so the repository and the submission no longer disagree. Three departures
from the list as written, each deliberate:

- **Edit 9 (Kajii 1998 renal footnote) was NOT applied.** Its own rationale says it must
  either be cited as weak and non-exclusive or left out until Task 2 runs. Task 2 has not
  run, so it is left out. It stays live here.
- **Three connective changes** were needed for the applied edits to be coherent rather
  than merely inserted: the Track 1 sentence "**Both of those conclusions are withdrawn**"
  became "**The first of those conclusions is withdrawn**" (Edit 6 reinstates the second);
  the biochemistry recommendation was decoupled from the withdrawn "congenital onset raises
  the prior" clause and now stands on its own indication; and the one-pager's "probably
  unstable — the published pattern for MVA variants **sitting where this one sits**" was
  rewritten, since that is precisely the positional argument Edit 1 withdraws. The
  one-pager's own "No edit required" note anticipated this.
- **Claims K4/K5 were propagated** beyond this list, into §3.2 limit 1 and Part 7
  Limitation 2 of the Track 2 report. They post-date this file (commit `6e6f81d`) and bear
  directly on the lead candidate's evidence tier: the mouse models cited throughout do not
  carry the human MVA genotype. Leaving that in the registers and out of the submission
  would have been the exact failure this file exists to prevent.

---

## From Task 1 — structural analysis of p.Asn1002Lys

Full finding: `data-notes/structural_analysis_n1002k.md`. Claims register **section H**.
Contradiction matrix **C12**.

**The direction of these edits is the opposite of what was expected.** The task was
commissioned to shore up the report's central claim. It found a specific, testable
mechanism — and it also found that the report's own cited counterexample, `Q921H`, is
structurally indistinguishable from the candidate. The net recommendation is to **tighten**
Limitation 1, not relax it.

### Edit 1 — Part 7, Limitation 1 *(the substantive one)*

**File:** `submissions/track2/gummietech_track2_report.md`, Part 7, item 1

**Current:**
> 1. **`p.Asn1002Lys` is not proven to destabilise BubR1.** It was not among the mutants
>    Suijkerbuijk tested, and `Q921H` is a same-domain counterexample that behaves like
>    wild-type. The mechanism for *this child* is probable by analogy, not demonstrated.
>    Track 1 classifies the variant as a VUS and this report does not upgrade it.

**Proposed:**
> 1. **`p.Asn1002Lys` is not proven to destabilise BubR1, and structural analysis makes the
>    analogy weaker rather than stronger.** It was not among the mutants Suijkerbuijk tested,
>    and `Q921H` is a same-domain counterexample that behaves like wild-type. Modelling both
>    residues on AlphaFold `AF-O60566-F1` (`data-notes/structural_analysis_n1002k.md`) shows
>    **Q921 is *more* buried than Asn1002 (RSA 1.1% vs 16.2%) and also makes buried
>    side-chain hydrogen bonds** — so every structural feature that would mark residue 1002
>    as critical is also present at a position where substitution demonstrably did nothing to
>    protein level. Position-based reasoning has a documented failure in this protein. What
>    the modelling does supply is a *specific and falsifiable* mechanism: Asn1002 makes three
>    side-chain hydrogen bonds cross-linking the Trp978 and Val998 backbone, and Asn→Lys
>    loses the acceptor outright while introducing a buried positive charge into an aromatic
>    pocket. That is a hypothesis to test, not evidence for the conclusion. The mechanism for
>    *this child* is probable by analogy, not demonstrated. Track 1 classifies the variant as
>    a VUS and this report does not upgrade it.

**Why:** claims register H8, H9, H11, H15, H16.

### Edit 2 — §1.x, the mechanism paragraph carrying the Q921H counterexample

**File:** `submissions/track2/gummietech_track2_report.md`, line ~130
(*"**And the counterexample belongs in the same paragraph.** `Q921H` lies inside the same…"*)

**Proposed addition** after the existing counterexample sentence:
> Structural modelling sharpens rather than dissolves this counterexample: Q921 is more
> deeply buried than Asn1002 and also hydrogen-bonded, so its tolerance cannot be explained
> away as a surface position. The distinction that survives is chemical, not positional —
> Gln→His preserves both hydrogen-bond donor and acceptor capability, whereas Asn→Lys
> preserves neither and adds a charge — and that distinction is itself weakened by `R814H`,
> a conservative Arg→His substitution that *was* destabilising.

**Why:** H8, H10.

### Edit 3 — §5.1 / §5.2, raise the priority of the western blot

**File:** `submissions/track2/gummietech_track2_report.md`, experimental section

**Proposed:** state explicitly that the structural work **raises** the value of the BubR1
western rather than substituting for it — the mechanism is now specific enough to be
falsified by a single abundance measurement, and no computational route can settle it.

**Why:** H15, H17. Also strengthens `literature/_open_questions.md` Q1.

### Edit 4 — Track 1 report, PM1 discussion *(optional, small)*

**File:** `submissions/track1/gummietech_track1_report.md`, PM1 paragraph

The PM1 rejection **stands** and should not change. Optional footnote: the standing
variation cited against PM1 includes `p.Asn1004Ser` (AF 6.0e-4), which is **surface-exposed
at RSA 53%** while the candidate two residues away is buried — the domain is not a hotspot,
and position within it still differs. Do not let this be read as reviving PM1.

**Why:** H7.

### Edit 5 — Part 11 verification table

**File:** `submissions/track2/gummietech_track2_report.md`, Part 11

Add rows: (20) AlphaFold-based structural characterisation of N1002 and the Suijkerbuijk
comparator set; (21) **no experimental structure covers residue 1002** — the UniProt PDB
cross-reference declaring "1-1050" for 5KHU/6TLJ is entity length, not modelled range
(C12); (22) ΔΔG **attempted and not obtained** — DDMut retrieval endpoint broken across
three API shapes.

### No edit required

- **The clinician one-pager.** It says the variant is "probably unstable… the published
  pattern for MVA variants sitting where this one sits" — already hedged, and it makes no
  structural claim. Nothing here contradicts it. *(If Edit 1 is taken, revisit whether
  "probably" is still the right word for a lay reader.)*
- **`pitch_script.md`.** Timed to 394 spoken words; makes no structural claim.
- **`pipeline/track2_scoring_rubric.md`.** Never edited — pre-registration provenance.

---

## From Task 4 — the nephrocalcinosis

Full finding: `literature/31_preterm_nephrocalcinosis.md`. Claims register **section I**.
Contradiction matrix **C13** (the adjudication) and **C14** (furosemide).

**These edits are to the Track 1 report, and they reverse a reversal.** Track 1 currently
argues that congenital onset *raises* the prior for a second monogenic renal cause. The
gestational-age-stratified evidence runs the other way: the monogenic yield is ~10× higher in
**full-term** children, and the recommendation to pursue monogenic causes is explicitly for
"full-term patients **without** known clinical risk factors." This proband is preterm, with
them.

**Read the adjudication before applying any of this.** The correction is that Track 1's
*inference* was backwards — **not** that the nephrocalcinosis is proven acquired. The imaging
date does not exist in any available file and recontact is prohibited, so that stays open
(**Q8**).

### Edit 6 — Track 1 report, the paragraph beginning "Congenital-onset nephrocalcinosis moves the prior in the opposite direction"

**File:** `submissions/track1/gummietech_track1_report.md`

**Current:**
> Congenital-onset nephrocalcinosis moves the prior in the opposite direction: it *raises*,
> not lowers, the probability of a monogenic renal or metabolic cause, since prenatal calcium
> deposition points toward an intrinsic tubular, metabolic or mineral-handling defect rather
> than an acquired insult.

**Proposed:**
> **That correction went one step too far, and the step is identifiable.** Withdrawing the
> claim that the acquired mechanisms were "each sufficient on its own" was right. Concluding
> that the genetic prior therefore *rises* does not follow, and the paediatric evidence runs
> the other way. In a stratified series of 464 children with nephrocalcinosis (Kim et al.
> 2023, `literature/31_...`), the monogenic yield was **~10-fold higher in full-term
> children** (OR 10.02, 95% CI 2.464–40.786, p = 0.001), and the authors recommend pursuing
> monogenic causes "especially in full-term patients **without known clinical risk factors**."
> This proband is preterm (HP:0001622) **with** known clinical risk factors, which is the
> profile associated with the *lower* yield.
>
> The premise is also weaker than this report treated it. *"Present since birth"* is one cell
> in a 2,750-character phenotype summary table written for a hackathon, not a clinical record,
> and it carries **no imaging date**. Preterm infants are not scanned at birth in any protocol
> in this literature: first scan at 1 month (Narendra 2001), diagnosis at 35 weeks corrected
> GA (Gilbert 2022), mean age at first diagnosis 385 days (Kim 2023). A summary clause is more
> likely to compress "identified in the neonatal period" than to date an observation to day 0.
>
> **What this report can honestly say is that it does not know.** If the finding truly were
> antenatal, the acquired mechanisms could not explain it and the monogenic prior would rise.
> The datum that would settle it is the date of the first renal ultrasound, which is not in
> any available file and which this analysis may not request.

**Why:** claims register I3, I4, I5, I6; matrix C13.

### Edit 7 — Track 1 report, the "materially weaker negative" sentence

**Current:** the 6-gene renal subset is "a **materially weaker negative** than this report
previously presented it as."

**Proposed:** keep the substance, drop the causal attribution to congenital onset. The panel
**is** 6 genes against ~30-gene commercial panels and that alone makes it non-exhaustive — the
honest reason, and one that does not depend on the timing question. Reframe the ~30-gene
recommendation as *reasonable but lower-yield in a preterm child with risk factors*, rather
than as correcting an error.

**Why:** I11 — the recommendation itself is not withdrawn.

### Edit 8 — Track 1 report, the withdrawn acquired mechanisms

Where loop diuretics are named, add that the association is **contested**: an adjusted OR of
1.26 (95% CI 1.02–1.57) in one VLBW case-control against a 32-study systematic review finding
"no evidence that furosemide exposure increases the risk," self-graded low strength. Furosemide
may be named as *a* plausible contributor, never as *the* mechanism — the original text was
overconfident in that direction too.

**Why:** I7; matrix C14.

### Edit 9 — Track 1 report, optional footnote on MVA renal phenotype

Kajii 1998's MVA/PCS patient had **renal cysts and Wilms tumour**, not nephrocalcinosis. This
is one case report and **not** the exhaustive cohort search Task 2 specifies, so it must be
cited as weak and non-exclusive, or left out until Task 2 runs.

**Why:** I9.

### No edit required

- **Track 1's factual statements** that NICU nephrocalcinosis develops over weeks and that the
  rhabdomyosarcoma came years later. Both correct; both survive.
- **The CASR MQ40 gap and the callability limit.** Untouched by this task.
- **The biochemistry recommendation** (serum/urine calcium, phosphate, magnesium, oxalate, PTH,
  1,25-vitamin D). Stands on its own merits regardless of how C13 resolves.
- **Anything in the Track 2 submission.** Task 4 touches Track 1 only.

---

## From Task 6 — surveillance after a first tumour

Full finding: `literature/32_surveillance_after_first_tumour.md`, **rewritten 2026-09-02 after
obtaining the primary source** (Hol et al. 2021, *Eur J Cancer* 153:51–63, CC-BY). Claims
register **section J**. Matrix **C15**, **C16**.

**Net effect: the surveillance section gets stronger, not weaker.** Reading the primary supplied
a risk figure the report does not have, corrected two things an earlier draft of this file got
wrong, and left the core Task 6 finding standing on firmer ground.

### Edit 10 — Track 2 report, surveillance section: add the risk figure and its provenance

**Proposed addition:**
> The primary recommendation quantifies the risk that justifies this protocol, and the figure is
> striking: **Wilms tumour has been reported in approximately 50% of patients with *BUB1B*
> variants** (Hol et al. 2021), against ~20% for *TRIP13* and none reported for *CEP57*. That is
> the highest Wilms risk in the guideline's "other syndromes" section. Two caveats travel with
> it: the estimate rests on small early case series (Jacquemont 2002, Hanks 2004), no
> denominator is given, and in a literature where patients are published because they developed
> tumours, ascertainment bias runs toward overestimation. The guideline's own framing is
> "because of the limited number of reported patients." Note also that the recommendation is
> anchored to **cytogenetically confirmed** MVA — which independently corroborates this
> project's decision to lead with karyotype as the confirmatory test.

**Why:** J6, J7. This is new quantitative content; Nakano's summary gives no figure.

### Edit 11 — Track 2 report: state what the protocol does not cover, and that the exclusion is deliberate

**Proposed addition:**
> **One limit has to travel with this protocol.** It is a *Wilms* surveillance programme, and
> this child has already had a rhabdomyosarcoma. The guideline does not address what
> surveillance becomes after a first malignancy; where it considers a prior tumour at all, it is
> a prior *renal* tumour, formerly a reason to prolong surveillance in *WT1*-related syndromes
> and since superseded by harmonising every syndrome to the 7th birthday. And the omission of
> non-renal surveillance is **explicit, not accidental** — the guideline states that "cancer
> surveillance for other tumour types is warranted in some of these conditions (but outside the
> scope of this guideline)." Nakano 2024 then adds only "regular clinical assessment including
> review of systems," with no modality, interval or endpoint. For this child the position across
> both sources is a well-specified renal protocol and, for everything else, clinical review with
> no protocol attached. **That is a documented gap in the evidence base, not a reason to depart
> from the protocol.**

**Why:** J2, J3, J12, J13.

### Edit 12 — Track 2 report: the age-7 endpoint is borrowed for MVA

**Proposed addition:**
> The 7th-birthday endpoint has a stated rationale — by age 7, 90% of sporadic Wilms tumours,
> 94% in Beckwith-Wiedemann and >95% in *WT1*-related syndromes have been diagnosed. But the
> guideline is explicit that "**for other CPS, the number of reported patients with WT was too
> small to determine this percentage**," and MVA is an "other CPS". **The endpoint applied to
> this child is therefore a harmonised convention borrowed from syndromes with larger case
> counts, not an MVA-derived figure.** The guideline is transparent about this; the report should
> be too.

**Why:** J4, J5. **Note:** an earlier draft of this file claimed no rationale was given. That was
wrong and came from reading only the summary. Do not carry that claim into the report.

### Edit 13 — Track 2 report: correct the tier of the radiation-avoidance claim, and decouple it from modality

**Proposed addition:**
> The recommendation to avoid radiation is **precautionary rather than MVA-specific**: a targeted
> search found no study of radiosensitivity in MVA, *BUB1B*-deficient or PCS-syndrome patients,
> and the guideline's supporting sentence is a class statement — "**many** of these genomic
> instability disorders also present with exquisite sensitivity" — which names
> ataxia-telangiectasia and Nijmegen breakage syndrome but not MVA. It remains sound as
> precaution and on the general position that no low-dose threshold is agreed. **Separately, do
> not present ultrasound as a compromise forced by radiosensitivity:** the guideline judges
> ultrasonography "equally effective for initial WT detection" compared with CT or MRI. The
> modality choice and the radiation-avoidance advice are independent.

**Why:** J8, J10, J11; matrix C16. The class-generalisation flag is the same move the report
criticises elsewhere, appearing inside a recommendation it endorses.

### Edit 14 — Track 2 report, Sources: cite the primary directly

Replace the second-hand citation. The recommendation now has a primary source that was read:
**Hol JA, Jewell R, Chowdhury T, Duncan C, Nakata K, Oue T, et al., *Eur J Cancer*
2021;153:51–63, PMID 34134020, CC-BY.** Nakano 2024 remains cited as the AACR endorsement.

**Why:** J14; matrix C15.

### Edit 15 — clinician one-pager, surveillance section

**Proposed addition** below the existing bullets:
> **Two things worth knowing about this list.** The reason it exists is a real risk: in children
> with MVA caused by *BUB1B* changes, kidney tumours have been reported in around half of
> published patients — though that figure comes from a small number of early reports and is
> likely an overestimate. And it was written as a *kidney-tumour* screening programme for young
> children. Because this child has already had a rhabdomyosarcoma, the situation is one the
> published guidance does not directly cover: it does not say whether screening should change
> after a first tumour, and it deliberately leaves screening for non-kidney tumours outside its
> scope. That is a gap in what has been studied, not a reason to do less — and it is a
> reasonable thing to raise with the treating team.

**Why:** J2, J6, J12. This is the artefact a family or clinician acts on.

### Edit 16 — Track 2 report, Part 11 verification table

Add rows: (23) **Hol 2021 primary obtained and read** as the version of record via OpenAlex →
Cambridge/Utrecht repository deposits, after Europe PMC's `isOpenAccess: N` was misread as
"closed"; (24) MVA section of Hol 2021 and Nakano 2024 both read end to end — **silent on
post-first-tumour surveillance**, with the non-renal exclusion explicit in the primary;
(25) MVA-specific radiosensitivity search returned **five records, all wrong-product**;
(26) NCBI elink returns a **false PMCID** for Hol 2021 (C15) — fourth identifier trap.

### Do not do

- **Do not import the Li-Fraumeni protocol.** Cited only as precedent for the *shape* of
  non-ionising surveillance. LFS is a dominant single-gene syndrome with a large evidence base;
  MVA has under 50 described patients. (J15)
- **Do not recommend deviating from the AACR/SIOP-E protocol.** It remains the best available
  guidance and the report should continue to lead with it.
- **Do not claim COG LTFU v6.0 covers MVA.** Not retrieved — survivorshipguidelines.org did not
  resolve from this environment. (J16, Q9)
- **Do not state the ~50% figure without its caveats.** Small series, no denominator,
  ascertainment bias. (J6)

---

## From Tasks 2, 3 and 5

Not started.
