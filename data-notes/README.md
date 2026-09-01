# data-notes/ — what is and isn't in version control

This project analyzes real whole-genome sequencing data from one identifiable pediatric patient, released under the hackathon's gated Data Transfer Agreement (DTA). That agreement includes:

> "I will not release or otherwise grant data access to anyone and I will establish appropriate safeguards to prevent unauthorized data use."
>
> "I understand and agree that I must delete all data after I have completed the Hackathon."

A GitHub repository — even a private one — is not an approved safeguard under that agreement, and git history is not a place data can later be reliably deleted from. Accordingly:

**Excluded from this repository** (see `.gitignore`):
- `data-notes/raw/` — the original downloaded VCF, its index, and the clinical phenotype document
- `data-notes/annotated/` — full-panel VEP annotation output (genotype-level data for all ~1,280 + ~1,065 variants across the primary and secondary gene panels, not just the reported candidates)
- Any region-restricted `.vcf.gz`/`.vcf.gz.tbi` files derived from the raw VCF

**Included** (contains no patient sequencing data):
- `data-notes/regions/` — gene coordinate lookups (public GRCh38 reference genome positions for the gene panels, not patient-specific)
- `data-notes/track1_findings.md` — interpretive working notes describing the specific variants also disclosed in the actual Track 1 submission (the authorized public-disclosure channel for this analysis, per the hackathon's CC-BY 4.0 submission terms) — not a release of the broader dataset
- `pipeline/*.py` — annotation/filtering scripts (code only, no embedded data)

To reproduce this analysis: obtain your own authorized access to the hackathon dataset via Hugging Face's gated-access flow, place the VCF in `data-notes/raw/`, and run the scripts in `pipeline/` against the region coordinates in `data-notes/regions/`.
