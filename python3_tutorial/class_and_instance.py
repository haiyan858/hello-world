# class_and_instance.py
# 2018年 2月27日 星期二 17时02分29秒 CST
# 面向对象编程——Object Oriented Programming，简称OOP
# 数据封装、继承和多态是面向对象的三大特点。

class Student(object):
	# 实例变量self
	def __init__(self, name, score):
		self.name = name
		self.score = score
	# 数据封装
	def print_score(self):
		print('%s : %s'%(self.name,self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
	def get_rank(self):
		if self.name.lower().startswith('a'):
			return 'A'
		elif self.name.lower().startswith('b'):
			return 'B'
		else:
			return 'C'


# bart = Student('Bart Simpson',59)
# bart.print_score()

# # 数据封装
# def print_score(std):
# 	print('%s : %s'%(std.name,std.score))

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

# python是动态语言，实例创建出来之后仍然可以被绑定其他属性，即使类中没有规定。
# Java/C#是静态语言，实例创建出来后属性就固定了，有什么属性是类规定好了的，不允许改变。
bart.age = 27
bart.age

lisa.age
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'age'

bart = Student('Bart', 59)
bart.get_rank()
