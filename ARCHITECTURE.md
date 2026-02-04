# System Architecture

## 1. Product Architecture (产品架构)

```mermaid
graph TD
    subgraph "内容生产 (Content Authoring)"
        Author[作者 / 开发者]
        MD[Markdown/MDX 文件]
        Config[Frontmatter 配置]
        Assets[图片/资源]
        
        Author -->|编写| MD
        Author -->|配置| Config
        Author -->|上传| Assets
    end

    subgraph "博客系统 (Blog System)"
        direction TB
        
        subgraph "内容展示 (Presentation)"
            Home[首页列表]
            Post[文章详情页]
            About[关于页面]
            Error404[404 页面]
        end
        
        subgraph "发现与导航 (Discovery & Navigation)"
            Tags[标签系统]
            Search[全站搜索 (Pagefind)]
            RSS[RSS 订阅源]
            Nav[全局导航]
        end
        
        subgraph "用户体验 (UX/UI)"
            Typography[极致排版体系]
            DarkMode[深色模式支持]
            Responsive[响应式布局]
        end
    end

    subgraph "终端用户 (End User)"
        Reader[读者]
    end

    MD --> Post
    Post --> Typography
    
    Reader -->|访问| Home
    Reader -->|阅读| Post
    Reader -->|搜索| Search
    Reader -->|筛选| Tags
    Reader -->|订阅| RSS
    
    Home -->|链接| Post
    Nav -->|跳转| Home
    Nav -->|跳转| Tags
    Nav -->|跳转| About
    
    Search -->|索引结果| Post
    Tags -->|聚合| Post
```

## 2. Technical Design Architecture (技术设计架构)

```mermaid
C4Context
    title 技术设计架构图 (Technical Architecture)

    Person(developer, "Developer", "撰写文章 & 代码")
    
    System_Boundary(source_layer, "Source Layer (src/)") {
        Container(content, "Content Collections", "Markdown/MDX", "src/content/posts/*.md")
        Container(pages, "Astro Pages", ".astro", "路由与页面逻辑")
        Container(components, "UI Components", ".astro", "Header, Footer, Search...")
        Container(styles, "Styling", "CSS/Tailwind", "Tailwind v4 + Typography")
    }

    System_Boundary(build_system, "Build System") {
        Component(astro_core, "Astro Core", "SSG", "静态站点生成")
        Component(vite, "Vite", "Bundler", "构建与优化")
        Component(tailwind_plugin, "Tailwind Plugin", "PostCSS/Vite", "样式生成")
        Component(shiki, "Shiki", "Syntax Highlighter", "代码高亮处理")
    }

    System_Boundary(integrations, "Integrations & Tools") {
        Component(pagefind, "Pagefind", "Search Engine", "构建后静态索引生成")
        Component(rss_plugin, "@astrojs/rss", "RSS Generator", "XML 生成")
    }

    System_Boundary(output_layer, "Dist / Output") {
        Container(static_html, "Static HTML", "HTML5", "预渲染页面")
        Container(static_assets, "Assets", "JS/CSS/Images", "优化后的资源")
        Container(search_index, "Search Index", "WASM/JSON", "Pagefind 索引文件")
    }

    developer --> content : 编写
    developer --> pages : 开发
    
    content --> astro_core : Data Ingestion (zod schema)
    pages --> astro_core : Page Generation
    components --> pages : Import
    styles --> tailwind_plugin : Configuration
    
    astro_core --> shiki : Markdown Processing
    astro_core --> vite : Bundle Assets
    astro_core --> rss_plugin : Generate Feed
    
    vite --> static_html : Emit
    vite --> static_assets : Emit
    
    static_html --> pagefind : Indexing (postbuild)
    pagefind --> search_index : Generate
```
