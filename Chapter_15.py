# /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "0LIN1ISA"
# Date:2018/3/10 19:51

"""
第15章 生成数据
"""

"""
15.1 安装matplotlib
"""
# pip install matplotlib

"""
15.2 绘制简单的折线图
"""
# 15.2.1 修改标签文字和线条粗细
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
