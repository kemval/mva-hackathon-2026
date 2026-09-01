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
exomes), ClinVar significance, and protein domains. Batches of 150 with rate-limit
spacing. Raw JSON responses are written alongside the TSV as an audit trail.

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

The deep-intronic secondary finding (`15:40216470 A>G`) is MODIFIER impact and so
does not pass this filter by design; it was surfaced separately when reviewing rare
variants across the BUB1B locus, and is reported as a lower-confidence secondary row.

## Note on the gnomAD AF field (audit, 2026-08-31)

The version of `max_gnomad_af()` that generated the committed annotation TSVs
matched `k.startswith("gnomadg") or k == "af"`, which excluded every gnomAD *exome*
frequency (those keys are `gnomade`, `gnomade_nfe`, …) while including the 1000
Genomes global `af` key. The error was permissive — it could only let a variant
through the rarity filter, never remove one — so no candidate could have been
missed. This was verified rather than assumed: the corrected computation was
replayed offline against the saved raw VEP responses and produces an **identical**
candidate set for both panels (primary 2/2, secondary 0/0; p.Leu737Ter's max AF
rises from 7.35e-5 to 9.982e-5, still far below the 0.001 threshold). `vep_annotate.py`
now computes the field correctly; the published results are unchanged by the fix.
