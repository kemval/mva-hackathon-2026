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
