# a.py
# 2018年 3月20日 星期二 14时53分49秒 CST

import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0

# 的两个解。

# 提示：计算平方根可以调用math.sqrt()函数：


def quadratic(a, b, c):
	delta = b*b - 4*a*c
	if delta > 0:
		x1 = (-b + math.sqrt(delta))/(2*a)
		x2 = (-b - math.sqrt(delta))/(2*a)
		return x1,x2
	else:
		return '无解'
	
# 位置参数
def power(x,n):
	s = 1
	while n >0:
		s = s*x
		n = n-1
	return s


# 默认参数
def power(x,n=2):
	s = 1
	while n >0:
		s = s*x
		n = n-1
	return s
	
# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

# 二是如何设置默认参数。

# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
calc(*nums)

calc(1, 2)

# 关键字参数
# 关键字参数


# 命名关键字参数
# 命名关键字参数


