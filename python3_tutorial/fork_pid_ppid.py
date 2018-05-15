# fork_pid_ppid.py
import os

print('Process (%s) start ...' % os.getpid())

pid = os.fork()

if pid == 0:
	print('I am chaild Process (%s) and my Parent is %s.' % (os.getpid(),os.getppid()))
else:
	print('I (%s) just created a child process (%s).' %(os.getpid(),pid))
