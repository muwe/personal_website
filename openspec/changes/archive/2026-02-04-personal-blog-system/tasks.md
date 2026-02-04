## 1. 基础架构搭建

- [x] 1.1 初始化 Astro 项目
  - 使用 `create-astro` 初始化项目骨架
  - 配置 TypeScript
  - 清理默认生成的示例文件
- [x] 1.2 配置 Tailwind CSS
  - 安装并初始化 Tailwind CSS
  - 配置 `tailwind.config.mjs`，设置字体栈（SF Pro, Inter, System UI）
  - 安装并配置 `@tailwindcss/typography` 插件
- [x] 1.3 建立项目目录结构
  - 创建 `src/components`, `src/layouts`, `src/pages`, `src/content` 等目录
  - 创建基础 CSS 文件 `src/styles/global.css` 并配置 @tailwind 指令

## 2. 核心布局与主题（Site Architecture）

- [x] 2.1 实现基础布局组件 (BaseLayout)
  - 创建 `src/layouts/BaseLayout.astro`
  - 实现 HTML 骨架、Meta 标签（SEO基础）
  - 集成 Header 和 Footer 组件槽位
- [x] 2.2 实现 Header 和 Navigation 组件
  - 创建响应式 Navigation 组件
  - 实现 Desktop/Mobile 菜单切换逻辑
- [x] 2.3 设置 Typography 主题样式
  - 在 `global.css` 或 tailwind config 中定义排版层级（H1-H6, p, ul/ol）
  - 针对中文阅读优化行高和字间距
- [x] 2.4 实现深色模式支持
  - 配置 Tailwind darkMode class 策略
  - 实现主题切换逻辑（检测系统偏好 + 手动切换按钮）

## 3. 内容与数据层（Content Management）

- [x] 3.1 配置 Content Collections
  - 定义 `src/content/config.ts`
  - 为 `posts` 集合定义 Schema（zod 验证：title, date, tags, description 等）
- [x] 3.2 实现 Markdown/MDX 渲染页面
  - 创建动态路由 `src/pages/posts/[...slug].astro`
  - 使用 Astro 内置的 `render()` 获取内容
  - 文章页面的排版容器 (`prose` class) 样式微调
- [x] 3.3 代码高亮与样式
  - 配置 Shiki (Astro 内置) 主题
  - 添加代码块的样式优化（如圆角、复制按钮准备）

## 4. UI 页面实现（User Interface）

- [x] 4.1 实现首页文章列表
  - 在 `src/pages/index.astro` 查询并排序最近文章
  - 设计并实现极简风格的文章卡片组件 (`PostPreview`)
- [x] 4.2 完善文章详情页设计
  - 优化 Header 元信息展示（日期、标签）
  - 添加“下一篇/上一篇”导航
- [x] 4.3 创建关于页面
  - `src/pages/about.astro`
- [x] 4.4 404 页面
  - `src/pages/404.astro`

## 5. 发现与功能特性（Discovery Features）

- [x] 5.1 实现标签（Tags）系统
  - 生成标签索引页 `src/pages/tags/index.astro`
  - 生成特定标签页 `src/pages/tags/[tag].astro`
- [x] 5.2 集成 Pagefind 搜索
  - 安装 Pagefind 依赖或 CLI 工具
  - 添加搜索组件 UI (`Search.astro`)
  - 配置构建后脚本 (`postbuild`) 运行 Pagefind 索引
- [x] 5.3 RSS Feed 生成
  - 安装 `@astrojs/rss`
  - 配置 `src/pages/rss.xml.js` 生成 Feed

## 6. 构建与验证

- [x] 6.1 生产环境构建测试
  - 运行 `npm run build`
  - 验证静态文件生成
- [x] 6.2 Lighthouse 性能初步跑分
  - 确保无明显的性能瓶颈或 CLS 问题
