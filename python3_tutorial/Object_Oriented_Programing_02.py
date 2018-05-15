# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/15 13:35
# Desc:  

class Animal(object):
    def run(self):
        print('Animal is running....')


class Dog(Animal):
    def run(self):
        print('Dog is running....')





d = Dog()

d.run()