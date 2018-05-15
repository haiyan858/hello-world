def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1,num * product)

# 请编写move(n, a, b, c)函数，
# 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

n = int(input("请输入层数"))


def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        #将n-1个盘子拿到b
        move(n-1,a,c,b)
        #将最后一个盘子n从a移到c
        print(a,"-->",c)
        #将n-1个盘子移到c
        move(n-1,b,a,c)


print('共需要步数:',2**n-1)
move(n,'a','b','c')


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')


def trim(s):
    while s[0:1]==' ':
        s = s[1:]
    while s[-1:0]==' ':
        s = s[0:-1]
    return s


请使用迭代查找一个list中最小和最大值，并返回一个tuple：

# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if L == []:
		return (None, None)
	max=min=L[0]
	for i in L:
		if i > max:
			max=i
		if i < min:
			min=i
	return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：




def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)




g = fib(6)
while True:
	try:
	    x = next(g)
	    print('g:', x)
	except StopIteration as e:
	    print('Generator return value:', e.value)
	    break







# -*- coding: utf-8 -*-

def triangles():
	l=[]
	n=1
	while n==1:
		l[0]=[1]
		# print[l]
		n=n+1
	while n==2:
		l[1]=[1,1]
		print[l]
		n=n+1
	while n==11:
		for i in l:
			print(i)
	while n>2:
		l[n-1][0]=1
		l[n-1][-1]=1
		for x in range(1,n-1):
			l[n-1][x]=l[n-2][x]+l[n-2][x-1]




def triangles():
	floor=1
	if floor == 1:
		l[0]=[1]
		floor = floor +1
	elif floor == 2:
		l[1]=[1,1]
		floor = floor +1
	elif floor >2:
		l.append([])

	for x in range(1,6):
		l.append([1,1])
	yield l


def triangles():
	n=0
	t=[]
	while n == 0:
		l[0]=[1]
		n=n+1
	while n == 1:
		l[1]=[1,1]
		n=n+1
	while n > 1:
		l[n]=l[n-1]
		for x in range(1,n-1):
			l[n].insert[x,l[n-1][x]+l[n-1][x-1]]
	yield t

  
n = 0
results = []
for t in triangles():
	print(t)
	results.append(t)
	n = n + 1
	if n == 10:
		break
if results == [
	[1],
	[1, 1],
	[1, 2, 1],
	[1, 3, 3, 1],
	[1, 4, 6, 4, 1],
	[1, 5, 10, 10, 5, 1],
	[1, 6, 15, 20, 15, 6, 1],
	[1, 7, 21, 35, 35, 21, 7, 1],
	[1, 8, 28, 56, 70, 56, 28, 8, 1],
	[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
	print('测试通过!')
else:
	print('测试失败!')




# 练习1

def normalize(name):
	return name[0].upper()+name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习2
from functools import reduce
def ji(x, y):
    return x * y

def prod(L):
	return reduce(ji,L)

def prod(L):
	return reduce(lambda x,y: x*y,L)

# 测试:
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# -*- coding: utf-8 -*-
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':10}
def char2num(s):
	return DIGITS[s]

def to_int(x,y):
	return x*10+y

def str2float(s):
	if '.' in s:
		return reduce(to_int,map(char2num,s.split('.')[0])) + to_int(reduce(to_int,map(char2num,s.split('.')[1])))


	reduce(to_int,map(char2num,s))
		



def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    l = s.split('.')
    def char2num(s):
        return DIGITS[s]

    def to_int(x,y):
        return x * 10 + y

    def to_float(f):
        n = 1
        i = 0
        while i < len(l[1]):
            n = n * 10
            i = i + 1
        return f / n

    if '.' not in s:
        result = reduce(to_int,map(char2num,l[0]),0.0)
    else:
        result = reduce(to_int,map(char2num,l[0]))+to_float(reduce(to_int,map(char2num,l[1])))
    return result





#encoding:UTF-8
def yield_test(n):
    for i in range(n):
    	print("i=",i)
        yield call(i)
        print("i=",i)
    #做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    return i*2

# 第一种方式调用函数
#使用for循环
# for x in yield_test(5):
#     print("x=",x,",")

# 第二种方式调用函数
list(yield_test(5))

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


import os

s='hotel'
for x in os.listdir():
	if os.path.isdir(x):
		for x2 in os.listdir(x):
			if s in x2:
				print(x2)
	else:
		if s in x:
			print(x)
			

s='hotel'
for x in os.listdir():
	if s in x:
		print(x)

def iter_dir(path,s):
	if os.path.isdir(path):
		for x in os.path.listdir(path):
			if s in x:
				return x




	for x in os.listdir():
		if iter_dir(x):

		else:
			if s in x :
				yield x


