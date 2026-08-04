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

ex

import math
print(math.sqrt(25))
------------------


2.sys
3.os
-------------------------------------
4.rondm
ex:

import random
print(random.randint(a=1000,b=9999))




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

details = {'name':'vyshnavi','ATM PIN':'1234'}
           
import random
remain_=3
while remain_>0:
    pin_=input('enter pin number:')
    if pin_==details['ATM PIN']:
        otp=random.randint(1000,9999)
        print(otp)
        user_otp=int(input('enter user otp: '))
        if user_otp==otp:
            otp=int(input('enter option \n1.withdraw \n2.deposite'))
    else:
        remain_-=1
        if remain_>0:
            print(f' incorrect pin enter and you have{remain_2}')
        else:
            print(f'you have entered 3 times incorrect pin')
        
    
























