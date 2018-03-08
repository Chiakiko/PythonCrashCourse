# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 10:23

# 第2章 变量和简单数据类型

# 变量
message = "Hello Python World"
print(message)

# 大小写输出
print(message.upper())
print(message.lower())
print(message.title())

# 合并字符串
first_name = "ada"
last_name = "lovelace"
print(first_name + last_name)

# 制表符和换行符
print("\tPython\nI love.")

# 删除空白
favorite_language = " Python "
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())

# 使用字符串避免语法错误
# 字符串含有单引号
message = "it's my dog."
print(message)
# 字符串含有单引号、双引号
message = "it's name \"hhhh\""
print(message)

# 使用str()函数转换数字类型
age = 12
print("my age is " + str(age))

