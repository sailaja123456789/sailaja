a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


...........................IF,ELIF AND ELSE INPUT FUNCTIONS................

number=int(input("enter the number of color:"))
if number == 1:
    print("red color")
elif number == 2:
    print("green color")
elif number == 3:
    print("blue color")
elif number == 4:
    print("white color")
else:
    print("no color")



name=int(input("enter the number of name:"))
if name == 1:
    print("gayathri")
elif name == 2:
    print("sailaja")
elif name == 3:
    print("jhansi")
elif name == 4:
    print("kishore")
else:
    print("no name")
    

number=int(input("enter the number:"))
if number%3==0 and number%5==0:
    print("sailajagayathri")
elif number%3==0:
    print("sailaja")
elif number%5==0:
    print("gayathri")
else:
    print(number)







................................IF AND ELSE STATEMENT..................................

age = 65

if age >= 60:
    print('Senior Discount')
else:
    print('No Discount')


age=25

if age>=45:
    print("senior discount")
else:
    print("no discount")



age=35
if age<60:
    print("senior discount")
else:
    print("no discount")


a = 2
b = 330
print("A") if a > b else print("B")




...................................IF,ELIF AND ELSE STATEMENT..........................................


price = 50
quantity = 5
amount = price*quantity

if amount > 100:
    if amount > 500:
        print("Amount is greater than 500")
    else:
        if amount < 500 and amount > 400:
            print("Amount is")
        elif amount < 500 and amount > 300:
            print("Amount is between 300 and 500")
        else:
            print("Amount is between 200 and 500")
elif amount == 100:
    print("Amount is 100")
else:
    print("Amount is less than 100")


number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')
































































































