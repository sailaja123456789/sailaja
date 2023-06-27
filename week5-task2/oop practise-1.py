


class SampleClass:
    attribute1=10
    attribute2=20

print(SampleClass.attribute1)
print(SampleClass.attribute2)



class SampleClass:
    attribute1=10
    attribute2=20

obj1=SampleClass()
obj2=SampleClass()
obj3=SampleClass()
print(obj1.attribute1)
print(obj2.attribute1)
print(obj3.attribute1)

class SampleClass1:
    def sampleMethod(self):
        print("this method s created to demonstrate methods in class")
        
newObject1=SampleClass1()
newObject1.sampleMethod()
    

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is started.")


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)


print(car1.make)  
print(car2.model)  


car1.start_engine() 
car2.start_engine()  
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 25)
person.display()  

class person:
    def __init__(self,name,age):
         self.name=name
         self.age=age
         
    def display(self):
        print(f"name:{self.name},age:{self.age}")
person=person("sailaja",22)
person.display()

class mobile:
    def __int__(self):
        print("this is init")
    def display(self):
        print("this method")
obj=mobile()
obj.display()
    

































    
