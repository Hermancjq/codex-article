#!/usr/bin/env python3
"""Archive official sources and prepare auditable extraction; standard library only.

Downloaded excerpts are candidates, never automatically accepted observations.
No TLS verification bypass, secret access, proxy modification or numerical imputation.
"""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import math
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parent
RAW = BASE / "raw"
TEXT = BASE / "extracted_text"
ALLOWED_ROOTS = ("caac.gov.cn", "stats.gov.cn")
SEEDS = [
    # Actual annual-report list linked by the public TJSJ iframe page.
    "https://www.caac.gov.cn/XXGK/XXGK/TJSJ/index_1214.html",
    "https://www.caac.gov.cn/XXGK/XXGK/TJSJ/index_1214_1.html",
    "https://www.stats.gov.cn/sj/ndsj/",
]
KEYWORDS = re.compile(r"运输总周转量|燃油|航油|吨公里油耗|单位.{0,12}油耗|每吨公里|二氧化碳")
REPORT = re.compile(r"(?:20\d{2}).{0,8}民航.{0,20}(?:统计公报|发展统计)|民航行业发展统计公报")
FIELDS = [
    "year", "turnover_100m_tkm", "fuel_intensity_kg_per_tkm",
    "reported_fuel_10000_tonnes", "publication_date", "source_url",
    "source_file", "source_sha256", "retrieval_utc", "page_or_table",
    "exact_quote", "scope_notes", "verification_status",
]


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def allowed(url):
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    return parsed.scheme == "https" and any(host == r or host.endswith("." + r) for r in ALLOWED_ROOTS)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks = []
        self.links = []
        self.anchor = None
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "a":
            self.anchor = [attrs.get("href", ""), []]
        if tag in ("p", "br", "div", "tr", "li", "h1", "h2", "h3"):
            self.chunks.append("\n")
        elif tag in ("td", "th"):
            self.chunks.append("\t")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "a" and self.anchor:
            self.links.append((self.anchor[0], "".join(self.anchor[1]).strip()))
            self.anchor = None
        if tag in ("p", "div", "tr", "li", "h1", "h2", "h3"):
            self.chunks.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        self.chunks.append(data)
        if self.anchor:
            self.anchor[1].append(data)


def decode_html(body, charset):
    match = re.search(br"charset\s*=\s*['\"]?([a-zA-Z0-9_-]+)", body[:10000], re.I)
    encodings = [charset, match.group(1).decode("ascii") if match else None, "utf-8", "gb18030"]
    for encoding in dict.fromkeys(e for e in encodings if e):
        try:
            return body.decode(encoding)
        except (UnicodeDecodeError, LookupError):
            pass
    raise ValueError("Unknown HTML encoding; preserve raw file and review manually")


def append_json(name, record):
    with (BASE / name).open("a", encoding="utf-8") as out:
        out.write(json.dumps(record, ensure_ascii=False) + "\n")


def fetch(url):
    if not allowed(url):
        raise ValueError("Only HTTPS official CAAC/NBS domains are permitted: " + url)
    req = urllib.request.Request(url, headers={"User-Agent": "SustainabilityResearchDataAudit/1.0 (public-statistics research)"})
    stamp = now()
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            final = response.geturl()
            if not allowed(final):
                raise ValueError("Redirect moved outside the official source boundary: " + final)
            body = response.read(25 * 1024 * 1024 + 1)
            if len(body) > 25 * 1024 * 1024:
                raise ValueError("Response exceeds the 25 MiB source limit")
            content_type = response.headers.get_content_type()
            charset = response.headers.get_content_charset()
            status = response.status
    except Exception as error:
        append_json("fetch_log.jsonl", {"url": url, "retrieval_utc": stamp, "status": "failed", "error": str(error)})
        raise
    digest = hashlib.sha256(body).hexdigest()
    is_pdf = body.startswith(b"%PDF") or content_type == "application/pdf"
    is_html = content_type in ("text/html", "application/xhtml+xml") or b"<html" in body[:5000].lower()
    suffix = ".pdf" if is_pdf else ".html" if is_html else Path(urllib.parse.urlsplit(final).path).suffix or ".bin"
    RAW.mkdir(exist_ok=True)
    TEXT.mkdir(exist_ok=True)
    raw_path = RAW / (digest[:20] + suffix)
    if not raw_path.exists():
        raw_path.write_bytes(body)
    record = {"url": url, "final_url": final, "retrieval_utc": stamp, "status": status,
              "content_type": content_type, "bytes": len(body), "sha256": digest,
              "source_file": str(raw_path)}
    links = []
    extracted = ""
    if is_pdf:
        output = TEXT / (digest[:20] + ".txt")
        if shutil.which("pdftotext"):
            result = subprocess.run(["pdftotext", "-layout", str(raw_path), str(output)], capture_output=True, text=True)
            if result.returncode == 0:
                extracted = output.read_text(encoding="utf-8")
            else:
                record["extraction_error"] = result.stderr[-2000:]
        else:
            record["extraction_error"] = "pdftotext not installed; inspect PDF manually"
    elif is_html:
        parser = Page()
        parser.feed(decode_html(body, charset))
        extracted = "".join(parser.chunks)
        extracted = re.sub(r"[ \t]+", " ", extracted)
        extracted = re.sub(r"\n\s*\n+", "\n", extracted)
        links = [(urllib.parse.urljoin(final, h), title) for h, title in parser.links if h]
        (TEXT / (digest[:20] + ".txt")).write_text(extracted, encoding="utf-8")
    append_json("fetch_log.jsonl", record)
    if extracted:
        excerpt_path = BASE / "excerpts.csv"
        existed = excerpt_path.exists()
        with excerpt_path.open("a", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["source_url", "source_file", "source_sha256", "retrieval_utc", "keyword", "character_offset", "candidate_excerpt", "review_status"])
            if not existed:
                writer.writeheader()
            for match in KEYWORDS.finditer(extracted):
                writer.writerow({"source_url": final, "source_file": str(raw_path), "source_sha256": digest,
                                 "retrieval_utc": stamp, "keyword": match.group(), "character_offset": match.start(),
                                 "candidate_excerpt": extracted[max(0, match.start() - 120):match.end() + 240],
                                 "review_status": "pending_manual_review"})
    print(json.dumps({k: record[k] for k in ("final_url", "status", "bytes", "source_file")}, ensure_ascii=False))
    return links


