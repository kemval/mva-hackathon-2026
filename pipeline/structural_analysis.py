#!/usr/bin/env python3
"""Structural characterisation of BUB1B p.Asn1002Lys against the AlphaFold model.

Task 1 of pipeline/gap_closure_brief.md. The Track 2 thesis is that this variant lowers
BubR1 *abundance*; the in-silico scores already held (AlphaMissense, REVEL, CADD) predict
*pathogenicity*, which is a different quantity. This script asks the structural question
instead: where does N1002 sit, what does it hold together, and what would Asn->Lys do there.

Comparators are the MVA alleles Suijkerbuijk et al. 2010 assayed for protein level, split
by their measured result, so that burial and position are calibrated against alleles with
a known abundance phenotype rather than asserted in isolation.

Requires: biopython, numpy. Network: AlphaFold EBI (model), MyVariant.info (conservation).

    python3 structural_analysis.py [--workdir DIR]
"""
import argparse, json, os, sys, urllib.request, warnings
warnings.filterwarnings("ignore")
import numpy as np
from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley

UNIPROT = "O60566"                      # human BUB1B / BubR1, 1050 aa
AF_API = f"https://alphafold.ebi.ac.uk/api/prediction/{UNIPROT}"
MYVARIANT = ("https://myvariant.info/v1/variant/chr15:g.40220612T>G"
             "?fields=dbnsfp.gerp%2B%2B,dbnsfp.phylop,dbnsfp.phastcons,dbnsfp.provean,"
             "dbnsfp.vest4,dbnsfp.alphamissense,dbnsfp.revel&assembly=hg38")
KINASE_DOMAIN = (766, 1050)             # UniProt O60566 feature range
SITE = 1002

# Suijkerbuijk 2010: which MVA alleles lowered BubR1 protein level, and which did not.
COMPARATORS = [
    (909,  "I909T",  "destabilising (abundance rescue restored checkpoint)"),
    (814,  "R814H",  "destabilising"),
    (1012, "L1012P", "destabilising (abundance rescue restored checkpoint)"),
    (727,  "R727C",  "destabilising"),
    (921,  "Q921H",  "NO effect - 'indistinguishable from wild-type'"),
    (550,  "R550Q",  "NO effect on protein level"),
    (155,  "Y155C",  "NO effect on protein level"),
    (1004, "N1004S", "gnomAD standing variation, AF 6.0e-4 - tolerated control"),
]

# Tien et al. 2013, theoretical maximum accessible surface area (A^2)
MAXASA = {'ALA':129,'ARG':274,'ASN':195,'ASP':193,'CYS':167,'GLU':223,'GLN':225,'GLY':104,
          'HIS':224,'ILE':197,'LEU':201,'LYS':236,'MET':224,'PHE':240,'PRO':159,'SER':155,
          'THR':172,'TRP':285,'TYR':263,'VAL':174}


def fetch(url, path, binary=False):
    if os.path.exists(path):
        return path
    with urllib.request.urlopen(url, timeout=120) as r:
        data = r.read()
    with open(path, "wb" if binary else "w") as fh:
        fh.write(data if binary else data.decode())
    return path


def load_model(workdir):
    """Resolve the current AlphaFold model version via the API rather than guessing a
    filename - the v4 URL 404s, the API reports the live version."""
    meta = json.load(open(fetch(AF_API, os.path.join(workdir, "af_api.json"))))
    entry = meta[0] if isinstance(meta, list) else meta
    pdb = fetch(entry["pdbUrl"], os.path.join(workdir, "af_model.pdb"), binary=True)
    print(f"AlphaFold model: {entry['entryId']} v{entry['latestVersion']} "
          f"({entry.get('modelCreatedDate','?')[:10]})\n")
    model = PDBParser(QUIET=True).get_structure("af", pdb)[0]
    ShrakeRupley().compute(model, level="R")
    chain = list(model)[0]
    return {r.id[1]: r for r in chain if r.id[0] == " "}


def rsa(res, i):
    return 100.0 * res[i].sasa / MAXASA[res[i].get_resname()]


