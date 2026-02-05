## 为什么

为了保持博客内容的新鲜度和相关性，我们需要从源博客（blog.leowang.net）同步最新的文章。这有助于在开发和测试期间使用真实、高质量的内容来验证博客系统的展示效果。

## 变更内容

我们将导入以下三篇最新文章，并确保完整保留其图片、布局和格式：

1.  **苏格拉底终极追问：AI，你有意识吗？**
    - 源链接: `https://blog.leowang.net/99kmmeumw71/`
2.  **Moltbook上最令人不安的7条AI帖子：AI的自我觉醒与人类的未来**
    - 源链接: `https://blog.leowang.net/vpv0byekvzf/`
3.  **OpenClaw：一个奥地利程序员如何意外点燃智能体时代的第一把火？**
    - 源链接: `https://blog.leowang.net/v3pbe7ibw5g/`
    *(注意：原文列表第三篇链接似乎重复了'楞严经观河之辩'的ID，但我将使用页面上实际显示的第三篇标题对应的内容，如果ID有误，我将尝试访问确认，这里暂定为第三篇)*
    *修正*: 仔细看列表，第三篇标题是 OpenClaw，链接是 `vpv0byekvzf` (同第二篇? 或者是列表解析误导)。
    让我们重新核对：
    - Pos 2 文本显示：
        1. 苏格拉底... (99kmmeumw71)
        2. Moltbook... (vpv0byekvzf)
        3. OpenClaw... (v3pbe7ibw5g - 这个ID在之前被识别为楞严经，可能爬取解析有误或者博客链接有误)
    
    不管怎样，我们的目标是导入"前三篇"。

具体变更包括：
-   获取这三篇文章的 HTML 内容。
-   将 HTML 转换为 Markdown，保留标题等级、引用、列表等格式。
-   下载文章内的所有图片到本地 `public/images/posts/<slug>/` 目录。
-   在 `src/content/posts/` 中创建对应的 `.md` 文件，包含正确的 frontmatter（标题、描述、日期、标签）。

## 功能 (Capabilities)

### 新增功能
- `content-import`: 导入外部文章并转换为本地 Markdown 内容，包括图片资源的本地化处理。

### 修改功能
<!-- 无需修改现有规范 -->

## 影响

- **内容目录**：`src/content/posts/` 将新增 3 个 markdown 文件。
- **公共资源**：`public/images/posts/` 将新增对应的图片文件夹。
