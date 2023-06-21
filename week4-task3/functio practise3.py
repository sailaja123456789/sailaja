def fun(*a):
    print(a)
fun(3,4,3,6)

def fun(**data):
    print(data)
fun(name="sailaja",message="hi",age=22,data="hello")





function is four types

..........without parameter,without return value......

def fun():
    print("hello,where are you!")
    print("welcome to our application!")
fun()


def fun():
    print("where are you going!")
    print("hi,what are you doing!")
fun()

..........without parameter,with return value.......

def some_of_first_10_numbers() :
    sum=0
    for i in range(1,11):
        sum=sum+i
        return sum
ans=some_of_first_10_numbers()
print(ans)

def some_of_first_10_numbers() :
    sum=1
    for i in range(1,11):
        sum=sum+i
        return sum
ans=some_of_first_10_numbers()
print(ans)

.........with parameter,without return value........

def welcome_user(name,gender):
    if gender =="m":

     print("welcome mr",name,"have a nice day!")
    else:
    
     print("welcome mrs",name,"have a nice day!")
name=input("enter your name")
gender=input("enter your gender(M/F)")
welcome_user(name,gender)
             

def welcome_user(name,gender):
    if gender =="m":

     print("welcome mr",name,"hi!")
    else:
    
     print("welcome mrs",name,"hello!")
name=input("enter your name")
gender=input("enter your gender(M/F)")
welcome_user(name,gender)
             

............with parameter,with return value......

def get_count(arr,size,target_value):
    cnt=0
    for i in range(0,size):
        if arr[i]==target_value:
            cnt=cnt+1
    return cnt

my_list=[1,2,2,2,2,1,1,1,1,3,3,3,3,4,4,3,3,3,3,3,2,2,2]
print('1 occurance:',get_count(my_list,len(my_list),1))
print('2 occurance:',get_count(my_list,len(my_list),2))
print('3 occurance:',get_count(my_list,len(my_list),3))
print('4 occurance:',get_count(my_list,len(my_list),4))






























