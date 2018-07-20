# import sys
# print(sys.path) 打印环境变量
# print(sys.argv) 打印相对路径
# val = sys.argv[0]


import os
# os.system('dir') 打印当前目录的文件
# cmd_res = os.system('dir') 直接执行命令 不保存结果
# print(cmd_res) -----> 0

# cmd_res = os.popen('dir').read() 
# print(cmd_res)

# os.mkdir('new') 创建文件夹

# 三元运算
# a, b , c = 1, 2, 3
# d = a if a < b else c
# print(d)

# msg = '我爱北京天安门'
# print(msg.encode('utf-8')) 没有指定编码 使用系统默认的编码格式

# msg = b'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'
# print(msg.decode('utf-8'))

name = [1, 3, 2, [7, 8], 4,]
name_1 = [5, 6, 7, 8]
# print(name[1:3]) # 切片
# print(name[len(name) - 1]) # 取出最后一个
# print(name[-1])
# print(name[-2:-1])
# print(name[-2:])

# name.append(5) 后面添加
# name.insert(1,6) 向某个位置插入
# name[2] = 6 直接修改某位置的值
# name.remove(4)  删除某值
# del name[1]  根据索引删除
# name.pop()  删除最后一个值
# print(name.count(4)) 统计个数
# name.clear() 清空数组
# name.reverse() 反转
# name.sort()  排序
# name.extend(name_1)  扩展合并
# print(name.index(2)) 返回某个值的索引
import copy
# name_2 = name.copy() 浅copy
# name_2 = copy.cpoy(name) 浅copy
# name_2 = copy.deepcopy(name) 深copy
# print(name)
# print(name_2)

# name[2] = '123'
# name[3][0] = 9
# print(name)
# print(name_2)
# for i in name:
#     print(i)

# print(name[0:-1:2])

# arr = ('a', 'b') 元组
# data = []
# money = int(input('money:'))
# print(money)
# goods = [['a', 100], ['b', 200], ['c', 300], ['d', 400]]
# print(goods)
# num = int(input('index:'))
# mon = goods[num][1]
# if mon > money:
#     print('your money not enough!')
# else:
#     data.append(goods[num])
#     money = money - mon
#     print(data)
#     print('your money is', money)        

#####    字符串

name = 'wan hua'
# print(name.capitalize())
# print(name.count('a'))  存在的个数
# print(name.center(50, '-')) 
# print(name.endswith('hu')) 是否以什么结尾
# print(name.expandtabs(tabsize=30)) 
# print(name.find('n')) 返回查找的索引
# print(name[4:9]) 截取
# print(name.format(name='aichi'))
# print(name.format_map(
#     {
#         'name': 'aichi'
#     }
# ))
# print(name.isalnum()) 判断是否是阿拉伯数字
# print(name.isalpha()) 判断是否是英文
# print(name.isdecimal) 判断是否是十进制数
# print(name.isdigit()) 判断是否是整数
# print(name.isidentifier()) 判断是否是合法的标识符
# print(name.islower()) 判断是小写
# print(name.isnumeric()) 判断是否只有数字
# print(name.isspace()) 判断是否是空格
# print(name.istitle())
# print(name.isprintable()) tty file, drive file
# print(name.isupper()) 判断是否是大写
# print('-'.join(['1', '2', '3'])) 1-2-3
# print(name.ljust(50, '*')) wan hua********************
# print(name.rjust(20, '*'))
# print(name.lower()) 把大写变成小写
# print(name.upper())
# print(name.lstrip()) 左边去空格
# print(name.rstrip())
# print(name.strip())

# a = str.maketrans('wnh', '123')
# print(name.translate(a))

# print(name.replace('a', '11', 1))
# print(name.rfind('a')) 找到最后面值的下标
# print(name.split())  按什么分解成数组
# print(name.splitlines())
# print(name.swapcase()) WAN HUA
# print(name.title())  Wan Hua
# print(name.zfill(20)) 0000000000000wan hua

###############    字典     ###############
# 字典是无序的 因为他没有下标
data = {
    "a": 123,
    "b": 456,
    "c": 789
}
# for key in data:
#     print(key)
#     print(data[key])
# data.pop('a') 删除
# data.popitem()
# del data['a']
# print(data.get('a')) 查询
# data.setdefault('a', '234')
# print(data.keys())
# value = {
#     'a': 234,
#     'f': 345,
#     'g': 456
# }
# data.update(value) 有则改之 无则加勉
# print(data.items()) dict_items([('c', 789), ('b', 456), ('a', 123)])
# val = data.fromkeys(['z', 'x', 'y'], ['test', {'1':1}, 'ddd']) 
# print(val) 

# for k, v in data.items():
#     print(k, v)

print(data)