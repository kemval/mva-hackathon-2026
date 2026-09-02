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
| 15 | Suijkerbuijk et al. 2010, *Cancer Res*, BUBR1 dysfunction in MVA | `15_suijkerbuijk2010_bubr1_abundance_mva.md` | ✅ Full text (PMC2887387, via NCBI BioC API). **The load-bearing Track 2 paper**: MVA patient cells with the truncating+missense genotype show low BubR1 abundance; forced overexpression of kinase-domain missense mutants fully restores checkpoint function; a threshold sits between ~6% and ~13% residual BubR1. Also yields a contraindication — mutant BubR1 is an HSP90 client cleared by the proteasome, so HSP90 inhibitors would deplete it |
| 16 | North/Sinclair et al. 2014, *EMBO J*, SIRT2 induces BubR1 | `16_north2014_sirt2_bubr1_nad.md` | ✅ Full text (PMC4194088) — **via PMC HTML render; the BioC and efetch routes both return abstract-only for this deposit**. Records the four limits on what it demonstrates, chiefly that **NMN was never administered to a BubR1-hypomorphic mouse** |
| 17 | Wijshake et al. 2012, *PLoS Genet*, mono-allelic BubR1 MVA mutation | `17_wijshake2012_monoallelic_bubr1.md` | ✅ Full text (PMC3531486, BioC). Supports the phase-robustness argument. **Citation corrected**: first author is Wijshake T, not van Deursen JM (senior) as the MVA Society bibliography lists |
| 18 | Kirsch-Volders & Fenech 2023, *Mutat Res Rev*, aneuploidy-associated senescence | `18_kirschvolders2023_aneuploidy_senescence.md` | ✅ Full text (PMC13019530, BioC). Closest prior art; expected to be paywalled and was not |
| 19 | Justice et al. 2019, *EBioMedicine*, senolytics in IPF | `19_justice2019_senolytics_ipf.md` | ✅ Full text (PMC6412088, BioC). First-in-human D+Q regimen |
| 20 | Hickson et al. 2019, *EBioMedicine*, senolytics in diabetic kidney disease **+ its 2020 corrigendum** | `20_hickson2019_senolytics_dkd_with_corrigendum.md` | ✅ Full text of both (PMC6796530, PMC6994619). **The substantive corrigendum is Appendix 1, which is not in the PMC record** — extracted from the Europe PMC supplementary bundle (`mmc1.docx`) via `webservices/rest/PMC6994619/supplementaryFiles`. Re-analysis withdrew the skin-senescence result and the individual IL-1α/IL-6/MMP-9 claims |
| 21 | Shoji et al. 2025, *Aging Cell*, NR in Werner syndrome RCT | `21_shoji2025_nr_werner_rct.md` | ✅ Full text (PMC12341770, BioC). Best-quality NAD⁺ evidence in a monogenic progeroid disease — and the source of the candidate's most awkward negative (sarcopenia indicators unchanged) |
| 22 | Veenhuis et al. 2021, *Mov Disord*, NR in ataxia telangiectasia | `22_veenhuis2021_nr_ataxia_telangiectasia.md` | ✅ Full text (PMC9291897, BioC). 17 of 24 participants were children — the paediatric-exposure citation |
| 23 | Nakano et al. 2024, *Clin Cancer Res*, surveillance in genomic instability disorders | `23_nakano2024_surveillance_genomic_instability.md` | ✅ Full text (PMC11705613, BioC). Contains the AACR-endorsed **MVA-specific** protocol: renal ultrasound q3 months birth→age 7, avoid radiation. **Citation corrected**: first author is Nakano Y, not Walsh MF (senior) as the bibliography lists |
| 24 | Mackenzie et al. 2017, *Nature*, cGAS surveillance of micronuclei | `24_mackenzie2017_cgas_micronuclei.md` | ✅ Full text (PMC5870830, BioC) |
| 25 | Bakhoum et al. 2018, *Nature*, CIN drives metastasis via cytosolic DNA | `25_bakhoum2018_cin_cytosolic_dna.md` | ✅ Full text (PMC5785464, BioC) |
| 26 | Tang et al. 2011, *Cell*, aneuploidy-selective compounds | `26_tang2011_aneuploidy_selective_REJECTED.md` | ⚠️ **Abstract only** — PMC3532042 exists but neither the BioC nor the efetch route exposes body text. Sufficient for its purpose: the paper is in the *rejected* tier and the abstract names the three compounds |
| 27 | Xu et al. 2015, *PNAS*, JAK inhibition and SASP | `27_xu2015_jak_inhibition_sasp.md` | ⚠️ **Abstract only** — PMC4655580, same limitation as row 26. Full text should be retried via PMC HTML render (the route that rescued row 16) if the senomorphic tier becomes load-bearing |

