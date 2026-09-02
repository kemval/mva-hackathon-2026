# Structural analysis of BUB1B p.Asn1002Lys

**Task 1 of `pipeline/gap_closure_brief.md`.** Generated 2026-09-02. Reproduce with
`python3 pipeline/structural_analysis.py`.

**Headline: the result is mixed, and the disconfirming half is the more important half.**
N1002 has a specific, describable structural role and a chemically severe substitution. But
the tolerated same-domain counterexample the report already cites, `Q921H`, turns out to be
**structurally indistinguishable from N1002 by every measure computed here** — more buried,
also hydrogen-bonded, same domain. Position-based reasoning therefore has a documented
failure in this exact protein, and this analysis does **not** license a stronger statement
of the mechanism than the report already makes.

## Why this was done

The Track 2 thesis is that this variant **lowers BubR1 abundance**. Limitation 1 concedes
that is *probable by analogy, not demonstrated*. The in-silico evidence already held —
AlphaMissense 0.92, CADD 24.5, REVEL 0.472 — predicts **pathogenicity**, a different
quantity from **destabilisation**. Nothing in the repository had looked at where residue
1002 actually sits.

Comparators are the MVA alleles **Suijkerbuijk et al. 2010** assayed for protein level,
split by their measured result, so structure is calibrated against alleles with a known
abundance phenotype rather than asserted in isolation.

---

## The model, and its first limit

`AF-O60566-F1` **v6** (2025-08-01). **pLDDT at residue 1002 = 91.1**; the window 990–1015
averages 91.5, against 63.6 for the whole protein. The geometry here is in the model's
confident regime — not guaranteed, since 1002 is 48 residues from the C-terminus.

**No experimental structure covers this residue.** Of nine PDB entries cross-referenced to
O60566, the X-ray structures cover 57–220, 647–720, 663–681 and 20–42 — none reaches the
pseudokinase domain. Two cryo-EM entries **declare** chains spanning "1-1050", but the
observed residues are **6TLJ: 19–345** and **5KHU: 26–479**. The declared range is the
entity length, not what was modelled.

> Third instance of the identifier/metadata trap already logged twice here (C7). Taking the
> cross-reference at face value would have produced a claim of experimental structural
> support that does not exist. Logged as **C12**.

**Every structural number below is predicted, not measured.**

---

## What N1002 is

A **buried polar residue whose side chain cross-links two backbone segments** — three
hydrogen bonds, all to backbone atoms of residues distant in sequence:

| bond | distance |
|---|---|
| Asn1002 **OD1** ← Trp978 backbone **N** | 2.83 Å |
| Asn1002 **ND2** → Val998 backbone **O** | 2.83 Å |
| Asn1002 **ND2** → Trp978 backbone **O** | 2.95 Å |

It sits in a **loop between two helices** (994–999 and 1008–1011 helical), in an aromatic
pocket — Phe977 4.6 Å from CB, Trp978 5.1, Phe997 6.0, Trp973 6.5, Phe954 7.6. Solvent
accessibility 16.2% (SASA 31.5 Å²).

**Asn→Lys is chemically severe here.** Lysine has no hydrogen-bond *acceptor*, so the
OD1←Trp978 bond is lost outright rather than repositioned; the side chain is two carbons
longer in a pocket lined by four aromatics; and it carries an **obligate positive charge**
into a partially buried, uncompensated environment.

Conservation is consistent: **phyloP 4.87** (100-way vertebrate) and **5.12** (470-way
mammalian), **phastCons 1.0** in both, GERP++ 3.99, PROVEAN −3.89, VEST4 0.885. **Primate
phyloP is only 0.665** — much weaker at the shallow end.

---

## The one clean positive: the tolerated neighbour is on the surface

**`p.Asn1004Ser` — two residues away, gnomAD AF 6.0e-4, AC 974 — is surface-exposed
(RSA 53.0%)**, while the candidate at 1002 is buried and hydrogen-bonded, 5.5 Å away.

This bears on Track 1's **PM1 rejection**, which stands and is not disturbed: the domain
genuinely is not depleted of missense variation (1.12 vs 1.25 variants per residue). But
that establishes only that *the domain* is not a hotspot. The standing variation Track 1
cited sits on the surface; the candidate does not. Both are true at once.

---

## Four findings that cut against the thesis

### 1. Q921H — the report's own counterexample is structurally indistinguishable

This is the decisive result. `Q921H` was "indistinguishable from wild-type" in
Suijkerbuijk's abundance assay, and the report already cites it as the counterexample that
keeps Limitation 1 honest. Structurally it is **not** the exposed, unremarkable residue that
would explain its tolerance:

