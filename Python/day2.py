# Tuples
# my_tuple = tuple((1, 2, 3))
# my_tuple = (1, 2, 3,'str')
# my_tuple = list(my_tuple)
# my_tuple.append(4)
# # my_tuple = tuple(my_tuple)
# my_tuple.reverse()
# print(my_tuple)
################################33
# Sets
# 1 unique value
# not ordered
# can't access by index
# changeable
# my_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# my_set = {'hello', 2, True, 'ahmed', 5, 1,(1,2,3)}
# my_set = {'hello', 2, True, 'ahmed', 5, 1,[1,2,3]}
# my_set.add(10)
# print(my_set)
# print(type(my_set))
# from click import prompt

#####################################
# Dictionaries
# my_dict = dict({'name': 'ahmed', 'age': 25, 'phone': '01000000000'})
# my_dict = {'name': 'ahmed', 'age': 25, 'phone': '01000000000'}
# my_dict.update({'city': 'cairo'})
# del my_dict['name']
# my_dict['name'] = 'cairo'
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())
# print(my_dict)
######################################################33
# DRY => Don't Repeat Yourself
# my_list = ['ahmed',5,'cairo', '01000000000']
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# my_dict = {'name': 'ahmed', 'age': 25, 'phone': '01000000000'}
# print(my_dict['name'])
# for key in my_dict:
#     print(f'{my_dict[key]}')
# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict['phone'])
# print(my_dict.items())
# my_list_new = [('name', 'ahmed'), ('age', 25), ('phone', '01000000000')]
# for key, value in my_list_new:
#     print(f'{key} ')
# i = 0
# while i < 10:
#     if i == 5:
        # print(i)
        # continue
    # i += 1
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# while True:
#     name = prompt('What is your name?')
#
#     if name == 'ahmed':
#         break
# age = int(prompt('What is your age?'))
# print(type(age))
# while not age.isnumeric():
# 64 '64'
# 011100 000012  000012110
# mynum = '10e'
# print(type(int(mynum)))
# if 1 == 1:
#     pass

###################################3
# Functions
# def my_func():
#     my_vay = 10*6*568
#     my_vay = my_vay * 2
#     return my_vay,20
# x,y = my_func()
# print(x)

# def do_sum(num1, num2):
#     return num1 + num2
# do_sum(10,20)
# print(do_sum(10,20))
# def validate_email(email):

# while True:
#     email = prompt("Enter your email")
#     if '@' in email and '.' in email:
#         break

# def my_func(num1=20, num2=10):
#     return num1 + num2
# print(my_func())

# def myfunc():
#     pass

# print(10,20,30)
# def do_sum(*args, **kwargs):
#    for arg in args:
#        print(arg)
#
#
# do_sum('ahmed')
# print('*'*5)
# [_,_,_,_]

# def cala(*args):
#     print(eval(args[0]))
#
# cala('10*20+500')
# print(10*512)