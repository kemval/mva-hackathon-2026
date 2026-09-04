# Pipeline — Track 1

Two scripts plus `bcftools`, run once per gene panel. Everything is parameterised
by CLI argument, so no file needs editing to re-run this in another environment.

**No patient data is committed to this repository.** The inputs and outputs below
live under `data-notes/raw/` and `data-notes/annotated/`, both gitignored per the
hackathon's Data Transfer Agreement — see `../data-notes/README.md`. Reproducing
this analysis requires obtaining your own authorized access to the dataset through
Hugging Face's gated-access flow.

## Prerequisites

- `bcftools` (region restriction and genotype extraction)
- Python 3 (standard library only — no third-party packages)
- The proband VCF and its `.tbi` index in `data-notes/raw/`

All commands below are written to be run **from this `pipeline/` directory** (hence the
`../data-notes/...` paths). Run them from the repository root instead and the paths
become `data-notes/...` with the scripts as `pipeline/vep_annotate.py`.

## 0. Gene panel coordinates

Gene body coordinates were resolved via the Ensembl REST `lookup/symbol` endpoint
against GRCh38 and padded by ±2kb to capture near-splice and UTR-proximal variants:

```bash
curl -s "https://rest.ensembl.org/lookup/symbol/homo_sapiens/BUB1B?content-type=application/json"
```

The captured coordinates and the derived padded BED files are committed (they are
public reference-genome positions, not patient data):

- `../data-notes/regions/mva_gene_panel_grch38.tsv` / `mva_gene_panel_padded.bed` — 9-gene primary MVA panel
- `../data-notes/regions/secondary_panel_grch38.tsv` / `secondary_panel_padded.bed` — 11-gene phenotype-driven secondary panel

Note that both BED files use unprefixed contig names (`15`, not `chr15`), matching
the contig naming in the provided VCF. The submission CSV uses the `chr15` form the
hackathon's published schema specifies.

## 1. Region-restrict the genome-wide VCF

Avoids annotating ~2M+ genome-wide records; uses the provided `.tbi` index.

```bash
bcftools view -R ../data-notes/regions/mva_gene_panel_padded.bed \
  -O z -o ../data-notes/mva_panel_variants.vcf.gz \
  ../data-notes/raw/WGS_EX2312012_HGWCNDSX7.vcf.gz
bcftools index -t ../data-notes/mva_panel_variants.vcf.gz

bcftools view -R ../data-notes/regions/secondary_panel_padded.bed \
  -O z -o ../data-notes/secondary_panel_variants.vcf.gz \
  ../data-notes/raw/WGS_EX2312012_HGWCNDSX7.vcf.gz
bcftools index -t ../data-notes/secondary_panel_variants.vcf.gz
```

Yield: 1288 records / 1281 PASS (primary panel), 1065 PASS (secondary panel).

## 2. Annotate via Ensembl VEP REST

Canonical transcript, HGVS nomenclature, max gnomAD subpopulation AF (genomes and
exomes), **max SpliceAI delta score**, ClinVar significance, and protein domains.
Batches of 150 with rate-limit spacing. Raw JSON responses are written alongside the
TSV as an audit trail.

SpliceAI comes from VEP's own plugin (`&SpliceAI=1` in `VEP_URL`), which is worth
knowing: the Broad's standalone SpliceAI Lookup API was unreachable across three
separate attempts, and Ensembl serves the same scores through the endpoint this
pipeline already calls. The `spliceai_max_ds` column is the max of the four delta
scores (DS_AG, DS_AL, DS_DG, DS_DL) across transcripts. It is **blank, not 0.00,
where SpliceAI has no data** for the position — the precomputed set does not reach
every position (227 indels and 365 SNVs across the two panels come back empty,
predominantly intronic, downstream and upstream), and "not scored" is a different
claim from "scored zero".

