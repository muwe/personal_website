import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import datetime
import re

# Articles to import
ARTICLES = [
    {
        "url": "https://blog.leowang.net/99kmmeumw71/",
        "slug": "socrates-ai-consciousness",
        "fallback_title": "苏格拉底终极追问：AI，你有意识吗？"
    },
    {
        "url": "https://blog.leowang.net/vpv0byekvzf/",
        "slug": "moltbook-ai-posts",
        "fallback_title": "Moltbook上最令人不安的7条AI帖子"
    },
    {
        # Using the correct URL from proposal logic
        "url": "https://blog.leowang.net/v3pbe7ibw5g/",
        "slug": "openclaw-agent-era",
        "fallback_title": "OpenClaw：一个奥地利程序员如何意外点燃智能体时代的第一把火"
    }
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_article_html(url):
    print(f"Fetching {url}...")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def download_image(url, save_dir):
    if not url:
        return None
    
    try:
        # Parse filename from URL
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename:
             return None
             
        # Create directory if needed
        os.makedirs(save_dir, exist_ok=True)
        
        save_path = os.path.join(save_dir, filename)
        
        if os.path.exists(save_path):
            print(f"Sample skipped (exists): {filename}")
            return filename

        print(f"Downloading image: {url}")
        response = requests.get(url, headers=HEADERS, stream=True)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        return filename
    except Exception as e:
        print(f"Error downloading image {url}: {e}")
        return None

def html_to_markdown(soup, img_save_dir, relative_img_path):
    # Find main content
    content_div = soup.find(class_='gh-content') 
    if not content_div:
        # Fallback for other themes
        content_div = soup.find('section', class_='post-content')
        
    if not content_div:
        return ""

    markdown_lines = []
    
    for element in content_div.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'blockquote', 'figure', 'pre'], recursive=False):
        if element.name == 'p':
            # Handle inline images within P tags (common in Ghost)
            img = element.find('img')
            if img:
                 src = img.get('src')
                 if src:
                    filename = download_image(src, img_save_dir)
                    if filename:
                        markdown_lines.append(f"![{img.get('alt', '')}]({relative_img_path}/{filename})\n")
            else:
                text = element.get_text().strip()
                if text:
                    markdown_lines.append(f"{text}\n")
                    
        elif element.name in ['h1', 'h2', 'h3', 'h4']:
            level = int(element.name[1])
            markdown_lines.append(f"{'#' * level} {element.get_text().strip()}\n")
            
        elif element.name == 'ul':
            for li in element.find_all('li'):
                markdown_lines.append(f"- {li.get_text().strip()}")
            markdown_lines.append("")
            
        elif element.name == 'ol':
            for i, li in enumerate(element.find_all('li'), 1):
                markdown_lines.append(f"{i}. {li.get_text().strip()}")
            markdown_lines.append("")
            
        elif element.name == 'blockquote':
            text = element.get_text().strip()
            markdown_lines.append(f"> {text}\n")
            
        elif element.name == 'figure':
            img = element.find('img')
            if img:
                src = img.get('src')
                if src:
                    filename = download_image(src, img_save_dir)
                    if filename:
                        caption = element.find('figcaption')
                        alt = img.get('alt', '')
                        if caption:
                            alt = caption.get_text().strip()
                        markdown_lines.append(f"![{alt}]({relative_img_path}/{filename})\n")

    return "\n".join(markdown_lines)

def process_article(article):
    html = fetch_article_html(article["url"])
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    
    # Meta extraction
    title = soup.find("meta", property="og:title")
    title = title["content"] if title else article["fallback_title"]
    
    desc = soup.find("meta", property="og:description")
    description = desc["content"] if desc else ""
    
    pub_time = soup.find("meta", property="article:published_time")
    pub_date = pub_time["content"].split("T")[0] if pub_time else datetime.date.today().isoformat()
    
    hero_meta = soup.find("meta", property="og:image")
    hero_image_url = hero_meta["content"] if hero_meta else None
    
    # Setup paths
    slug = article["slug"]
    img_dir = f"public/images/posts/{slug}"
    rel_img_path = f"/images/posts/{slug}"
    
    # Download hero image
    hero_image_path = ""
    if hero_image_url:
        filename = download_image(hero_image_url, img_dir)
        if filename:
            hero_image_path = f"{rel_img_path}/{filename}"
            
    # Convert content
    content_md = html_to_markdown(soup, img_dir, rel_img_path)
    
    # Create Markdown file
    md_content = f"""---
title: '{title}'
description: '{description}'
pubDate: '{pub_date}'
heroImage: '{hero_image_path}'
tags: ["AI", "Imported"]
---

{content_md}
"""

    output_file = f"src/content/posts/{slug}.md"
    os.makedirs("src/content/posts", exist_ok=True)
    
    with open(output_file, "w") as f:
        f.write(md_content)
        
    print(f"Successfully processed {slug} -> {output_file}")

if __name__ == "__main__":
    for article in ARTICLES:
        process_article(article)
