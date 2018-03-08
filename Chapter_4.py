# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 11:45

# 第4章 操作列表

# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Python函数range()来创建数值列表
for i in range(1, 5):
    print(i)

# 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)

# 对数字列表进行简单统计
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 列表解析，让你一行代码就可以生成列表
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:])
print(players[0:3])
print(players[:2])

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players:
    print(player)

# 复制切片

players1 = ['charles', 'martina', 'michael', 'florence', 'eli']
# 浅复制
players2 = players1
# 深复制
players2 = players1[:]

print(players2)

# 定义元组(tuple)
dimensions = (200, 50)
print(dimensions[0])

# 元组不可修改
# dimensions[0] = 100
print(dimensions)

for dimension in dimensions:
    print(dimension)