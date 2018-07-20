# -*- coding: utf-8 -*-
#!/usr/bin/env python
# print('hello world')
# print('ni hao')
name = 'wanhua'
age = '19'
name_1 = name
name = 'chufeng'

# print('my name is', name, ', age is', age)
# print('my name is', name_1, ', age is', age)

# 变量只能是数字 字母 下划线的任意组合
import getpass

# _username = 'wanhua'
# _password = '123'
# 字符串 变量的拼接
# username = input('username:')
# password = getpass.getpass('password:')
# int str 
# '''
# info = 
#     info of %s
# username: %s
# password: %s
#  % (username, username, password)
# print(username, password)
# print(info)
# print(type(password))
# '''
# info = '''
#     info of {_username}
# username: {_username}
# password: {_password}
#  '''.format(_username=username,
#     _password=password
#  )
# print(info)

# info_1 = '''
#     info of {0}
#     username: {1},
#     password: {1}
# '''.format(username, password)
# print(info_1)

# 流程控制 逻辑判断
# if _username == username and _password == password:
#     print('welcome user {name} web!'.format(name=username))
# else:
#     print('login failed')  

age_of_boy = '45'


# if guess_age == age_of_boy:
#     print('yes')
# elif guess_age > age_of_boy:
#     print('big')
# else: 
#     print('small')    

count = 0
# while count < 3:
#     if count == 3:
#         break
#     guess_age = input('guess_age: ')
#     if guess_age == age_of_boy:
#         print('yes')
#         break
#     elif guess_age > age_of_boy:
#         count = count + 1
#         print('big')
#     else: 
#         count = count + 1
#         print('small') 

# else:
#     print('please fuck off')

###### for 循环

# for i in range(0, 10, 3):
#     print(i)
    
# while count < 3:
#     get_li = input('get:')
#     if get_li == '4':
#         print('yes')
#         break   
#     elif get_li > '4':
#         print('big')
#     else:
#         print('small')
#     count += 1    
#     if count == 3:
#         aa = input('agian?')
#         if aa == 'y':
#             count = 0

# continue 跳出本次循环 继续进入到下一次循环