## 新增需求

### 需求：HTML 内容转换
导入工具必须能够将源网址的 HTML 内容转换为符合 Astro 内容集合格式的 Markdown。

#### 场景：转换文章正文
- **当** 工具获取到文章页面的 HTML
- **那么** 它必须将 `.gh-content` (或对应正文容器) 内的 HTML 转换为 Markdown
- **并且** 保留标题 (h1-h6)、列表 (ul/ol)、引用 (blockquote) 和粗体/斜体格式

### 需求：本地化图片资源
导入工具必须下载文章中引用的外部图片并存储到本地。

#### 场景：处理文章图片
- **当** 工具在正文中发现 `<img>` 标签
- **那么** 它必须下载 `src` 指向的图片文件
- **并且** 将其保存到 `public/images/posts/<slug>/` 目录
- **并且** 将 Markdown 中的图片链接替换为本地相对路径 `/images/posts/<slug>/<filename>`

### 需求：Frontmatter 生成
导入工具必须根据页面元数据生成完整的 Markdown Frontmatter。

#### 场景：生成 Frontmatter
- **当** 解析文章页面时
- **那么** 必须从 `<meta property="og:title">` 提取标题
- **并且** 从 `<meta property="og:description">` 提取描述
- **并且** 从 `<meta property="article:published_time">` 提取发布日期
- **并且** 从 `<meta property="og:image">` 提取头图（heroImage）并下载到本地
