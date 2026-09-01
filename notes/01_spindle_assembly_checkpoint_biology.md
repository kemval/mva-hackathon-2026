# Synthesis Notes: Mitosis & the Spindle Assembly Checkpoint (SAC)

*Synthesized from general cell-biology knowledge (equivalent territory to Molecular Biology of the Cell, Alberts et al., mitosis/cell-cycle chapters). Written for this project rather than copied from any copyrighted source — treat as a study primer, not a citation-grade reference. For textbook-grade depth, consult Molecular Biology of the Cell directly.*

## Why this matters for MVA

BUB1B, CEP57, and TRIP13 — the three genes known to cause Mosaic Variegated Aneuploidy — all converge on one cellular process: making sure chromosomes segregate correctly during mitosis. Understanding this pathway is the load-bearing piece of both hackathon tracks: it's what lets you (a) argue convincingly *why* a candidate variant is pathogenic (Track 1 write-up), and (b) reason from mechanism to therapeutic hypothesis (Track 2).

## The core problem the SAC solves

During mitosis, replicated chromosomes (sister chromatids) must attach to spindle microtubules via kinetochores, then be pulled apart symmetrically — one copy to each daughter cell. If chromatids separate before every kinetochore is properly attached to the spindle, the result is **aneuploidy**: daughter cells with the wrong number of chromosomes. The Spindle Assembly Checkpoint (SAC, a.k.a. Mitotic Checkpoint) is the surveillance system that delays anaphase onset until every kinetochore is correctly attached and under tension.

## Key molecular players

- **BUB1B / BubR1**: A core SAC kinase. Unattached kinetochores generate a "wait" signal; BubR1 is a central component of the resulting Mitotic Checkpoint Complex (MCC), which inhibits the Anaphase-Promoting Complex/Cyclosome (APC/C). Without functional BubR1, cells can't sustain the checkpoint signal, so anaphase proceeds even when chromosomes aren't properly attached — directly causing chromosome missegregation and mosaic aneuploidy. BubR1 also has a separate, checkpoint-independent role in stabilizing kinetochore-microtubule attachments.
- **CEP57**: A centrosomal protein involved in microtubule nucleation/stabilization at the centrosome. Its loss affects spindle pole integrity and proper microtubule dynamics, producing aneuploidy through a distinct route from BUB1B — this is consistent with CEP57-MVA (MVA type 2) having a different phenotype profile (e.g. rhizomelic limb shortening, less cancer predisposition) than BUB1B-MVA.
- **TRIP13**: An AAA+ ATPase that recycles MAD2 from its checkpoint-active "closed" conformation back to the inactive "open" conformation once the checkpoint is satisfied. TRIP13 dysfunction disrupts the checkpoint's ability to properly turn off (or, depending on the specific defect, to properly assemble), again undermining faithful chromosome segregation.

## APC/C, the real "go" switch

The Anaphase-Promoting Complex/Cyclosome (APC/C) is a ubiquitin ligase that, once activated, tags securin and cyclin B for degradation — triggering separase activation (which cleaves the cohesin holding sister chromatids together) and mitotic exit. The SAC's entire job is to keep the APC/C inhibited (via the MCC, of which BubR1 is a core subunit) until every kinetochore is attached. This is the direct mechanistic link between "BUB1B is broken" and "chromosomes separate at the wrong time."

