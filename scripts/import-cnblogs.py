#!/usr/bin/env python3
import argparse
import html
import re
import sys
import hashlib
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from typing import Optional, Tuple

BLOG_URL = "https://www.cnblogs.com/chenyanbin"
RSS_URL = BLOG_URL + "/rss"
SITEMAP_URL = BLOG_URL + "/sitemap.xml"
POST_DIR = Path("content/posts")

DEFAULT_TAGS = {
    "github": ["GitHub", "开源"],
    "nvm": ["Node.js", "工具"],
    "learnClaudeCode": ["AI", "Claude"],
    "opencode": ["AI", "工具"],
    "agentskills": ["AI", "Agent"],
    "logback": ["Java", "日志"],
    "mvnrepository": ["Java", "Maven"],
    "ik_dic": ["搜索", "中文分词"],
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read().decode("utf-8", "ignore")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "post"


def short_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def parse_date(value: str) -> str:
    if not value:
        return "2026-01-01"
    value = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(value)
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return value[:10]


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\u3000", " ")
    return re.sub(r"\s+", " ", text).strip()


def strip_tags(fragment: str) -> str:
    fragment = re.sub(r"(?is)<(script|style).*?>.*?</\1>", "", fragment)
    fragment = re.sub(r"(?s)<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment)
    return re.sub(r"\s+", " ", fragment).strip()


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def extract_rss_urls() -> dict[str, str]:
    rss = fetch(RSS_URL)
    root = ET.fromstring(rss)
    ns = "{http://www.w3.org/2005/Atom}"
    out = {}
    for entry in root.findall(ns + "entry"):
        link = entry.find(ns + "link")
        updated = entry.findtext(ns + "updated") or ""
        if link is not None and link.attrib.get("href"):
            out[link.attrib["href"]] = updated
    return out


def extract_sitemap_map() -> dict[str, str]:
    xml = fetch(SITEMAP_URL)
    urls = {}
    for chunk in re.finditer(
        r"<url>\s*<loc>(.*?)</loc>\s*<lastmod>(.*?)</lastmod>.*?</url>",
        xml,
        re.I | re.S,
    ):
        urls[chunk.group(1)] = chunk.group(2)
    return urls


def extract_meta(html_text: str, name: str) -> str:
    patterns = [
        rf'<meta\s+name="{re.escape(name)}"\s+content="([^"]*)"',
        rf'<meta\s+property="{re.escape(name)}"\s+content="([^"]*)"',
    ]
    for pat in patterns:
        m = re.search(pat, html_text, re.I)
        if m:
            return clean_text(m.group(1))
    return ""


def extract_title(html_text: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html_text, re.I | re.S)
    if not m:
        return "Untitled"
    title = clean_text(m.group(1))
    title = re.sub(r"\s*-\s*陈彦斌\s*-\s*博客园\s*$", "", title)
    title = re.sub(r"\s*-\s*博客园\s*$", "", title)
    return title.strip()


def extract_post_body(html_text: str) -> str:
    patterns = [
        r'<div\s+id="cnblogs_post_body"[^>]*>(.*?)</div>\s*<!--end:\s*cnblogs_post_body-->',
        r'<div\s+id="cnblogs_post_body"[^>]*>(.*?)</div>',
    ]
    for pat in patterns:
        m = re.search(pat, html_text, re.I | re.S)
        if m:
            return m.group(1).strip()
    return ""


def normalize_body(body: str) -> str:
    body = body.replace('src="//', 'src="https://')
    body = body.replace('href="//', 'href="https://')
    body = re.sub(r'src="/(?!/)', f'src="{BLOG_URL}/', body)
    body = re.sub(r'href="/(?!/)', f'href="{BLOG_URL}/', body)
    body = re.sub(r"<img(.*?)>", r"<img\1 />", body)
    return body


def build_markdown(title: str, date_str: str, description: str, tags: list[str], source_url: str, body: str) -> str:
    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"date: {date_str}",
        f"description: {yaml_quote(description)}",
        "tags:",
    ]
    for tag in tags:
        lines.append(f"  - {yaml_quote(tag)}")
    lines.extend([
        "source: \"cnblogs\"",
        f"source_url: {yaml_quote(source_url)}",
        "---",
        "",
        body,
        "",
    ])
    return "\n".join(lines)


def clean_output_dir() -> None:
    for path in POST_DIR.glob("*.md"):
        if path.name != "_index.md":
            path.unlink()


def infer_post_id(url: str) -> str:
    parts = urlparse(url).path.rstrip("/").split("/")
    for part in parts:
        if part.isdigit():
            return part
    return "post"


def import_one(url: str, lastmod: Optional[str]) -> Optional[Tuple[str, str]]:
    if "/p/" not in url:
        return None

    html_text = fetch(url)
    body = normalize_body(extract_post_body(html_text))
    if not body:
        return None

    title = extract_title(html_text)
    description = extract_meta(html_text, "description") or strip_tags(body)[:180]
    date_match = re.search(r'property="article:published_time" content="([^"]+)"', html_text, re.I)
    if date_match:
        date_str = parse_date(date_match.group(1))
    elif lastmod:
        date_str = parse_date(lastmod)
    else:
        date_str = "2026-01-01"

    post_id = infer_post_id(url)
    tags = DEFAULT_TAGS.get(urlparse(url).path.rstrip("/").split("/")[-1], [])
    if not tags:
        meta_keywords = extract_meta(html_text, "keywords")
        if meta_keywords:
            tags = [t.strip() for t in re.split(r"[;,，]", meta_keywords) if t.strip()]
    if not tags:
        tags = ["cnblogs"]

    filename = f"{date_str}-{post_id}-{short_hash(url)}-{slugify(title)[:60]}.md"
    out_path = POST_DIR / filename
    out_path.write_text(
        build_markdown(title, date_str, description or title, tags, url, body),
        encoding="utf-8",
    )
    return str(out_path), title


def main() -> int:
    parser = argparse.ArgumentParser(description="Import cnblogs posts into Hugo content.")
    parser.add_argument("--clean", action="store_true", help="Remove existing posts before importing.")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent fetch workers.")
    parser.add_argument("--limit", type=int, default=0, help="Optional limit for testing.")
    args = parser.parse_args()

    POST_DIR.mkdir(parents=True, exist_ok=True)
    if args.clean:
        clean_output_dir()

    try:
        sitemap_map = extract_sitemap_map()
    except Exception:
        sitemap_map = {}

    try:
        rss_map = extract_rss_urls()
    except Exception:
        rss_map = {}

    urls = list(sitemap_map.keys() or rss_map.keys())
    if not urls:
        print("No article URLs found.", file=sys.stderr)
        return 1

    urls = [u for u in urls if "/p/" in u]
    if args.limit and args.limit > 0:
        urls = urls[: args.limit]

    written = 0
    skipped = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(import_one, url, sitemap_map.get(url) or rss_map.get(url)): url
            for url in urls
        }
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                result = fut.result()
            except Exception as exc:
                skipped += 1
                print(f"skip {url}: {exc}")
                continue
            if result is None:
                skipped += 1
                print(f"skip empty body: {url}")
                continue
            written += 1
            path, title = result
            print(f"wrote {path} :: {title}")

    print(f"done: {written} written, {skipped} skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
