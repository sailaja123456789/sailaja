class Hello:

    def run(self):
        for i in range(4):
            print("Hello")


class Hi:
    def run(self):
        for i in range(3):
            print("Hi")
            
t1=Hello()
t2=Hi()

t1.run()
t2.run()




class Hello:

    def start(self):
        for i in range(4):
            print("Hello")


class Hi:
    def start(self):
        for i in range(3):
            print("Hi")
            
t1=Hello()
t2=Hi()

t1.start()
t2.start()



from time import sleep
from threading import*
class Hello(Thread):

    def run(self):
        for i in range(4):
            print("Hello")
            sleep(3)


class Hi(Thread):
    def run(self):
        for i in range(3):
            print("Hi")
            sleep(2)
            
t1=Hello()
t2=Hi()

t1.start()
t2.start()

t1.join()
t2.join()



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
def calc_square(numbers):
    print("square number : ")
    for number in numbers:
        time.sleep(0.2)
        print("square : ",number*number)

def calc_cube(numbers):
    print("cube number : ")
    for number in numbers:
        time.sleep(0.2)
        print("cube : ",number*number*number)

initial_time=time.time()
l=[1,2,3,4,5]
calc_square(l)
calc_cube(l)
print("Time taken : ",time.time()-initial_time)


import time
def calc_square(numbers):
    print("square number : ")
    for number in numbers:
        time.sleep(0.2)
        print("square : ",number*number)

def calc_cube(numbers):
    print("cube number : ")
    for number in numbers:
        time.sleep(0.2)
        print("cube : ",number*number*number)

initial_time=time.time()
l=[2,5,8,7,4]
calc_square(l)
calc_cube(l)
print("Time taken : ",time.time()-initial_time)



import threading
    
import time
def calc_square(numbers):
    print("square number : ")
    for number in numbers:
        time.sleep(0.2)
        print("square : ",number*number)

def calc_cube(numbers):
    print("cube number : ")
    for number in numbers:
        time.sleep(0.2)
        print("cube : ",number*number*number)

initial_time=time.time()
l=[1,2,3,4,5]


t1 =threading .Thread(target=calc_square,args=(l,))
t2 =threading .Thread(target=calc_cube,args=(l,))


t1.start()
t2.start()

t1.join()
t2.join()


print("Time taken : ",time.time()-initial_time)



from threading import Thread

def display():
    for i in range(5):
        print("hello")

t1=Thread(target=display)

t1.start()
              
