function without argument or parameter or signature


def sadist():
    print("gopi")
sadist()

def fun():

    print("gayathri")
    print("Kishore")
    a = input("Enter your name")
    print(a)

fun()    


function with arguments

def fun(name):
    print("gayathri", name)
fun("jhansi")
fun("gopi")
fun("kishore")
fun("gayathri")
fun("sailaja")


def fun(name,age):
    print("gayathri",name,age)
fun("sailaja",44)
fun("gopi",45)
fun("kishore")
fun("gayathri")
fun("sailaja")

def fun(name,food):
    print("gopi",name,food)
fun("gayathri","chicken")
fun("sailaja","chapathi")

def int(age1,weight):
    print("gopi",age1,weight)
int(24,95)


function with default argument

def fun(name,fruit=["apple"]):
    print(name,fruit)
fun("gopi")


def fun(name,fruit=["mango"]):
    print(name,fruit)
fun("gopi")
##
def fun(name=["mango"],fruit="list"):
    print(name,fruit)
fun(fruit="gopi")

def fun(x,y):
    c=x+y
    d=x-y
    e=x*y
    print(e,d,c)

fun(45,56)


def fun(x,y,z):
    a=x+y-z
    b=x-y+z
    c=x%y*z
    print(a,b,c)
fun(45,65,78)


.....................calling a function...........

def fun():
  print("Hello from a function")
fun()



def sadist():
    print("gopi")
sadist()

def fun():
    print("sailaja")
fun()

def fun():
    print("kishore")
fun()


..............POSITIONAL ARGUMENTS.......................
def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet("Alice", 25)

def fun(name,age):
    print(name,age)
fun("kishore",26)


..............KEYWORD ARGUMENTS.................

def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet(age=25, name="Alice")


def fun(name,fruits):
    print(name,fruits)
fun("sailaja","mango")

def int(name,age):
    print(name,age)
int("sailaja",22)

def int(age,size,weight):
    print(age,size,weight)
int(22,4,45)



def fun(age,size,weight):
    print(age,float(size),weight)
fun(25,8,56)


..........DEFAULT ARGUMENT.................
def greet(name, age=30):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet("Bob")  

def fun(name,fruit="mango"):
    print(name,fruit)
fun("sailaja")

def fun(name,fruit=["mango"]):
    print(name,fruit)
fun("gopi")

def fun(name=["mango"],fruit="list"):
    print(name,fruit)
fun(fruit="gopi")

def fun(name=["mango"],fruit="list"):
    print(name,fruit)
fun(name="gopi")
....................variable length arguments..................

def calculate_sum(*args):
    total = sum(args)
    return total

print(calculate_sum(1, 2, 3, 4))  


def fun(w,x,y,z):
    a=w+x+y+z
    b=w-x-y-z
    c=w+x-y+z
    print(a,b,c)
fun(23,45,65,45)


def fun(x,y):
    c=x+y
    d=x-y
    e=x*y
    print(e,d,c)

fun(45,56)


def fun(x,y,z):
    a=x+y-z
    b=x-y+z
    c=x%y*z
    print(a,b,c)
fun(45,65,78)






























