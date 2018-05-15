# thread_01.py
# _*_ coding:urf-8 _*_

import time, threading

# 新线程执行的代码:
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n=0
	while n<5:
		n = n+1
		print('thread %s >>> %s' %(threading.current_thread().name,n))
		time.sleep(1)
	print('1-thread %s ended.' % threading.current_thread().name)



print('thread %s is running ... '% threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('2-thread %s ended.' % threading.current_thread().name)
