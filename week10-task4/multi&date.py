

from _thread import start_new_thread
from time import sleep

threadId = 1
waiting = 2 

def factorial(n):
    global threadId
    rc = 0
    
    if n < 1:   
        print("{}: {}".format('\nThread', threadId ))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factorial( n - 1 )  
        print("{} != {}".format(str(n), str(returnNumber)))
        rc = returnNumber
    
    return rc

start_new_thread(factorial, (5, ))
start_new_thread(factorial, (4, ))

print("Waiting for threads to return...")
sleep(waiting)



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


  






import datetime

x = datetime.datetime.now()
print(x)


import datetime
tdate=datetime.date(2016,7,7)

print("date format:",tdate)

##tdate=datetime.date.today()
##print("today date:",tdate)

print("day:",tdate.day)
print("month:",tdate.month)
print("year:",tdate.year)
wday=tdate.weekday()
print("weekday:",wday)


wday=tdate.isoweekday()
print("iso weekday:",wday)




tdelta=datetime.timedelta(days =5)
print("time delta:",tdate+tdelta)


import datetime
x=datetime.datetime.now().strftime("%A")
print(x)


import datetime
x=datetime.datetime.now().strftime("%d")
print(x)

import datetime
x=datetime.datetime.now().strftime("%D")
print(x)


import datetime
x=datetime.datetime.now().strftime("%f")
print(x)

import datetime
x=datetime.datetime.now().strftime("%d %m %y")
print(x)


import datetime
x=datetime.datetime.now().strftime("%d %b %m")
print(x)

import datetime
x=datetime.datetime.now().strftime("%a %d %m %y")
print(x)

import datetime
x=datetime.datetime.now().strftime("%A %d %m %y")
print(x)

import datetime
x=datetime.datetime.now().strftime("%d %m %y %h")
print(x)



import datetime
x=datetime.datetime.now().strftime("%A %d %B %y %H")
print(x)


import datetime
x=datetime.datetime.now().strftime("%H")
print(x)

import datetime
x=datetime.datetime.now().strftime("%d %m %y")
print(x)


import datetime
x=datetime.datetime.now().strftime("%d %B %A %H %Y")
print(x)

import datetime
x=datetime.datetime.now().strftime("%a %A %w %d %b %B %m %y %Y %H %I %p %m %S %f %z %Z %j %U %W %C %c %x %x %% 5g 5v 5u")
print(x)

















   
