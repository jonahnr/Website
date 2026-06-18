from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = '<a href="power-bi-consultant-cincinnati.html">Power BI Consultant Cincinnati</a>'
NESTED_LINK = '<a href="../power-bi-consultant-cincinnati.html">Power BI Consultant Cincinnati</a>'


def link_for(path: Path) -> str:
    return NESTED_LINK if "insights" in path.parts and path.parent != ROOT else LINK


def main() -> None:
    changed = []
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "Power BI Consultant Cincinnati" in text:
            continue
        needle = '<h3>Services</h3>\n'
        if needle not in text:
            continue
        new = text.replace(needle, needle + "      " + link_for(path) + "\n", 1)
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(path.relative_to(ROOT).as_posix())
    print("changed_count=", len(changed))
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()
