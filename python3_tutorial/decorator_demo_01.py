# decrator_demo_01.py
# -*- coding: utf-8 -*-
# 2018年 2月 9日 星期五 16时28分10秒 CST


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools

def metric(fn):
	time.time()
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)		
	print('%s executed in %s ms' % (fn.__name__, 10.24))
	return fn

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper



# 测试
@metric
def fast(x, y):
	time.sleep(0.0012)
	return x + y;

@metric
def slow(x, y, z):
	time.sleep(0.1234)
	return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
	print('测试失败!')
elif s != 7986:
	print('测试失败!')

