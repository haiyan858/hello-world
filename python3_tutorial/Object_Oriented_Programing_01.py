# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/11 11:46
# Desc:  对象三大特点：数据的封装，继承和多态


# 面向对象编程，Object Oriented Programing
# 简称OOP,是一种程序设计思想。对象作为程序最基本的单元
# 一个对象包含了：数据和操作数据的函数

# std1 = {'name':'Mike','score':98}
# std2 = {'name':'Bob','score':81}
#
# def print_score(std):
#     print('score of {} is {}'.format(std['name'],std['score']))
#
# print_score(std1)

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('score of {} is {}'.format(self.name,self.score))

# bart = Student('Mike',99)
# bart.print_score()

# class Student(object):
#     pass
#
# bart = Student()
# bart.name = 'Mike'
# print(bart.name)
#
# print(Student)

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self,name):
#         self.__name = name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if 0< score <=100:
#             self.__score = score
#         else:
#             raise ValueError('bad Score , plz check')
#
#
# bart = Student('mike',123)
# bart.print_score()
#
# # bart.set_score(123)
# # print(bart.get_score())
#
# bart.__name = 'bad'
#
# print(bart.get_name())


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender in ['male','female','x']:
            self.__gender = gender
        else:
            raise ValueError('Bad Gender')

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')



