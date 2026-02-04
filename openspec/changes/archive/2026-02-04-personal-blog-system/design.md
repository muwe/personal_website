## 上下文

当前用户希望建立一个新的个人博客，强调极简美学和极致的文字排版体验。参考对象为 [blog.leowang.net](https://blog.leowang.net/)。项目将是一个全新的代码库，位于现有工作区中。

## 目标 / 非目标

**目标：**
- **极致的阅读体验**：专注于字体、行高、间距与其垂直韵律（Vertical Rhythm）。
- **高性能**：Lighthouse 评分目标 100（Performance, Accessibility, Best Practices, SEO）。
- **极简设计**：无干扰元素，内容优先。
- **现代化开发体验**：基于 Astro + Tailwind，支持组件化开发。
- **易于写作**：支持 Markdown/MDX，方便管理文章。

**非目标：**
- **不支持后台管理界面**：通过 Git + Markdown 文件管理内容，不开发 CMS 后台。
- **不包含复杂的用户系统**：无登录/注册/评论系统（评论可接入第三方如 Cusdis/Giscus，但不在本次核心构建范围内）。

## 决策

1.  **框架选择：Astro**
    - **理由**：Astro 默认输出 0 KB JavaScript，非常适合内容驱动的网站（Content-focused websites）。其 Islands Architecture 允许按需加载交互组件。
    - **替代方案**：Hugo（构建极快但模板语法较旧，扩展性不如组件化框架），Next.js（对于纯静态博客略显厚重）。

2.  **样式方案：Tailwind CSS + @tailwindcss/typography**
    - **理由**：Tailwind 提供了一致的设计系统约束（Design Tokens），配合 Typography 插件可以快速实现高质量的排版默认值（prose），随后进行微调。
    - **替代方案**：CSS Modules / Scoped CSS（编写和维护成本较高）。

3.  **搜索方案：Pagefind**
    - **理由**：专为静态站点设计的搜索库，构建时索引，运行时零后端依赖，带宽占用极低。
    - **替代方案**：Fuse.js（需加载全量 JSON 索引，文章多时影响性能），Algolia（需外部服务配置）。

4.  **字体策略：系统字体栈优先 + Web Font 优化**
    - **理由**：优先使用 Apple 系统的 San Francisco / New York 字体以获得原生体验。对于中文，使用系统默认衬线/无衬线栈，辅以 Web Font（需进行子集化 Subsetting）以保证美观与性能的平衡。

## 风险 / 权衡

- **风险**：Web Font 中文字体体积过大导致 LCP (Largest Contentful Paint) 延迟。
  - **缓解**：默认使用系统字体栈；若必须引入自定义中文字体，使用字体子集化工具或 Google Fonts 的切片加载；配置 `font-display: swap`。
- **风险**：极致微调排版非常耗时。
  - **缓解**：先使用 Typography 插件的默认优秀配置，再针对中文阅读习惯（如行高 1.6-1.8）进行覆盖调整。

## 迁移计划

- 这是一个新项目，无需迁移旧数据。
- 部署流程：配置 `npm run build` 生成 `dist/` 目录，可直接部署至任何静态托管服务。

## Open Questions

- 是否需要深色模式（Dark Mode）？默认设计包含深色模式支持。
