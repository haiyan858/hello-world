# task_master.py
# _*_coding:utf-8_*_
# 简单的Master/Worker模型

import random, time, queue
from multiprocess.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc'---为了保证两台机器正常通信，不被其他机器恶意干扰:
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(20):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(20):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')



# import random, time, queue
# from multiprocess.managers import BaseManager


# task_queue = queue.Queue()
# result_queue = queue.Queue()


# class QueueManager(BaseManager):
# 	pass

# QueueManager.register('get_task_queue',callable=lambda: task_queue)
# QueueManager.register('get_result_queue',callable=lambda: result_queue)

# manager = QueueManager(address=('',5000),authkey=b'abc')
# manager.start()
# task = manager.get_task_queue()
# result = manager.get_result_queue()

# for i in range(10):
# 	n = random.randint(0,10000)
# 	print('Put task %d...' %n)
# 	task.put(n)

# print('Try get results...')
# for i in range(10):
# 	r = result.get(timeout = 10)
# 	print('Result:%s' % r)

# manger.shutdown()
# print('manager exit.')

