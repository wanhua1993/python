### 匿名函数
# lambda 
# lambda x: x + 1
# func = lambda x: x + 1
# print(func(10))
#  对每一个数据 进行处理 得到的结果是一个 列表  该列表 元素的个数与原来文职一样
# array = [1, 2, 3, 4]
# def test(x):
#     x = x -1
#     print(x)

# list(map(test, array)
# 对返回 true 的数据进行返回处理
# 遍历每一个元素 判断每一个元素 得到一个布尔值 如果是true 则留下
# filter 
# movie = ['a', 'b', 'c', 'd']
# res = list(filter(lambda n:n.endswith('a'), movie))
# print(res)

# reduce

num = [1, 2, 3, 4, 5, 6]
# total = 0
# for i in num:
#     total += i

# print(total)

# 对每一个数据进行压缩处理 返回一个值
# def reduce_test(func, ary):
#     res = ary.pop(0)
#     for i in ary:
#         res = func(res, i)
#     return res
# data = reduce_test(lambda x, y: x * y, num)
# print(data)
# from functools import reduce
# print(reduce(lambda x, y: x * y, num))

 # age = 22
# def test():
#     global age
#     age = 24
#     print(age)
# test()
# print(age)




