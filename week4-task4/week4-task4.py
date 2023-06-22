name = "Alice"
age = 25
print("My name is", name, "and I am", age, "years old.")

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print("The sum is:", result)



def fun(**name):
    print(name)
    return name
fun(name=)

..........pass statement.............

def fun(name):
    pass
   



.............keyword....
def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
    
print( "Without using keyword" )    
function( 50, 30)       
        

print( "With using keyword" )    
function( n2 = 50, n1 = 30)    

.....positional 0r required....... 

def function( n1, n2 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2)    
    
  
print( "Passing out of order arguments" )    
function( 30, 20 )       
    
   
print( "Passing only one argument" )    
try:    
    function( 30 )    
except:    
    print( "Function needs two positional arguments" )

.............variable length argument.......

....*arg...
def fun(*name):
    for i in name:
     print(i)
fun("sailaja","hello")

def fun(*name):
    for i in name:
     print(i)
fun("mahi",33,"oieryoeifioher","ijjfeeeeeeef")

def fn(*name):
    print(name)
fun(23,45,56)

def fun(*num):
    print(num)
fun(22,45,34)


............**kwarg........


def fun(**name):
    print(name)
fun(name="sailaja",message="hello",age=22)


def fun(**data):
    print(data)
fun(name="sailaja",message="hi",age=22,data="hello")

def fun(**data):
    for i in data:
     print(i)
fun(shape="circle",size="round",data="sailu")










..................default argument...........
def fun(name,age):
    print(name,age)
fun("sailaja",age=22)


def fun(name,age,message):
    print(name,age,message)
fun("sailaja",22,"hi")

