#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to Markdown converter
将HTML文章转换为Markdown格式
"""

import os
import re
from bs4 import BeautifulSoup

def html_to_markdown(html_file_path, output_file_path=None):
    """
    将HTML文件转换为Markdown格式
    
    Args:
        html_file_path (str): HTML文件路径
        output_file_path (str): 输出的Markdown文件路径，如果为None则自动生成
    
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
    
    # 转换为Markdown
    markdown_content = convert_to_markdown(content_div)
    
    # 生成输出文件路径
    if output_file_path is None:
        base_name = os.path.splitext(html_file_path)[0]
        output_file_path = base_name + '.md'
    
    # 写入Markdown文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
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
            # 处理图片
            src = child.get('data-src') or child.get('src', '')
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
    # 转换article.html
    html_file = "article.html"
    
    if os.path.exists(html_file):
        try:
            output_file = html_to_markdown(html_file)
            
            # 读取生成的Markdown并清理格式
            with open(output_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            cleaned_markdown = clean_markdown(markdown_content)
            
            # 重新写入清理后的内容
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_markdown)
            
            print(f"HTML转换完成！输出文件：{output_file}")
            print(f"文件大小：{len(cleaned_markdown)} 字符")
            
        except Exception as e:
            print(f"转换失败：{e}")
    else:
        print(f"HTML文件不存在：{html_file}")