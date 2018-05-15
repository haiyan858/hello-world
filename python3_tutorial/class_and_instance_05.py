# 2018年 2月28日 星期三 17时39分00秒 CST
# slots

#A 加限制实例属性，类方法用MethodType绑定
class Student1(object):
	slots = ('name', 'age')#指定实例可用的属性

s1 = Student1()#实例化
s2 = Student1()
s1.name = 'zhangsan'#动态绑定属性
s2.age = 'lisi'#动态绑定属性

def set_info(self, m, n):
	self.height = m
	self.weight = n

from types import MethodType
Student1.set_info = MethodType(set_info, Student1)#给类绑定方法并赋值给class.set_info

s1.set_info('175cm', '65kg')#调用方法
s2.set_info('180cm', '80kg')
print (s1.name, s2.age)
print (s1.height, s2.weight)

#B 不加实例属性限制slots，类方法不用MethodType绑定
class Student2(object):
	pass

s3 = Student2()
s4 = Student2()
s3.name = 'zhangsan'
s4.age = 'lisi'

#动态绑定方法
def new_info(self, x, y):
	self.height = x
	self.weight = y
	return ('%s, %s') % (x, y)


Student2.new_info = new_info

s3.new_info('175cm', '65kg')
s4.new_info('180cm', '80kg')
print (s3.name, s4.age)
print (s3.height, s4.weight)

#C 加实例属性限制，类方法不用MethodType绑定
class Student3(object):
	slots = ('name', 'age')

s5 = Student3()
s6 = Student3()
s5.name = 'zhangsan'
s6.age = 'lisi'

def creat_info(self, z, t):
	self.height = z
	self.weight = t
	return '%s, %s' % (z, t)

Student3.creat_info = creat_info

s5.creat_info('175cm', '65kg')
s6.creat_info('180cm', '80kg')
print (s5.name, s6.age)
print (s5.weight, s6.height)
# 报错

# 总结 加slots 实例属性限制后，给类绑定方法要用MethodType

# 在给类(Class)进行绑定时才能直接用Student.set_age=set_age的方式，
# 而给实例进行绑定则要使用 s.set_age = MethodType(set_age, s)的方式。
