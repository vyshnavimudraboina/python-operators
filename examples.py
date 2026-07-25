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
print('*', end = '')
print()
print('****' ,end ='')
print()
print('**',end = '')
print()
--------------------------
fabanocci series
ex;
tab_ = int(input('enter a number:' )
for j in range (1,11):
    print(f'{tab_} X {j} = {tab_*j}')

output;
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
------------------
amstrong number
 ex;
num = int(input('enter anumber: '))
length_ = len(str(num))
am_ = 0
for j in str(num):
    am_ = int(j) ** length_ + am_
if am_ == num:
    print(f'{num} is amstrong')
else:
    print(f'{num} is not')
--------------------------------
fabonocci series

ex:
limit_ = int(input("ente a number: "))
num = 0
num_2 = 1
print(num,num_2,end=' ')
for j in range (1,limit_+1):
    all_ad =  num + num_2
    num = num_2
    num_2 = all_ad
    print(all_ad,end=' ')
--------------------------------
calculation
ex;
num_1 = int(input("enter a number: "))
num_2 = int(input("enter a number: "))
opt_ = int(input("enter \n1.add \n2.sub \n3.* \n4./: "))
if opt_ == 1:
    print(num_1 + num_2)
elif opt_ == 2:
    print(num_1 - num_2)



       
'''




