```bash
python3 vep_annotate.py \
  --vcf     ../data-notes/mva_panel_variants.vcf.gz \
  --out-tsv ../data-notes/annotated/vep_panel_annotated.tsv \
  --out-raw ../data-notes/annotated/vep_raw_responses.jsonl

python3 vep_annotate.py \
  --vcf     ../data-notes/secondary_panel_variants.vcf.gz \
  --out-tsv ../data-notes/annotated/vep_secondary_annotated.tsv \
  --out-raw ../data-notes/annotated/vep_secondary_raw_responses.jsonl
```

## 3. Filter to rare + damaging

```bash
python3 filter_candidates.py --tsv ../data-notes/annotated/vep_panel_annotated.tsv
python3 filter_candidates.py --tsv ../data-notes/annotated/vep_secondary_annotated.tsv
```

Expected output: **2 candidates** from the primary panel (both BUB1B —
`15:40209701 T>G` p.Leu737Ter and `15:40220612 T>G` p.Asn1002Lys) and **0** from
the secondary panel. These two rows are the primary finding in the submission.

## 4. Surface the deep-intronic secondary row

The deep-intronic secondary finding (`15:40216470 A>G`) is MODIFIER impact, so it does
not pass the step-3 filter by design — that filter exists to discard intronic variants.
It is recovered by re-running the same script at MODIFIER impact and restricting to the
gene carrying the primary finding:

```bash
python3 filter_candidates.py \
  --tsv ../data-notes/annotated/vep_panel_annotated.tsv \
  --impacts MODIFIER | awk -F'\t' 'NR==1 || $5=="BUB1B"'
```

Expected output: **1 row**, `15:40216470 A>G` (`c.2679-1026A>G`, `gnomad_max_af` blank —
VEP carried no gnomAD frequency, and a direct gnomAD v4 query returns "Variant not found" —
`spliceai_max_ds` 0.00).
The rarity filter leaves 10 MODIFIER variants across the nine-gene panel (spread over
MAD1L1, BUB1, SLF2, BUB1B and BUB3), of which exactly one is in BUB1B — so this is a
narrow, stated query, not a hunt through intronic space until something interesting
appears.

Every row in the submitted CSV therefore traces to a command in this file: CSV row 1
(the compound-heterozygous pair, both variants) from step 3, CSV row 2 (the secondary
finding) from step 4.

## 5. Panel-wide splice screen

Because deep-intronic and pseudoexon variants are MODIFIER impact and so never reach the
step-3 candidate list, the whole annotated set is screened separately for splice impact:

```bash
for t in vep_panel_annotated vep_secondary_annotated; do
  awk -F'\t' 'NR>1 && $11!="" && $11+0>=0.2' ../data-notes/annotated/$t.tsv
done
```

Expected output: **nothing**. No variant in either panel reaches SpliceAI's 0.2
high-recall threshold. For the record, as run on 2026-08-31:

| Panel | PASS variants | SpliceAI-scored | Max delta | ≥ 0.2 |
|---|---|---|---|---|
| Primary (9 genes) | 1281 | 1007 (78.6%) | 0.18 | 0 |
| Secondary (11 genes) | 1065 | 747 (70.1%) | 0.13 | 0 |

The 0.18 maximum is a common MAD1L1 intronic polymorphism (gnomAD AF 0.77); among the
14 rare (AF<0.001) scored variants across both panels the maximum is 0.03. The `$11!=""`
guard matters: blank means SpliceAI has no data for that position, which is not the same
as a score of zero and must not be counted as a pass.

## 6. What the dataset actually contains, and why no coverage track exists

**Checked against the repository manifest on 2026-09-01, not against the hackathon site's
description of it.** The two disagree, and the manifest wins.

The site says raw sequencing data is available "optionally in BAM/CRAM". It is not. The dataset is
**13 files totalling 79 GB**, and 78.9 GB of that — 99.7% — is raw FASTQ:

