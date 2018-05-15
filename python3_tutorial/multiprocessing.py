#!/usr/bin/env python
# _*_coding:utf-8_*_

# multiprocessing.py

import multiprocess
import os


# 子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)' %(name,os.getpid()))

if __name__ == '__main__':
	print('Parent procee %s.' % os.getpid())
	p = multiprocess.Process(target=run_proc,args=('test',))
	print('Child procee will start.')
	p.start()
	p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
	print('Child process end.')
