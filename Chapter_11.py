# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 14:26

"""
第11章 测试代码
"""

"""
11.1 测试函数
"""


def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name


# 11.1.1 单元测试和测试用例
# unittest：提供了代码测试

# 11.1.2 可通过的测试

# 11.1.3 不能通过测试

# 11.1.4 测试未通过时怎么办

# 11.1.5 测试新测试

# 11.1.6 添加新测试

"""
11.2 测试类
"""
# 11.2.1 各种断言方法
# assertEqual(a, b) ：核实 a == b
# assertNotEqual(a, b)：核实 a != b
# assertTure(x)：核实 x 为 True
# assertFalse(x)：核实 x 为 False
# assertIn(item, list)：核实 item在list中
# assertNotIn(item,list)：核实 item不在list中

# 11.2.2 一个要测试的类
# #survey.py

# 11.2.3 测试AnonymousSurvey类

# 11.2.4 方法setUp()
