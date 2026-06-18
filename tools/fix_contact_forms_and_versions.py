from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def update(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html

    # Keep the backend endpoint only for the scorecard form.
    html = re.sub(
        r'<form action="/api/scorecard-submit" data-form-user="jonahnr" data-form-domain="gmail.com" class="about-contact-form"',
        '<form action="https://formsubmit.co/" data-form-user="jonahnr" data-form-domain="gmail.com" class="about-contact-form"',
        html,
    )
    html = re.sub(
        r'<form action="/api/scorecard-submit" data-form-user="jonahnr" data-form-domain="gmail.com" class="assessment-form" method="POST"(?![^>]*data-scorecard-delivery)',
        '<form action="https://formsubmit.co/" data-form-user="jonahnr" data-form-domain="gmail.com" class="assessment-form" method="POST"',
        html,
    )

    html = re.sub(r"home\.css\?v=\d+", "home.css?v=133", html)
    html = re.sub(r"home\.js\?v=\d+", "home.js?v=133", html)

    if html != original:
        path.write_text(html, encoding="utf-8", newline="")
        return True
    return False


def main():
    changed = []
    for path in list(ROOT.glob("*.html")) + list(ROOT.glob("*/*.html")) + list(ROOT.glob("insights/*/index.html")):
        if update(path):
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Updated {len(changed)} HTML files.")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()