## Action items to close gaps

0. **Track 2 fetch round, 2026-09-02** — rows 15-27 added above. Two methodological notes
   worth reusing: (a) the NCBI **BioC API** (`research/bionlp/RESTful/pmcoa.cgi/BioC_json/<PMCID>/unicode`)
   is the most reliable bulk route and succeeded on 9/12 first-pass attempts, but returns
   abstract-only for some author-manuscript deposits — **fall back to a plain PMC HTML
   render**, which recovered the Sinclair 2014 full text after two API routes failed;
   (b) **a corrigendum's substance can live in a supplementary appendix invisible to PMC
   and PubMed** — the Hickson 2019 re-analysis was only obtainable from the Europe PMC
   `supplementaryFiles` bundle. Anyone citing that trial from its abstract is citing
   withdrawn claims. Both traps are worth remembering for the remaining fetches.
1. Nature Reviews Genetics 2024 MVA review and the Cell Reports p21/BubR1 paper remain paywalled with no PMC copy located in this session's searches — try again later (a PMC deposit can appear after an embargo period) or seek institutional/library access for full text. Baker 2011 was found and fetched in full on the 2026-08-31 audit pass (see row 04b) — the earlier "no PMC copy" note for it was a search-thoroughness error, not a real unavailability; worth re-attempting the other two with more search variants before concluding they're truly unavailable.
2. **Verified 2026-08-31**: the three MVA gene-discovery papers' abstracts (Hanks 2004 BUB1B, Snape 2011 CEP57, Yost 2017 TRIP13) were directly confirmed via PubMed eutils — see corrected citations in `04_mva_society_bibliography.md`. Full text not yet fetched for Snape/Yost (Hanks 2004 also still abstract-only) — low priority unless the Track 1/2 write-ups need to quote beyond the abstract.
3. Remaining ~22 papers in `04_mva_society_bibliography.md` still title/date-only — fetch each on demand as Weeks 3-6 mechanism/drug research actually needs it, not all at once.
4. Consider fetching `mvasociety.org/symptoms-and-diagnosis/` and `/for-healthcare-professionals/` pages, not yet captured.
5. Fetch GATK's "Germline short variant discovery" and "Data pre-processing for variant discovery" sub-pages in full once Week 2 pipeline work resumes.
6. **Rows 26 and 27 remain abstract-only.** Retry both via the PMC HTML render route
   before the Track 2 report is finalised, in case body text is recoverable.
7. **New source added 2026-08-31, not in original list**: Kops et al. 2012, *Dev Cell*, "The vertebrate mitotic checkpoint protein BUBR1 is an unusual pseudokinase" (PMID 22698286) — abstract verified directly, confirms BubR1's N-terminal KEN-box (resolving an open question flagged in `notes/01`). Full text not yet fetched.


---

# Pass 3 — Adversarial review pass, 2026-09-02

Purpose: find where the literature **disagrees with itself** and adjudicate, rather than
summarise. Deliverables: `_contradiction_matrix.md`, `_claims_register.md`,
`_open_questions.md`.

## Successes

