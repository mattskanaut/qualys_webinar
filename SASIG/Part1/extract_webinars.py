#!/usr/bin/env python3
"""
Extract SASIG webinar date + excerpt pairs from webinarcode.html into a CSV.

For each <article class="webinar-event"> we pull:
  - the YYYY-MM-DD date out of the first /calendar/event/<date>-<slug>/ href
  - the text inside <p class="event-excerpt">...</p>
"""

import csv
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "webinarcode.html"
OUT = HERE / "webinars.csv"

ARTICLE_RE = re.compile(
    r'<article class="webinar-event">(.*?)</article>',
    re.DOTALL,
)
DATE_RE = re.compile(
    r'/calendar/event/(\d{4}-\d{2}-\d{2})-',
)
ALT_DATE_RE = re.compile(
    r'alt="[^"]*?(\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}:\d{2}"',
)
EXCERPT_RE = re.compile(
    r'<p class="event-excerpt">(.*?)</p>',
    re.DOTALL,
)


def clean(text: str) -> str:
    """Decode HTML entities and collapse whitespace."""
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def main() -> int:
    if not SRC.exists():
        print(f"Source file not found: {SRC}", file=sys.stderr)
        return 1

    raw = SRC.read_text(encoding="utf-8")
    rows = []
    skipped = 0

    for body in ARTICLE_RE.findall(raw):
        date_match = DATE_RE.search(body) or ALT_DATE_RE.search(body)
        excerpt_match = EXCERPT_RE.search(body)
        if not date_match or not excerpt_match:
            skipped += 1
            continue
        rows.append((date_match.group(1), clean(excerpt_match.group(1))))

    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["date", "excerpt"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT}")
    if skipped:
        print(f"Skipped {skipped} articles with missing date or excerpt", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