| files | size | status |
|---|---|---|
| `WGS_EX2312012_HGWCNDSX7.vcf.gz` + `.tbi` | 0.29 GB | already held; this analysis runs on it |
| `Challenge_Clinical_Phenotype_1.docx`, `README.md` | < 0.1 GB | already held |
| `*_S16_L00{1,2,3,4}_R{1,2}_001.fastq.gz` | **78.9 GB** | 8 files, 4 lanes, paired-end |

```bash
# reproduce the manifest (no auth needed for the file list)
curl -s https://huggingface.co/api/datasets/SageBio/mva-hackathon-2026-data/tree/main \
  | python3 -m json.tool | grep '"path"'
```

**There is no BAM and no CRAM.** So the coverage track that would close this report's largest
limitation — the sites-only VCF cannot distinguish absence of a call from absence of coverage —
does not exist in the dataset and cannot be sliced out of it. Producing one means aligning the FASTQ
yourself: ~79 GB of transfer, a GRCh38 index, and a full 30x WGS alignment.

**That is not attempted here — but the reason previously given for not attempting it was wrong, and
is corrected.** This README used to argue that the whole route was infeasible because a human-genome
BWA index needs ~6-7 GB of RAM (minimap2 ~11 GB, bwa-mem2 ~40 GB) against 8 GB installed. **You do
not need a whole-genome index.** A reduced reference containing only the panel and PGx regions has an
index around 30 MB, and the RAM objection does not apply to it at all.

The honest re-costing is in `realignment_feasibility.md`. In short: the real costs are ~79 GB of
transfer, streaming (20 GB free disk, re-measured 2026-09-04, cannot hold the input), and a multi-day
run on 8 cores — because the aligner must examine every read regardless of how small the reference
is. All three dissolve on a larger machine. The binding objection is instead **scientific**: a
decoy-free targeted reference inflates MAPQ, because a read from a paralogue elsewhere has nowhere
else to map and lands confidently on the only copy present. Queried live against UCSC
`genomicSuperDups`, **BUB1B has zero segmental duplications in its gene body or padded region**, so
for the callability question the route is sound; **CYP2D6 has six, including a 97.0%-identity 9 kb
pair**, so for the pharmacogenomic question it is not.

So the limitation is **not closed, and is differently open** than this repository previously stated:
feasible by a route this analysis did not run, at named costs and with one named failure mode that
applies to the PGx half and not the BUB1B half. The report therefore continues to state the
callability limitation rather than measure it, and uses call-density-against-flanking-sequence as an
explicitly labelled proxy.

### `coverage_analysis.py`

Kept because it is correct and needs no download to be worth reading: it specifies exactly what would
settle the question if an alignment ever existed. Given any BAM covering the panel it reports
callable fraction per gene, tests each of the six permissive deletion windows against BUB1B's own
diploid baseline (a hemizygous deletion halves depth), and prints the BUB1B depth profile in 1 kb
bins.

```bash
python3 coverage_analysis.py --bam <alignment.bam>
```

### `deletion_windows.py`

Derives the permissive multi-exon-deletion windows instead of asserting them. The report bounds a
hemizygous BUB1B deletion to the intervals *between* the proband's heterozygous calls, since a het
call is positive evidence of diploidy at that position. That list used to live in prose, with
`coverage_analysis.py` carrying a hardcoded copy of it — so when the list was short by one window,
neither artefact could catch it, and two audit passes that checked *the windows listed* against the
Ensembl exon structure did not, because both took the list as given.

This script reads the het calls from the region-restricted VCF, pulls the canonical transcript's
exons from Ensembl, and emits every inter-het interval that fully contains a coding exon, with the
summed CDS length and whether a whole-window deletion would be in-frame. The frame column is not
decoration: the report lowers the prior on a deletion in trans on the grounds that it would produce
a truncating/truncating genotype, and an in-frame deletion would not.

```bash
python3 deletion_windows.py --vcf ../data-notes/mva_panel_variants.vcf.gz
```

