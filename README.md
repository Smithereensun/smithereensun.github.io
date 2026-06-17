# 浮光笔记

一个基于 Hugo + GitHub Pages + GitHub Actions 的个人博客模板。

## 本地预览

```bash
hugo server -D
```

## 部署方式

1. 把仓库推到 GitHub。
2. 在仓库设置里打开 GitHub Pages，Source 选 `GitHub Actions`。
3. 直接推送到 `main` 分支即可自动构建和发布。

## 你可以直接改的地方

- `hugo.toml` 里的站点标题、简介、联系方式。
- `content/posts/` 下的文章。
- `content/about.md` 里的个人介绍。

## 设计取向

- 大面积留白 + 柔和渐变背景。
- 卡片式文章列表，移动端优先。
- 首页强调作者气质和最新内容，而不是堆功能。
