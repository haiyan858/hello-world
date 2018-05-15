# 2018年 2月27日 星期二 17时02分29秒 CST
# 访问限制

class Student(object):
	# 实例变量self
	# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_name(self,name):
		self.__name = name
	# def set_score(self,score):
	# 	self.__score = score
	# 因为在方法中，可以对参数做检查，避免传入无效的参数：
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
