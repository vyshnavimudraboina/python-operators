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

'''
import itertools import permutations,combinations

data = permutations([1,2,3],2)
print(list(data))

any_ = combinations([1,2,3],2)
print(list(any_))


