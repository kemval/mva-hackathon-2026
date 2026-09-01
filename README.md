# MVA Hackathon 2026 — Project Workspace

Working directory for "Rare Disease, Real Kid: The MVA Hackathon 2026" (SageBio / Hugging Face / MVA Society / BEACON, prizes from AWS + Anthropic). Submissions close **Oct 24, 2026 23:59 UTC**.

Full strategy plan: `~/.claude/plans/id-like-to-participate-golden-haven.md`

## Folder structure

- `literature/` — full text of open-access papers, guideline docs, and official reference material (site captures, journal articles, tool docs). Start with `00_hackathon_site_full_capture.md` (the complete live-site capture: Overview, FAQ, Official Rules, both Submit tabs, leaderboard snapshot) and `_fetch_log.md` (status of every fetched source) once populated.
- `notes/` — original synthesis docs covering material from copyrighted textbooks (can't be bulk-copied) — mitosis/spindle-checkpoint biology, ACMG variant classification workflow, VCF/BAM/HPO pipeline mechanics, drug repurposing methodology. These are scaffolding/orientation, not a replacement for the actual primary literature in `literature/` or the textbooks themselves.
- `data-notes/` — working notes on the actual case once data access is granted (HPO terms, variant candidates, phasing results, ACMG evidence per candidate).
- `pipeline/` — scripts (annotation, filtering, Exomiser runs, phasing, drug-target queries).
- `submissions/` — drafts of both tracks' CSVs, reports, and the pitch video script.

## Key strategic takeaway (don't lose this)

Track 1's automated leaderboard is already saturated (~30+ entries at a perfect 100/1.000 score, most explicitly reference BUB1B). Raw Track 1 score will not differentiate this submission. The two real levers are: (1) Track 1's judged methods write-up (scientific rigor / depth of understanding — requires independently re-deriving the answer from the actual VCF+HPO data, not copying the crowd), and (2) the Track 2 drug-repurposing report, which is 100% panel-judged and where the majority of effort should go.

## Knowledge graph

Built — `graphify-out/` (graph.html, GRAPH_REPORT.md, graph.json). 243 nodes / 282 edges / 12 communities. Query it with `graphify query "<question>"` or `graphify path "<a>" "<b>"` instead of re-reading raw files. Re-run `/graphify /Users/kiki/mva-hackathon-2026 --update` after adding/editing files in `literature/` or `notes/` (cheap — only re-extracts changed files).

## Track 1 status (2026-08-31) — analysis substantively complete, draft submission ready

Independent pipeline (region-restrict → VEP annotate → ACMG filter) run against the real proband VCF + HPO phenotype. Result: a compound-heterozygous BUB1B candidate (p.Leu737Ter, ClinVar pathogenic + novel p.Asn1002Lys missense), independently derived — not copied from the leaderboard. Full findings in `data-notes/track1_findings.md`; draft submission in `submissions/track1/` (CSV + methods report, both marked DRAFT v1).

**Still pending before actual submission:**
1. SpliceAI check on the secondary deep-intronic finding (chr15:40216470).
2. Formal PM3/PP3 in-silico scoring (AlphaMissense/REVEL/CADD) on the missense candidate.
3. UniProt/Pfam domain boundary confirmation for residue 1002.
4. Set up the GitHub repo (required for submission — can stay private during the hackathon).
5. Final proofread, then actually upload via the "Submit - Track 1" tab on the hackathon Space.

## Next actions
1. Close out the Track 1 pending items above.
2. Begin Weeks 3-4: mechanism deep-dive bridging this confirmed variant into the Track 2 drug-repurposing report (see plan).
