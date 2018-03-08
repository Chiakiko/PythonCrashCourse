# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 18:09

# 第8章 函数

# 定义函数
def function_name():
    pass


# 向函数传递参数
def function_name(username):
    print(username)


function_name('joy')


# 位置参数
def function_name(x, y):
    print(x + y)


function_name(3, 5)


# 关键字实参
def function_name(x, y):
    print(x)
    print(y)


function_name(y=3, x=1)


# 默认值
def function_name(x, y=4):
    print(x)
    print(y)


function_name(3, 1)
function_name(5)


# 函数返回值
def function_name(x, y):
    return x + y


sumnum = function_name(3, 2)
print(sumnum)


# 让实参编程可选，可提供空的默认值
def func_name(x, y, z=''):
    print(x)
    print(y)
    print(z)


func_name('a', 'b')


# 返回一个字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


print(build_person('lu', 'qianqiu'))
print(type(build_person('lu', 'qianqiu')))


# 传递任意数量的实参
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('a', 'b', 'c')


# 使用关键字实参
def build_person(**username):
    mykey = {}
    for k, v in username.items():
        mykey[k] = v

    return mykey


print(build_person(username='joh', age=18))

# 导入整个模块
import Chapter_1

# 导入模块某个函数
from Chapter_7 import unconfimed_users

# 导入模块全部函数
from Chapter_7 import *

# 使用as给函数指定别名
from Chapter_7 import unconfimed_users as uu

# 使用as给模块指定别名
import Chapter_7 as c7
