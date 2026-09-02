# Pending submission edits — written, not applied

Findings from `pipeline/gap_closure_brief.md` imply the edits below. **None has been
applied.** The submission text moves only after review, per the brief's deferred-edit rule.

Status: **Task 1 complete. Tasks 2–6 not started.**

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

## From Tasks 2–6

Not started.
