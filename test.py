# import numpy as np
# # import pyperclip
# import time
# import math

# 生成一个包含 随机数字的数组
# array = np.random.randint(-1000000, 10000000, size=1000000)

# 打印数组
# print(array)
# 打印数组，使用,分割
# print(','.join(map(str, array)))

# 将数组内容复制到剪贴板
# pyperclip.copy(','.join(map(str, array)))

# # 冒泡排序函数
# def bubble_sort(arr):
#   n = len(arr)
#   for i in range(n):
#     for j in range(0, n-i-1):
#       if arr[j] > arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]

# # 记录排序开始时间
# start_time = time.time()

# # 对数组进行排序
# bubble_sort(array)

# # 记录排序结束时间
# end_time = time.time()

# # 打印排序所需时间
# print(f"排序所需时间: {end_time - start_time}秒")

# 快速排序函数
# def quick_sort(arr):
#   if len(arr) <= 1:
#     return arr
#   pivot = arr[len(arr) // 2]
#   left, middle, right = [], [], []
#   for x in arr:
#     if x < pivot:
#       left.append(x)
#     elif x == pivot:
#       middle.append(x)
#     else:
#       right.append(x)
#   return quick_sort(left) + middle + quick_sort(right)

# # 记录排序开始时间
# start_time = time.time()

# # 对数组进行排序
# sorted_array = quick_sort(array)

# # 记录排序结束时间
# end_time = time.time()

# # 打印排序所需时间
# print(f"排序所需时间: {end_time - start_time}秒")
# def calculate_pi(n_terms):
#   pi_estimate = 0
#   for k in range(n_terms):
#     pi_estimate += (1 / (16 ** k)) * (
#       (4 / (8 * k + 1)) -
#       (2 / (8 * k + 4)) -
#       (1 / (8 * k + 5)) -
#       (1 / (8 * k + 6))
#     )
#   return pi_estimate
# # 获取用户输入
# n_terms = int(input("请输入计算π的项数（越大精度越高）: "))

# # 记录计算开始时间
# start_time = time.time()

# pi_value = calculate_pi(n_terms)

# # 记录计算结束时间
# end_time = time.time()

# # 打印结果，保留用户指定的小数位数
# decimal_places = int(input("请输入希望保留的小数位数: "))
# print(f"计算得到的π值: {pi_value:.{decimal_places}f}")

# # 打印计算所需时间
# print(f"计算所需时间: {end_time - start_time}秒")

# from random import random
# from time import perf_counter

# def calPI(N = 100):
#     hits = 0
#     start = perf_counter()
#     for i in range(1, N*N+1):
#         x, y = random(), random()
#         dist = pow(x ** 2 + y ** 2, 0.5)
#         if dist <= 1.0:
#             hits += 1
#     pi = (hits * 4) / (N * N)
#     use_time = perf_counter() - start
#     return pi, use_time

# PI, use_time = calPI(10000)
# print('use Monte Carlo method to calculate PI: {}'.format(PI))
# print('use time: {} s'.format(use_time))
# def calPI():
#   n = 10000 + 4
#   p = 2 * 10 ** n
#   a = p // 3
#   p += a
#   i = 2

#   while a > 0:
#     a = a * i // (i * 2 + 1)
#     p += a
#     i += 1

#   p //= 10000
#   return p
# # 记录计算开始时间
# start_time = time.time()

# p = calPI()

# # 记录计算结束时间
# end_time = time.time()

# print("PI =", p)
# print(f"计算所需时间: {end_time - start_time}秒")