| Target | Route | Result |
|---|---|---|
| Tang 2011 (PMC3532042) | PMC HTML render | ✅ 61,704 chars — full text recovered after two API routes had failed |
| Xu 2015 (PMC4655580) | PMC HTML render | ✅ 78,403 chars — same |
| Fuhrmann-Stroissnigg 2017 (PMC5583353) | PMC HTML render | ✅ 86,808 chars |
| Aalinkeel 2008 (PMC2826114) | PMC HTML render | ✅ 80,475 chars |
| Shahid 2026 (PMC13212844) | PMC HTML render | ✅ 79,666 chars |
| Corrigendum sweep, 18 PMC sources | eutils efetch, `CommentsCorrections` | ✅ Ran clean — exactly one hit (Hickson 2019 → PMID 31982828). No retractions, no expressions of concern |
| Title-vs-identifier verification, all PMC-sourced files | elink PMC→PubMed + esummary | ✅ 2 genuine mismatches found (both corrected), 6 benign flags |
| Disconfirming-evidence searches | PubMed esearch | ✅ 5 NAD⁺ RCTs incl. 3 muscle nulls |
| Author-order verification, 4 papers | esummary | ✅ All correct as cited |

## Failures and gaps — recorded as prominently as the successes

| Target | Route attempted | Outcome |
|---|---|---|
| **Kirsch-Volders & Fenech 2023 full text** | NCBI elink → PMC13019530 | ❌ **Returned the wrong paper.** No correct deposit exists. Remains abstract-only. Elsevier; needs institutional access |
| **Kıyga 2020 (Mol Biol Rep) primary study** | elink PMID 32638319 → PMC13212844 | ❌ **Returned the wrong paper** (the 2026 review that cites it). Not fetched; file `29_` marks it unread and cites the review as a review |
| **Five NAD⁺ RCT full texts** | Not attempted this pass | ❌ Abstracts only. Deliberate scope limit, recorded as a gap in `30_` |
| NCBI `idconv` v1.0 endpoint | `pmc/utils/idconv/v1.0/` | ❌ Returned non-JSON; appears deprecated. Worked around with `elink` — which is itself unreliable (see below) |
| Nature Reviews Genetics 2024 MVA review | Not re-attempted this pass | ❌ Still outstanding from pass 1 |
| Cell Reports p21/BubR1 paper | Not re-attempted this pass | ❌ Still outstanding from pass 1 |
| Pushpakom 2019 | Not re-attempted this pass | ❌ Still outstanding from pass 1 |

## Scope this pass did NOT cover — stated so coverage is not overclaimed

This pass was **depth-first on contradictions**, not breadth-first on acquisition. It did
**not** run: EU CTR, ISRCTN, WHO ICTRP, jRCT, ChiCTR; openFDA/EMA/Health Canada/PMDA
brand-name label searches; OMIM, DECIPHER, Orphanet, GeneReviews; ClinVar submitter-level
detail beyond the RYR1 variant already adjudicated; non-English (Japanese/Chinese) MVA
cohort literature; systematic cited-by and reference-list traversal; or patient-organisation
newsletters, conference abstracts and theses. ClinicalTrials.gov v2 with structured
`minimumAge`/`stdAges` fields, ClinGen VCEP/SVI decisions and the PharmCAT/CPIC layer were
covered in **earlier** passes and are recorded in `data-notes/`. **Non-English MVA cohort
literature remains the largest untouched acquisition gap in this repository** and is the
single most likely place for an unfound MVA case series.

## Three reusable methodological findings

1. **The PMC HTML render route is the reliable fallback and should be tried before
   declaring a source abstract-only.** It has now rescued full text in **five of five**
   attempts where the BioC and efetch routes returned abstract-only (Sinclair 2014 in pass
   2; Tang 2011, Xu 2015 and two new sources in pass 3). The earlier "abstract only"
   verdicts on rows 26 and 27 were a route problem, not an availability problem.

2. **NCBI's PMID↔PMCID links can be wrong, and the forward and reverse mappings can
   disagree.** Two independent collisions were found this pass, both involving recent
   high-numbered deposits (PMC130–132 million) with overlapping authors or topics. In both
   cases the fetched text was internally coherent and by plausible authors, so **reading
   carefully would never have caught it.** The only defence is mechanical: resolve the
   cited identifier back to its title and compare. That check is now written, has been run
   corpus-wide, and should be re-run whenever a source is added.

