##.............................SET..............................


##set{}
##set is not allow the duplicates

####..................ADD()...................................


##var={"hi","hello","who"}
##var.add("where")
##print(var)
##
##
##var={34,4353,4474,657387}
##var.add(546484644746)
##print(var)
##
##
##name={"sailaja","divya","gayathri","jhansi"}
##name.add("ruffiya")
##print(name)


#...................................COPY()..................

##fruits = {"apple", "banana", "cherry"}
##
##fruits.copy()
##
##print(fruits)
##
##flower={"rose","jasmeen","lilly"}
##n=flower.copy()
##print(n)
##
##
##a={434,543,53738,54782}
##b=a.copy()
##print(b)
##


##...........................clear()..............................
##


##a={"apple","mango","banana"}
##a.clear()
##print(a)
##
##
##a={235,433,35474,5446}
##a.clear()      
##print(a)
##
##
##a={"chocolate"}
##a.clear()
##print(a)


##..............................difference()...............................
##x = {"grapes", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.difference(y)
##
##print(z)
##
##a={"rose","jasmeen","red rose","mango"}
##b={"water melon","banana","mango"}
##c=a.difference(b)
##
##print(c)


##.........................................difference update......................................

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.difference_update(y)
##
##print(x)
##
##a={"rose","jasmeen","red rose","mango"}
##b={"water melon","banana","mango"}
##c=a.difference(b)
##
##print(c)
##
##name={3634,564,5}
##name1={3634,6576,65755756}
##c=name1.difference(name)
##print(c)
##

##........................discard().......................


##fruits = {"apple", "banana", "cherry"}
##
##fruits.discard("banana")
##
##print(fruits)
##
##
##name={"sailaja","amma","nanna","annayya"}
##name.discard("sailaja")
##print(name)
##
##
##var={5373537,544,64738746,143}
##var.discard(143)
##print(var)


##........................INTERSECTON..............................

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.intersection(y)
##
##print(z)
##
##a={"fruits","flowers","sweets"}
##b={"flowers","apples","mango"}
##c=a.intersection(b)
##print(c)
##
##a={"chocolates","fruits","flowers"}
##b={"chocolates","grocerry","flowers"}
##c=a.intersection(b)
##print(c)


##.................................INTERSECTION UPDATE................



##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.intersection(y)
##
##print(z)
##
##var={32,4645,5464545,6666,7777}
##var1={4354,675656,3788,7777,6666}
##var2=var.intersection(var1)
##print(var2)



##x={"divya","jhansi"}
##y={"gopi","kishore","divya"}
##print(x.isdisjoint(y))
##x={"divya","jhansi"}
##y={"gopi","kishore","divya","jhansi"}
##print(x.issubset(y))
##x={"divya","jhansi","gopi","kishore"}
##y={"gopi","kishore","divya"}
##print(x.issuperset(y))
##x={"divya","jhansi"}
##y={"gopi","kishore","divya"}
##print(x.union(y))

##.................isdisjoint.............

##var={"sailaja","mahndra varama",}
##y={"amma","nanna"}
##print(var.isdisjoint(y))
##
##var={"jhansi","ruffiya"}
##y={"sreenu","bhanu","jhansi"}
##print(var.isdisjoint(y))

##..........................issubset.............

##x={"grapes","flowers","sweets"}
##y={"grapes","mango","banana"}
##print(x.issubset(y))
##
##x={"mobile","laptop"}
##y={"headaet","bluetooth","mobile","laptop"}
##print(x.issubset(y))


##.....................issuperset...............

##x={"size","shape","sides","set"}
##y={"size","shape"}
##print(x.issuperset(y))
##
##
##x={"size","shape","sides","set","shadow"}
##y={"size","shape","grapes"}
##print(x.issuperset(y))
##
##
##
##x={"amma","nanna"}
##y={"anna","chelli","arya"}
##print(x.issuperset(y))

##....................................union.............


##x={"arya","mahi"}
##y={"arya","sweety","laddu"}
##print(x.union(y))
##
##
##x={"sweety","dog","cat"}
##y={"tiger","lion","parrot","dog"}
##print(x.union(y))


##.......................pop...............

##fruits = {"apple", "banana", "cherry"}
##
##fruits.pop()
##
##print(fruits)
##
##var={"dog","cat","tiger","lion"}
##var.pop()
##print(var)
##
##x={2,3373,25353,647855}
##x.pop()
##print(x)
##
##a={22324,4353,3634353,54454645}
##a.pop()
##print(a)

##
##a={234,43544,546454,45464545}
##a.pop()
##print(a)
##
##a={"juwyeuye","hsyuyeeueyue","hdyeye"}
##a.pop()
##print(a)
##
##x={5454545,6466658330,66656565656556,6565656,"hhfrururysjkekf"}
##x.pop()
##print(x)
##
##x={"amma","nanna","annayya","chelli"}
##   
##x.pop()
##print(x)
##
##
##
##a={"amma","nanna","mahi","sailaja"}
##a.pop()
##print(a)



##................................remove...............

##a={"dog","banana","cat"}
##a.remove("banana")
##print(a)
##
##a={"cat","dog","parrot"}
##a.remove("parrot")
##print(a)

##............................symmetric difference..........

##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.symmetric_difference(y)
##
##print(z)
##
##
##
##x={"cat","dog","parrot"}
##y={"cat","nanna","amma"}
##z=x.symmetric_difference(y)
##print(z)
##
##
##a={"relative","enemy","family"}
##b={"friends","relative"}
##c=a.symmetric_difference(b)
##print(c)



##.............................symmetric_difference_update..................


##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.symmetric_difference_update(y)
##
##print(x)




##..................UPDATE................

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)

a={"relative","enemy","family"}
b={"friends","relative"}
a.update(b)
print(a)












