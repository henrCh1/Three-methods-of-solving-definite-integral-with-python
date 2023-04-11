# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:12:41 2023

@author: 86319
"""

# 导入math模块
import math

# 定义矩形法函数
# 参数f：被积函数，n：矩形个数，min：积分下界，max：积分上界
def rectangle(f, n, min, max):
    # 计算矩形宽度
    h = (max - min) / n
    # 打印矩形个数n和矩形宽度h
    print('N', n)
    print('h', h)
    # 初始化积分值为0
    S=0
    # 遍历每个矩形
    for i in range(0, n):
        # 计算当前矩形的高度并累加到积分值中
        S += f(min + i * h) * h
    # 返回积分值
    return S

# 定义函数 f(x)
f = lambda x: math.cos(1/(1+x**2))

# 调用 rectangle() 函数，计算 f(x)在 [0, pi] 区间内的积分值
result = rectangle(f, 1000, 0, math.pi)

# 输出积分值
print(result)
