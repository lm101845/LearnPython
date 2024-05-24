# @Date : 2024/3/21 16:18
# @Author : liming
import os
import re


def find_images_in_markdown_files(folder_path):
    # 正则表达式匹配Markdown中的图片链接，假设图片链接格式如：<img src="绝对路径\图片名.png">
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    # 遍历指定文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):  # 检查文件是否为Markdown文件
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    # 使用正则表达式查找图片链接
                    images = image_pattern.findall(content)
                    for image_path in images:
                        print(f"在文件 {file_path} 中找到图片: {image_path}")

                    # 使用函数，将你的文件夹路径替换为'your_folder_path'


find_images_in_markdown_files('D:\\01-file\\03-简书文章备份\\文章\\文章\\日记（2020）')

