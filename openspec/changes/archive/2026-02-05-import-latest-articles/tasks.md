## 1. 脚本准备

- [x] 1.1 创建 `import_articles.py` 脚本，引入必要的 Python 库 (requests, beautifulsoup4)
- [x] 1.2 实现 `fetch_article_html(url)` 函数，模拟浏览器 User-Agent 获取内容
- [x] 1.3 实现 `download_image(url, save_path)` 函数，处理图片下载

## 2. 核心逻辑实现

- [x] 2.1 实现 `parse_frontmatter(html)` 提取 Title, Description, PublishedTime, Tags 和 HeroImage
- [x] 2.2 实现 `html_to_markdown(html)` 转换逻辑，保留指定标签格式，替换图片路径为本地相对路径
- [x] 2.3 集成主流程：遍历目标文章列表，执行下载、转换和文件写入

## 3. 执行与验证

- [x] 3.1 运行脚本导入“苏格拉底终极追问”
- [x] 3.2 运行脚本导入“Moltbook上最令人不安的7条AI帖子”
- [x] 3.3 运行脚本导入“OpenClaw”（确认并使用正确链接）
- [x] 3.4 验证所有导入文章在本地服务器 (`npm run dev`) 显示正常，图片加载无误
