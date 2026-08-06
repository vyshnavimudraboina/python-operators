'''
modules
-------------
-->modules are the python code which is saved in (.py) that contains functions,variables,classes


types of modules
---------------
1.build in function
--------------
--> the build in modules that are already designed which comes with python  when we are installing

--
1.math
---> math module used to work on mathematical functionality
ex

import math
print(math.sqrt(25))

floor
--->it will round down to the near value
ex:
--------------------
lcm
ex:

import math
print(math.lcm(24,36))

square root

----> it will get square value
ex:

import math
print(math.sqrt(25))
------------------------
factorial
---> it will give factorial value

ex:

import math
print(math.factorial(5))
--------------
log
--->
import math
print(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)



------------------
2.sys
---> sys is used to get the details of python interperter

i.version

ex:
import sys
print(sys.version)
-----------------------
ii..py path  we will get by this func
ex

import sys
print(sys.version)
print(sys.path)
----------------------
iii.exit
---> this function will exit from the program
ex:

import sys
print(sys.exit())#there is no show output
print(sys.platform)
--------------
vi.platform
--->it will the python run platform
ex:

import sys
print(sys.platform)
------------------
v argv
----> it will give the current run path
ex:

import sys
print(sys.argv)
---------------------
vi.datetime
--->it will give the today time + time

ex:

from datetime import datetime
print(datetime.now())
print(d)

ex:


from datetime import datetime
now = (datetime.now())
print(now.strftime('%Y-%m-%d'))
print(now.strftime('%A'))
print(now.strftime('%B'))
print(now.strftime('%h:%m:%s'))
print(now.strftime('%y-%m-%d'))

%y-->year
%m-->month
%d--->day
%h--->hour
%s---->second
%A--->current date
%B--->current month
----------------------------
vii.collections
---> the collectyion module will provide container type data which is more powerful than build in data types

ex:
import collections
data=['apple','banana','orange','banana','pineapple']
print(collections.Counter(data))

i.deque

ex:

from collections import deque
data = deque([1,2,3])
data.appendleft(7)
print(data)
----------------
ii.pop

ex:

from collections import deque
data = deque([1,2,3])
data.pop()
print(data)
-------------------
iii.namedtuple

ex:

from collections import namedtuple
data = namedtuple(typename='stu',field_names=('name','age'))
print(data('join','18'))

-------------------
itertools
---------------

i.count

ex:

from itertools import count
c = count(100)
for j in range(5):
    print(next(c))

ii.ex:

import itertools

for j in itertools.repeat(p_object('python',10)):
    print(j)

iii.permitations,and combinations

ex:

import itertools import permutations,combinations

data = permutations([1,2,3],2)
print(list(data))

any_ = combinations([1,2,3],2)
print(list(any_))


--------------------------------------
3.os
-------------------------------------
4.rondm
ex:

import random
print(random.randint(a=1000,b=9999))
---------
i. randint
--->used to generate random numbers based on the range
ex:

import random
print(random.randint(a=1000,b=9999))
---------------------
choice
-----
---> it will the random value from the given data

ex:

import random
color =['red','green','blue']
print(random.choice(color))

-------------------
suffle

---> it can shuffle the data randomly

ex:

import random
color =['red','green','blue']
print(random.choice(color))
random.shuffle(color)
print(color)
--------------
uniform

---> will give the decimal in a range given

ex:

import random
print(random.uniform(a=1,b=100))

-------------------

---------------------
2.user defined
--------------------
--> the user define modules are create by the programmer

ex:

import firstfile

print(firstfile.add(a=56,b=8))
print(firstfile.sub(a=56,b=8))

------------------
pre defined
----------------
--->we can also import a module with different name
---->after importing with the alias name,we have to use that alias name in the cod
ex:

import firstfile as am

print(am.add(a=56,b=8))
print(am.sub(a=56,b=8))
------------------------------
importing only need function
------------------------------
--> when we are importing the new function from the module can only access that function

syntax:---> from(keyword) module_name import(keyword) functions

ex:

from firstfile import add,sub,mul

print(add(a=56,b=8))
print(sub(a=56,b=8))
print(mul(a=56,b=8))
----------------------------
importing all functions
----------------------------
-->use the all function in that module we have use(*) to get all of those..

syntax:-->from(keyword) module_name import(keyword)*)

ex

from firstfile import *

print(add(a=56,b=8))
print(sub(a=56,b=8))
print(mul(a=56,b=8))
print(div(a=56,b=8))

---------------------------
random pass ganerator

string

import random
import string
print(string.ascii_letters)#--> this string module function that give 
print(string.digits)#upper and lower letters digits: string module function that can given us numbers(0-9)
print(string.punctuation)#string module function that can given us(special characters @$&)

ex:

import random
import string
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
special_char = '$%&@/\\'

all_chars = letters + digits + special_char

password =''
for i in range(5):
    password += random.choice(all_chars)
print(password)
-----------------------------------

bank_balance = 10000
from datetime import datetime

import sys
now = datetime.now()
while True:
    print("---welcome to SBI ATM---")
    user_opt = int(input("\n1.withdraw \n2.deposite \n3.check balance \n4.exit")
                if user_opt==1:
                   with_m = int(input("enter a money you want to withdraw:"))
                   if with_m > bank_balance:
                   bank_balance -= with_m
                   print(f"remaing  money {bank_balance} {now.strftime("%H:%M %Y-%m-%d"}")
                   else:
                       print('insufficient money')
                       elif user_opt == 2:
                           Deposite_m = int(input('enter the money you want to deposite: '))
                        
                           print(f"money added successfuully:{bank_balance} {now.strftime("%H:%M%Y-%m-%d"}")
                           elif user_opt == 4:
                               sys.exit()
                               else:
                                   print("incorrect chioce")
                                   print("thank for visiting the atm")
                                   sys.exit()
                                    
                           
number game

import random
num=(random.randint(a=1, b=5))
print(num)
user_opt = int(input("pick a number(1-5): "))
if user_opt == num:
    print(f"you have picked {user_opt} number")
else:
    print("better luck next time")



1.

name = 'vyshnavi'
age = 34
avg = 89.4
print(name)
print(age)
print(avg)


2

name = 'vyshnavi'
user_name = 'mudraboina'
print(name + user_name)

3.

fruits = ['mongo','apple','banana']
print(fruits[1])

4.

list = [1,2,4,5,6]
avg = 18/5 
print(sum(list))
print(avg)

5.

a = int(input('enter a number: '))
if a%2==0:
    print('even')
else:
    print('odd')

6.

a = [34,6,78,93,5,1]
print(max(a))
print(min(a))

7.

length = float(input('enter a length:'))
width = float(input('enter a width:'))
area = length * width
print('Area of a rectangle:', area)

8.

a = int(input('enter a number'))
b = int(input('enter a number'))
print(a+b)


9.

a = input(' enter name')
age= 79
print(f"hello",a)


10.

def palindrome(s):
    if s == s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
text = input("enter a string:" )
palindrome(text)
    

'''
a = [2,4,6,8,3,5,9,11]
if a%2==0:
    print(sum(a))



