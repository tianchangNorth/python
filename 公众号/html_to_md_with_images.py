#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to Markdown converter with image download support
将HTML文章转换为Markdown格式，同时下载图片避免防盗链问题
"""

import os
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup
import time
import hashlib

def download_image(image_url, save_dir="images", referer=None):
    """
    下载图片并返回本地路径
    
    Args:
        image_url (str): 图片URL
        save_dir (str): 保存目录
        referer (str): 设置referer头，避免防盗链
    
    Returns:
        str: 本地图片路径，如果下载失败返回原URL
    """
    try:
        # 创建图片保存目录
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # 设置请求头，模拟浏览器请求并设置referer
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        
        # 设置referer为微信域名，避免防盗链
        if referer:
            headers['Referer'] = referer
        elif 'mmbiz.qpic.cn' in image_url:
            headers['Referer'] = 'https://mp.weixin.qq.com/'
        
        # 发送请求下载图片
        response = requests.get(image_url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 根据URL生成文件名
        parsed_url = urllib.parse.urlparse(image_url)
        
        # 从URL中提取文件扩展名
        path = parsed_url.path
        if '?' in image_url:
            # 处理带参数的URL，如 ?wx_fmt=jpeg
            query = urllib.parse.parse_qs(parsed_url.query)
            if 'wx_fmt' in query:
                ext = '.' + query['wx_fmt'][0]
            else:
                ext = os.path.splitext(path)[1] or '.jpg'
        else:
            ext = os.path.splitext(path)[1] or '.jpg'
        
        # 使用URL的hash作为文件名，避免重复和特殊字符问题
        url_hash = hashlib.md5(image_url.encode()).hexdigest()[:12]
        filename = f"image_{url_hash}{ext}"
        filepath = os.path.join(save_dir, filename)
        
        # 如果文件已存在，直接返回路径
        if os.path.exists(filepath):
            print(f"图片已存在: {filename}")
            return filepath
        
        # 保存图片
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"下载成功: {filename}")
        time.sleep(0.5)  # 避免请求过快
        return filepath
        
    except Exception as e:
        print(f"下载图片失败 {image_url}: {e}")
        return image_url  # 下载失败时返回原URL

def html_to_markdown_with_images(html_file_path, output_file_path=None, download_images=True):
    """
    将HTML文件转换为Markdown格式，同时下载图片
    
    Args:
        html_file_path (str): HTML文件路径
        output_file_path (str): 输出的Markdown文件路径，如果为None则自动生成
        download_images (bool): 是否下载图片
    
    Returns:
        str: 生成的Markdown文件路径
    """
    
    # 读取HTML文件
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 查找主要内容区域
    content_div = soup.find('div', {'id': 'js_content'})
    if not content_div:
        content_div = soup.find('body')
    
    if not content_div:
        raise ValueError("无法找到HTML内容区域")
    
    # 如果需要下载图片，先处理所有图片
    if download_images:
        images = content_div.find_all('img')
        print(f"找到 {len(images)} 张图片，开始下载...")
        
        # 创建图片目录
        html_dir = os.path.dirname(html_file_path)
        images_dir = os.path.join(html_dir, "images")
        
        for img in images:
            src = img.get('data-src') or img.get('src')
            if src and src.startswith('http'):
                local_path = download_image(src, images_dir)
                # 更新图片标签的src属性为本地路径
                if local_path != src:  # 下载成功
                    # 转换为相对路径
                    rel_path = os.path.relpath(local_path, html_dir)
                    img['src'] = rel_path
                    img['data-src'] = rel_path
    
    # 转换为Markdown
    markdown_content = convert_to_markdown(content_div)
    
    # 生成输出文件路径
    if output_file_path is None:
        base_name = os.path.splitext(html_file_path)[0]
        output_file_path = base_name + '.md'
    
    # 清理和格式化Markdown
    cleaned_markdown = clean_markdown(markdown_content)
    
    # 写入Markdown文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_markdown)
    
    return output_file_path

def convert_to_markdown(element):
    """
    递归将HTML元素转换为Markdown
    
    Args:
        element: BeautifulSoup元素
    
    Returns:
        str: Markdown格式的文本
    """
    markdown = ""
    
    for child in element.children:
        if child.name is None:  # 文本节点
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
        elif child.name == 'strong' or child.name == 'b':
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '**' + content + '**'
        elif child.name == 'em' or child.name == 'i':
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '*' + content + '*'
        elif child.name == 'img':
            # 处理图片，优先使用本地路径
            src = child.get('src') or child.get('data-src', '')
            alt = child.get('alt', '')
            if src:
                markdown += f'\n![{alt}]({src})\n'
        elif child.name == 'a':
            # 处理链接
            href = child.get('href', '')
            text = convert_to_markdown(child).strip()
            if href and text:
                markdown += f'[{text}]({href})'
            elif text:
                markdown += text
        elif child.name in ['ul', 'ol']:
            # 处理列表
            list_content = convert_list_to_markdown(child)
            if list_content:
                markdown += '\n' + list_content + '\n'
        elif child.name == 'li':
            content = convert_to_markdown(child).strip()
            if content:
                markdown += '- ' + content + '\n'
        elif child.name == 'span':
            # 检查是否有特殊样式
            style = child.get('style', '')
            content = convert_to_markdown(child).strip()
            
            if 'color: rgb(16, 188, 97)' in style and content:
                # 绿色文字，可能是重点内容
                markdown += '**' + content + '**'
            elif content:
                markdown += content
        else:
            # 递归处理其他元素
            content = convert_to_markdown(child)
            markdown += content
    
    return markdown

def convert_list_to_markdown(list_element):
    """
    将HTML列表转换为Markdown列表
    
    Args:
        list_element: BeautifulSoup列表元素
    
    Returns:
        str: Markdown格式的列表
    """
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
    """
    清理和格式化Markdown文本
    
    Args:
        markdown_text (str): 原始Markdown文本
    
    Returns:
        str: 清理后的Markdown文本
    """
    # 移除多余的空行
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    
    # 移除行首行尾的空白字符
    lines = markdown_text.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    markdown_text = '\n'.join(cleaned_lines)
    
    # 再次移除多余的空行
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    
    return markdown_text.strip()

if __name__ == "__main__":
    # 转换article.html并下载图片
    html_file = "article.html"
    
    if os.path.exists(html_file):
        try:
            print("开始转换HTML并下载图片...")
            output_file = html_to_markdown_with_images(html_file, download_images=True)
            
            print(f"转换完成！输出文件：{output_file}")
            
            # 显示文件信息
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"文件大小：{len(content)} 字符")
            
            # 统计下载的图片数量
            images_dir = os.path.join(os.path.dirname(html_file), "images")
            if os.path.exists(images_dir):
                image_count = len([f for f in os.listdir(images_dir) 
                                 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))])
                print(f"共下载图片：{image_count} 张")
            
        except Exception as e:
            print(f"转换失败：{e}")
    else:
        print(f"HTML文件不存在：{html_file}")