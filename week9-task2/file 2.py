f=open("sailu.txt","w")
f.write("hello, sailaja")
f.close()


f=open("suresh.txt","w")
f.write("hello, sailaja")
f.close()


f=open("suresh.txt","r")
x=f.read()
f.close()
print(x)


f=open("mahi.txt","w")
name=input("enter your name")
f.write("welcome to my world".format(name))



f=open("abc.txt","w")
f.write("mahi,sailu,arya")
f.close()


f=open("abc.txt","r")
x=f.read()
f.close()
print(x)

f=open("abc.txt","a")
f.write("mahi")



f=open("nana.txt","w")
f.write("welcome to new life my dear cats")
f.close()



f=open("nana.txt","r")
x=f.read()
f.close()
print(x)




file = open('file.txt', 'a')
file.write('New line\n')
file.close()

f=open("ms.txt","a")
f.write("fake peoples")
f.close()

f=open("mr.txt","a")
f.write("fake frinds")
f.close()




with open('file.txt', 'a') as file:
    
    file.write('This is a new line.\n')




with open('file.txt', 'a') as file:
   
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)