def initialize_manifest():
    path = BASE / "official_aviation_2010_2025.csv"
    if path.exists():
        return
    with path.open("w", encoding="utf-8-sig", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows({"year": year, "verification_status": "pending"} for year in range(2010, 2026))


def discover(max_documents):
    candidates = {}
    fetched = set()
    # Follow actual archive pagination; do not invent annual-report URLs.
    queue = [(seed, "official_entry_candidate") for seed in SEEDS]
    while queue and len(fetched) < max_documents:
        url, origin = queue.pop(0)
        if url in fetched or not allowed(url):
            continue
        fetched.add(url)
        try:
            links = fetch(url)
        except Exception as error:
            print("FETCH FAILED: " + url + " :: " + str(error), file=sys.stderr)
            # One failed domain is enough to stop unchanged retries for that domain.
            host = urllib.parse.urlsplit(url).hostname
            queue = [(u, title) for u, title in queue if urllib.parse.urlsplit(u).hostname != host]
            continue
        for target, title in links:
            target = urllib.parse.urldefrag(target)[0]
            if not allowed(target):
                continue
            years = re.findall(r"20\d{2}", title)
            relevant = bool(REPORT.search(title)) and (not years or any(2010 <= int(y) <= 2025 for y in years))
            attachment = bool(REPORT.search(origin)) and bool(re.search(r"\.(?:pdf|docx?|xlsx?)(?:\?|$)", target, re.I))
            pagination = bool(re.search(r"/XXGK/XXGK/TJSJ/(?:index_1214(?:_\d+)?\.html)?$", urllib.parse.urlsplit(target).path))
            if relevant or attachment:
                candidates[target] = {"url": target, "link_title": title, "discovered_on": url,
                                      "status": "retrieved_if_present_in_fetch_log_otherwise_pending"}
                queue.append((target, title or origin))
            elif pagination:
                queue.append((target, "archive_pagination"))
    with (BASE / "source_candidates.csv").open("w", encoding="utf-8-sig", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=["url", "link_title", "discovered_on", "status"])
        writer.writeheader()
        writer.writerows(candidates.values())
    print(f"Archived/attempted {len(fetched)} unique source URLs; discovered {len(candidates)} annual-report candidates.")


def validate():
    path = BASE / "official_aviation_2010_2025.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    valid = []
    errors = []
    seen_years = set()
    for row in rows:
        year = row["year"]
        if year in seen_years:
            errors.append(f"Duplicate year: {year}")
        seen_years.add(year)
        if row["verification_status"] != "verified":
            continue
        for field in ("turnover_100m_tkm", "fuel_intensity_kg_per_tkm"):
            try:
                value = float(row[field])
                if not math.isfinite(value) or value <= 0:
                    raise ValueError("not positive")
            except ValueError:
                errors.append(f"{year}: invalid {field}")
        for field in ("source_url", "source_file", "source_sha256", "retrieval_utc", "page_or_table", "exact_quote", "scope_notes"):
            if not row.get(field):
                errors.append(f"{year}: missing {field}")
        if not allowed(row.get("source_url", "")):
            errors.append(f"{year}: non-official or non-HTTPS source URL")
        source = Path(row.get("source_file", ""))
        if not source.is_file():
            errors.append(f"{year}: archived source missing")
        elif hashlib.sha256(source.read_bytes()).hexdigest() != row.get("source_sha256"):
            errors.append(f"{year}: SHA-256 mismatch")
        valid.append(year)
    report = {"check_utc": now(), "verified_years": valid, "verified_n": len(valid),
              "errors": errors, "analysis_ready": bool(valid) and not errors,
              "note": "A passed mechanical gate does not substitute for scope and transcription review."}
    (BASE / "validation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["analysis_ready"] else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("discover", help="Archive official indexes and linked annual reports")
    cmd.add_argument("--max-documents", type=int, default=60)
    cmd = sub.add_parser("fetch", help="Archive one known official URL")
    cmd.add_argument("--url", required=True)
    sub.add_parser("init", help="Create blank extraction manifest without overwriting existing input")
    sub.add_parser("validate", help="Reject unverified/uncited data before empirical analysis")
    args = parser.parse_args()
    initialize_manifest()
    if args.command == "discover":
        discover(args.max_documents)
    elif args.command == "fetch":
        fetch(args.url)
    elif args.command == "validate":
        return validate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
