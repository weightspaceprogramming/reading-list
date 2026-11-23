#!/usr/bin/env python3
"""Build the annotated reading list and BibTeX from the guide's research records."""

import argparse
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://weightspaceprogramming.tech/library.json"
GUIDE = "https://weightspaceprogramming.tech"

GROUPS = [
    ("Foundations and formal compilation", [
        "fast-weight-memories", "a-neural-compiler", "thinking-like-transformers", "tracr",
    ]),
    ("Trained compilers and weight generators", [
        "hypernetworks", "hypter", "hypertuning", "hint", "text-to-lora",
        "code-to-lora", "program-as-weights", "compile-by-training",
    ]),
    ("LLM reasoning over weights and experimental feedback", [
        "sparks-weight-space-programming", "weight-space-programming-simple-tasks",
        "weightloop", "exploring-weight-space-programming", "weight-space-policy-verification",
        "interpretable-weight-space-programming", "weightbench", "zero-shot-structured-data",
        "weight-space-tractor-control", "weight-space-diffusion-editing",
        "weight-space-without-transformers", "weightcode",
    ]),
    ("Replications, criticism and responses", [
        "honnibal-sparks-critique", "goedecke-superhuman-critique", "willison-local-weight-reading",
        "weight-reading-audit", "sparks-response-to-comments", "replicating-weight-space-programming",
    ]),
    ("Tutorials, tools and collections", [
        "wsp-visual-tutorial", "wsp-agent-harnesses", "awesome-wsp-boom5426", "awesome-wsp-brighterr",
    ]),
]


def validate(data):
    entries = data["entries"]
    ids = [entry["id"] for entry in entries]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate research record ID")
    grouped = [entry_id for _, group in GROUPS for entry_id in group]
    if len(grouped) != len(set(grouped)):
        raise ValueError("An entry occurs in more than one reading-list section")
    if set(grouped) != set(ids):
        raise ValueError(f"Update GROUPS for added/removed records: {set(ids) ^ set(grouped)}")
    for entry in entries:
        for field in ("id", "title", "authors", "kind", "links", "bibtex"):
            if not entry.get(field):
                raise ValueError(f"Missing {field} in {entry.get('id', 'unknown record')}")
        if not entry.get("en", {}).get("summary"):
            raise ValueError(f"Missing summary in {entry['id']}")
        for link in entry["links"]:
            if not link["url"].startswith("https://"):
                raise ValueError(f"Expected a public HTTPS source in {entry['id']}")


def markdown(data):
    entries = {entry["id"]: entry for entry in data["entries"]}
    text = [
        "# Weight-Space Programming: Papers, Code, Models and Guides",
        "",
        "An annotated collection of research on representing and constructing programs in neural-network weights: formal compilation, trained weight generators, LLM reasoning over weights, and experimental feedback.",
        "",
        f"[Read the guide]({GUIDE}/) · [Search the collection]({GUIDE}/research/) · [BibTeX](citations.bib) · [JSON](library.json) · [Dated releases](https://github.com/weightspaceprogramming/reading-list/releases)",
        "",
        f"{len(entries)} resources. Updated {data['updated']}.",
        "",
        "## Start here",
        "",
        f"- [How neural networks represent programs]({GUIDE}/learn/how-neural-networks-represent-programs/) — concepts and concrete examples.",
        f"- [Compare construction methods]({GUIDE}/learn/comparing-methods/) — construction inputs, training, saved artifacts and execution.",
        f"- [Choose a reading path]({GUIDE}/learn/reading-paths/) — routes through the literature.",
        f"- [Research history]({GUIDE}/history/) — contributions, dates and original sources.",
        f"- [Build a reusable neural function]({GUIDE}/build/reusable-neural-function/) — a Program-as-Weights example with a [playground](https://programasweights.com/playground).",
        "",
        "## Contents",
        "",
    ]
    for name, _ in GROUPS:
        anchor = name.lower().replace(",", "").replace(" ", "-")
        text.append(f"- [{name}](#{anchor})")
    text.extend(["", "Dates below are the first public dates recorded for each resource; conference years are shown separately.", ""])
    for name, ids in GROUPS:
        text.extend([f"## {name}", ""])
        for entry_id in ids:
            entry = entries[entry_id]
            primary = next((link for link in entry["links"] if link["kind"] == "paper"), entry["links"][0])
            text.extend([
                f"### [{entry['title']}]({primary['url']})",
                "",
                ", ".join(entry["authors"]) + ".",
                "",
                " · ".join(value for value in [entry.get("venue"), entry.get("date")] if value),
                "",
                entry["en"]["summary"],
                "",
                " · ".join([f"[{link['label']}]({link['url']})" for link in entry["links"]] + [f"[Research profile]({GUIDE}/research/{entry_id}/)"]),
                "",
            ])
    text.extend([
        "## Use the collection",
        "",
        "Download `library.json` for stable record IDs, authors, dates, venues, summaries, method descriptions, source links and BibTeX. The `mechanisms`, `operations` and `artifacts` fields support filtering and analysis. `citations.bib` contains the citations for the collected works.",
        "",
        "Cite the original work when discussing its contribution. To identify the collection version used in an analysis, link to a dated release or a commit.",
        "",
        "To rebuild the README and citations from a local copy of the research records:",
        "",
        "```sh",
        "python3 scripts/sync.py --source /path/to/library.json",
        "python3 scripts/sync.py --check",
        "```",
        "",
        f"Running `python3 scripts/sync.py` without `--source` downloads the guide's public [JSON export]({SOURCE_URL}). Python 3 and its standard library are sufficient.",
        "",
        "## Contribute",
        "",
        "Suggest a paper, implementation, model, critique or correction through an issue or pull request. Include the primary source and a short explanation of the connection. See [CONTRIBUTING.md](CONTRIBUTING.md) for the record format and checks.",
        "",
        f"Edited by [Yuntian Deng](https://yuntiandeng.com/), a coauthor of [Program-as-Weights](https://programasweights.com/). Read more about the guide on its [About page]({GUIDE}/about/).",
        "",
    ])
    return "\n".join(text)


def outputs(data):
    validate(data)
    return {
        "library.json": json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        "citations.bib": "\n".join(entry["bibtex"].rstrip() for entry in data["entries"]) + "\n",
        "README.md": markdown(data),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", help="Local JSON file or public HTTPS JSON URL")
    parser.add_argument("--check", action="store_true", help="Check existing exports without downloading or writing")
    args = parser.parse_args()
    if args.check and args.source:
        parser.error("--check uses the existing library.json; do not supply --source")
    source = args.source or (str(ROOT / "library.json") if args.check else SOURCE_URL)
    if source.startswith("https://"):
        with urllib.request.urlopen(source, timeout=45) as response:
            data = json.load(response)
    else:
        data = json.loads(Path(source).read_text())
    rendered = outputs(data)
    if args.check:
        mismatches = [name for name, content in rendered.items() if not (ROOT / name).exists() or (ROOT / name).read_text() != content]
        if mismatches:
            raise SystemExit("Exports differ: " + ", ".join(mismatches))
        print(f"Checked {len(data['entries'])} records and matching README, JSON and BibTeX.")
    else:
        for name, content in rendered.items():
            (ROOT / name).write_text(content)
        print(f"Generated {len(data['entries'])} annotated entries and matching exports.")


if __name__ == "__main__":
    main()
