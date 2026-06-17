#!/usr/bin/env python3
import json
import re
import shutil
import hashlib
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path("/Users/chen/Desktop/data/download_doc/cnblogs_markdown_export/posts")
CONTENT_DIR = ROOT / "content" / "posts"
STATIC_ASSET_DIR = ROOT / "static" / "imported" / "posts"

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


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "post"


def short_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def parse_date(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return "2026-01-01"
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y/%m/%d %H:%M", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return value[:10]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def strip_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"^[>\-\*\+\d\.\s]+", "", text, flags=re.M)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_existing_tags() -> dict[str, list[str]]:
    tags_by_post_id = {}
    if not CONTENT_DIR.exists():
        return tags_by_post_id

    for path in CONTENT_DIR.glob("*.md"):
        if path.name == "_index.md":
            continue
        text = read_text(path)
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            front = yaml.safe_load(parts[1]) or {}
        except Exception:
            continue
        source_url = str(front.get("source_url") or "")
        if not source_url:
            continue
        match = re.search(r"/p/(\d+)", source_url)
        if not match:
            continue
        tags = front.get("tags") or []
        if tags:
            tags_by_post_id[match.group(1)] = tags
    return tags_by_post_id


def cleanup_body(body: str, title: str) -> str:
    lines = body.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    while lines and not lines[0].strip():
        lines.pop(0)

    if lines and re.match(r"^#\s+", lines[0]):
        first_heading = re.sub(r"^#\s+", "", lines[0]).strip()
        if first_heading == title.strip():
            lines.pop(0)

    while lines and not lines[0].strip():
        lines.pop(0)

    filtered = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- 原文:"):
            continue
        if stripped.startswith("- 发布时间:"):
            continue
        filtered.append(line)

    while filtered and not filtered[0].strip():
        filtered.pop(0)

    return "\n".join(filtered).strip() + "\n"


def rewrite_asset_paths(body: str, asset_prefix: str) -> str:
    body = body.replace("](./images/", f"]({asset_prefix}/images/")
    body = body.replace("](images/", f"]({asset_prefix}/images/")
    body = body.replace('src="./images/', f'src="{asset_prefix}/images/')
    body = body.replace('src="images/', f'src="{asset_prefix}/images/')
    body = body.replace("='images/", f"='{asset_prefix}/images/")
    body = body.replace("='./images/", f"='{asset_prefix}/images/")
    return body


def infer_tags(meta: dict, existing_tags: dict[str, list[str]]) -> list[str]:
    post_id = str(meta.get("post_id") or "")
    if post_id in existing_tags:
        return existing_tags[post_id]

    url = str(meta.get("url") or "")
    slug = url.rstrip("/").split("/")[-1]
    if slug in DEFAULT_TAGS:
        return DEFAULT_TAGS[slug]

    title = str(meta.get("title") or "")
    rules = [
        ("springboot", "Spring Boot"),
        ("springcloud", "Spring Cloud"),
        ("spring", "Spring"),
        ("mysql", "MySQL"),
        ("oracle", "Oracle"),
        ("docker", "Docker"),
        ("redis", "Redis"),
        ("nginx", "Nginx"),
        ("java", "Java"),
        ("python", "Python"),
        ("vue", "Vue"),
        ("git", "Git"),
        ("linux", "Linux"),
        ("mac", "Mac"),
        ("es", "Elasticsearch"),
        ("jvm", "JVM"),
        ("agent", "AI"),
        ("claude", "AI"),
        ("opencode", "AI"),
    ]

    title_lower = title.lower()
    tags = []
    for needle, tag in rules:
        if needle in title_lower:
            tags.append(tag)
    return tags[:3] or ["笔记"]


def build_description(body: str, title: str) -> str:
    plain = strip_markdown(body)
    if not plain:
        return title
    return plain[:150]


def build_front_matter(meta: dict, description: str, tags: list[str]) -> str:
    front = {
        "title": str(meta.get("title") or "Untitled"),
        "date": parse_date(str(meta.get("published_at") or "")),
        "description": description,
        "tags": tags,
        "source": "cnblogs-export",
        "source_url": str(meta.get("url") or ""),
    }
    return "{\n" + json.dumps(front, ensure_ascii=False, indent=2)[1:-1] + "\n}\n\n"


def clean_targets() -> None:
    if CONTENT_DIR.exists():
        for path in CONTENT_DIR.iterdir():
            if path.name == "_index.md":
                continue
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

    if STATIC_ASSET_DIR.exists():
        shutil.rmtree(STATIC_ASSET_DIR)
    STATIC_ASSET_DIR.mkdir(parents=True, exist_ok=True)


def ensure_posts_index() -> None:
    index_path = CONTENT_DIR / "_index.md"
    if index_path.exists():
        return
    index_path.write_text(
        "---\n"
        'title: "文章"\n'
        'description: "持续更新的技术与学习笔记。"\n'
        "---\n",
        encoding="utf-8",
    )


def import_posts() -> tuple[int, int]:
    existing_tags = extract_existing_tags()
    clean_targets()
    ensure_posts_index()

    imported = 0
    skipped = 0
    for folder in sorted(p for p in SOURCE_DIR.iterdir() if p.is_dir()):
        meta_path = folder / "meta.json"
        post_path = folder / "post.md"
        if not meta_path.exists() or not post_path.exists():
            skipped += 1
            continue

        meta = json.loads(read_text(meta_path))
        title = str(meta.get("title") or folder.name)
        source_url = str(meta.get("url") or folder.name)
        date_str = parse_date(str(meta.get("published_at") or ""))
        file_base = f"{date_str}-{meta.get('post_id')}-{short_hash(source_url)}-{slugify(title)[:60]}"
        asset_prefix = f"/imported/posts/{file_base}"

        body = cleanup_body(read_text(post_path), title)
        body = rewrite_asset_paths(body, asset_prefix)
        description = build_description(body, title)
        tags = infer_tags(meta, existing_tags)
        front_matter = build_front_matter(meta, description, tags)

        out_path = CONTENT_DIR / f"{file_base}.md"
        out_path.write_text(front_matter + body, encoding="utf-8")

        src_images = folder / "images"
        if src_images.exists():
            dst_images = STATIC_ASSET_DIR / file_base / "images"
            dst_images.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src_images, dst_images)

        imported += 1

    return imported, skipped


def main() -> int:
    imported, skipped = import_posts()
    print(f"Imported {imported} posts; skipped {skipped}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
