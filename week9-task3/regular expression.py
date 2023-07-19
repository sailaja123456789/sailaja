
RegExp Function............
....................findall()................................

import re
str="sandeep sadist"
x=re.findall("e",str)
print(x)


import re
str="sandeep sadist"
x=re.findall("a",str)
print(x)


import re
str="sandeep sadist"
x=re.findall("s",str)
print(x)

import re
str="sandeep sadist"
x=re.findall("xyz",str)
print(x)

...............................search().....................
import re
str="sandeep sadist"
x=re.search("xyz",str)
print(x)

import re
str="sandeep sadist"
x=re.search("e",str)
print(x)

import re
str="sandeep sadist"
x=re.search("s",str)
print(x.start())


import re
str="sandeep sadist"
x=re.search("d",str)
print(x.start())


import re
str="sandeep sadist"
x=re.search("e",str)
print(x.start())


import re
str="sandeep sadist"
x=re.search("sadist",str)
print(x.span())


import re
str="sandeep sadist"

x=re.search("sadist",str)
print(x.string)

...................split().......................



import re
str="sandeep sadist"
x=re.split("sadist",str)
print(x)


import re
str="sandeep sadist"
x=re.split("s",str)
print(x)



import re
str="sandeep sadist "
x=re.split("",str)
print(x)


import re
str="sandeep sadist is an youtuber"
x=re.split(" ",str)
print(x)


import re
str="sandeep sadist is an youtuber"
x=re.split(" ",str,1)
print(x)

import re
str="sandeep sadist is an youtuber"
x=re.split(" ",str,5)
print(x)


import re
str="sandeep sadist is an youtuber"
x=re.split(" ",str,3)
print(x)
...................sub()..............................
import re
str="sandeep sadist is an youtuber"
x=re.sub("s","r",str)
print(x)

import re
str="sandeep sadist is an youtuber"
x=re.sub("s","r",str,2)
print(x)


import re
str="sandeep sadist is an youtuber"
x=re.sub("s","r",str,1)
print(x)


import re
str="sandeep sadist is an youtuber"
x=re.sub("s","A",str,)
print(x)

..............................................................................meta characters....................


..............[]............................
import re
str="example for metal characters in regular expression"
x=re.findall("[a]",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("[in]",str)
print(x)

...................(^)..................
import re
str="example for metal characters in regular expression"
x=re.findall("^example",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("^meta",str)
print(x)

..................$..................

import re
str="example for metal characters in regular expression"
x=re.findall("meta$",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("ssion$",str)
print(x)
...................(.).................
import re
str="example for metal characters in regular expression"
x=re.findall("exam...",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("exam..",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("exam.",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("exam.....",str)
print(x)


import re
str="example for metal characters in regular expression"
x=re.findall("......exam...",str)
print(x)

import re
str="example for metal characters in regular expression"
x=re.findall("...r",str)
print(x)


...................(*).......................


import re
str="example for metal characters in regular expression"
x=re.findall("m*",str)
print(x)

import re
str="example for metal characters in regular expression"
x=re.findall("m*",str)
print(x)

import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("ee*",str2)
print(x)

import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("ee*",str)
print(x)


import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("is*",str2)
print(x)

....................(+).......................

import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("ie+",str2)
print(x)

............{}...............

import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("e{2}",str2)
print(x)


import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("e{1}",str2)
print(x)



............................................................................special sequences......................


......................./s...................


import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("/s",str2)
print(x)


import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("\s",str2)
print(x)

............/S................
import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("\S",str2)
print(x)

import re
str="example for metal characters in regular expression"
str2="friend in need is a friend in deed"
x=re.findall("/S",str2)
print(x)

....................\d.................
import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("\d",str2)
print(x)


.................\D......................

import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("\D",str2)
print(x)

.......................\w.................

import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("\w",str2)
print(x)

.........................\W..............

import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("\W",str2)
print(x)




..................................................................................sets..................

..............[abc]....................

import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("[123]",str2)
print(x)

...................[abc^]......................
import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("[^123]",str2)
print(x)
.....................[0-9][0-9]........................

import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("[0-9][0-9][0-9]",str2)
print(x)


import re
str="example for metal characters in regular expression"
str2="123 friend in need is a friend in deed"
x=re.findall("",str2)
print(x)









