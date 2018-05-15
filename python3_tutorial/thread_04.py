# thread_04.py
import threading
global_dict1={}
global_dict2={}

def get(name,act):
   global_dict1[threading.current_thread()]=name
   global_dict2[threading.current_thread()]=act
   action()

def action():
   print(global_dict1[threading.current_thread()] ,end='')
   print(' is ',end='')
   print(global_dict2[threading.current_thread()])

th1=threading.Thread(target=get,args=('Jone','batting'),name='Th_Jone')
th2=threading.Thread(target=get,args=('Dannis','kicking'),name='Th_Dannis')
th1.start()
th2.start()
th1.join()
th2.join()