def report(res):
    lo, hi = KINASE_DOMAIN
    tgt = res[SITE]

    print("=== Burial, and how it compares to alleles with a known abundance phenotype ===")
    print(f"{'site':<10} {'res':<5} {'SASA':>7} {'RSA%':>7} {'pLDDT':>6}  {'':<9} class")
    rows = [(SITE, f"N{SITE}K", "<-- PROBAND")] + COMPARATORS
    for i, label, cls in rows:
        v = rsa(res, i)
        tag = "BURIED" if v < 20 else ("partial" if v < 50 else "EXPOSED")
        print(f"{label:<10} {res[i].get_resname():<5} {res[i].sasa:>7.1f} {v:>7.1f} "
              f"{res[i]['CA'].get_bfactor():>6.1f}  {tag:<9} {cls}")

    dom = [i for i in range(lo, hi + 1) if i in res]
    vals = np.array([rsa(res, i) for i in dom])
    pct = 100.0 * (vals < rsa(res, SITE)).sum() / len(vals)
    print(f"\nBurial needs a denominator: pseudokinase domain {lo}-{hi} has median RSA "
          f"{np.median(vals):.1f}% and {100.0*(vals<20).sum()/len(vals):.0f}% of residues "
          f"below 20%.\nN{SITE} at RSA {rsa(res,SITE):.1f}% is the {pct:.0f}th percentile "
          f"- buried, but NOT unusually so for this domain.")

    print(f"\n=== Side-chain hydrogen bonds of Asn{SITE} (N/O pairs within 3.5 A) ===")
    hb = []
    for r in res.values():
        if r.id[1] == SITE:
            continue
        for a in r:
            if a.element not in ("N", "O"):
                continue
            for b in tgt:
                if b.get_name() not in ("OD1", "ND2"):
                    continue
                d = np.linalg.norm(a.coord - b.coord)
                if d < 3.5:
                    hb.append((d, r.id[1], r.get_resname(), a.get_name(), b.get_name()))
    for d, i, rn, an, bn in sorted(hb):
        print(f"  Asn{SITE}.{bn:<3} -- {rn}{i}.{an:<3}  {d:.2f} A")
    print(f"  {len(hb)} bond(s). Lys has no acceptor, so any OD1-mediated bond is lost outright.")

    print(f"\n=== Environment: what a longer, positively charged side chain enters ===")
    cb = tgt["CB"].coord
    for r in res.values():
        if r.id[1] == SITE or r.get_resname() not in ("PHE", "TRP", "TYR", "HIS"):
            continue
        d = min(np.linalg.norm(a.coord - cb) for a in r if a.element != "H")
        if d < 8.0:
            print(f"  {r.get_resname()}{r.id[1]:<5} {d:.1f} A from CB   (RSA {rsa(res,r.id[1]):.0f}%)")

    print(f"\n=== Distance from N{SITE}: do the destabilising alleles cluster in 3D? ===")
    print(f"{'allele':<10} {'CA-CA':>8} {'min-atom':>9}  class")
    for i, label, cls in COMPARATORS:
        dca = np.linalg.norm(res[i]["CA"].coord - tgt["CA"].coord)
        dmin = min(np.linalg.norm(a.coord - b.coord)
                   for a in res[i] for b in tgt if a.element != "H" and b.element != "H")
        print(f"{label:<10} {dca:>8.1f} {dmin:>9.1f}  {cls}")

    print(f"\n=== Local secondary structure (CA(i)-CA(i+4); <6.5 A helical) ===")
    for i in range(SITE - 8, SITE + 10):
        if i in res and i + 4 in res:
            d = np.linalg.norm(res[i]["CA"].coord - res[i + 4]["CA"].coord)
            cls = "helix" if d < 6.5 else ("extended" if d > 10.5 else "turn/coil")
            mark = "  <--" if i == SITE else ""
            print(f"  {i:>4} {res[i].get_resname():<4} {d:>5.1f}  {cls}{mark}")


def conservation(workdir):
    print("\n=== Conservation at the nucleotide/residue level (dbNSFP via MyVariant.info) ===")
    try:
        d = json.load(open(fetch(MYVARIANT, os.path.join(workdir, "conservation.json"))))
    except Exception as exc:                                  # network or field change
        print(f"  UNAVAILABLE: {exc}")
        return
    d = d.get("dbnsfp", {})
    for key in ("gerp++", "phylop", "phastcons", "provean", "vest4", "alphamissense"):
        v = d.get(key)
        if v:
            print(f"  {key}: {json.dumps(v)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=".", help="cache directory for downloads")
    args = ap.parse_args()
    os.makedirs(args.workdir, exist_ok=True)
    res = load_model(args.workdir)
    if SITE not in res or res[SITE].get_resname() != "ASN":
        sys.exit(f"residue {SITE} is not ASN in the model - check the isoform")
    report(res)
    conservation(args.workdir)
    print("\nNOTE: no experimental structure covers residue 1002. The PDB entries "
          "cross-referenced\nto O60566 that declare chains '1-1050' (5KHU, 6TLJ) model only "
          "26-479 and 19-345\nrespectively - the declared range is the entity length, not "
          "the observed residues.\nEvery number above is therefore predicted structure, not "
          "measured structure.")


if __name__ == "__main__":
    main()
