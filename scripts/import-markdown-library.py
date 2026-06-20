#!/usr/bin/env python3
import json
import re
import shutil
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path("/Users/chen/Desktop/Markdown")
CONTENT_DIR = ROOT / "content" / "posts"
STATIC_ASSET_DIR = ROOT / "static" / "imported" / "markdown"
REPOSITORY_ARCHIVE_DIR = ROOT / "repository-archive" / "posts"
REPOSITORY_ARCHIVE_PAGE = ROOT / "content" / "repository-archive" / "_index.md"
REPOSITORY_TREE_BASE = "https://github.com/Smithereensun/smithereensun.github.io/tree/main/repository-archive/posts"
LIGHT_POST_MAX_ASSET_MB = 5
SOURCE_NAME = "local-markdown-library"
UNDATED_SORT_DATE = "1900-01-01"


TAG_ALIASES = {
    "ai": "AI",
    "agent": "Agent",
    "algorithmsguide": "算法",
    "architectural-ideas": "架构",
    "bigdata": "大数据",
    "books": "读书",
    "cs-basics": "计算机基础",
    "database": "数据库",
    "mysql": "MySQL",
    "redis": "Redis",
    "framework": "框架",
    "spring": "Spring",
    "springai": "Spring AI",
    "springboot": "Spring Boot",
    "orm": "ORM",
    "web": "Web",
    "interview": "面试",
    "java": "Java",
    "collection": "集合",
    "concurrent": "并发",
    "jvm": "JVM",
    "microservices": "微服务",
    "message-queue": "消息队列",
    "system-design": "系统设计",
    "design-pattern": "设计模式",
    "security": "安全",
    "tool-library": "工具库",
    "tools": "工具",
}


IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)|<img([^>]+)>", re.I)
IMG_SRC_PATTERN = re.compile(r"src=[\"']([^\"']+)[\"']", re.I)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def short_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "post"


def parse_date(text: str) -> Optional[str]:
    match = re.search(r"^- 最近更新：(.+)$", text, flags=re.M)
    if not match:
        return None

    value = match.group(1).strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(value).strftime("%Y-%m-%d")
    except ValueError:
        return value[:10]


def split_filename(path: Path) -> tuple[str, str]:
    stem = path.stem.strip()
    if " - " in stem:
        slug, title = stem.split(" - ", 1)
        return slug.strip(), title.strip()
    return slugify(stem), stem


