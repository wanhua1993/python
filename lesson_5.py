# print(list(zip(('a', 'b'), (1, 2, 3))))

p = {
    "name": 'wanhua',
    'age': 12
}

# print(list(zip(p.keys(), p.values())))
# print(list(p.keys()))
# print(list(p.values()))

# print(list(zip(['a', 'b'], '123')))

# 不同类型之间不能进行比较
# l = 'hello'
# s = slice(1, 4, 2)
# print(l[s])

# pep = [
#     {
#         'name': 'a', 'age': 1
#     },
#     {
#         "name": 'b', 'age': 2
#     },
#     {
#         "name": 'c', 'age': 3
#     }
# ]
# print(sorted(pep, key=lambda dic: dic['name']))

# name = {
#     'wan': 123,
#     'hua': 234,
#     'aichi': 43
# }
# print(sorted(name)) # 按照 key 来排队
# print(sorted(name, key=lambda key: name[key])) # 按 value 来排序
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(6)
#  while True:
#      try:
#          x = next(g)
#          print('g': x)
#          except StopIteration as e:
#              print('Generator return value:', e.value)
#              break