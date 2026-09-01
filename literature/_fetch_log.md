# Literature Fetch Log

Captured: 2026-08-31. Status of every source attempted for the `literature/` folder.

| # | Source | File | Status |
|---|---|---|---|
| 00 | Hackathon site (Overview/FAQ/Rules/Submit specs/leaderboard) | `00_hackathon_site_full_capture.md` | ✅ Full capture via browser rendering |
| 01 | Wikipedia — MVA syndrome | `01_wikipedia_mva_syndrome.md` | ✅ Full |
| 02 | JCI — Cep57 tumor suppression (Aziz et al. 2018) | `02_jci_cep57_tumor_suppression.md` | ✅ Full (open access) |
| 03 | MVA Society — site content (About/Explained/Research/George's Story) | `03_mva_society_site_content.md` | ✅ Full |
| 04 | MVA Society — curated Related Publications bibliography | `04_mva_society_bibliography.md` | ✅ Full list captured; most individual papers not yet fetched (fetch on demand — see file) |
| 05 | HPO / Open Targets / DGIdb / Exomiser overviews | `05_tool_docs_hpo_opentargets_dgidb_exomiser.md` | ✅ Full (via browser render — WebFetch alone only returned page titles for these JS-rendered SPAs) |
| 09 | Richards et al. 2015 ACMG/AMP guidelines | `09_acmg_amp_2015_guidelines.md` | ✅ Full text (PMC4544753, open access author manuscript — via browser render; WebFetch hit a reCAPTCHA wall) |
| 14 | Bohr 2025/2026, NAD supplementation in premature-aging rare diseases | `14_bohr2026_nad_supplementation.md` | ✅ Full text (PMC12727671, open access — via browser render) |
| — | Nature Reviews Genetics 2024, MVA review (Villarroya-Beltri et al.) | not fetched | ❌ Paywalled — Nature redirects to login (303). Abstract/summary obtained via WebSearch earlier in session; full text needs institutional access or a preprint/PMC version (search PMC for "Villarroya-Beltri mosaic variegated aneuploidy 2024" — not yet located) |
| 04b | Baker et al. 2011, Nature, senescent cell clearance (BubR1 progeroid mice) | `04b_baker2011_senescence_clearance_fulltext.md` | ✅ **CORRECTED 2026-08-31**: originally logged as "no PMC copy found" — this was wrong. PMC3468323 exists and is fetched in full. Reveals an important nuance not captured in the earlier secondhand summary: senescent-cell clearance in this model helps p16Ink4a-dependent tissues (muscle/fat/eye) but explicitly does NOT help p16Ink4a-independent phenotypes (cardiac arrhythmia, arterial stiffening) or extend overall survival — scope the Track 2 senolytic hypothesis accordingly. |
| — | Pushpakom et al. 2019, Nature Reviews Drug Discovery, drug repurposing review | not fetched | ❌ Paywalled — Nature redirects to login (303). Abstract obtained via WebSearch. A PMC copy was NOT confidently located in this session — search again, NIH/Wellcome-funded reviews often have a PMC deposit |
| — | Cell Reports — "p21 Both Attenuates and Drives Senescence..." (BubR1 progeroid mice) | not fetched | ❌ 403 Forbidden on direct PDF URL. Try the HTML article page instead of the PDF URL, or search PMC |
| 07 | GATK Best Practices Workflows overview | `07_gatk_best_practices.md` | ✅ Full index (via browser render — WebFetch got 403 from Zendesk bot protection). Only the index/section list was captured; individual workflow sub-pages (e.g. "Germline short variant discovery" full content) not yet fetched — pull on demand during Week 2 pipeline work |
| 12 | Pushpakom et al. 2019, Nature Reviews Drug Discovery, drug repurposing review | not fetched (no PMC copy located) | ❌ Paywalled, no open PMC deposit found. **Substitute fetched instead**: `12_drug_repurposing_nexus_editorial.md` (De Rosa et al. 2023, Scientific Reports editorial, open access) — a much shorter piece, use alongside `notes/04_drug_repurposing_methodology.md` (built from Pushpakom's abstract + general knowledge) rather than as a full replacement |

## Action items to close gaps
1. Nature Reviews Genetics 2024 MVA review and the Cell Reports p21/BubR1 paper remain paywalled with no PMC copy located in this session's searches — try again later (a PMC deposit can appear after an embargo period) or seek institutional/library access for full text. Baker 2011 was found and fetched in full on the 2026-08-31 audit pass (see row 04b) — the earlier "no PMC copy" note for it was a search-thoroughness error, not a real unavailability; worth re-attempting the other two with more search variants before concluding they're truly unavailable.
2. **Verified 2026-08-31**: the three MVA gene-discovery papers' abstracts (Hanks 2004 BUB1B, Snape 2011 CEP57, Yost 2017 TRIP13) were directly confirmed via PubMed eutils — see corrected citations in `04_mva_society_bibliography.md`. Full text not yet fetched for Snape/Yost (Hanks 2004 also still abstract-only) — low priority unless the Track 1/2 write-ups need to quote beyond the abstract.
3. Remaining ~22 papers in `04_mva_society_bibliography.md` still title/date-only — fetch each on demand as Weeks 3-6 mechanism/drug research actually needs it, not all at once.
4. Consider fetching `mvasociety.org/symptoms-and-diagnosis/` and `/for-healthcare-professionals/` pages, not yet captured.
5. Fetch GATK's "Germline short variant discovery" and "Data pre-processing for variant discovery" sub-pages in full once Week 2 pipeline work resumes.
6. **New source added 2026-08-31, not in original list**: Kops et al. 2012, *Dev Cell*, "The vertebrate mitotic checkpoint protein BUBR1 is an unusual pseudokinase" (PMID 22698286) — abstract verified directly, confirms BubR1's N-terminal KEN-box (resolving an open question flagged in `notes/01`). Full text not yet fetched.
