## 上下文

当前博客系统使用 Markdown 文件管理内容（`src/content/posts/`）。之前已成功手动/脚本批量导入过一批文章。本次需要定向导入特定的三篇最新文章。
由于这是单次操作而非建立永久同步流水线，我们将采用脚本辅助的方式进行。

## 目标 / 非目标

**目标：**
- 从 `blog.leowang.net` 精确导入 3 篇指定文章。
- 将 HTML 内容转换为高质量 Markdown。
- 自动提取并下载文章中的所有图片（从 Ghost 图床/CDN 下载到本地 `public/images/posts/<slug>/`）。
- 生成符合 Astro 内容集合 Schema 的 Frontmatter（Title, PubDate, Description, Tags, HeroImage）。

**非目标：**
- 建立持续自动同步机制。
- 处理非标准 HTML 结构（仅针对 Ghost 博客结构优化）。

## 决策

1.  **工具选择**：
    -   **选择**：复用/修改之前的 Python 脚本 `process_articles.py`（虽然之前已删除，我们将重新创建并针对性调整）。
    -   **理由**：Python 的 `BeautifulSoup` (或简单的 HTMLParser) 处理 HTML 抓取和图片下载非常高效。脚本是一次性的，用完即可归档。

2.  **图片存储**：
    -   **选择**：本地存储于 `public/images/posts/<slug>/`。
    -   **理由**：避免依赖外部图床链接（可能失效或有防盗链），符合已有的架构设计。

3.  **Frontmatter 提取**：
    -   **选择**：从 HTML Meta 标签提取（og:title, og:description, article:published_time）。
    -   **理由**：比解析正文更准确。

## 风险 / 权衡

-   **风险**：源站反爬虫。
    -   *缓解*：设置 User-Agent，适当延时。鉴于仅请求 3 个页面，风险极低。
-   **风险**：链接解析错误（如 Proposal 中提到的重复 ID）。
    -   *缓解*：手动确认 URL 列表，确保准确性。

## 迁移计划

无。此为新增内容操作。

## 未解决问题

-   需确认第三篇文章 "OpenClaw" 的准确 URL。将在脚本执行前或执行中再次验证。
