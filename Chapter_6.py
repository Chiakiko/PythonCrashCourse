# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 16:09

# 第6章 字典

# 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}

# 访问字典中的值
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 3
alien_0['y_position'] = 4

print(alien_0)

# 创建空字典
alien_0 = {}
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 修改字典中的值
alien_0['color'] = "red"
print(alien_0)

# 删除字典中的键值对
del alien_0['points']
print(alien_0)

# 由类似对象组成的字典
favorite_languages = {'jen': 'python', 'sarch': 'c', 'edward': 'ruby'}
print(favorite_languages)

for k, v in favorite_languages.items():
    print(k)
    print(v)

for k in favorite_languages.keys():
    print(k)

# 按顺序遍历字典中的所有键
favorite_languages = {'jen': 'python', 'sarch': 'c', 'edward': 'ruby'}
for k in sorted(favorite_languages.keys()):
    print(k)

# 遍历字典中的所有值
favorite_languages = {'jen': 'python', 'sarch': 'c', 'edward': 'ruby'}
for v in favorite_languages.values():
    print(v)

# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 3}
alien_2 = {'color': 'yello', 'points': 2}

list_alien = [alien_0, alien_1, alien_2]

print(list_alien)

# 在字典中存储列表
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
print(pizza)
