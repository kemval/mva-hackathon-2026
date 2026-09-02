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

Working from `pipeline/gap_closure_brief.md`. **Tasks 1, 4 and 6** — Tasks 2, 3 and 5 not
attempted in this pass.

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

## Task 4 — preterm nephrocalcinosis

| # | Target | Route | Result |
|---|---|---|---|
| 35 | PubMed, 5 queries: preterm NC incidence/timing; furosemide; serial ultrasound onset; congenital/antenatal NC; BUB1B+renal | eutils esearch/esummary | ✅ All 5 returned. The BUB1B+renal query is **90% wrong-product matches** — renal-cell-carcinoma drug-discovery papers using BUB1B as a tumour marker. Failure mode 4, exactly as the original brief predicted |
| 36 | Kim 2023, gestational-age stratification | Europe PMC `fullTextXML` | ✅ **Full text** (PMC10485931). The decisive source — monogenic OR 10.02 in full-term |
| 37 | Gilbert 2022, VLBW incidence/natural course | Europe PMC `fullTextXML` | ✅ **Full text** (PMC9587072) |
| 38 | Santos 2018, furosemide systematic review | Europe PMC `fullTextXML` | ✅ **Full text** (PMC6240934) — the deliberately-sought disconfirming source |
| 39 | Narendra 2001, prospective preterm NC | efetch abstract | ⚠️ **Abstract only** — Europe PMC returned **HTTP 404** for PMC1721318 (scanned-era deposit). The study-design sentence needed is in the abstract and is quoted as such |
| 40 | Bonnett 1991, serial ultrasound incidence | efetch abstract | ⚠️ **Abstract only** |
| 41 | Kajii 1998, MVA renal phenotype | efetch abstract | ⚠️ **Abstract only.** Renal cysts + Wilms tumour, **no nephrocalcinosis** — one case report, not the Task 2 cohort search |

### ⚠️ A route this repository relied on has closed

| # | Target | Route | Outcome |
|---|---|---|---|
| F5 | Full text for PMC10485931, PMC1721318, PMC9587072 | **PMC HTML render** | ❌ **BLOCKED.** All three returned HTTP 200 with a ~21 KB **Google reCAPTCHA interstitial** ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov"), extracting to 167 characters. **No attempt was made to bypass or complete the CAPTCHA.** |
| F6 | Same three, via BioC | `pmcoa.cgi/BioC_json` | ❌ Non-JSON response for all three |

**The "PMC HTML render route is 5-for-5" finding recorded in Pass 3 is now stale.** As of
2026-09-02 that route is behind a bot check. **The working replacement is the Europe PMC REST
API** — `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` — which is
openly served, returned full text for 3 of 4 attempts here, and was named in the original
brief. Use it first. Note its one failure mode seen here: older scanned-era deposits return
HTTP 404 rather than partial content.

### Incidental Task 3 hit

PMID **30512160** — *Zhonghua Yi Xue Yi Chuan Xue Za Zhi* (Chinese Journal of Medical
Genetics) 2018, "[Clinical features and genetic analysis of a child with mosaic variegated
aneuploidy syndrome]" — a **Chinese-language MVA case report**, surfaced incidentally by an
English-language query. Not fetched. Recorded because Task 3 is otherwise untouched, and
because it is direct evidence that the non-English cohort literature is real and reachable.

## Task 6 — surveillance after a first tumour

| # | Target | Route | Result |
|---|---|---|---|
| 42 | PubMed, 5 queries: SIOP-E Wilms surveillance; WBMRI in paediatric predisposition; AACR 2024 series; post-first-tumour/survivorship; **MVA/BUB1B radiosensitivity** | eutils esearch/esummary | ✅ All returned |
| 43 | Frebourg 2020, LFS/hTP53rc guidelines | efetch abstract | ✅ The non-ionising-surveillance precedent, with the "avoid genotoxic therapy in carriers" statement |
| 44 | Kratz 2017, LFS screening (Toronto protocol) | efetch abstract | ✅ Confirms AACR adoption of a modified Toronto protocol |
| 45 | Bhatia 2025, COG LTFU v6.0 review | efetch abstract | ✅ v6.0 added genetic-predisposition surveillance sections; covers survivors ≥2 y post-therapy |
| 46 | Nakano 2024 MVA section, re-read end to end | local file | ✅ **Silent on post-first-tumour surveillance.** No imaging modality for RMS; no WBMRI for MVA; no rationale for stopping renal US at 7 |

### Failures and gaps

| # | Target | Route | Outcome |
|---|---|---|---|
| F7 | **Hol et al. 2021 — the SIOP-E primary recommendation** (PMID 34134020, *Eur J Cancer*) | Europe PMC `search?query=EXT_ID:` | ❌ **UNOBTAINABLE.** `pmcid: None`, `isOpenAccess: N`, `inPMC: N` — Elsevier, closed, no open deposit. **The surveillance protocol this project recommends is cited second-hand through Nakano's summary and cannot be verified against its primary text.** |
| F8 | Same paper, via NCBI elink | `elink` pubmed→pmc | ❌ **FALSE LINK — fourth identifier trap.** Returned PMC13164404, which is *"Genetic and Epigenetic Drivers of Wilms Tumor Predisposition in Russian Pediatric Patients," Int J Mol Sci* **2026**. Same topic, so it would have read as corroboration. Caught by the mechanical title check before anything was quoted. Matrix **C15** |
| F9 | **MVA-specific radiosensitivity evidence** | PubMed targeted query | ⚠️ **NONE EXISTS (in English, on PubMed).** 5 hits, all wrong-product: radiation-induced PCS in carcinoma cells, BUB1B in breast-cancer HR repair, a mouse *Apc* QTL study, phototherapy on fibroblasts, visceral obesity. The guideline's advice rests on a **class** statement — "**many** of these genomic instability disorders" — that names A-T and NBS but **not MVA**. Matrix **C16** |
| F10 | COG LTFU v6.0 guideline content | not attempted | ⚠️ Separate document at survivorshipguidelines.org. Whether it names MVA or BUB1B is **unknown**. Named as an actionable gap (Q9) |

## Scope this pass did NOT cover

Tasks **2 (MVA cohort genotype–phenotype table)**, **3 (Japanese/Chinese PCS literature)** and
**5 (coverage re-costing)** of the brief are **untouched**. Everything recorded in Pass 3's
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

6. **The identifier trap has now fired four times, and the wrong record is always plausible.**
   Two PMID↔PMCID collisions (C7), one declared-vs-observed PDB chain range (C12), and now an
   elink PMCID for a paper with **no PMC deposit at all** (C15) — which landed on a paper about
   the very topic being researched. In every case the wrong content was coherent, on-topic, and
   by credible authors. **Careful reading has never once caught one of these; the mechanical
   title check has caught all four.** Treat Europe PMC's `search?query=EXT_ID:<pmid>` record as
   authoritative for open-access status, since it reports `pmcid`, `isOpenAccess` and `inPMC`
   directly and does not fabricate links.

