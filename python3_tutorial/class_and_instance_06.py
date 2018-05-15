# 2018年 02月 28日 星期三 18:19:43 CST
# 使用@property

class Student(object):
	def get_score(self):
		return self.__score
	def set_score(self,s):
		if not isinstance(s,int):
			raise ValueError('score must be an integer!')
		if s<0 or s>100:
			raise ValueError('score must be between 0~100 !')
		self.__score = s
