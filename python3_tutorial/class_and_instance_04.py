# -*- coding: utf-8 -*-
# 继承和多态
# 2018年 2月27日 星期二 17时33分56秒 CST

# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
	count = 0
	def __init__(self, name):
		# count是类属性、name是实例属性
		self.name = name
		# count += 1
		Student.count=Student.count+1

# 类变量是静态的，实例变量是非静态的。
# 静态变量的定义就是只初始化一次，然后存在内存中便于修改访问。

# 类和实例变量的严格访问方式：
# 1、在内部和外部，类变量都用 类名.类变量名 来进行访问，比如Student.count。
# 2、在内部，实例变量用 self.实例变量 来进行访问，比如self.count；
# 	 在外部，实例变量用 实例名.实例变量 来进行访问，比如stu.count。


class Student(object):
    count=0
    def init(self,name):
        self.name=name
        Student.count+=1
# 1.name 属性，每次创建一个实例的时候需要传入参数，每个实例对它产生实例本身的影响，
# 	所以name可以当做是每个实例的属性；
# 2.count属性，每次创建实例时不需要对其传入参数，但创建一个实例就会对count加一，
# 	是所有实例一起对它即count产生影响，所以它是一个类属性。



# 测试:
if Student.count != 0:
	print('测试失败!')
else:
	bart = Student('Bart')
	if Student.count != 1:
		print('测试失败!')
	else:
		lisa = Student('Bart')
		if Student.count != 2:
			print('测试失败!')
		else:
			print('Students:', Student.count)
			print('测试通过!')
