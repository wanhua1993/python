## 装饰器 = 高阶函数 + 函数嵌套 + 闭包
# import time

# def timer(func):
#     #  加上参数
#     def wapper(*args, **kwagrs):
#         print(args, kwagrs)
#         start_time = time.time()
#         res = func(*args, **kwagrs)
#         stop_time = time.time()
#         print('函数运行时间为%s' %(stop_time - start_time))
#         return res
#     return wapper
# @timer
# def test(name, age):
#     time.sleep(2)
#     print('我的名字叫%s 年龄是%s' %(name, age))
#     print('test 运行完毕！')
#     return 'nihao'
# val = test('wanhua', age=56)
# print(val)

# l = [0, 2, 3, 4, 5, 5, 6, 6]
# a,*_,b = l
# print(a)
# print(b) 

# 函数闭包为函数加上认证功能
# user = {
#     "name": None,
#     "password": False
# }
# def auth(func):
#     def wapper(*args, **kwargs):
#         if user['name'] and user['password']:
#             res = func(*args, **kwargs)
#             return res
#         username = input('用户名：')
#         password = input('密码：')
#         if username == 'wanhua' and password == '123':
#             user['name'] = username
#             user['password'] = password
#             res = func(*args, **kwargs)
#             return res
#     return wapper    
# @auth    
# def index():
#     print('欢迎到家')
# @auth
# def kaimen():
#     print('已经开门了')
# index()
# kaimen()


##########    查询功能     #########
# def fetch(data):
#     print('你输入的数据时%s' %(data))
#     res = []
#     with open('test.md', 'r') as f:
#         tag = False
#         for i in f:
#             print(i)
#             if i.strip() == data:
#                 tag = True
#                 print(i)
#             if tag: 
#                 if i.startswith('hua'):
#                     break
#             if tag:
#                 res.append(i)
#                 print(i)

#         return res        

# def change(data):
#     print('你要修改的数据是 %s' %(data))
#     return data            

# def delete(data):
#     return data

# def add(data):
#     return data


# def exit():
#     return 'exit'   
# msg = '''
#         1: 查询
#         2: 修改
#         3: 删除
#         4: 增加
#         5: 退出
#     '''        
# data = {
#     '1': fetch,
#     '2': change,
#     '3': delete,
#     '4': add,
#     '5': exit    
# }
# while True:
#     print(msg)
#     choice = input('请选择你的选择：')
#     if not choice: continue
#     if choice == '5':
#         break
#     val = input('请输入你的数据：').strip()
#     res = data[choice](val)
#     print(res)
#     if res:
#         break
#     if res == 'exit':
#         break      

# def destructurArray(a, b):
#     res = list(zip(a, b))
#     return res

# val = destructurArray([1, [2, 4], 3], ['a', ['b'], 'c'])
# print(val)