| | RSA | side-chain H-bonds | pLDDT | domain |
|---|---|---|---|---|
| **N1002** (candidate) | 16.2% | **3** | 91.1 | pseudokinase |
| **Q921** (tolerated) | **1.1%** | **2** | 83.2 | pseudokinase |

Q921 is **more buried than N1002**, also makes buried side-chain hydrogen bonds, and sits in
the same domain 26.0 Å away. Every structural feature this analysis uses to argue N1002 is
important is **also present at a position where substitution demonstrably did nothing to
protein level.**

The only surviving distinction is **substitution chemistry**: Gln→His is conservative — His
retains both donor and acceptor capability at similar bulk — whereas Asn→Lys loses the
acceptor entirely and introduces a buried charge. That distinction is real, but it is a
weaker and more post-hoc claim than "this position is structurally critical", and it is
**not** what the report currently argues.

### 2. Substitution class does not separate the groups either

`R814H` is also a conservative Arg→His substitution and **is** destabilising. So the
chemistry rule that rescues Q921H fails on R814H. Across all eight calibration alleles —
four destabilising, four tolerated — **no single structural or chemical feature computed
here separates the two groups.**

### 3. N1002 is not unusually buried for this domain

The pseudokinase domain has median RSA 15.6% and 58% of residues below 20%. At 16.2%, N1002
is the **51st percentile** — almost exactly median. Burial distinguishes nothing here.
`Y155C` is the most buried residue in the set (**RSA 0.9%**) and did **not** lower protein
level. "Buried ⇒ destabilising" is false, and Suijkerbuijk's own controls prove it.

### 4. The 3D clustering test returns nothing usable

| allele | CA–CA from N1002 | measured effect on protein level |
|---|---|---|
| L1012P | 12.3 Å | destabilising — *abundance rescue restored checkpoint* |
| I909T | 24.4 Å | destabilising — *abundance rescue restored checkpoint* |
| **Q921H** | **26.0 Å** | **no effect** |
| R814H | 28.0 Å | destabilising |
| R727C | 32.5 Å | destabilising |
| Y155C | 82.0 Å | no effect |
| R550Q | 90.7 Å | no effect |

The destabilising alleles are distributed at 10–33 Å, not clustered — and **Q921H sits at
26 Å, inside that band.** The apparent separation (everything ≤33 Å is destabilising,
everything ≥82 Å is not) collapses once Q921H is included: what remains is only that alleles
in the same domain are near each other and alleles in other domains are far. That is a
restatement of the domain boundary, not a finding.

**"The destabilising alleles cluster in 3D and N1002 sits among them" is not supported and
must not be asserted.**

---

## ΔΔG — not obtained

**No stability-specific ΔΔG was produced, and none is claimed.** DDMut accepted two
submissions (HTTP 200, jobs `17883629491989634` full-length and `17883630984480202`
domain-trimmed, 2026-09-02) but every retrieval path failed: `GET ?job_id=` returned
`Internal Server Error` on six polls across both jobs; `POST` with `job_id` was rejected as
`Unknown arguments: job_id` when required fields were supplied, and demanded those fields
when they were not. DynaMut2 returned HTTP 400 to a bare probe. No FoldX or Rosetta locally.

Per the brief's pre-commitment: **inspection is reported as inspection.** A prediction that
was not obtained is not a prediction that is held.

---

## Verdict against the pre-committed limit

The brief pre-committed that this task **cannot** reach "demonstrated". It does not — and it
falls further short than anticipated.

What it delivers is a **specific, falsifiable mechanism** where the report previously had
only positional analogy: loss of a buried bidentate hydrogen bond to two backbone segments,
plus a buried positive charge in an aromatic pocket, at a position with high mammalian
constraint. That is worth having, because it is testable.

What it also delivers — and this is the more consequential half — is a **demonstration that
same-domain structural reasoning fails in this protein.** The tolerated counterexample the
report already cites is more buried and equally hydrogen-bonded. Any argument of the form
"N1002 is buried and makes hydrogen bonds, therefore substitution destabilises" is refuted by
Q921 before it is made.

**Net effect on Limitation 1: it should be tightened, not relaxed.** The mechanism is now
stated more precisely, and the evidence that it applies to *this* variant is no stronger than
before. Evidence tier unchanged: **in silico**. Only the BubR1 western blot
(`literature/_open_questions.md` Q1) can settle it, and this analysis raises rather than
lowers the value of running it.

## Evidence tier

**In silico**, on a predicted structure with no experimental coverage of the residue. No
human data, no cell data, no ΔΔG. Generates **no** ACMG PS3 evidence — PS3 requires a
functional assay, which is precisely what Q1 proposes. Variant 2 remains a VUS.
