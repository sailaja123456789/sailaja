def fun(name):
    print(name)
fun("sailaja")

..........positional arguments........
def fun(a,b,c):
    return a,b,c
print(fun(45,54,66))

def fun(a,b,c):
    return a,b,c
a=13
b=33
c=45
print(fun(a,b,c))

def fun(name,fruits):
    return name,fruits
print(fun("sailaja","mango"))

...keyword arguments...

def fun(a,b,c):
    return a,b,c
print(fun(a=34,b=56,c=67))

......default argument...

def fun(a=23,b=45,c=4):
    return a,b,c
print(fun())

def fun(a=23,b=45,c=4):
    return a,b,c
print(fun(1,3,4))

def fun(name,fruit=mango):
    return name,fruit=mango
print(fun("arya "))

.....variable length arguments...
def fun(*args):
    return args
print(fun(1,2,3,))
def fun(*args):
    return args
print(fun())

def fun(**kwargs):
    return kwargs
print(fun(a=23,b=34,c=45))

def fun(**kwargs):
    return kwargs
print(fun())

def fun(**k):
    return k
print(fun(a=23,b=34,c=45))

def fun(**k):
    return k
print(fun())

def add(a,b):
    c=a+b
    print(c)
add(4,5)


def mul(a,b,c):
    d=a-b-c
    print(d)
mul(45,56,67)


def person(name,age):
    print(name)
    print(age)
person("arya",8)


def person(name,age=10):
    print(name)
    print(age)
person("arya"),8

def sum(x, *y):
      c=x
      
  for i in y:
        c=c+i
    print(c)
sum(34,45,343,45)


def person(name,**age):
    print(name)

    for i,j in age.items():
        print(i,j)
person ("arya",age=9,city="andhra",mob=454554453)



def person(name,**data):
    print(name)
    
    for i,j in data.items():
        print(i,j)
person("arya",age=8,city="andhra",mob=6565656644)

def fun(name,message,age):
    print(name,message,age)
fun(name=23,message="hi",age=22)
fun("sailaja","hi",22)
fun("rose",message="hi",age=22)
fun("gaya","hello",age=22)
fun("jhanu",message="hello",age=44)

def fun(fruits,flower):
    print(fruits,flower)
    
fun("banana",flower="rose")
fun(fruits="mango",flower="lilly")
fun("apple","rose")

...............*arg..............

def fun(*name):
    return name
    print(name)
fun("jaga","kishore","gopi")


def fun (*fruits):
    print(fruits)
fun()

def fun(*name):
    print(name)
fun("arya","mahi",56)

def fun(a,*b):
    c=a
    for i in b:
        d=c+i
    print(d)
fun(43,56)

def fun(**name):
    print(name)
fun(name="arya",age=34)
fun(name="arya",age=22,weight=3)

def int(**numbers):
    print(numbers)
int(age=23,weight=45,size=45,shape=6)

 A simple Python function

def fun():
	print("Welcome to GFG")


 Driver code to call a function
fun()


def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

 Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
 some more functions
def is_prime(n):
	if n in [2, 3]:
		return True
	if (n == 1) or (n % 2 == 0):
		return False
	r = 3
	while r * r <= n:
		if n % r == 0:
			return False
		r += 2
	return True
print(is_prime(78), is_prime(79)


 A simple Python function to check
 whether x is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


 Driver code to call the function
evenOdd(2)
evenOdd(3)


 Python program to demonstrate
 default arguments
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)


 Driver code (We call myFun() with only
 argument)
myFun(10)


 Python program to
 demonstrate accessing of
 variables of nested functions

def f1():
	s = 'I love GeeksforGeeks'
	
	def f2():
		print(s)
		
	f2()

 Driver's code
f1()
























