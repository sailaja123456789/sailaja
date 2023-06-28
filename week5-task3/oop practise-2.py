...............inheritance......
when a child class inherts the properties of a parent class. it is class inheritance

class parent:
    def fun1(self):
        print("this is a parent function")


class child(parent):
    def fun2(self):
        print("this is a child function")
obj=child()
obj.fun1()
obj.fun2()
    


class mobile:
    def fun1(self):
        print("this is a mobile function")
        
class laptop(mobile):
    def fun2(self):
        print("this is a laptop")
obj=laptop()
obj.fun1()
obj.fun2()



...................__init__() function....................

............auto matically every time the class is used to create an object...........


class parent:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
    def view(self):
        print(self.name,self.age)

class child(parent):
    def __init__(self,fname,fage):
        parent.__init__(self,fname,fage)
        
        self.lastname="edureka"
    def view(self):
        print(self.age,self.name,self.lastname)
obj=child(23,"python")
obj.view()

 
................single inheritance............

class person:
    def fun1(self):
        print("arun annayya")

        
class person1(person):
    def fun2(self):
        print("murali annayya")

obj=person1()
obj.fun1()
obj.fun2()


class mobile:
    def fun1(self):
        print("sailaja")

class cell(mobile):
    def fun2(self):
        print("gayathri")
obj=cell()
obj.fun1()

        
.......................multiple inheritance...........................................  
    
    

class person:
    def fun1(self):
        print("arun annayya")
class person2:
    def fun3(self):
        print("this is a function3")

        
class person1(person,person2):
    def fun2(self):
        print("murali annayya")


obj=person1()
obj.fun1()
obj.fun3()

...............multilevelinheritance.........



class person:
    def fun1(self):
        print("arun annayya")
class person2(person):
    def fun3(self):
        print("this is a function3")

        
class person(person2):
    def fun2(self):
        print("murali annayya")


obj=person()
obj.fun1()
obj.fun3()

......................hierachical..............


class person:
    def fun1(self):
        print("arya is a dog")
class person2(person):
    def fun3(self):
        print("this is a function3")

        
class person(person2):
    def fun2(self):
        print("mahi is a dog")


obj=person()
obj=person2()
obj.fun1()
obj.fun1()











































































































