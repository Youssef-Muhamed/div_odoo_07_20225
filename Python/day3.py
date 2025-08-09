# my_str = 'ahmed'
# my_str = ' omar'
# def my_func():
#     my_str = 'mohamed'
#     print(my_str)
#
# my_func()
# print(my_str)
##################################

# my_str = 'ahmed'
# def my_func():
#     global my_str
#     my_str = 'mohamed'
#     print(my_str)
# print(my_str)
# my_func()

##################################33
# my_str = 'ahmed'
# def my_outer():
#     global my_str
#     my_str = 'mohamed'
#     def my_inner():
#         # my_str = 'omar'
#         print(my_str)
#     my_inner()
#     print(my_str)
#
# my_outer()
# print(my_str)
#######################################
# my_str = 'ahmed'
# def my_outer():
#     my_str = 'mohamed'
#     def my_inner():
#         nonlocal my_str
#         my_str = 'omar'
#         print(my_str)
#     my_inner()
#     print(my_str)
#
# my_outer()
# print(my_str)
################################

# my_str = 'ahmed'
# def my_outer():
#     global my_str
#     my_str = 'mohamed'
#     def my_inner():
#         nonlocal my_str
#         my_str = 'omar'
#         print(my_str)
#     my_inner()
#     print(my_str)
#
# my_outer()
# print(my_str)
######################################
# my_str = 'ahmed'
# def my_outer():
#     my_str = 'mohamed'
#     def my_inner():
#         global my_str
#         my_str = 'omar'
#         print(my_str)
#     my_inner()
#     print(my_str)
#
# my_outer()
# print(my_str)
######################################

# Modules
# import module_one
# from module_one import *
#
#
# my_func()
# my_func2()
#################################
# from helpers import module_one
#
# module_one.my_func()
# module_one.my_func2()

# import datetime
# print(datetime.datetime.now())
#
# from datetime import datetime
# print(datetime.now())

###################################
# Error Handling
# print('hello first')
# print(10/0)
# print('hello second')

# try:
#     print('hello first')
#     print(10/0)
#     print('hello second')
# except:
#     print('Error')
# else:
#     print('No Error')
# finally:
# #     print('Done')
# my_num = 2
# # if my_num == 2:
# #     print(10 / my_num)
# #     raise ValueError('can not divide by 2')
#     # print('hello second')
# try:
#     print(10/0)
#     # if my_num == 2:
#     #     raise ValueError('can not divide by 2')
#     print('hello second')
# except Exception as e:
#     print('Error',e)

##############################################3
# File Handling
# f = open('file.txt', 'r')
# print(f.readlines())
# f.close()

# f = open('file.txt', 'w')
# f.write('Test')
# f.write('Test2')
# f.close()

# f = open('file.txt', 'r')
# # f.seek(4)
# print(f.read(4))
#
# f.close()

# f = open('file.txt', 'w')
# f.seek(4)
# f.write('Test')
# f.close()
# f = open('file.txt', 'a')
# f.seek(4)
# f.write('Test')
# f.close()
f = open('file.txt', 'r')

# f.write('hello')
# print(f.read())
user = f.read().split('\n')
for u in user:
    print(u.split(':')[0])
f.close()

#################################
