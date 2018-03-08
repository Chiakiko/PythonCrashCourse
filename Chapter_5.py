# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 15:56

# 第5章 if语句

# 一个简单的示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())

# 检查特定值是否包含在列表中
if 'bens' in cars:
    print('has bens')
else:
    print('not has bens')

if 'bmw' in cars:
    print('has bmw')
else:
    print('not has bmw')

# 确定列表不是空的
if cars:
    print(cars)
