'''
limit_ = int(input("enter the limit: "))
for j in range (1,limit_+1):
    if j % 2 == 0:
       print(f'{j} is aeven')
    else:
       print(f'{j} is a odd')
----------------------
prime or not

ex;
num = int(input("enter a number: "))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
         print(f'{num} is prime')
else:
         print(f'{num} is not prime')

------------------------------------
ex;

for i in range (2,10):
    count = 0
    for j in range (1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')
-------------------------------------
        
ex;
rev_ = input('enter a word')
emp_ = " "
for j in rev_:
    emp_ = j+emp_
if emp_ == rev_:
   print(f'{rev_} is pal')
else:
    print(f'{rev_} not pal')
-------------------------------------
    
ex;

start_ = int(input("enter a number: "))
for j in range (1, start_+1):
    for i in range (1,j+1):
        print('*',end='')
    print()
----------------------------------------
ex;

start_ = int(input("enter a number: "))
for j in range (1, start_+1):
    for i in range (1,j+1):
        print(i,end='')
    print()
-----------------------------------------

count = 0
start_ = int(input("enter a number: "))
for j in range (start_ , 0,-1):
    for i in range(1,j+1): 
        count += 1
        print("*",end='')
    print()
------------------------------------
num = 7
for j in range(num):
    print(" " * (num - j -1),end = '')
    print('* ' * (j+1))
-------------------------------------------
num = 7
for j in range(num):
    print(" " * (num - j),end = '')
    print('* ' * j)
-------------------------------------
num = [1,2,2,5,5]
emt_ = []
for j in num:
    if j not in emt_:
        emt_.append(j)
print(emt_)
---------------------------
        
'''
num = int(input('enter a number: '))
per_num = 0
for j in range(1,num):
    if num % j == 0:
       per_num += j
if per_num == num:
   print(f'{num} is per num')
else:
   print(f'{num} is not per num')







