Output (2026-09-04) — six windows, three of them in-frame:

```
# BUB1B 15:40160984-40221137  het calls: 8 padded / 7 in gene body
interval                 size_bp  complete_coding_exons  cds_nt  frame
40,160,984-40,168,264      7,280  exons 1-2                 179  frameshift
40,168,264-40,181,093     12,829  exons 3-5                 402  in-frame
40,182,809-40,192,892     10,083  exons 6-8                 477  in-frame
40,192,892-40,209,701     16,809  exons 9-16               1085  frameshift
40,209,701-40,216,470      6,769  exons 18-20               394  frameshift
40,216,470-40,220,612      4,142  exons 21-22               279  in-frame
```

`WINDOWS` in `coverage_analysis.py` is regenerated from this, not edited by hand.

**What it could never resolve**, so it is not oversold: phase. The two variants are ~11 kb apart,
beyond short-read fragment span, and read-backed phasing faces the identical physical limit. Nor the
MVA diagnosis, which needs a karyotype that is not in the dataset in any form.

## Notes on the gnomAD AF field

Two distinct defects were found in this field, at different times. Both were permissive
rather than exclusionary — each could only admit a variant to the candidate list, never
remove one — and neither changed the result.

**1. Missing exome frequencies (found and fixed first).** The `max_gnomad_af()` version
that produced the *original* annotation run excluded gnomAD *exome* frequencies. Replaying
the corrected computation offline against the saved raw VEP responses gave an identical
candidate set for both panels, and the point is moot in any case: the SpliceAI
re-annotation regenerated both TSVs from scratch with the corrected function.

**2. Blank conflated with zero (found later, in the review pass).** `max_gnomad_af()`
returned `0.0` both when gnomAD recorded an allele at frequency zero and when VEP attached
no gnomAD frequency at all — the same blank-vs-zero conflation this pipeline documents
avoiding for SpliceAI, sitting undisclosed in the AF column. It returns `None` now and the
column is **blank where the frequency is unknown**, matching `spliceai_max_ds`. Exactly two
rows change, both in BUB1B and both variants this submission reports:
`15:40220612` (p.Asn1002Lys, true AF 6.84e-7) and `15:40216470` (absent from gnomAD),
each previously written as `0.000000`.

`filter_candidates.py` now handles blank explicitly. **Blank is kept, not dropped**, and a
note is written to stderr prompting direct verification. The reasoning: absence from a
population database is evidence *for* rarity in a rare-disease search, so dropping such
rows would be exclusionary and could discard a true ultra-rare causal allele — which is
not hypothetical, since p.Asn1002Lys is one of the two affected rows. This is deliberately
the opposite call from the *unparseable*-AF branch, which drops: a blank means the source
had nothing to say, whereas an unparseable value means the field is corrupt and the row
cannot be trusted at all.

The candidate set is unchanged by both fixes (primary 2, secondary 0), verified by
replaying the shipped corrected function against
`data-notes/annotated/vep_*raw_responses.jsonl`. Full detail is in the `max_gnomad_af`
docstring and the submission report's Verification table.

---

# Pipeline — Track 2

Four scripts. Two query public drug/trial databases, one applies the pre-registered
scoring rubric, and one runs a CPIC-guided pharmacogenomic screen against the proband's
own genome. As with Track 1, everything is CLI-parameterised and no patient data is
committed.

## Prerequisites (Track 2)

- Python 3, standard library only (the drug-search and scoring scripts)
- For the PGx screen only: `bcftools`, `bgzip`, `tabix`, `samtools`, Java 17+,
  the PharmCAT v3.4.0 pipeline bundle, and a GRCh38 FASTA (bgzip-compressed,
  faidx-indexed, chr-prefixed contigs)

## 7. Pre-register the scoring rubric — before anything else

`track2_scoring_rubric.md` was written and committed **before any query was run**
(commit `20eda20`). The commit order is the guarantee that the rubric was not
reverse-engineered around a favoured candidate, and it is checkable:

