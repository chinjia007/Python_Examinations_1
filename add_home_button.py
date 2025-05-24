#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

# 要处理的文件列表
files_to_process = [
    "lesson1.html", "lesson2.html", "lesson3.html", "lesson4.html", "lesson5.html",
    "lesson6.html", "lesson7.html", "lesson8.html", "lesson9.html", "lesson10.html",
    "python_train.html"
]

print("开始处理文件...")

# CSS样式代码
home_button_css = """
/* 返回主页按钮样式 */
.home-button {
    position: absolute;
    right: 2rem;
    top: 50%;
    transform: translateY(-50%);
    background-color: var(--accent-color);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.2s ease, transform 0.2s ease;
    font-size: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    display: inline-flex;
    align-items: center;
}

.home-button:hover {
    background-color: var(--accent-color-dark);
    transform: translateY(-50%) translateY(-2px);
}

.home-button .fa-house {
    margin-right: 0.5rem;
}
"""

# HTML按钮代码
home_button_html = """
        <a href="index.html" class="home-button">
            <i class="fas fa-house"></i> 返回主页
        </a>"""

# 处理所有文件
for filename in files_to_process:
    print(f"正在处理文件: {filename}")
    
    if not os.path.exists(filename):
        print(f"文件 {filename} 不存在，跳过")
        continue
    
    # 读取文件内容
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"已读取文件: {filename}")
    except Exception as e:
        print(f"读取 {filename} 时出错: {e}")
        continue
    
    # 检查文件中是否已经有home-button样式或按钮
    if 'class="home-button"' in content:
        print(f"文件 {filename} 已存在home-button，跳过")
        continue
    
    # 添加CSS样式 - 在</style>标签之前添加
    css_added = False
    if "</style>" in content:
        content = content.replace("</style>", f"{home_button_css}\n    </style>", 1)
        css_added = True
        print(f"已为 {filename} 添加CSS样式")
    
    if not css_added:
        print(f"在 {filename} 中找不到</style>标签，无法添加CSS")
        continue
    
    # 添加按钮HTML - 在header标签中course-unit-title div后添加
    button_added = False
    
    # 尝试更精确的模式
    header_pattern = r'(<div class="course-unit-title">.*?</div>\s*</div>)(\s*</header>)'
    match = re.search(header_pattern, content, re.DOTALL)
    if match:
        content = re.sub(header_pattern, r'\1' + home_button_html + r'\2', content, flags=re.DOTALL)
        button_added = True
        print(f"已为 {filename} 添加返回主页按钮")
    
    if not button_added:
        print(f"在 {filename} 中找不到合适的位置添加按钮")
        continue
    
    # 写回文件
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"成功更新文件 {filename}")
    except Exception as e:
        print(f"写入 {filename} 时出错: {e}")

print("处理完成！") 