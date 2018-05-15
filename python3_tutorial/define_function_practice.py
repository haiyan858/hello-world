# define_function_practice.py
# 2018年 03月 21日 星期三 10:39:01 CST

# 位置参数
# 位置参数
# 位置参数

# 计算x2的函数：
def power(x):
	return x*x
# 对于power(x)函数，参数x就是一个位置参数。
power(5)

# 如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
# 可以计算任意n次方：
# 修改后的power(x, n)函数有两个参数：x和n，
# 这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
def power(x,n):
	s = 1
	while n>0:
		s = s*x
		n = n-1
	return s

power(2,4)

# 默认参数
# 默认参数
# 默认参数

# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

def power(x,n=2):
	s = 1
	while n>0:
		s = s*x
		n = n-1
	return s

power(2,4)
power(2)

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
# >>> add_end()
# ['END']
# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']

def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

# >>> add_end()
# ['END']
# >>> add_end()
# ['END']
# >>> add_end()
# ['END']


# 可变参数
# 可变参数
# 可变参数

# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 输入参数个数不确定
def calc(*numbers):
	s=0
	for n in numbers:
		s = s + n*n
	return s

calc(1,2,3,4,5,6)

nums=[1,2,3,4,5,6]
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
calc(*nums)
assert calc(1,2,3,4,5,6)

# 关键字参数
# 关键字参数
# 关键字参数

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict,
# 然后把该dict转换为关键字参数传进去：
def person(name,age,**kw):
	print('name:',name,'age:',age,'other_info:',kw)

person('Jack',27,city='Beijing',job='Engineer')
# name: Jack age: 27 other_info: {'city': 'Beijing', 'job': 'Engineer'}
person('tom',25)
# name: tom age: 25 other_info: {}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 27, **extra)
# name: Jack age: 27 other_info: {'city': 'Beijing', 'job': 'Engineer'}

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。

# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
# 利用关键字参数来定义这个函数就能满足注册的需求。


# 命名关键字参数
# 命名关键字参数
# 命名关键字参数

# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 如果要限制关键字参数的名字，就可以用命名关键字参数，

# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 使用命名关键字参数时，要特别注意，
# 如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，
# Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack',27,city='Beijing',job='Engineer')

person('Jack',27)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack',27,city='Beijing',job='Engineer')
# Jack 27 () Beijing Engineer

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
person('Jack',27, 'Beijing', 'Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

person('Jack',27,1,2,3,4,city='Beijing',job='Engineer')
# Jack 27 (1, 2, 3, 4) Beijing Engineer


# 参数组合：
# 参数组合：
# 参数组合：
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意：
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1,2,4,5,6,7)

# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
	return x * y


	def product(*nums):
		s = 1
		if len(nums) == 1:
			return nums[0]
		elif len(nums) == 0:
			return None
		else:
			for v in nums:
				s = s*v
			return s


	# 测试
	print('product(5) =', product(5))
	print('product(5, 6) =', product(5, 6))
	print('product(5, 6, 7) =', product(5, 6, 7))
	print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
	if product(5) != 5:
	    print('测试失败!')
	elif product(5, 6) != 30:
	    print('测试失败!')
	elif product(5, 6, 7) != 210:
	    print('测试失败!')
	elif product(5, 6, 7, 9) != 1890:
	    print('测试失败!')
	else:
	    try:
	        product()
	        # 修改
	        print('测试成功!')
	    except TypeError:
	        print('测试失败!')



