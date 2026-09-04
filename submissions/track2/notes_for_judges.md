# Notes for judges

*For the optional "Notes for judges" field on the Track 2 submission form. Paste the
body below, or read it here.*

---

Three things in this repository are worth a judge's time more than the ranked candidate
list, because they are what the list rests on.

**1. The pre-registration is verifiable, not asserted.** The scoring rubric with its four
exclusion gates was committed at `20eda20` on 2026-09-02, **before** any drug database was
queried and before any candidate list existed. `git log` shows the order. The rubric has
never been edited since — refinements are recorded in the report as dated
post-registration clarifications precisely so the commit stays clean.

**2. We tested our own headline generalisation and it partly failed.** The report claimed
the loss-of-function/inhibitor mismatch is "a fact about every loss-of-function rare
disease." We pre-registered that as a falsifiable prediction (`pipeline/scalability_
prediction.md`, commit `98b9b04`), including a written commitment to **withdraw rather than
soften** if it failed at NPC1 — then ran the same pipeline on NPC1, ATM and CFTR, with tier
assignment done mechanically by network distance rather than curated, because curation was
the obvious attack on the original result.

Two of three predictions failed. NPC1 measured **54.5%** inhibitory against a predicted
≥80%. The monotonic rise with distance did not survive the mechanical rule and failed even
for BUB1B itself. **The claim is withdrawn.** What replaces it is narrower and more useful:
the skew tracks whether the causal gene sits in a pathway oncology has invested in
inhibiting (BUB1B **95.8%**, ATM **93.4%**) rather than whether the disease is
loss-of-function (NPC1 **54.5%**, CFTR **37.5%**). That rule is diagnostic — it says in
advance which rare diseases face this problem — and it makes this child's position worse,
not better.

A note on how those percentages are counted, because we got it wrong once. They use unique
`(gene, drug, action_type)` triples — the same unit as the report's own `129/142`. Our first
pass counted raw rows and printed the result beside the report's figure as though the two
were comparable; they were not. `scale_measure.py --selfcheck` now re-derives the report's
`129/142` and fails loudly before emitting any other number. Correcting it changed no
verdict and **widened** the split.

A finding worth flagging on its own: **all ten action-typed compounds against ATM are
inhibitors, in a disease of ATM deficiency.** The same trap we identified for MVA is
sitting unremarked in ataxia-telangiectasia.

**3. The verification table lists 42 findings that each changed the submission**, and
several cut against its own thesis. The structural analysis commissioned to *support* the
central claim weakened it and Limitation 1 was tightened as a result. The mouse models the
lead candidate rests on turn out not to carry the human MVA genotype. A standing overclaim
of our own about the coverage limitation was withdrawn. Five identifier/duplicate traps
were caught, one of which would have double-counted a patient in the cohort table.

**The last seven rows are a closing numeric audit of Track 2, and its result has a shape
worth naming.** Every figure in the report was re-derived from the committed artefacts —
the drug tallies, all six tier counts, every trial row, all ten ranking totals and fifty
axis scores, the pharmacogenomic counts, and all sixteen scalability figures. **All
reproduce; not one number changed.** Every defect the audit found was instead a *sentence*
that had outrun its number, and three of the six were the same failure: a correction the
report had already made to itself never reached the files that quote it. The withdrawn
loss-of-function generalisation was still live in the methods-description form, the README
and the visual explainer. A Track 1 inference that Track 1 had withdrawn was still standing
in Track 2's phenotype table. And one claim — "the lowest minimum age across the entire
senolytic trial landscape is 18" — was refuted by the table printed immediately above it,
which records six paediatric-eligible navitoclax trials with minimum ages down to 1 year.

That is a finding about this kind of work rather than about this repository. **Verification
that runs on figures does not catch prose, and correction does not propagate on its own.**
The figures here that are checked by a script — `129/142`, the pitch script's word counter —
were all correct. The ones copied by hand between files were the ones that had gone stale.

So the fix is not another hand-copied number. `pipeline/check_consistency.py` now fails
loudly if any withdrawn claim is *asserted* in a reader-facing file, or if any cross-file
figure stops matching the source it names. It is one command and it is the check we did not
have.

**On the two things we did not do.** Seven national literature databases (CiNii, J-STAGE,
J-GLOBAL, KAKEN, CNKI, Wanfang, VIP) and the Japanese/Chinese native-script search terms
were **not** queried; the fetch log says so as prominently as it records its successes. And
no coverage track was produced — but the reason is now stated correctly, which it was not
before: it is feasible by a reduced-reference route we did not run, at named costs, and it
is scientifically sound for BUB1B (zero segmental duplications) while unsound for CYP2D6
(six, including a 97%-identity pair).

**What we would actually do first, if this were a clinic rather than a hackathon, is not
prescribe anything.** It is a western blot for BubR1. If the protein is absent, our entire
top tier is futile, and we would want to know that before anyone gives a child anything.
