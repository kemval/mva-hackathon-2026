# MVA Hackathon 2026 — Full Site Capture (Overview, FAQ, Official Rules, Submit Tracks 1 & 2, Leaderboard snapshot)

Source: https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/ (live Gradio app behind the HF Space landing page — the public HF page alone does not render this content)
Captured: 2026-08-31

## Overview

🧬 Rare Disease, Real Kid: The MVA Hackathon 2026

The genome and clinical story on this page belong to a real child living with Mosaic Variegated Aneuploidy (MVA), an ultra-rare genetic condition affecting fewer than 50 people worldwide. There is currently no established treatment, and care today means managing symptoms.

The family has opened the case to the research community, hoping someone can find an answer.

THE MVA HACKATHON IS NOT INTENDED TO PROVIDE GENERAL MEDICAL CARE, DIAGNOSIS, OR PROFESSIONAL MEDICAL ADVICE.

Every person's DNA contains millions of tiny variations, and almost all of them are harmless. But every so often, one of those variations disrupts something important, and the result is a disease. For many rare diseases, doctors and researchers recognize the symptoms but don't know the exact genetic variations responsible for them.

This MVA Hackathon releases real genetic and clinical data, shared with full, explicit permission from the family it belongs to, and asks the global research community to help make sense of it.

Access to the data is controlled. The research outputs are open: participant submissions, code, and reports are released under CC BY 4.0, so methods developed for this case can be reused for other undiagnosed individuals.

### Why This Hackathon Exists

Behind this project is a family who made a deeply personal decision: to share their child's most private information - their genome - with strangers around the world, in the hope that someone, somewhere, might help understand their child's rare condition.

Their child lives with Mosaic Variegated Aneuploidy (MVA), a condition few clinicians will ever encounter in their careers. There is currently no established treatment, but the MVA Society is funding focused research to bring treatments closer. Care today means managing symptoms and fighting cancer cells.

### Two Tracks

**🧬 Track 1 - Variant Prediction**

The Goal: Predict the specific genetic variant(s) that may be driving the child's condition using their clinical symptoms and genomic data.

You'll be given the child's genomic data (FASTQ + VCF) and a description of their symptoms, and asked to predict which specific variant(s) may be causing the condition. Secondary or incidental findings are welcome too.

Your ranked predictions are automatically checked against the clinically confirmed answer and your score updates live on the public leaderboard.

What you submit: A ranked list of variant predictions, a Github link, and a methods writeup.
Submission limit: 6

Scoring: This is a foundational track — the goal is to validate that your pipeline can recover a clinically confirmed variant from real patient data. Prediction files are scored automatically on two primary metrics:
- Rank points - How high did you rank the true variant(s). If your top-ranked variant(s) is correct, you'll get 100pts. If you get the correct variant(s) within your top 10 ranked ones, you'll get partial credit. If you correctly identify one of the two variants in a heterozygous pair, you'll get half credit.
- F-max - the best balance of precision and recall your submission achieves at any confidence threshold, rewarding submissions that pinpoint the right answer without burying it in noise. Secondary or incidental findings won't hurt your automated score.

Your methods write-up is reviewed separately by a judging panel for scientific rigor and depth of understanding.

**💊 Track 2 - Drug Repurposing**

The Goal: Identify existing, approved medications that are plausible candidates for further investigation, based on the biological mechanisms disrupted in this case. Submissions are hypotheses for follow-up, not evidence that a medicine works.

Once you know (or have a strong guess at) what biological mechanisms are involved, the next question is: Does an existing medication work on this biological problem?

For this track, you'll characterize the mechanism behind the variant(s) and write up your reasoning and proposed candidate medication(s). An independent panel of expert judges evaluates submissions on scientific merit and real-world potential.

What you submit: A detailed report, a Github link, and a 3-minute pitch video
Submission limit: 3

