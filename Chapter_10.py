# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 12:54

"""
第10章 文件和异常
"""

"""
10.1 从文件中读取数据
"""

# 10.1.1 读取整个文件
with open('Chapter_10.py', 'r', encoding='utf-8') as f:
    print(f.read())

# 10.1.2 文件路径
