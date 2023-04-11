# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:39:31 2023

@author: 86319
"""

# 导入 math 模块
import math

# 定义梯形法函数
# 参数f：被积函数，n：梯形个数，min：积分下界，max：积分上界
def trapezoid(f, n, min, max):
    # 计算每个梯形的宽度
    h = (max - min) / n
    # 打印梯形个数n和梯形宽度h
    print('N', n)
    print('h', h)
    # 初始化积分值为0
    S = 0
    # 遍历每个梯形，注意这里从1开始循环
    for i in range(1, n):
        # 计算当前梯形的高度并累加到积分值中
        S += f(min + i * h) * h
    # 加上首尾两个端点处的函数值乘以梯形宽度的一半，并返回积分值
    return S + 0.5 * h * (f(min) + f(max))

# 定义函数 f(x)
f = lambda x: math.cos(1/(1+x**2))

# 调用 trapezoid() 函数，计算 f(x)在 [0, pi] 区间内的积分值
result = trapezoid(f, 1000, 0, math.pi)

# 输出积分值
print(result)
