# Targeted realignment: an honest re-costing

**Task 5 of `gap_closure_brief.md`. No alignment was run in this task, and none is
proposed as part of the submission.** The deliverable is a corrected claim.

## The claim being corrected

`README.md`, `pipeline/README.md` and `data-notes/track1_findings.md` all stated that the
callability limitation **"cannot be closed by acquiring data,"** and justified it on RAM:
a human-genome BWA index needs ~6–7 GB (minimap2 ~11 GB, bwa-mem2 ~40 GB) against 8 GB
installed.

**That justification does not survive scrutiny, because you do not need a whole-genome
index.** The question is callability across a 9-gene panel and a PGx position list, not
across the genome. A reduced reference containing only those regions has an index four
orders of magnitude smaller than the objection assumes:

| Reference | Approx. size | BWA index RAM (~5.5 bytes/base) |
|---|---|---|
| GRCh38, whole genome | 3.1 Gb | ~6–7 GB — the figure the old claim used |
| BUB1B padded region alone (chr15:40,158,984–40,223,137) | 64.2 kb | ~350 KB |
| A generous reduced reference (both panels + PGx regions) | ~5 Mb | ~30 MB |

Against 8 GB installed, the RAM objection is not close to binding. **The claim as written
was stronger than the situation warranted, and it is withdrawn.**

## Machine constraints, re-measured 2026-09-04

Re-measured rather than carried forward, and one figure has moved materially:

| | Repo previously said | Measured 2026-09-04 |
|---|---|---|
| RAM | 8 GB | **8 GB** (`hw.memsize` = 8589934592) |
| Cores | 8 | **8** |
| Free disk | 33 GB (README), 30 GB (brief, 2026-09-02) | **20 GB** |
| Aligner present | none | **none** — bwa, bwa-mem2, minimap2, bowtie2, hisat2 all absent |
| `samtools` | installed | **installed** (`/opt/homebrew/bin/samtools`) |

## What the real costs are

The RAM objection dies. Three real costs replace it, and they are different in kind —
none of them is a memory ceiling:

1. **Transfer.** ~78.9 GB of FASTQ across 8 files / 4 lanes must cross the network.
2. **Disk.** At **20 GB free**, the FASTQ cannot be stored at all. Streaming is not an
   optimisation here, it is the only option.
3. **CPU — and this is the one that actually binds.** A small reference does not make the
   alignment small. The aligner must examine **every read in the 79 GB**, not just the
   ones belonging to the target, because it cannot know which those are until it has tried
   to align them. The CPU cost is that of a whole-genome alignment even though the
   reference is a few megabases. On 8 cores that is a multi-day run.

All three are costs that a larger machine or a cloud instance dissolves. That is precisely
why the honest statement is **"feasible by a route this analysis did not run"** and not
"cannot be closed."

## The real objection is scientific, not resource-based

Decoy-free targeted realignment has a specific failure mode. **MAPQ is computed relative
to the reference you provide.** A read that truly originates from a paralogous locus
elsewhere in the genome has nowhere else to go when that locus is absent from the
reference — so it maps to the single copy that *is* present, uniquely and with high
confidence. The aligner reports a high MAPQ for a read that is in the wrong place. The
result is **false coverage that is indistinguishable from real coverage**, which is worse
than no coverage track at all, because it would silently convert this report's honest
"absence of a call is not absence of coverage" into a confident wrong answer.

Segmental duplication content is the standard proxy for that risk, since misalignment
needs high nucleotide identity over read length. Queried live against the UCSC
`genomicSuperDups` track (hg38), 2026-09-04:

| Locus | Window | Segdup records | Verdict |
|---|---|---|---|
| **BUB1B gene body** | chr15:40,160,984–40,221,137 (60.2 kb) | **0** | Low risk |
| **BUB1B ±2 kb padded** | chr15:40,158,984–40,223,137 | **0** | Low risk |
| BUB1B ±40 kb neighbourhood | chr15:40,150,000–40,240,000 | 1, at 40,153,334–40,155,456 (97.1% to chr15:40,123,488–40,125,292) | 5.5 kb **upstream** of the padded region — outside it |
| **CYP2D6** | chr22:42,120,000–42,155,000 (35 kb) | **6**, incl. a 9.0 kb ↔ 10.5 kb pair at **97.0%** identity and further pairs at 91.0–91.7% | **Genuinely fatal** |

```bash
# reproduce either row
curl -s "https://api.genome.ucsc.edu/getData/track?genome=hg38;track=genomicSuperDups;chrom=chr15;start=40160984;end=40221137"
curl -s "https://api.genome.ucsc.edu/getData/track?genome=hg38;track=genomicSuperDups;chrom=chr22;start=42120000;end=42155000"
```

**This splits the reduced-reference route in two, and the two halves get different
answers:**

- **For the BUB1B callability question it is sound.** Zero segmental duplications in the
  gene body or the padded region. The nearest one is upstream and outside. There is no
  high-identity competitor anywhere for reads from this locus to have come from.
- **For the pharmacogenomic question it is not.** CYP2D6/CYP2D7 is the textbook case of
  the failure mode, and the numbers above are why. A decoy-free targeted realignment
  would produce a confident, clean, wrong CYP2D6 call — the same class of error as the
  `--missing-to-ref` result already reported in Track 2 §4.2.

**Note on BUB1B-PAK6.** The readthrough locus (`ENSG00000259288`, chr15:40,218,500–
40,264,890) overlaps BUB1B's 3′ end, and `p.Asn1002Lys` at chr15:40,220,612 sits inside
that overlap. This is **not** a misalignment risk and should not be reported as one: a
readthrough transcript is an annotation over the *same* genomic sequence, not a second
copy of it. It affects transcript-level annotation, which Track 1 already handles by
reporting across all 22 BUB1B transcripts. It does not affect alignment.

## The corrected claim

> Producing a coverage track is **feasible by a route this analysis did not run** —
> alignment of the 79 GB FASTQ against a reduced reference, whose index is trivially small
> and for which the RAM objection previously stated does not apply. The costs are
> ~79 GB of transfer, streaming (20 GB free disk cannot hold the input), and a multi-day
> CPU run on 8 cores. For **BUB1B the route is scientifically sound** — zero segmental
> duplications in the padded region. For **CYP2D6 it is not**, and a targeted realignment
> there would manufacture false coverage at high MAPQ. The limitation is therefore not
> closed, and it is **differently open** than this repository previously stated.

## What survives the correction unchanged

Two things in the previous text were right and are not weakened by any of the above:

- **Short reads cannot resolve phase across ~11 kb.** The two variants are beyond fragment
  span; read-backed phasing faces the identical physical limit. No alignment changes this.
- **The dataset genuinely contains no BAM or CRAM.** 13 files, 79.1 GB, 78.9 GB of it
  FASTQ. The hackathon site's "optionally in BAM/CRAM" description is wrong and the
  manifest wins.