Scoring — Track 2 is scored by the expert panel across four weighted criteria:
- Scientific Rigor — 35% — Is the variant mechanism characterization sound, and is the proposed drug repurposing candidate well-supported by that mechanism?
- Potential Impact — 25% — If independently validated, how much could this contribute to understanding or diagnosing MVA, for this child or for others living with it?
- Innovation — 25% — Did you bring a genuinely creative angle, method, or tool to the problem?
- Scalability — 15% — Could your approach realistically be applied to other individuals, other diseases, or larger datasets - not just this one case?

### Prizes

$50,000 total - $25,000 in cash from the AWS Imagine Grant program + $25,000 in Claude credits from Anthropic.

- 🥇 1st Place: $12,000 cash + $12,000 credits
- 🥈 2nd Place: $7,000 cash + $7,000 credits
- 🥉 3rd Place: $4,000 cash + $4,000 credits
- 🌟 Innovation Award: $2,000 cash + $2,000 credits

*Anthropic credits are provided for use with Claude Science, intended to help winning teams deepen their computational analysis and extend their findings on MVA beyond the Hackathon itself, not as a cash-equivalent award.

### How to Participate

Anyone can join, no previous hackathon experience needed. Built for ML engineers, computational biologists, clinicians, geneticists, students, citizen scientists.

