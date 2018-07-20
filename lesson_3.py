######    集合     #####

list_1 = [1, 3, 4, 2, 5, 6, 5]
list_1 = set(list_1) 
# print(list_1, type(list_1)) {1, 2, 3, 4, 5, 6} <class 'set'>

list_2 = [3, 5, 7, 8 , 9]
list_2 = set(list_2)
# 交集
# print(list_1.intersection(list_2))

# 并集
# print(list_1.union(list_2))

# 差集 in list_1 not in list_2
# print(list_1.difference(list_2))

# 子集
# print(list_1.issubset(list_2)) 

# print(list_1.issuperset(list_2))

# 对称差集  把他们相同的去掉 然后合并
# print(list_1.symmetric_difference(list_2)) 

# print(list_1.isdisjoint(list_2)) 是否有交集

# print(list_1 & list_2)
# print(list_1 | list_2)
# print(list_1 - list_2)
# print(list_1 ^ list_2)
# list_1.add(9) 添加
# list_1.update() 修改

# list_1.discard()

##########  文件操作   ##########

# data = open('linux.md', encoding='utf-8').read()
# print(data)

# f = open('linux_1.md', 'r', encoding='utf-8')
# data = f.read()
# data_1 = f.read()
# print(data)
# print('data_1:', data_1)

#  r 读   w 写   a 追加
# f = open('linux_1.md', 'w', encoding='utf-8')
# f.write('你好A！\n')
# f.write('A by B!')
# f.close()

# f = open('linux.md', 'r', encoding='utf-8')
# data = f.readline() # 读取一行
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print('---------------------')
#         continue
#     print(line.strip())
# count = 0
# for line in f:
#     if count == 9:
#         print('++++++++++')
#         conut += 1
#     print(line.strip())
#     count += 1
# f.readline()       
# print(f.tell())  当前位置
# f.seek(0)       回到某一个位置
# print(f.encoding)
# print(f.fileno())
# print(f.seekable())  判断是否可以移动
# print(f.readable())  判断文件是否可读
# print(f.flush()) 

# import sys, time
# for i in range(50):
#     sys.stdout.write('#')
#     sys.stdout.flush()
#     time.sleep(0.1)
# print('\n 加载完成！')

# f.truncate(10)
# f = open('linux.md', 'r+', encoding='utf-8')
# print(f.readlines)
# print(f.readlines)
# print(f.readlines)

# f = open('linux_1.md', 'wb') #二进制文件 
# f.write('hello\n'.encode())
# f.close()

# f = open('linux_1.md', 'r', encoding='utf-8')
# f_new = open('linux_2.md', 'w', encoding='utf-8')
# for line in f:
#     if 'hello' in line:
#         line = line.replace('hello', 'wanhua')    
#     f_new.write(line)
# f.close()
# f_new.close()    
        
# with open('linux.md', 'r', encoding='utf-8') as f_new


########   字符串编码与转码    #########

# s = '你好'
# s_gbk = s.encode('gbk')
# print(s_gbk)
# s_gbk.decode('gbk').encode('utf-8')


########   函数    ########

# def test(x):
#     if x > 10:
#         return 10
#     return x + test(x + 1)
# a = test(1)
# print(a)    

# 默认参数 调用函数的时候 默认参数非必须传递
# 用途 默认安装值
# def test(x,y=2):
#     print(x)
#     print(y)

# test(1)

# def test(*wan):
#     print(wan)

# test(*[1, 2, 3, 4])

##  把N个关键词参数 转换成字典的方式
# def test(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])

# test(name='wanhua', age='23')
# test(**{'name':'wanhua'})

# def test(name, **kwargs):
#     print(name)
#     print(kwargs)

# test('wanhua', age=12)

def test(name, age=19, **kwargs):
    print(name)
    print(age)
    print(kwargs)

test('wanhua', 10, sex='m', hobby='tesla')