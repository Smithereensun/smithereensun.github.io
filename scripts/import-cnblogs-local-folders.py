#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "posts"
STATIC_ASSET_DIR = ROOT / "static" / "imported" / "cnblogs-local"
REPOSITORY_ARCHIVE_DIR = ROOT / "repository-archive" / "posts"
REPOSITORY_ARCHIVE_PAGE = ROOT / "content" / "repository-archive" / "_index.md"
REPOSITORY_TREE_BASE = "https://github.com/Smithereensun/smithereensun.github.io/tree/main/repository-archive/posts"
LIGHT_POST_MAX_ASSET_MB = 5
SOURCE_NAME = "cnblogs-local-export"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def short_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "post"


def parse_date(value: str) -> Optional[str]:
    value = (value or "").strip()
    if not value:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y/%m/%d %H:%M", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return value[:10] if re.match(r"\d{4}-\d{2}-\d{2}", value) else None


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


def cleanup_body(body: str, title: str) -> str:
    lines = body.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    while lines and not lines[0].strip():
        lines.pop(0)

    if lines and re.match(r"^#\s+", lines[0]):
        first_heading = re.sub(r"^#\s+", "", lines[0]).strip()
        if first_heading == title.strip():
            lines.pop(0)

    filtered = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- 原文:") or stripped.startswith("- 发布时间:"):
            continue
        filtered.append(line)

    while filtered and not filtered[0].strip():
        filtered.pop(0)

    return "\n".join(filtered).strip() + "\n"


def rewrite_asset_paths(body: str, asset_prefix: str) -> str:
    replacements = {
        "](./images/": f"]({asset_prefix}/images/",
        "](images/": f"]({asset_prefix}/images/",
        'src="./images/': f'src="{asset_prefix}/images/',
        'src="images/': f'src="{asset_prefix}/images/',
        "='./images/": f"='{asset_prefix}/images/",
        "='images/": f"='{asset_prefix}/images/",
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    return body


def build_description(body: str, title: str) -> str:
    plain = strip_markdown(body)
    return (plain or title)[:150]


def infer_tags(title: str) -> list[str]:
    title_lower = title.lower()
    rules = [
        ("ai agent", "AI"),
        ("agent", "Agent"),
        ("vibe coding", "Vibe Coding"),
        ("vibe", "Vibe Coding"),
        ("claude", "Claude"),
        ("codex", "Codex"),
        ("prompt", "Prompt"),
        ("skill", "Skill"),
        ("ai", "AI"),
    ]
    tags = []
    for needle, tag in rules:
        if needle in title_lower and tag not in tags:
            tags.append(tag)
    return tags[:4] or ["笔记"]


def build_front_matter(meta: dict, date: Optional[str], description: str, tags: list[str], source_path: str) -> str:
    payload = {
        "title": str(meta.get("title") or "Untitled"),
        "has_date": bool(date),
        "description": description,
        "tags": tags,
        "source": SOURCE_NAME,
        "source_path": source_path,
    }
    if date:
        payload["date"] = date
    if meta.get("url"):
        payload["source_url"] = str(meta["url"])
    return "{\n" + json.dumps(payload, ensure_ascii=False, indent=2)[1:-1] + "\n}\n\n"


def asset_stats(images_dir: Path) -> tuple[int, int]:
    total = 0
    files = 0
    if not images_dir.exists():
        return total, files
    for path in images_dir.rglob("*"):
        if path.is_file():
            total += path.stat().st_size
            files += 1
    return total, files


def remove_previous_imports() -> int:
    removed = 0
    for path in CONTENT_DIR.glob("*.md"):
        if path.name == "_index.md":
            continue
        text = read_text(path)
        if f'"source": "{SOURCE_NAME}"' in text:
            path.unlink()
            removed += 1

    if STATIC_ASSET_DIR.exists():
        shutil.rmtree(STATIC_ASSET_DIR)
    STATIC_ASSET_DIR.mkdir(parents=True, exist_ok=True)

    for path in REPOSITORY_ARCHIVE_DIR.glob("cnblogs-local-*"):
        if path.is_dir():
            shutil.rmtree(path)
    return removed


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
    return [
        item
        for item in payload.get("items", [])
        if not str(item.get("path", "")).startswith("repository-archive/posts/cnblogs-local-")
    ]


def write_archive_page(items: list[dict]) -> None:
    items = sorted(items, key=lambda item: (bool(item.get("has_date", bool(item.get("date")))), str(item.get("date") or "")), reverse=True)
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
        lines.append(f"- [{item['title']}]({item['github_url']}) · {' · '.join(meta_parts)}")
    REPOSITORY_ARCHIVE_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def import_folder(root: Path) -> tuple[int, int, int, list[dict]]:
    imported = 0
    archived = 0
    skipped = 0
    archive_items = []
    posts_dir = root / "posts"
    if not posts_dir.exists():
        return imported, archived, skipped + 1, archive_items

    for folder in sorted(path for path in posts_dir.iterdir() if path.is_dir()):
        meta_path = folder / "meta.json"
        post_path = folder / "post.md"
        if not meta_path.exists() or not post_path.exists():
            skipped += 1
            continue

        meta = json.loads(read_text(meta_path))
        title = str(meta.get("title") or folder.name)
        date = parse_date(str(meta.get("published_at") or ""))
        source_key = f"{root.name}/{folder.name}"
        file_date = date or "undated"
        source_id = str(meta.get("post_id") or short_hash(source_key))
        file_base = f"{file_date}-local-{source_id}-{short_hash(source_key)}-{slugify(title)[:60]}"
        images_dir = folder / "images"
        asset_bytes, asset_files = asset_stats(images_dir)
        body = cleanup_body(read_text(post_path), title)
        description = build_description(body, title)
        tags = infer_tags(title)
        front_matter = build_front_matter(meta, date, description, tags, source_key)

        if asset_bytes <= LIGHT_POST_MAX_ASSET_MB * 1024 * 1024:
            asset_prefix = f"/imported/cnblogs-local/{file_base}"
            out_path = CONTENT_DIR / f"{file_base}.md"
            out_path.write_text(front_matter + rewrite_asset_paths(body, asset_prefix), encoding="utf-8")
            if images_dir.exists():
                dst_images = STATIC_ASSET_DIR / file_base / "images"
                dst_images.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(images_dir, dst_images)
            imported += 1
            continue

        archive_dir = REPOSITORY_ARCHIVE_DIR / f"cnblogs-local-{file_base}"
        archive_dir.mkdir(parents=True, exist_ok=True)
        (archive_dir / "index.md").write_text(front_matter + rewrite_asset_paths(body, "./images"), encoding="utf-8")
        if images_dir.exists():
            shutil.copytree(images_dir, archive_dir / "images")
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

    return imported, archived, skipped, archive_items


def main() -> int:
    parser = argparse.ArgumentParser(description="Incrementally import local cnblogs Markdown export folders.")
    parser.add_argument("folders", nargs="+", type=Path)
    args = parser.parse_args()

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    REPOSITORY_ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    removed = remove_previous_imports()
    imported = archived = skipped = 0
    archive_items = []

    for folder in args.folders:
        folder_imported, folder_archived, folder_skipped, folder_archive_items = import_folder(folder.expanduser().resolve())
        imported += folder_imported
        archived += folder_archived
        skipped += folder_skipped
        archive_items.extend(folder_archive_items)

    if archived or removed:
        write_archive_page(load_existing_archive_items() + archive_items)

    print(
        f"Imported {imported} local cnblogs posts; "
        f"archived {archived} heavy posts; "
        f"skipped {skipped}; "
        f"removed {removed} previous imports."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