1. Sign in with Hugging Face account.
2. Get the data — request access via the dataset page (gated, requires agreeing to data usage rules; data shared under protocol approved by WCG IRB, protocol #20252010).
3. Choose your track — Track 1, Track 2, or both.
4. Build and submit — via "Submit - Track 1"/"Submit - Track 2" tabs.
5. Join the community — Discussions tab.

### Timeline

| Date | Milestone |
|---|---|
| August 24 | Hackathon launch; dataset available for request and download |
| August 25 | Submissions open |
| October 24 (23:59 UTC) | Submissions close; Track 1 leaderboard frozen |
| October 24 – November 24 | Track 1 qualitative evaluation; Track 2 expert panel judging |
| November 25 | Winners announced; prizes awarded |

### Acknowledgements

Organized in partnership with Sage Bionetworks, the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. Guidance from the Wilhelm Foundation.

---

## FAQ (full, expanded)

**Who can participate?** Anyone with a Hugging Face account - data scientists, ML engineers, clinicians, students, citizen scientists alike. Must be at least 18 years old. See Official Rules.

**Can I participate in both tracks?** Yes. Track 1 and Track 2 are scored independently. You can submit to one or both.

**Can I participate as a team?** Yes. Each team member must register individually with their own Hugging Face account. For Track 1, each team member may submit independently and your best score counts. For Track 2, designate one person to submit on the team's behalf — only one Track 2 submission per team is accepted, additional submissions from other team members are ignored.

**How many submissions can I make?** Track 1: up to 6 per participant; only highest-scoring appears on leaderboard. Track 2: up to 3 per team; the panel only reviews your latest entry.

**How is Track 1 scored?** Submissions are scored the way large-scale rare disease benchmarks (like Stenton et al., 2024) score solved cases applied to this single, clinically confirmed answer. Two metrics computed automatically: rank points (how high true variant(s) land in ranked list, partial credit if only one of two compound-het variants recovered) and F-max (best precision/recall balance across submitted confidence thresholds). Methods write-up also reviewed by judging panel for scientific rigor and depth of understanding.

**Why are there perfect scores on the Track 1 leaderboard?** Track 1 is a foundational track — designed to be achievable. Leaderboard validates pipeline can recover the clinically confirmed variant(s). BUT recovering the correct variant(s) is not the finish line — all teams must also submit a methods write-up explaining approach and interpretation. This component cannot be scored automatically and is where the judging panel evaluates scientific rigor and depth of understanding.

**Are secondary or incidental findings scored?** Won't hurt automated Track 1 score — include as additional rows if desired. Set aside for qualitative review by judging panel rather than folded into automated rank points/F-max, since there's no fixed "correct" answer for secondary findings. Use the optional notes column to explain why flagging it (e.g. "well-established pathogenic variant, unrelated to primary phenotype, recommend clinical follow-up").

**How is Track 2 scored?** Reports reviewed by independent panel, judged on scientific rigor, potential impact, innovation, and scalability.

**Can I keep my GitHub repository private during the Hackathon?** Yes, may remain private while running. Must be made public once Hackathon ends so expert panel can review code/methods.

**What compute resources are available?** This Space runs on CPU-basic hardware. Participants welcome to use own compute for training; only final submission files need to be uploaded here.

**Are third-party LLMs allowed with this Hackathon's dataset?** Conditions apply — see detailed answer in Community discussion for provider terms, data handling, deletion requirements.

**What is the data license?** Underlying dataset is gated, subject to Hackathon Rules and Data Transfer Agreement — access requires approval, redistribution prohibited, all data must be deleted upon conclusion. Participant submissions/results (predictions, code, reports) released under CC BY 4.0, may be reused with attribution.

**When will results be announced?** Final rankings announced after ~2-3 month judging window closes; exact date posted in Community tab.

**Unanswered questions?** Post in Discussions tab.

---

## Official Rules (full)

### Terms of Service & Eligibility
- Must abide by Hugging Face Terms of Service and these Hackathon Rules.
- Must be 18+.
- Each team member must individually register and agree to these Rules.

### Data Privacy & Recontact Restrictions
- Must NOT attempt to recontact the data subject, family members, or MVA Society points of contact.
- Use of data must comply with all applicable laws/regulations/professional standards.
- Suspected unauthorized disclosure → contact Sage Bionetworks' Privacy and Compliance Office via Sage's Help Center.
- Will not release/grant data access to anyone; must establish safeguards preventing unauthorized use.

### Hackathon Flow
- **Registration**: HF registration + data access request incl. valid email + attestation.
- **Tasks**:
  - Track 1 - Variant Identification: identify disease-causing variant(s) using genetic variant info + phenotypic presentations.
  - Track 2 - Drug Repurposing: leveraging genetic info + variant prediction from Track 1, identify existing market-approved medications whose mechanism of action may target the disease-causing pathway(s).
- **Team Formation**: Not required; participants may form teams.
- **Data and Resource Provision**:
  - File types: genomic data in VCF format; raw sequencing data optionally in BAM/CRAM. Phenotypic data as standardized HPO terms.
  - Data size: ~85 GB (single-subject dataset).
  - Access: via HF gated-dataset mechanism. No data may be reshared through any channel.
  - Compute: participants responsible for own compute + costs.
- **Development**: teams work intensively — brainstorming, coding, data analysis, design.
- **Data Deletion**: no retention after Hackathon for any purpose. All data deleted within 30 days of Hackathon close from ALL environments (local machines, cloud instances, notebooks, private repos, intermediate/derived datasets). Must email RarediseaserealkidMVAhackathon2026@synapse.org to confirm deletion, or organizers may contact directly in 30 days.
- **Presentations & Judging**: each team submits written report, GitHub repo, 3-min recorded pitch video. Expert panel (researchers, clinicians, patient advocates) reviews all Track 2 submissions. Judging ~2-3 months post submission close. Pre-recorded, no live Q&A.

### Evaluation and Outcome
- Track 1 (automated): scored against NHS-validated causal variant(s) using rank points and F-max.
- Track 2 (panel-judged): Scientific Rigor 35%, Potential Impact 25%, Innovation 25%, Scalability 15%.

### Prizes
Total $50,000, sponsored by AWS Imagine Grant program and Anthropic:
- 1st: $12,000 cash + $12,000 Claude credits
- 2nd: $7,000 cash + $7,000 Claude credits
- 3rd: $4,000 cash + $4,000 Claude credits
- Innovation/Community Award: $2,000 cash + $2,000 Claude credits — awarded at judges' discretion for exceptional creativity, community impact, or patient-centered design, independent of overall placement.

### Research Progress & Post-Hackathon Data Handling
- May publish/present on results subject to embargo policy.
- All data deleted within 30 days of Hackathon close.
- Anonymized results remain available to research community via Synapse and/or HF.
- Submissions released under CC-BY license.

### Embargo Policy
- Embargo begins at Hackathon close, ends upon public posting of the hackathon summary report/preprint by organizing team.
- During embargo, cannot submit manuscripts for peer-reviewed publication using the hackathon dataset.
- Free to publicly share code, models, derived outputs any time.
- May present preliminary findings in conference abstracts/posters with prior written approval from organizers.

### Submission Reuse
- Submissions may be rerun by organizers. Subject to CC-BY license; name shared as part of open-access attribution.

### Recontact
- By providing email and participating, consent to being recontacted by organizers for Hackathon-related purposes (NOT the family).

### Post-Hackathon Information Sharing
- Results accessible to broader research community. Leading submissions may be featured on HF/Sage Bionetworks/Synapse sites. Follow-up blog posts, video recaps, social media highlights.

### Citation and Acknowledgement
Required acknowledgement text for any publication/preprint/abstract/public communication:

> "This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible."

Additional requirements:
- Data subject privacy: publications referencing individual-level data must not include re-identifying info beyond what's already public via the family's own blog posts/communications.
- Dataset citation: must cite using reference on Hackathon Synapse page at time of publication.

---

## Submit - Track 1 (full instructions)

Upload predictions file for instant evaluation against confirmed clinical groundtruth. Up to 6 submissions; only highest-scoring featured on leaderboard.

Team Participation: each member gets own submission quota; coordinate to avoid wasting submissions; use exact same team name so entries group together.

### 1. Create your predictions file
One row per proposed causal variant (or compound-het pair). Rank by own estimated probability of causal relationship (EPCR), 1 = most likely causal, 0 = least likely. No fixed "confident enough" cutoff — only ranking relative to own guesses matters. **Coordinates must use GRCh38.**

Up to 10 candidate rows accepted (one case, not a cohort — best-ranked guesses, not exhaustive list). Flag primary vs secondary/incidental via `finding_type` column. Secondary/incidental findings won't hurt automated score.

**CSV Schema:**
| Field | Type | Description |
|---|---|---|
| proband_id | string | Proband identifier (provided in dataset) |
| chrom_1 | string | Chromosome of first/only variant (e.g. chr15) |
| pos_1 | integer | GRCh38 base-pair position of first variant |
| ref_1 | string | Reference allele of first variant |
| alt_1 | string | Alternate allele of first variant |
| chrom_2 | string | Chromosome of second variant (compound-het pairs only, blank otherwise) |
| pos_2 | integer | GRCh38 position of second variant (blank if N/A) |
| ref_2 | string | Reference allele of second variant (blank if N/A) |
| alt_2 | string | Alternate allele of second variant (blank if N/A) |
| epcr | float | Estimated probability of causal relationship, (0, 1] |
| finding_type | string | "primary" or "secondary" |
| notes | string | Optional rationale, esp. for secondary findings |

Filename convention: include username/team name + short descriptive model name, e.g. `jane-doe_gatk-haplotype.csv`, `jane-doe_deepvariant-v2.csv`.

### 2. Write your report
Brief report (PDF or Markdown) describing approach, rationale, supporting evidence. Required for judging, not scored automatically.

**Update 28 Aug 2026**: If used an LLM/AI assistant, record provider, plan/tier, relevant data-handling setting in methods description. E.g.: "Anthropic API, Claude Sonnet, commercial terms, no training on customer content."

Filename convention: `jane-doe_track1_report.pdf` (.md also accepted).

### 3. Prepare other supporting materials
GitHub Repository — may remain private during Hackathon, must be public once it ends. Include: documented reproducible code (all scripts/configs needed to reproduce results), submission files (optional), methods description (optional but recommended).

### 4. After submission
CSV evaluated automatically (rank points, F-max) against clinically confirmed answer on leaderboard. Method(s) reviewed separately as part of judging criteria (innovation, scalability).

Submission fields: Team/Display Name (optional), GitHub repo URL*, Predictions file (CSV)*, Report file (PDF/Markdown)*.

---

## Submit - Track 2 (full instructions)

Upload Track 2 proposal for review by independent expert judging panel. Qualitative evaluation, not automated scoring.

Up to 3 submissions (in case updates needed). Panel reviews only latest entry — make sure final submission is the one you want reviewed.

Team Participation: designate single team member to submit on team's behalf. Additional/duplicate submissions from other members not reviewed.

### 1. Write your report
Written report (PDF or Markdown) proposing repositioned drug candidates supported by analysis. Include characterization of variant's mechanism (loss-of-function/gain-of-function, pathway disrupted, downstream biological consequence) as basis for repurposing rationale.

**Update 28 Aug 2026**: same LLM/AI-assistant disclosure requirement as Track 1.

Filename convention: `jane-doe_track2_report.pdf` (.md also accepted).

### 2. Prepare other supporting materials
GitHub Repository — same public-after-close requirement. Include: documented reproducible code, methods description (optional but recommended).

Pitch Video — record 3-minute pitch video walking through reasoning and proposed candidates, upload to YouTube or Vimeo.

### 3. After submission
Independent panel reviews all entries over ~2-3 month window. Results announced at later date.

Submission fields: Team/Display Name (optional), GitHub repo URL*, Pitch video URL*, Notes for judges (optional), Report file (PDF/Markdown)*.

---

## Track 1 Leaderboard Snapshot (captured 2026-08-31, reflects submissions through 2026-08-27 01:09 UTC)

Metrics: Rank Points & F-max (adapted from Stenton et al., 2024). Note: final Track 1 evaluation also includes the methods write-up, not reflected in this automated leaderboard.

All 32 entries at time of capture scored a perfect 100.0 rank points / 1.000 F-max. Most model/filename labels explicitly reference "bub1b" and "compound-het" / "comphet", e.g.:
`model1_gamow_sentieon-vcf-targeted-acmg.csv`, `model1_scottmastro_bub1b-targeted-acmg.csv`, `model1_benshap_go-tiered-cadd-recessive.csv`, `model1_eppo-r_genotype-architecture-sweep.csv`, `model1_anonwebber_bub1b-compound-het.csv`, `model1_ericmodesitt_readlevel-verified-acmg.csv`, `model1_noqcks_bub1b-compound-het.csv`, `model1_paraxaQQ_exomiser15-cis-aware.csv`, `model1_samistus1234_vep-compoundhet.csv`, `model1_MarxistLeninist_bub1b_compound_het.csv`, `model1_Kuberwastaken_bub1b-pair.csv`, `model1_rogerking_bub1b-comphet-wgs.csv`, `model1_michaldobiezynski_bub1b-triage-v1.csv`, `model1_aman-code_bub1b-compound-het.csv`, `model3_kavya5cloud_submission3_bub1b_compoundhet.csv`, `model1_ramadistra_bub1b-comphet-bcftools.csv`, `model2_liam0798_track1_bub1b_rank.csv`, `model1_neilkale_bub1b-compound-het_v1.csv`, `model1_adriamasnou_vcf-targeted-bub1b.csv`, `model1_johnpccd_bub1b-compound-het.csv`, `model1_Silico-EVEE_bub1b-comphet.csv`, `model1_josephmayo_track1_bub1b_pair.csv`, `model1_genobank_acmg-bub1b.csv`, `model2_anaygarodia_sac-panel-vep-clinvar.csv`.

**Interpretation**: the crowd has essentially converged on a BUB1B compound-heterozygous call via publicly known MVA genetics. Raw automated Track 1 score is not a competitive differentiator anymore — the differentiators are (a) the judged Track 1 methods write-up depth/rigor, and (b) the Track 2 drug-repurposing report, which is entirely panel-judged.

## Dataset page notes (SageBio/mva-hackathon-2026-data on HF)

- Submission Period: 24 August 2026 – 24 October 2026.
- Dataset Size: ~85 GB across 11 files. Recommend 100-150 GB storage for caching/indexing/pipeline intermediates.
- Example filename pattern: `WGS_EX2312012_HGWCNDSX7.vcf.gz` (whole-genome sequencing).
- Gated: requires HF login + agreeing to Hackathon Rules to view/download.
