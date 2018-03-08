# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 10:58

# 第3章 列表简介

# 在Python中，用方括号“[]”来表示列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0])

# 修改列表元素
bicycles[0] = 'ducati'
print(bicycles)

# 在列表中添加元素
bicycles.append('ducati')
print(bicycles)

# 在列表中插入元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
bicycles.insert(0, 'ducati')
print(bicycles)

# 在列表中删除元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[0]
print(bicycles)

# 使用方法pop()删除元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
pop_bicycles = bicycles.pop()
print(bicycles)
print(pop_bicycles)

# 根据值来删除元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
bicycles.remove('redline')
print(bicycles)

# 使用方法sort()对列表进行永久排序
cars = ['bmd', 'audi', 'toyota', 'subaru']
# 正向排序
cars.sort()
print(cars)
# 反向排序
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表进行临时排序
cars = ['bmd', 'audi', 'toyota', 'subaru']
sorted_cars = sorted(cars, reverse=True)
print(cars)
print(sorted_cars)

# 倒着打印列表
cars = ['bmd', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# 确定列表的长度
cars = ['bmd', 'audi', 'toyota', 'subaru']
print(len(cars))

