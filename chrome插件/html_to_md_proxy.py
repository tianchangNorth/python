#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to Markdown converter with anti-hotlinking bypass solutions
使用代理服务绕过防盗链，无需下载图片
"""

import os
import re
from bs4 import BeautifulSoup
import urllib.parse

def get_proxy_image_url(original_url, proxy_service="images.weserv.nl"):
    """
    通过代理服务获取图片URL，绕过防盗链
    
    Args:
        original_url (str): 原始图片URL
        proxy_service (str): 代理服务类型
    
    Returns:
        str: 代理后的图片URL
    """
    
    if not original_url or not original_url.startswith('http'):
        return original_url
    
    # 编码原始URL
    encoded_url = urllib.parse.quote(original_url, safe='')
    
    if proxy_service == "images.weserv.nl":
        # 使用 images.weserv.nl 服务（免费图片代理CDN）
        base_url = f"https://images.weserv.nl/?url={encoded_url}"
        
        # 检查是否为GIF图片，如果是则添加&n=-1参数以支持动图
        if 'gif' in original_url.lower() or 'wx_fmt=gif' in original_url.lower():
            base_url += "&n=-1"
        
        return base_url
    
    elif proxy_service == "imageproxy.pimg.tw":
        # 使用 imageproxy 服务
        return f"https://imageproxy.pimg.tw/resize?url={encoded_url}"
    
    elif proxy_service == "cors-anywhere":
        # 使用 CORS Anywhere 代理（需要自建或使用公共服务）
        return f"https://cors-anywhere.herokuapp.com/{original_url}"
    
    elif proxy_service == "proxy.cors.sh":
        # 使用 proxy.cors.sh 服务
        return f"https://proxy.cors.sh/{original_url}"
    
    elif proxy_service == "github_proxy":
        # 对于微信图片，可以尝试GitHub代理方案
        if 'mmbiz.qpic.cn' in original_url:
            # 将微信图片URL转换为可访问的格式
            return original_url.replace('https://mmbiz.qpic.cn', 'https://mmbiz.qpic.cn')
    
    return original_url

def create_data_uri_placeholder(original_url):
    """
    创建占位符data URI，显示图片URL信息
    
    Args:
        original_url (str): 原始图片URL
    
    Returns:
        str: Base64编码的占位符图片
    """
    # 简单的SVG占位符
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">
    <rect width="100%" height="100%" fill="#f0f0f0" stroke="#ccc"/>
    <text x="200" y="100" text-anchor="middle" font-family="Arial" font-size="12" fill="#666">
        图片链接: {original_url[:50]}...
    </text>
    </svg>'''
    
    import base64
    encoded = base64.b64encode(svg_content.encode()).decode()
    return f"data:image/svg+xml;base64,{encoded}"

def html_to_markdown_with_proxy(html_file_path, output_file_path=None, proxy_method="images.weserv.nl"):
    """
    将HTML转换为Markdown，使用代理服务处理图片防盗链
    
    Args:
        html_file_path (str): HTML文件路径
        output_file_path (str): 输出文件路径
        proxy_method (str): 代理方法选择
    
    Returns:
        str: 输出文件路径
    """
    
    # 读取HTML文件
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    content_div = soup.find('div', {'id': 'js_content'}) or soup.find('body')
    
    if not content_div:
        raise ValueError("无法找到HTML内容区域")
    
    # 处理图片链接
    images = content_div.find_all('img')
    print(f"找到 {len(images)} 张图片，正在处理...")
    
    for img in images:
        original_src = img.get('data-src') or img.get('src', '')
        if original_src and original_src.startswith('http'):
            if proxy_method == "placeholder":
                # 使用占位符方案
                new_src = create_data_uri_placeholder(original_src)
            else:
                # 使用代理服务
                new_src = get_proxy_image_url(original_src, proxy_method)
            
            img['src'] = new_src
            if img.get('data-src'):
                img['data-src'] = new_src
            
            print(f"处理图片: {original_src[:50]}... -> {new_src[:50]}...")
    
    # 转换为Markdown
    markdown_content = convert_to_markdown(content_div)
    cleaned_markdown = clean_markdown(markdown_content)
    
    # 输出文件
    if output_file_path is None:
        base_name = os.path.splitext(html_file_path)[0]
        suffix = f"_proxy_{proxy_method.replace('.', '_')}"
        output_file_path = base_name + suffix + '.md'
    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_markdown)
    
    return output_file_path

def convert_to_markdown(element):
    """转换HTML元素为Markdown"""
    markdown = ""
    
    for child in element.children:
        if child.name is None:
            text = str(child).strip()
            if text:
                markdown += text
        elif child.name == 'br':
            markdown += '\n'
        elif child.name in ['p', 'div', 'section']:
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '\n\n' + content + '\n'
        elif child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(child.name[1])
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '\n' + '#' * level + ' ' + content + '\n'
        elif child.name in ['strong', 'b']:
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '**' + content + '**'
        elif child.name in ['em', 'i']:
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '*' + content + '*'
        elif child.name == 'img':
            src = child.get('src') or child.get('data-src', '')
            alt = child.get('alt', '')
            if src:
                markdown += f'\n![{alt}]({src})\n'
        elif child.name == 'a':
            href = child.get('href', '')
            text = convert_to_markdown(child).strip()
            if href and text:
                markdown += f'[{text}]({href})'
            elif text:
                markdown += text
        elif child.name in ['ul', 'ol']:
            list_content = convert_list_to_markdown(child)
            if list_content:
                markdown += '\n' + list_content + '\n'
        elif child.name == 'span':
            style = child.get('style', '')
            content = convert_to_markdown(child).strip()
            if 'color: rgb(16, 188, 97)' in style and content:
                markdown += '**' + content + '**'
            elif content:
                markdown += content
        else:
            content = convert_to_markdown(child)
            markdown += content
    
    return markdown

def convert_list_to_markdown(list_element):
    """转换列表为Markdown"""
    markdown = ""
    items = list_element.find_all('li', recursive=False)
    
    for i, item in enumerate(items):
        content = convert_to_markdown(item).strip()
        if content:
            if list_element.name == 'ol':
                markdown += f"{i+1}. {content}\n"
            else:
                markdown += f"- {content}\n"
    
    return markdown

def clean_markdown(markdown_text):
    """清理Markdown文本"""
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    lines = markdown_text.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    markdown_text = '\n'.join(cleaned_lines)
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    return markdown_text.strip()

def show_proxy_options():
    """显示可用的代理选项"""
    options = {
        "images.weserv.nl": "免费图片CDN代理服务，支持防盗链绕过",
        "imageproxy.pimg.tw": "台湾的图片代理服务",
        "cors-anywhere": "CORS代理服务（可能需要自建）",
        "proxy.cors.sh": "CORS代理服务",
        "placeholder": "生成占位符图片，显示原始链接信息"
    }
    
    print("可用的防盗链绕过方法：")
    for key, desc in options.items():
        print(f"  {key}: {desc}")
    print()

if __name__ == "__main__":
    html_file = "article.html"
    
    if not os.path.exists(html_file):
        print(f"HTML文件不存在：{html_file}")
        exit(1)
    
    show_proxy_options()
    
    # 提供多种方案
    methods = ["images.weserv.nl", "imageproxy.pimg.tw", "placeholder"]
    
    for method in methods:
        try:
            print(f"\n使用方法: {method}")
            output_file = html_to_markdown_with_proxy(html_file, proxy_method=method)
            
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"转换完成：{output_file}")
            print(f"文件大小：{len(content)} 字符")
            
        except Exception as e:
            print(f"方法 {method} 失败：{e}")
    
    print(f"\n推荐使用: article_proxy_images_weserv_nl.md")
    print("该文件使用 images.weserv.nl 代理服务，可以绕过大部分防盗链限制。")