##............encapsulation.......



public
private__
proteccted_

class demo():
    __a=2
    _b=4
    print(__a)
    print(_b)


class MyClass():
    def __init__(self):
        self.public_var = 10

    def public_method(self):
        print("This is a public method.")


obj = MyClass()


print(obj.public_var)  
obj.public_var = 20
print(obj.public_var)  


obj.public_method(



class students:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def classroom(self):
        print("gayathri",self.__name)
        print("sailu",self.__age)
x=students("gai","hii")
x.classroom()




class demo():
    def __init__(self,name,age,hour):
        self.name=name
        self.age=age
        self.hour=hour
    def public(self):
        print("first")
    def _protected(self):
        print("second")
    def __private(self):
        print("three")
    def fun(self):
        print("abc")

x=demo(3,5,4)

x.name
x.public()


x.age
x._protected()


x._demo__private()
x.fun()

class person():
    def __init__(self,name,age,data):
        self.name=name
        self.age=age
        self.data=data
    def public(self):
        print("red")
    def _protect(self):
        print("blue")
    def __private(self):
        print("pink")
    def fun(self):
        print("sailaja")

x=person("sailu",44,35)
x.name
x.public()
x.age
x._protect()
x._person__private()
x.fun()
   










































