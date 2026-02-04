## 为什么

当前需要构建一个专注于极致文字排版美感的个人博客系统。目标是参考 [blog.leowang.net](https://blog.leowang.net/) 的风格（极简、高对比度、优秀衬线字体排版），并使用现代化的技术栈（Astro + Tailwind CSS）来实现高性能和易维护性。

## 变更内容

将构建一个新的博客站点，主要包含以下内容：
1. **基础架构**：使用 Astro 框架初始化项目，配置 Tailwind CSS。
2. **视觉设计**：复刻极简主义风格，专注于字体排版（Typography）、间距和阅读体验。
3. **内容系统**：支持 Markdown/MDX 撰写文章，支持 YAML Frontmatter 元数据。
4. **功能模块**：
   - 首页文章列表
   - 文章详情页
   - 标签（Tags）系统
   - 站内搜索功能
   - 响应式设计（移动端适配）

## 功能 (Capabilities)

### 新增功能

- `site-architecture`: 站点基础架构，包含 Astro 配置、Tailwind 主题定制（字体、配色）、布局组件（Layouts）。
- `content-management`: 内容管理功能，处理 Markdown 解析、MDX 组件支持、代码高亮、Frontmatter 验证。
- `user-interface`: 核心页面实现，包括首页列表、文章详情页（排版优化）、关于页面。
- `discovery-features`: 内容发现功能，包含全站搜索（基于静态索引或轻量级方案）、标签云/分类归档。

### 修改功能

<!-- 现有功能，其需求发生变更（不仅仅是实现）。
     仅当规范级行为发生变更时才在此列出。每个都需要一个增量规范文件。
     使用项目目录中 specs/ 的现有规范名称。如果没有需求变更，请留空。 -->

## 影响

- **代码结构**：将在工作区中新增 Astro 项目相关文件。
- **依赖项**：引入 Astro, Tailwind CSS, 及相关排版插件 (`@tailwindcss/typography`)。
- **构建流程**：需要配置静态站点生成（SSG）的构建脚本。
