# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/8 16:09


# 第7章 用户输入和while循环

# input()函数用法
message = input("Tell me your age:")
print(message)

# 使用while循环
nums = 5
while nums > 0:
    print(nums)
    nums -= 1

# 在列表中移动元素
unconfimed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfimed_users:
    confirmed_users.append(unconfimed_users.pop())
print(confirmed_users)

# 删除特定值的元素
unconfimed_users = ['alice', 'brian', 'candace']
unconfimed_users.remove('alice')
print(unconfimed_users)
