####   生成器    ####
# 迭代器协议
# def test():
#     yield 1   # 相当于 return 但是可以多次返回
# g = test()
# print(g)
# print(g.__next__())

# l = [i for i in range(10)]
# print(l)

# l = [i for i in range(10) if i > 5]
# print(l)
### 生成器表达式 ###
# l = (i for i in range(10))
# print(next(l))
# print(next(l))
# print(next(l))

# 生成器函数

# def xiadan():
#     for i in range(10):
#         yield i
# alex = xiadan()
# jidan = alex.__next__()
# jidan_1 = alex.__next__()
# print(jidan) # 第一个
# print(jidan_1) # 第二个


# def test():
#     with open('test.md', 'r', encoding='utf-8') as f:
#         for i in f:
#             yield i

# g = test()
# all_num = sum(eval(i)['num'] for i in g)
# print(all_num)

#  生产者 消费者模型 #

# import time
# def customer(name):
#     print('我是%s' %name)
#     while True:
#         baozi = yield
#         time.sleep(0.5)
#         print('%s 吃掉了第一个%s 包子' %(name, baozi))

# def productor():
#     a = customer('wan')
#     b = customer('hua')
#     a.__next__()
#     b.__next__()
#     for i in range(10):
#         a.send(i)
#         b.send(i)

# productor()

# def func(start, end, a = 0, b = 0):
#     if start == end:
#         return a, b
#     if start%3 == 0 or start%5 == 0:
#         a += 1
#         b += start
#     ret = func(start + 1, end, a, b)
#     return ret
# res = func(1, 15)
# print(res)    

# def func(x, *z, **y):
#     print(x, y, z)
# func(1, 2, 3)   

# def func(*y, **z):
#     print(y, z)

# func([1, 2])

# def func(*y, **z):
#     print(y, z)

# func(*[1, 2, 3], **{'name': 'wanhua'})    

# obj = [1, 2, 3, 5, 4]
# for i in obj:
#     print(i)

# print('nihao')
# for i in obj:
#     print(i)    

# l1 = ['a', 1]
# l2 = ['b', 2]
# l3 = ['c', 3]
# a = zip(l1, l2, l3)
# print(a)
# b = list(a)
# print(b)
# c = '_'.join(b[0])
# print(c)

# def func(n):
#     if n == 0:
#         return 1
#     return n * func(n - 1)

# a = func(7)
# print(a)

###   装饰器   ####
#@ 高阶函数  +  闭包