```bash
git log --oneline --follow pipeline/track2_scoring_rubric.md
git log --oneline --diff-filter=A -- data-notes/track2_target_drugs.tsv
```

## 8. Search the pathway node set for drugs

Queries Open Targets (GraphQL v4) and DGIdb (GraphQL) for every node in the table, and
records each target's tractability assessment alongside its drug count.

```bash
python3 track2_target_search.py \
  --nodes ../data-notes/regions/track2_pathway_nodes.tsv \
  --out ../data-notes/track2_target_drugs.tsv \
  --raw-log ../data-notes/track2_search_raw.jsonl
```

Yield: 1,716 gene-drug rows across 24 genes. Open Targets returns **zero** drugs for
BUB1B, BUB1, BUB3, MAD1L1, MAD2L1, CDC20, SIRT2, NMNAT1, CGAS, CDKN2A and CDKN1A.

Note the script raises rather than returning empty on a schema error: Open Targets
renamed `knownDrugs` to `drugAndClinicalCandidates`, and a script that swallowed that
error would silently report no drugs for every gene.

## 9. Retrieve trial evidence, with paediatric eligibility

```bash
python3 track2_trial_evidence.py \
  --candidates ../data-notes/track2_candidates.tsv \
  --out ../data-notes/track2_trials.tsv
```

Paediatric eligibility is read from each trial's structured eligibility module
(`minimumAge`, `stdAges`), never from free text. Yield: 888 trial rows. Zero of the 22
dasatinib+quercetin trials enrol anyone under 18.

## 10. Apply the rubric

Judgement lives in `../data-notes/track2_scores.tsv`, where every axis score carries a
written justification. This script does only the mechanical part — gates, sum, declared
tie-break, two rankings.

```bash
python3 track2_score_candidates.py \
  --scores ../data-notes/track2_scores.tsv \
  --candidates ../data-notes/track2_candidates.tsv \
  --out ../data-notes/track2_ranking.tsv
```

Highest overall: nicotinamide riboside (13), a supplement. Highest approved medication:
dasatinib + quercetin (10). Three candidates excluded by hard gate.

## 11. Pharmacogenomic screen (requires the patient VCF)

Runs PharmCAT twice — strict, and with `--missing-to-ref` — and compares. The comparison
is the deliverable, not either run alone.

```bash
./track2_pgx_screen.sh \
  /path/to/pharmcat-pipeline-3.4.0 \
  /path/to/GRCh38.chr.fa.bgz \
  ../data-notes/raw/WGS_EX2312012_HGWCNDSX7.vcf.gz \
  ../data-notes/pgx
```

Outputs go to `data-notes/pgx/`, which is **gitignored** — these are derived patient
genotype data, excluded for the same DTA reason as `data-notes/raw/`.

Result on this proband: only 22 of 1,226 PharmCAT positions carry a variant call, and
**16 of 23 genes change their call** between the two assumptions. Every "Normal
Metabolizer" call for TPMT, NUDT15, UGT1A1, CYP2C9 and SLCO1B1 exists only under the
assumption PharmCAT's own CLI labels "DANGEROUS!".

The reference FASTA must be bgzip-compressed with chr-prefixed contigs. Ensembl ships
plain gzip, so it needs recompressing:

```bash
zcat < Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz \
  | sed 's/^>\([0-9XYMT]*\) />chr\1 /' | bgzip -@ 4 -c > GRCh38.chr.fa.bgz
samtools faidx GRCh38.chr.fa.bgz
```

The comparison step can also be run standalone against existing PharmCAT output:

```bash
python3 track2_pgx_compare.py \
  --strict   ../data-notes/pgx/strict/proband_strict.phenotype.json \
  --missing-to-ref ../data-notes/pgx/missing_to_ref/proband_mtr.phenotype.json
```

---

## 8. Scalability replication (Part 8)

