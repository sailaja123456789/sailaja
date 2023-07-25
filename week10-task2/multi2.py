import threading  
def print_hello(n):
    print("Hello, how old are you ", n)  
t1 = threading.Thread( target = print_hello, args =(18,))  

import threading
def fun():
    print("amma")

def fun1():
    print("nana")

t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun)

t1.run()
t2.start()



import time
import _thread

def thread_test(name, wait):
   i = 0
   while i <= 3:
      time.sleep(wait)
      print("Running %s\n" %name)
      i = i + 1

   print("%s has finished execution" %name)

if __name__ == "__main__":
    
    _thread.start_new_thread(thread_test, ("First Thread", 1))
    _thread.start_new_thread(thread_test, ("Second Thread", 2))
    _thread.start_new_thread(thread_test, ("Third Thread", 3))






import time
import threading

class threadtester (threading.Thread):
    def __init__(self, id, name, i):
       threading.Thread.__init__(self)
       self.id = id
       self.name = name
       self.i = i
       
    def run(self):
       thread_test(self.name, self.i, 5)
       print ("%s has finished execution " %self.name)

def thread_test(name, wait, i):

    while i:
       time.sleep(wait)
       print ("Running %s \n" %name)
       i = i - 1

if __name__=="__main__":
    thread1 = threadtester(1, "First Thread", 1)
    thread2 = threadtester(2, "Second Thread", 2)
    thread3 = threadtester(3, "Third Thread", 3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


import threading
import time


def print_numbers():
    for i in range(5):
        print(threading.current_thread().name, i)
        time.sleep(1)


thread1 = threading.Thread(target=print_numbers, name='Thread 1')
thread2 = threading.Thread(target=print_numbers, name='Thread 2')


thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Multithreading example has finished.")

















