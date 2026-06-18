from __future__ import annotations

import csv
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_OUT = ROOT / "seo-page-metadata-audit-final.csv"
MD_OUT = ROOT / "seo-page-metadata-audit-final.md"


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title_parts: list[str] = []
        self.h1_parts: list[str] = []
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self.in_title = True
        elif tag == "h1" and not self.h1_parts:
            self.in_h1 = True
        elif tag == "meta":
            self.meta.append(attr_map)
        elif tag == "link":
            self.links.append(attr_map)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_h1:
            self.h1_parts.append(data)

    @property
    def title(self) -> str:
        return clean(" ".join(self.title_parts))

    @property
    def h1(self) -> str:
        return clean(" ".join(self.h1_parts))

    def meta_content(self, *, name: str | None = None, prop: str | None = None) -> str:
        for attrs in self.meta:
            if name and attrs.get("name") == name:
                return attrs.get("content", "")
            if prop and attrs.get("property") == prop:
                return attrs.get("content", "")
        return ""

    def canonical(self) -> str:
        for attrs in self.links:
            if attrs.get("rel") == "canonical":
                return attrs.get("href", "")
        return ""


def clean(value: str) -> str:
    return " ".join(value.split())


def canonical_editable_pages() -> list[Path]:
    pages = []
    for page in ROOT.rglob("*.html"):
        if ".git" in page.parts:
            continue
        rel = page.relative_to(ROOT).as_posix()
        if rel.endswith("/index.html"):
            continue
        pages.append(page)
    return sorted(pages, key=lambda p: p.relative_to(ROOT).as_posix())


def page_row(page: Path) -> dict[str, str | int]:
    parser = MetadataParser()
    parser.feed(page.read_text(encoding="utf-8", errors="ignore"))
    desc = parser.meta_content(name="description")
    og_title = parser.meta_content(prop="og:title")
    og_desc = parser.meta_content(prop="og:description")
    twitter_title = parser.meta_content(name="twitter:title")
    twitter_desc = parser.meta_content(name="twitter:description")
    return {
        "file": page.relative_to(ROOT).as_posix(),
        "canonical": parser.canonical(),
        "title": parser.title,
        "title_length": len(parser.title),
        "description": desc,
        "description_length": len(desc),
        "h1": parser.h1,
        "og_title": og_title,
        "og_description": og_desc,
        "og_url": parser.meta_content(prop="og:url"),
        "og_image": parser.meta_content(prop="og:image"),
        "twitter_card": parser.meta_content(name="twitter:card"),
        "twitter_title": twitter_title,
        "twitter_description": twitter_desc,
        "twitter_image": parser.meta_content(name="twitter:image"),
        "title_matches_og_title": "yes" if parser.title == og_title else "no",
        "description_matches_og_description": "yes" if desc == og_desc else "no",
        "title_matches_twitter_title": "yes" if parser.title == twitter_title else "no",
        "description_matches_twitter_description": "yes" if desc == twitter_desc else "no",
    }


def write_csv(rows: list[dict[str, str | int]]) -> None:
    fields = list(rows[0].keys()) if rows else []
    with CSV_OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str | int]]) -> None:
    lines = [
        "# Current SEO Page Metadata Audit",
        "",
        "Generated from the current HTML files. Clean-route `index.html` copies are excluded so the sheet shows the editable canonical pages.",
        "",
        "| File | Canonical | Title | Title Len | Meta Description | Desc Len | H1 | OG Image |",
        "|---|---|---:|---:|---|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {file} | {canonical} | {title} | {title_length} | {description} | {description_length} | {h1} | {og_image} |".format(
                file=escape_md(str(row["file"])),
                canonical=escape_md(str(row["canonical"])),
                title=escape_md(str(row["title"])),
                title_length=row["title_length"],
                description=escape_md(str(row["description"])),
                description_length=row["description_length"],
                h1=escape_md(str(row["h1"])),
                og_image=escape_md(str(row["og_image"])),
            )
        )
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def escape_md(value: str) -> str:
    return value.replace("|", "\\|")


def main() -> None:
    rows = [page_row(page) for page in canonical_editable_pages()]
    write_csv(rows)
    write_md(rows)
    print(f"metadata_rows={len(rows)}")
    print(CSV_OUT.relative_to(ROOT).as_posix())
    print(MD_OUT.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