def extract_title(path: Path, text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    if match:
        return match.group(1).strip()
    return split_filename(path)[1]


def cleanup_body(text: str, title: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")

    while lines and not lines[0].strip():
        lines.pop(0)

    if lines and re.match(r"^#\s+", lines[0]):
        first_title = re.sub(r"^#\s+", "", lines[0]).strip()
        if first_title == title:
            lines.pop(0)

    while lines and not lines[0].strip():
        lines.pop(0)

    if lines and lines[0].startswith("- 最近更新："):
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and lines[0].strip() == "---":
            lines.pop(0)

    while lines and not lines[0].strip():
        lines.pop(0)

    return escape_angle_brackets("\n".join(lines).strip()) + "\n"


def escape_angle_brackets(text: str) -> str:
    placeholders = {}

    def stash(match: re.Match) -> str:
        key = f"@@HTML_IMG_{len(placeholders)}@@"
        placeholders[key] = match.group(0)
        return key

    text = re.sub(r"<img\b[^>]*>", stash, text, flags=re.I)
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text


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


def build_description(body: str, title: str) -> str:
    plain = strip_markdown(body)
    return (plain or title)[:150]


def infer_tags(path: Path, title: str) -> list[str]:
    rel_parts = path.relative_to(SOURCE_DIR).parts[:-1]
    tags = []
    for part in rel_parts:
        tag = TAG_ALIASES.get(part)
        if tag and tag not in tags:
            tags.append(tag)

    title_lower = title.lower()
    keyword_rules = [
        ("mysql", "MySQL"),
        ("redis", "Redis"),
        ("springboot", "Spring Boot"),
        ("spring boot", "Spring Boot"),
        ("spring", "Spring"),
        ("java", "Java"),
        ("jvm", "JVM"),
        ("kafka", "Kafka"),
        ("rabbitmq", "RabbitMQ"),
        ("rocketmq", "RocketMQ"),
        ("dubbo", "Dubbo"),
        ("nacos", "Nacos"),
        ("zookeeper", "ZooKeeper"),
        ("git", "Git"),
        ("maven", "Maven"),
        ("agent", "Agent"),
        ("rag", "RAG"),
        ("mcp", "MCP"),
    ]
    for needle, tag in keyword_rules:
        if needle in title_lower and tag not in tags:
            tags.append(tag)

    return tags[:4] or ["笔记"]


def front_matter(title: str, date: Optional[str], description: str, tags: list[str], source_path: Path) -> str:
    payload = {
        "title": title,
        "has_date": bool(date),
        "description": description,
        "tags": tags,
        "source": SOURCE_NAME,
        "source_path": str(source_path.relative_to(SOURCE_DIR)),
    }
    if date:
        payload["date"] = date
    return "{\n" + json.dumps(payload, ensure_ascii=False, indent=2)[1:-1] + "\n}\n\n"


def image_refs(text: str, md_path: Path) -> list[tuple[str, Path]]:
    refs = []
    for match in IMAGE_PATTERN.finditer(text):
        raw = ""
        if match.group(2) is not None:
            raw = match.group(2).strip()
        elif match.group(3) is not None:
            src_match = IMG_SRC_PATTERN.search(match.group(3))
            if src_match:
                raw = src_match.group(1).strip()

        if not raw:
            continue

        parsed = urlparse(raw)
        if parsed.scheme in {"http", "https", "data", "file"}:
            continue

        clean_ref = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        target = (md_path.parent / clean_ref).resolve()
        if target.exists() and target.is_file():
            refs.append((raw, target))

    return refs


def unique_refs(refs: list[tuple[str, Path]]) -> list[tuple[str, Path]]:
    seen = set()
    result = []
    for raw, path in refs:
        if path in seen:
            continue
        seen.add(path)
        result.append((raw, path))
    return result


def rewrite_image_paths(body: str, refs: list[tuple[str, Path]], asset_prefix: str) -> str:
    by_path = {}
    counters = {}
    for _, path in refs:
        count = counters.get(path.name, 0) + 1
        counters[path.name] = count
        new_name = path.name if count == 1 else f"{path.stem}-{count}{path.suffix}"
        by_path[path] = new_name

    def replace(match: re.Match) -> str:
        if match.group(2) is not None:
            alt = match.group(1)
            raw = match.group(2).strip()
            parsed = urlparse(raw)
            if parsed.scheme == "file":
                return ""
            if parsed.scheme in {"http", "https", "data"}:
                return match.group(0)
            clean_ref = unquote(raw.split("#", 1)[0].split("?", 1)[0])
            target = (current_md_path.parent / clean_ref).resolve()
            if target not in by_path:
                return match.group(0)
            return f"![{alt}]({asset_prefix}/images/{by_path[target]})"

        attrs = match.group(3)
        src_match = IMG_SRC_PATTERN.search(attrs or "")
        if not src_match:
            return match.group(0)
        raw = src_match.group(1).strip()
        parsed = urlparse(raw)
        if parsed.scheme == "file":
            return ""
        if parsed.scheme in {"http", "https", "data"}:
            return match.group(0)
        clean_ref = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        target = (current_md_path.parent / clean_ref).resolve()
        if target not in by_path:
            return match.group(0)
        return IMG_SRC_PATTERN.sub(f'src="{asset_prefix}/images/{by_path[target]}"', match.group(0))

    return IMAGE_PATTERN.sub(replace, body)


def copy_assets(refs: list[tuple[str, Path]], target_dir: Path) -> tuple[int, int]:
    image_dir = target_dir / "images"
    image_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    total = 0
    counters = {}
    for _, path in refs:
        count = counters.get(path.name, 0) + 1
        counters[path.name] = count
        new_name = path.name if count == 1 else f"{path.stem}-{count}{path.suffix}"
        shutil.copy2(path, image_dir / new_name)
        copied += 1
        total += path.stat().st_size

    if copied == 0:
        shutil.rmtree(image_dir)
    return total, copied


def remove_previous_imports() -> None:
    for path in CONTENT_DIR.glob("*.md"):
        if path.name == "_index.md":
            continue
        text = read_text(path)
        if f'"source": "{SOURCE_NAME}"' in text:
            path.unlink()

    if STATIC_ASSET_DIR.exists():
        shutil.rmtree(STATIC_ASSET_DIR)
    STATIC_ASSET_DIR.mkdir(parents=True, exist_ok=True)

    for path in REPOSITORY_ARCHIVE_DIR.glob("markdown-*"):
        if path.is_dir():
            shutil.rmtree(path)


def load_existing_archive_items() -> list[dict]:
    if not REPOSITORY_ARCHIVE_PAGE.exists():
        return []
    text = read_text(REPOSITORY_ARCHIVE_PAGE)
    match = re.search(r"```json\n(.*?)\n```", text, flags=re.S)
    if not match:
        return []
    try:
        payload = json.loads(match.group(1))
    except json.JSONDecodeError:
        return []
    items = payload.get("items") or []
    return [item for item in items if not str(item.get("path", "")).startswith("repository-archive/posts/markdown-")]


def archive_sort_key(item: dict) -> tuple[bool, str]:
    date = str(item.get("date") or "")
    return bool(item.get("has_date", bool(date))) and bool(date), date


def write_archive_page(items: list[dict]) -> None:
    items = sorted(items, key=archive_sort_key, reverse=True)
    payload = {
        "threshold_mb": LIGHT_POST_MAX_ASSET_MB,
        "count": len(items),
        "asset_files": sum(int(item.get("asset_files") or 0) for item in items),
        "asset_bytes": sum(int(item.get("asset_bytes") or 0) for item in items),
        "items": items,
    }

    lines = [
        "---",
        'title: "仓库归档"',
        'description: "这些文章内容较大，不在博客正文中展示，统一放在 GitHub 仓库中归档查看。"',
        "layout: repository-archive",
        "---",
        "",
        "这些文章因为图片或资源体积较大，没有放进博客正文页面。",
        "你仍然可以在 GitHub 仓库里查看完整归档目录，里面包含 Markdown 和图片等配套资源。",
        "",
        "```json",
        json.dumps(payload, ensure_ascii=False, indent=2),
        "```",
        "",
    ]

    for item in items:
        size_mb = int(item["asset_bytes"]) / 1024 / 1024
        meta_parts = []
        if item.get("has_date", bool(item.get("date"))) and item.get("date"):
            meta_parts.append(str(item["date"]))
        meta_parts.extend([f"{size_mb:.1f}MB", f"{item['asset_files']} 张资源"])
        lines.append(
            f"- [{item['title']}]({item['github_url']})"
            f" · {' · '.join(meta_parts)}"
        )

    REPOSITORY_ARCHIVE_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def import_library() -> tuple[int, int, int]:
    remove_previous_imports()
    existing_archive_items = load_existing_archive_items()
    imported = 0
    archived = 0
    skipped = 0
    archive_items = []

    for md_path in sorted(SOURCE_DIR.rglob("*.md")):
        if md_path.name == "README.md" or "_images" in md_path.parts:
            skipped += 1
            continue

        text = read_text(md_path)
        title = extract_title(md_path, text)
        date = parse_date(text)
        sort_date = date or UNDATED_SORT_DATE
        body = cleanup_body(text, title)
        refs = unique_refs(image_refs(body, md_path))
        asset_bytes = sum(path.stat().st_size for _, path in refs)
        asset_files = len(refs)
        file_slug, _ = split_filename(md_path)
        rel_slug = slugify("-".join(md_path.relative_to(SOURCE_DIR).with_suffix("").parts))
        file_prefix = sort_date if date else "undated"
        file_base = f"{file_prefix}-markdown-{short_hash(str(md_path.relative_to(SOURCE_DIR)))}-{slugify(title or file_slug)[:60]}"
        description = build_description(body, title)
        tags = infer_tags(md_path, title)
        front = front_matter(title, date, description, tags, md_path)

        global current_md_path
        current_md_path = md_path

        if asset_bytes <= LIGHT_POST_MAX_ASSET_MB * 1024 * 1024:
            asset_prefix = f"/imported/markdown/{file_base}"
            rewritten = rewrite_image_paths(body, refs, asset_prefix)
            (CONTENT_DIR / f"{file_base}.md").write_text(front + rewritten, encoding="utf-8")
            if refs:
                copy_assets(refs, STATIC_ASSET_DIR / file_base)
            imported += 1
            continue

        archive_dir = REPOSITORY_ARCHIVE_DIR / f"markdown-{rel_slug}"
        archive_dir.mkdir(parents=True, exist_ok=True)
        rewritten = rewrite_image_paths(body, refs, "./images")
        (archive_dir / "index.md").write_text(front + rewritten, encoding="utf-8")
        copy_assets(refs, archive_dir)
        archive_items.append(
            {
                "title": title,
                "date": date or "",
                "has_date": bool(date),
                "asset_bytes": asset_bytes,
                "asset_files": asset_files,
                "github_url": f"{REPOSITORY_TREE_BASE}/{archive_dir.name}",
                "path": f"repository-archive/posts/{archive_dir.name}",
            }
        )
        archived += 1

    write_archive_page(existing_archive_items + archive_items)
    return imported, archived, skipped


def main() -> int:
    imported, archived, skipped = import_library()
    print(f"Imported {imported} markdown posts; archived {archived} heavy posts; skipped {skipped}.")
    return 0


current_md_path = SOURCE_DIR


if __name__ == "__main__":
    raise SystemExit(main())
