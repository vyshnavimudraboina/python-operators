'''
functions
-----------
-->func is a block that can be executes when we call it
-->to avoid the repeated lines of code
syntax:
def function_name(parameters):
     -----------
     -----------
     -----------
function_name(arguments)
----------------------------
types of functions
1.bulit-in
ex;
i.print()
ii.len()
iii.max()
iv.min()

2.user-define
==> user-define are the functions that are develop by the user
ex;
num = 56
num_2 = 89
def total_(num , num_2):
    print(num + num_2)
total_(num,num_2)
total_ (1,2)
-------------------
ex;
required arguments

num = 56
num_2 = 89
num_3 = 7
def total_(num , num_2,num_3):
    print(num)
total_(num,num_2,num_3)
total_(1,2,3)
------------------------
positional arguments
------------------
==>i t does not matter how we are passing the variable,
if we assign the value to that variable in the calling

ex;
def name_(name,name_):
    print(name)
    print(name_)
name_(name = 'vyshnavi',name_ ='mudraboina')
----------------------------------
defult argument value
-------------------------
ex:no automatically used parameters if no arguments passed

def any_(age,edu,name):
    print(name)
any_('vyshu',50,'b.tech')
----------
ex: passed arguments

def any_(age,edu,name):
    print(name)
any_( name='vyshu',age=50,edu='b.tech')
------------------
variable-length positional arguments
i.*args
--->we can pass tuple of arguments and stored in a single parameter bt just adding* before the parameter
--->*single take tuples
--------------------
ex:we want particaler value

def all_(*nums):
    print(nums[1])
all_(10,30,20,8)
-------
ex:adding

def all_(*nums):
    print(nums[1]+nums[3])
all_(10,30,20,8)
--------
ex:print all list

def all_(*nums):
    print(nums)
all_(10,30,20,8)
-------

ii.**kargs
--->by pass keyword arguments in the arguments,will get it as dic just adding ** before the parameter
--->and can access by using dc methods...
ex:

def dct(**all_in):
    for key,val in all_in.items():
        print(key,':',val)
dct(name = 'teja',age ='56',role ='mentor')
-------------
both using *args and **kargs
ex:

def dct_nums(*args,**kargs):
    print(args)
    print(kargs)
dct_nums(12,33,56,name='vyshnavi',age=50,edu='b.tech')
-------------------------------
--scope of the varibles---
i.local variable :outside the varible
ex:

num_2 = 89
def nums(num_2):
    num = 90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)
----------
fabanocci

limit_ = int(input('enter the limit: '))
num = 0
num_2 = 1
def fibonocci(limit_,num,num_2):
    print(num,num_2,end=' ')
    for j in range(1,limit_+1):
        num_3 = num+num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
fibonocci(limit_,num,num_2)
----------------------

---passing by value--

ex:
def any_(a,b):
    print(a)
    print(b)
any_(23,34)
--------------
--passing by reference----

ex:

def any_(num,num_2):
    print(num)
    print(num_2)
any_(num = 8 , num_2 = 9)
--------------

Anonymous function
------------------
--->anonymous function is a function that dont any name
-->this also called as lamda
--->lamda function will take n number arguments but only one expression
sytax;
lamda arguments : expresssion

ex:
so = lambda a,b,c,d : a+b+c+d
print(so(2,3,4,5))
1.map()
-->the map func will be applied on the given func of each and every element of an itterable
ex:
nums = [1,2,3,5,4,7]
so = list(map(lambda x: x*x,nums))
print(so)

output:

[1, 4, 9, 25, 16, 49]

2.filter()
--->filter () function we only consider if the condition is true then it will keep that values

ex:

nums = [1,2,3,5,4,7]
so = list(filter(lambda x: x%2==0,nums))
print(so)

output:
[2,4]

3.reduce




'''
from functools import reduce
nums = [1,2,3,5,4,7]
so = reduce(lambda x,y: x+y,nums)
print(so)



































