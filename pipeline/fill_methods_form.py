#!/usr/bin/env python3
"""Write the methods-description answers into the organisers' xlsx.

The answers live in submissions/methods_description.md, which is the source of
truth because it is diffable in the public repo. This script parses that file's
'### <question>' sections and writes them into column B of the organisers' blank
form, preserving the original workbook rather than rebuilding one, so the file the
panel opens is the file they issued.

Usage:
    python3 fill_methods_form.py --md ../submissions/methods_description.md \
        --template ../literature/methods_description_form.xlsx \
        --out ../submissions/methods_description_gummietech.xlsx
"""
import argparse
import re
import shutil
import zipfile
import xml.etree.ElementTree as ET

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace("", NS)
Q = f"{{{NS}}}"


def parse_md(path):
    """Return {'Track 1': [(question, answer), ...], 'Track 2': [...]}."""
    text = open(path).read()
    out = {}
    for track in ("Track 1", "Track 2"):
        m = re.search(rf"^# {track} \(.*?$(.*?)(?=^# Track |\Z)", text, re.S | re.M)
        if not m:
            continue
        body = m.group(1)
        pairs = []
        # the two leading fields are bolded, not '###' headed
        for label, pat in (("Team name", r"\*\*Team name:\*\*\s*(.+)"),
                           ("Model number", r"\*\*Model number:\*\*\s*(.+?)(?=\n\n)")):
            mm = re.search(pat, body, re.S)
            if mm:
                pairs.append((label, mm.group(1).strip()))
        for mm in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", body, re.S | re.M):
            pairs.append((mm.group(1).strip(), clean(mm.group(2))))
        out[track] = pairs
    return out


def clean(s):
    """Markdown -> plain text suitable for a spreadsheet cell."""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s, flags=re.S)
    s = re.sub(r"\*(.+?)\*", r"\1", s, flags=re.S)
    s = re.sub(r"`(.+?)`", r"\1", s, flags=re.S)
    s = re.sub(r"^\s*[-*]\s+", "- ", s, flags=re.M)
    s = re.sub(r"\n{3,}", "\n\n", s)
    # unwrap hard-wrapped prose but keep blank lines and list breaks
    s = re.sub(r"(?<![\n\-])\n(?![\n\-])", " ", s)
    return s.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    answers = parse_md(a.md)
    shutil.copy(a.template, a.out)

    zin = zipfile.ZipFile(a.template)
    strings = [re.sub(r"<[^>]+>", "", x)
               for x in re.findall(r"<si>(.*?)</si>", zin.read("xl/sharedStrings.xml").decode(), re.S)]

    # Explicit positional mapping rather than fuzzy heading matching. The form's
    # questions are long prose and the md headings are abbreviations of them, so
    # substring matching silently dropped two thirds of the answers. The md is
    # authored in the form's own question order, and this asserts that the counts
    # agree, so a drift in either file fails loudly instead of writing a partial form.
    sheets = {"xl/worksheets/sheet1.xml": ("Track 1", 7, 19),
              "xl/worksheets/sheet2.xml": ("Track 2", 7, 17)}
    new_parts = {}
    added = []
    for sheet, (track, first_row, last_row) in sheets.items():
        root = ET.fromstring(zin.read(sheet))
        pairs = answers.get(track, [])
        expected = last_row - first_row + 1
        if len(pairs) != expected:
            raise SystemExit(
                f"{track}: {len(pairs)} answers in the markdown but {expected} "
                f"questions in rows {first_row}-{last_row} of the form. "
                f"Parsed: {[q for q, _ in pairs]}")
        by_row = {}
        for row in root.iter(f"{Q}row"):
            r = int(row.get("r"))
            if first_row <= r <= last_row:
                by_row[r] = row
        for i, (qtext, ans) in enumerate(pairs):
            r = first_row + i
            row = by_row.get(r)
            if row is None:
                raise SystemExit(f"{track}: row {r} missing from the template")
            # confirm the target row actually carries a question in column A
            qa = None
            for c in row.iter(f"{Q}c"):
                if (c.get("r") or "") == f"A{r}" and c.get("t") == "s":
                    qa = strings[int(c.findtext(f"{Q}v"))]
            if qa is None:
                raise SystemExit(f"{track}: row {r} has no question text in column A")
            # The template already carries empty B cells (the "Answers" column is
            # pre-formatted). Appending a second <c r="Bn"> produced duplicate cell
            # references in one row, which Excel may reject outright. Reuse the
            # existing cell when there is one, and only create it when there is not.
            bcell = None
            for c in row.findall(f"{Q}c"):
                if (c.get("r") or "") == f"B{r}":
                    bcell = c
                    break
            if bcell is None:
                bcell = ET.SubElement(row, f"{Q}c")
                bcell.set("r", f"B{r}")
            else:
                for child in list(bcell):
                    bcell.remove(child)
            bcell.set("t", "inlineStr")
            is_el = ET.SubElement(bcell, f"{Q}is")
            t_el = ET.SubElement(is_el, f"{Q}t")
            t_el.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            t_el.text = ans
            added.append(f"{track} B{r}  <- {qtext[:44]:44s} | form asks: {qa[:44]}")
        new_parts[sheet] = ET.tostring(root, encoding="UTF-8", xml_declaration=True)

    zout_name = a.out
    zin2 = zipfile.ZipFile(a.template)
    with zipfile.ZipFile(zout_name, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin2.infolist():
            data = new_parts.get(item.filename) or zin2.read(item.filename)
            zo.writestr(item, data)
    print(f"wrote {zout_name}")
    for line in added:
        print("  " + line)
    print(f"total answers written: {len(added)}")


if __name__ == "__main__":
    main()