Tests the report's own generalisation on three further diseases. The prediction was
committed **before** any query here ran (`scalability_prediction.md`, commit `98b9b04`);
`track2_scoring_rubric.md` is untouched, since its pre-registration argument depends on it.

Node sets are built **mechanically** from STRING network distance rather than curated,
because curation is the obvious objection to a generalisation drawn from a hand-picked
gene set. The same rule is re-applied to BUB1B so the original result is re-derived
without its own curation.

```bash
# 1. build a distance-tiered node set for any causal gene
#    d0 = the gene, d1 = STRING partners (score >= 700), d2 = partners of partners
for g in NPC1 ATM CFTR BUB1B; do
  lc=$(echo $g | tr 'A-Z' 'a-z')
  python3 build_node_set.py --gene $g --out ../data-notes/regions/scale_${lc}_nodes.tsv
done

# 2. run the UNMODIFIED Track 2 search over each
mkdir -p ../data-notes/scale
for g in npc1 atm cftr bub1b; do
  python3 track2_target_search.py \
    --nodes   ../data-notes/regions/scale_${g}_nodes.tsv \
    --out     ../data-notes/scale/${g}_target_drugs.tsv \
    --raw-log ../data-notes/scale/${g}_search_raw.jsonl
done

# 3. measure the two pre-registered quantities
for g in npc1 atm cftr bub1b; do
  G=$(echo $g | tr 'a-z' 'A-Z')
  python3 scale_measure.py --drugs ../data-notes/scale/${g}_target_drugs.tsv \
    --nodes ../data-notes/regions/scale_${g}_nodes.tsv --gene "$G"
done
```

Results and the verdict against each prediction: `../data-notes/scale/RESULTS.md`.
**Two of three predictions failed**, and the report's generalisation was withdrawn rather
than softened, per the pre-registration's own instruction.

**Two traps worth knowing if you re-run this.** STRING's `interaction_partners` endpoint
silently defaults to **10** partners per protein — left implicit it would have capped tier 1
at 10 and broken the pre-registered 25-per-tier rule; `build_node_set.py` now sets `limit`
explicitly. And STRING's preferred names lag HGNC (`GBA`, `SLC9A3R1`, `SLC9A3R2`), so the
script falls back to the Ensembl `xrefs` endpoint; without that fallback the drug search
raises, which is the designed behaviour rather than silently reporting zero drugs.

## 9. Cross-file consistency check

Run last, and re-run after editing any submission text:

```bash
python3 check_consistency.py
```

It enforces the two things the 2026-09-04 Track 2 audit found nothing was enforcing.
**No withdrawn claim may be asserted** in any of the ten reader-facing files — it may appear
only inside the paragraph that retracts it, and the report's Part 11 verification table and
`submissions/track2/_pending_edits.md` are exempt, because quoting withdrawn text is their
purpose. **And every hand-copied cross-file figure must equal its source**: the
verification-row count quoted in the judges' note, the pitch script's spoken-word count
quoted in the README, the commit count quoted in the methods form, the form's 500-word
abstract limit, and `scale_measure.py --selfcheck`.

The audit's own result is why this exists. Every *number* in the Track 2 report re-derived
from the artefacts and none changed; six *prose* claims had drifted, three of them because a
correction the report had made to itself never reached the files that quote it. Figures under
a script were correct; figures copied by hand were not.

## 10. Methods description form

The organisers' `literature/methods_description_form.xlsx` is answered from a Markdown
source of truth so the answers are diffable in the public repo:

```bash
python3 fill_methods_form.py \
  --md       ../submissions/methods_description.md \
  --template ../literature/methods_description_form.xlsx \
  --out      ../submissions/methods_description_gummietech.xlsx
```

Answers map to form rows **positionally** (Track 1 rows 7–19, Track 2 rows 7–17) and the
script **fails loudly** if the counts drift, rather than writing a partially-filled form —
which is what an earlier fuzzy-matching version did, silently filling 8 of 24.
