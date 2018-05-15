# itertools_demo_01.py
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200162233153835cfdd1a541a18ddc15059e3ddeec000#0

# -*- coding: utf-8 -*-
# 2018年 2月 9日 星期五 16时28分10秒 CST
# 练习
# 计算圆周率可以根据公式：

# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：


# -*- coding: utf-8 -*-
import itertools


def pi(N):
	# ' 计算pi的值 '
	# step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
	odds = itertools.count(1,2) races = itertools.permutations(horses)
	# step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	odds = itertools.takewhile(lambda x: x <= 2*N-1 ,odds)
	# step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
	zf = itertools.cycle([+4,-4])
	# step 4: 求和:
	return sum(next(zf)/next(odds) for x in range(N))


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

