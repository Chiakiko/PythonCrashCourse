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
with open('venv\\pip-selfcheck.json') as f:
    print(f.read())

# 10.1.3 逐行读取
with open('Chapter_10.py', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

# 10.1.4 创建一个包含文件各行的列表
lines = []
with open('Chapter_10.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(type(lines))
print(lines)

# 10.1.5 使用文件的内容

# 10.1.6 包含一百万位的大型文件

# 10.1.7 圆周率中包含你的生日吗
birthday = '20180202'
pi_string = '3.14xxxxxxxxxxxxxxxx...'
if birthday in pi_string:
    print('yes has')
else:
    print('not has')

"""
10.2 写入文件
"""
# 10.2.1 写入空文件
filename = 'write_message.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write('I love python.')

# 10.2.2 写入多行
filename = 'write_message.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write('1:I love python.\n')
    f.write('2:I love python.\n')

# 10.2.3 附加到文件
filename = 'write_message.txt'
with open(filename, 'a', encoding='utf-8') as f:
    f.write('3:I love python.\n')

"""
10.3 异常
"""
# 10.3.1 处理ZeroDivisionError异常

# 10.3.2 使用try-except代码块

# 10.3.3 使用异常避免崩溃

# 10.3.4 else代码块：在正常执行try代码块后，跳过excepition代码块，进而执行else代码块。

# 10.3.5 处理FileNotFoundError异常

# 10.3.6 分析文本
# string.split()

# 10.3.7 使用多个文件

# 10.3.8 失败时一声不啃
try:
    with open('notfile') as f:
        print(f.readlines())
except FileNotFoundError:
    # 一声不啃
    pass
else:
    pass

# 10.3.9 决定报告哪些错误

"""
10.4 存储数据
"""
# 10.4.1 使用json.dump()和json.load()
import json


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def obj_2_json(obj):
    return {'name': obj.name,
            'age': obj.age}


a = A('john', 26)
with open('obj.json', 'w') as f_obj:
    f_obj.write(json.dumps(a, default=obj_2_json))

# dumps是将dict转化成str格式，loads是将str转化成dict格式。
# dump和load也是类似的功能，只是与文件操作结合起来了。

# 10.4.2 保存和读取用户生成的数据
# json.dump()和json.load()用法

# 10.4.3 重构

"""
10.5 小结
"""