**Domain-level detail worth knowing for variant interpretation** (verified 2026-08-31 against UniProt O60566 direct query + Kops et al. 2012, *Dev Cell*, PMID 22698286, "The vertebrate mitotic checkpoint protein BUBR1 is an unusual pseudokinase" — both primary sources, not from memory): BubR1 is 1050 aa. UniProt's feature table confirms a BUB1 N-terminal domain (62-226), a D-box motif (224-232), and a **C-terminal protein kinase (pseudokinase) domain spanning residues 766-1050** — roughly the last quarter of the protein. UniProt's feature table alone does *not* list a KEN-box, but Kops et al. 2012 directly confirms one exists: "preservation of the ancestral, amino-terminal KEN box" is a defining feature of the BUBR1/Mad3 lineage (as opposed to the paralogous BUB1, which instead preserved the kinase domain in most species) — human BUBR1 is the exception that kept *both* the KEN-box and a catalytically-intact kinase domain (though Kops et al. show the kinase activity itself is dispensable for BUBR1's checkpoint function; ATP-binding residues instead matter for conformational stability). Point-of-fact lesson: a specific domain-existence claim can be true even when one database's (UniProt's) feature curation doesn't list it — cross-check against primary literature before concluding a claim is wrong just because one source is silent on it.

A truncating or frameshift variant that removes the C-terminal kinase domain (766-1050) is a stronger loss-of-function candidate than one only affecting an unstructured linker region — this kind of domain-mapping is exactly what strengthens a Track 1 "depth of understanding" argument.

## Downstream consequences of chronic SAC weakening (not full loss — MVA patients survive, so this is typically hypomorphic/partial function)

1. **Mosaic aneuploidy**: because the checkpoint is weakened rather than absent, missegregation happens stochastically in some cell divisions and not others — producing a mosaic pattern of trisomic/monosomic cells across tissues, exactly matching the disease name.
2. **Chromosomal instability (CIN)** creates ongoing genomic stress: aneuploid cells experience proteotoxic stress (imbalanced gene dosage), replication stress, and DNA damage.
3. **Cellular senescence**: chronically stressed/damaged cells frequently enter a senescent state (permanent cell-cycle arrest, often p16^INK4a/p21-driven) rather than dying outright. Accumulation of senescent cells — which secrete inflammatory factors (the "senescence-associated secretory phenotype," SASP) — is mechanistically linked to tissue dysfunction and premature-aging-like phenotypes. This is the direct bridge to the Baker et al. 2011 BubR1-progeroid-mouse literature and the senolytic drug-repurposing hypothesis (see `notes/03_track2_mechanism_to_drug_bridge.md` once written, and `literature/04_baker2011_senescence_clearance.md`).
4. **Cancer predisposition**: aneuploid, genomically unstable cells are also a substrate for oncogenic evolution — a subset of aneuploid clones can acquire growth advantages instead of senescing, which is the accepted explanation for why BUB1B-MVA in particular carries elevated childhood cancer risk (classically rhabdomyosarcoma, Wilms tumor, leukemia).
5. **Growth failure / microcephaly**: proliferative tissues that depend on high mitotic fidelity during development (notably the brain, given how many neural progenitor divisions occur prenatally) are disproportionately affected by chronic missegregation and the resulting senescence/apoptosis, which is the leading mechanistic explanation for the microcephaly and growth retardation seen across MVA subtypes.

## Verified structure: CIN is a fork, not a chain (confirmed via `/graphify query`, 2026-08-31)

Tracing the local knowledge graph (`~/mva-hackathon-2026/graphify-out/`) between these concepts turned up a structural point worth being precise about in the write-up:

```
graphify path "Cellular senescence" "Chromosomal instability (CIN)" --undirected
  → Cellular senescence <--[references]-- Chromosomal instability (CIN)   (1 hop)

graphify path "Cellular senescence" "Cancer predisposition" --undirected
  → Cellular senescence <--[references]-- Chromosomal instability (CIN) --[references]--> Cancer predisposition   (2 hops)
```

**Senescence and cancer predisposition are siblings off the same CIN parent node, not a sequential chain.** CIN is the single shared consequence of BUB1B/SAC dysfunction; from there, a genomically-stressed aneuploid cell resolves into one of two separate fates:

```
                              ┌──> Cellular senescence  (common outcome; most stressed cells)
BubR1/SAC dysfunction ──> CIN ┤
                              └──> Cancer predisposition  (rare outcome; a clone evades senescence/death and gains a growth advantage)
```

**Why this matters for the Track 2 report**: it would be a mechanistic error to write "senescence leads to cancer" — they are not causally linked to each other in this pathway; both are downstream of CIN but via different, non-overlapping cell-fate decisions. This has a direct consequence for how the report should be structured:

- The senescence branch is the one an NAD+/NMN or senolytic intervention targets (see `notes/04_drug_repurposing_methodology.md`) — restoring BubR1 (NMN) or clearing senescent cells (senolytics) addresses the aging-like/tissue-dysfunction phenotype.
- The cancer-predisposition branch is a **separate concern that a senescence-targeting drug is not expected to address** — an intervention that clears senescent cells or restores BubR1 doesn't obviously reduce the risk from the clones that already escaped senescence. This branch calls for a surveillance/screening argument instead (cite the AACR "Update on Recommendations for Cancer Screening and Surveillance in Children with Genomic Instability Disorders" paper and George's Story precedent from `literature/04_mva_society_bibliography.md` and `literature/03_mva_society_site_content.md`), not a repurposing hypothesis.
- Conflating the two branches into "treat senescence to reduce cancer risk" would overstate the therapeutic hypothesis's scope beyond what the mechanism actually supports — worth flagging explicitly as a limitation in the report rather than eliding it.

## Bridging general mechanism to the case's own variants: one domain, stated twice (traced via `/graphify`, 2026-08-31)

Tracing the knowledge graph for the node that bridges the SAC-mechanism community to the case's confirmed variants surfaced a gap worth being explicit about in the write-up, not just a connection:

```
graphify explain "BUB1B / BubR1"
  → 1 hop to "BubR1 C-terminal (pseudo)kinase domain (766-1050)"   (this note's general mechanism)

graphify explain "p.Leu737Ter"  /  graphify explain "p.Asn1002Lys"
  → 1 hop each to "BubR1 kinase domain (766-1050)"                  (data-notes/track1_findings.md + the methods report)

graphify path "BubR1 kinase domain (766-1050)" "BubR1 C-terminal (pseudo)kinase domain (766-1050)" --undirected
  → 5 hops, routed through Kops et al. 2012 and the trust-audit node — no direct edge
```

**These are the same physical protein region** — both citations resolve to UniProt O60566 residues 766-1050 — but they exist in this project as two separately-written facts: this note describes the domain as general SAC/mitotic-checkpoint mechanism, while `data-notes/track1_findings.md` and the methods report describe the same residue range as the specific thing `p.Leu737Ter` truncates and `p.Asn1002Lys` falls inside. Nothing in either write-up currently states outright that they're the same fact — a reader has to infer it.

**Why this matters for the Track 2 report**: don't leave this implicit. The mechanistic argument for *why the child's specific genotype* causes SAC dysfunction (and, downstream, the CIN → senescence branch this note describes above) depends on this being one continuous chain, not two adjacent-but-separate claims:

```
p.Leu737Ter (truncates before residue 766)  ─┐
p.Asn1002Lys (missense, inside 766-1050)     ├──> removes/disrupts the C-terminal kinase domain (766-1050)
                                              │      = the same domain this note's SAC/MCC mechanism section describes
                                              └──> SAC dysfunction ──> CIN ──> {senescence, cancer predisposition} (see fork above)
```

State this explicitly as one sentence in the Track 2 mechanism section (e.g. "the domain destabilized in this specific case is the same C-terminal kinase domain the SAC/MCC checkpoint mechanism depends on for BubR1 function") rather than assuming the reader connects the general-biology paragraph to the case-specific variant table on their own.

## How to use this section in the actual write-ups

- **Track 1**: cite the specific domain/motif disrupted by the confirmed variant, and state explicitly which of the three genes' mechanisms is implicated and why the phenotype (from the case's HPO terms) is consistent with that specific gene's mechanism (e.g., presence/absence of cancer predisposition and limb anomalies distinguishes BUB1B from CEP57).
- **Track 2**: structure the report as two clearly separated sections mirroring the fork above — (1) a therapeutic hypothesis (NMN/senolytics) for the senescence/tissue-dysfunction branch, and (2) a surveillance/impact discussion (not a drug proposal) for the cancer-predisposition branch. Don't just search "BUB1B inhibitor" — search the *downstream consequences* on each branch separately, since BUB1B itself isn't really druggable in a way that helps a patient who already has a germline loss-of-function variant.
