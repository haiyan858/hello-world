# thread_02.py
# _*_ coding:urf-8 _*_

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	# 先存后取，结果应该为0:
	balance = balance +n 
	balance = balance -n



def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(i)
		finally:
			lock.release()
		



t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()
print(balance)


