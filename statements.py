'''
statements
--------------
there are three types of statements
1.condition statements
2.control statements
3.looing statements(iteration loops)
-----------------------------------------------
1.condition statements
there are:
i)if
ii)if else
iii)elif
iv)nested if
-------------------------------
2.control statements
there are:
i)break
ii)pass
iii)continue
------------------------------
3.looping statements
i)while
ii)do while
iii)for
---------------------------------------
if condition
--------------
ex;
a = int(input("enter a age: "))
if 18 <=a:
    print(" eligible ")
else:
    print("not eligible")
    
examples:
age= int(input("enter a age: "))
if age >=18:
    print(f"your age is {age} and eligible to vote ")
else:
    print(f" your age is {age},you have to wait {18-age} years")
-------------------------------------------------------------------------

a= int(input("enter a number: "))
if a%2==0:
    print("even")
else:
    print("odd")
--------------------------------------
vol_ = input("enter a letters:" )
if vol_ in "AEIOUaeiou" :
    print(f'{vol_} is vol')
else:
    print(f'{vol_} is con')
---------------------------------------
so = 'python'
do = so[::-1]
print(do)
if so[::-1]==so:
    print(f'{so} is pali')
else:
    print(f'{so} is not pali')
-----------------------------
year_ = int(input("enter a year:"))
if year_%4==0  and year_%100!=0 or year_% 400 == 0:
   print("leaper")
else:
    print("not leaper")


'''