3. **A clean corrigendum sweep is necessary but not sufficient.** The sweep detects only
   corrections indexed by PubMed — and the Hickson 2019 case is itself the proof that a
   substantive withdrawal can live in a supplementary appendix invisible to that index.
   A negative sweep bounds the risk; it does not eliminate it.

---

# Pass 4 — gap closure, 2026-09-02

Working from `pipeline/gap_closure_brief.md`. **Task 1 (structural analysis of
p.Asn1002Lys) only** — Tasks 2–6 not attempted in this pass.

## Successes

| # | Target | Route | Result |
|---|---|---|---|
| 31 | UniProt **O60566** full entry | `rest.uniprot.org/uniprotkb/O60566.json` | ✅ Confirms residue 1002 = Asn, 1050 aa, and lists 9 PDB cross-references |
| 32 | **AlphaFold** model for O60566 | `alphafold.ebi.ac.uk/api/prediction/O60566` → v6 pdbUrl | ✅ `AF-O60566-F1` **v6** (2025-08-01), 1050 residues, pLDDT 91.1 at residue 1002 |
| 33 | PDBe observed-residue coverage for **6TLJ**, **5KHU** | `ebi.ac.uk/pdbe/api/pdb/entry/polymer_coverage/` | ✅ Both resolved — and both **contradict** the UniProt cross-reference (below) |
| 34 | Conservation at chr15:g.40220612T>G | MyVariant.info dbNSFP | ✅ phyloP 4.87 / 5.12, phastCons 1.0 / 1.0, GERP++ 3.99, PROVEAN −3.89, VEST4 0.885 |

## Failures and gaps — recorded as prominently as the successes

| # | Target | Route | Outcome |
|---|---|---|---|
| F1 | **ΔΔG for N1002K** | DDMut `POST /ddmut/api/prediction_single` | ⚠️ **NOT OBTAINED.** Two jobs accepted (HTTP 200, ids `17883629491989634` full-length and `17883630984480202` domain-trimmed). Every retrieval path failed: `GET ?job_id=` → `Internal Server Error` on six polls across both jobs; `POST` with `job_id` → `Unknown arguments: job_id` when required fields were supplied, and demanded those fields when they were not. |
| F2 | ΔΔG, alternative predictor | DynaMut2 `POST /dynamut2/api/prediction_single` | ⚠️ HTTP 400 to a bare probe; not pursued further after DDMut's retrieval proved broken |
| F3 | ΔΔG, local | `foldx`, `rosetta_scripts` | ⚠️ Neither installed |
| F4 | AlphaFold model, first attempt | `files/AF-O60566-F1-model_v4.pdb` | ⚠️ **HTTP 404** — the v4 filename many tools hard-code is dead. Resolved by querying the API for the live version (now v6). Worth knowing: a hard-coded AlphaFold URL is now a silent failure. |

**Consequence:** the structural claim is reported as **inspection, not ΔΔG**, exactly as the
brief pre-committed. See `data-notes/structural_analysis_n1002k.md`.

## Scope this pass did NOT cover

Tasks **2 (MVA cohort genotype–phenotype table)**, **3 (Japanese/Chinese PCS literature)**,
**4 (preterm nephrocalcinosis)**, **5 (coverage re-costing)** and **6 (post-first-tumour
surveillance)** of the brief are **untouched**. Everything recorded in Pass 3's
"scope this pass did NOT cover" section also remains outstanding, including the
non-English MVA cohort literature.

## Two reusable findings

4. **A PDB cross-reference's declared chain range is not the modelled range.** UniProt
   lists 5KHU and 6TLJ with chains `1-1050` — that is the *entity* length. The observed
   residues are 26–479 and 19–345. **Neither models residue 1002, and no experimental
   structure of the BubR1 pseudokinase domain exists.** Trusting the cross-reference would
   have produced a claim of experimental structural support that does not exist. This is the
   same family of error as the two identifier collisions in Pass 3 — logged as **C12**.

5. **AlphaFold model versions move, and the old URL 404s rather than redirecting.** Always
   resolve `api/prediction/<accession>` for the live version instead of constructing a
   filename. `pipeline/structural_analysis.py` does this.
