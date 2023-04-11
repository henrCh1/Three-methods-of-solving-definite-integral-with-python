# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:04:20 2023

@author: 86319
"""

# 导入math模块
import math

# 定义一个函数，用于求给定函数在指定区间内各点的值的总和
def summation(f, range):
   r = 0
   for i in range:
      r += f(i)
   return r

# 定义辛普森积分函数，f为函数，h为区间宽度，2n为区间个数，min为积分下限，max为积分上限
def simpson(f, h, min, max):
   # 计算n值
   n = math.floor((max - min) / (h * 2))
   print('N', 2*n)
   print('h', h)
    
   # 定义 lambda 函数 g(i)，用于计算每个区间边界的函数值
   g = lambda i: f(min + i * h)

   # 计算 a、b、c、d 值
   a = g(0)
   b = summation(lambda i: g(2 * i - 1), range(1, n+1))
   c = summation(lambda i: g(2 * i), range(1, n))
   d = g(2 * n)

   # 返回辛普森积分结果
   return (h / 3) * (a + (4 * b) + (2 * c) + d)

# 定义函数 f(x)
f = lambda x: (math.sqrt(400*((math.sin(x))**2)+100*((math.cos(x))**2)))

# 调用 simpson() 函数，计算 f(x)在 [0, 2pi] 区间内的积分值的平方根
result = simpson(f, 0.0001, 0, 2*math.pi)

# 输出积分值
print(result)
