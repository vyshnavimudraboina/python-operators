'''
elif
-----------
ex
marks_ = 78
if marks_ >= 90:
    print('A+')
elif marks_ >= 80:
    print('A')
elif marks_ >= 70:
    print('B+')
elif marks_ >= 60:
    print('B')
elif marks_ >=35:
    print('C')
else:
    print("fail")
-----------------------

ex;

num = 89
num_2 = 102
num_3 = 5
if num > num_2 and num > num_3:
    print(f'{num} is greater value')
elif num_2 > num and num_2 > num_3:
    print(f'{num_2} is greater value')
else:
    print(f'(num_3) is greater value')
-------------------------------------------

nested if
------------
details_ = {'ATMPIN': 3455}
atm_ = input('enter tour 4 digit atm pin: ')
if len(atm_) == 4:
   if atm_ == details_['ATMPIN']:
       OP_ = int(input("enter \n1.withdraw \n2.deposite \n3.pinchange"))
       if op_ == 1:
           money_W = int(input('enter money to withdraw: '))
        elif op_ ==2:
            money_D = int(input('enter a money to deposite: '))
    else:
        print('incorrect pin enter')
else:
    print('pls enter only 4 digit pin')
---------------------------------------------------------------------------
loops
-------
1.for loop
---for loop is used to itterate over sequence such as str,list,tuple
--else in for loop it will execute when whole itterate are completed
---incase if condition become true,then else will never execute..
range()
 sytanx:
 range (start,end,stop)
 
 ex;
 for j in range(1,10,3):
    print (j)
ex;
num = 'python is a language'
for i in num:
    print(i)
ex;
num = 'python is a language'
for i in num:
    print(i)
else:
    print('end')
output;
p
y
t
h
o
n

i
s

a

l
a
n
g
u
a
g
e

e
n
d

------------------
i)break
ex;
num = [34,34,45,56,7,87]
for i in num:
    print(i)
    if i == 56:
        break
else:
    print('end')

ii)continue
num = [34,38,45,56,7,87]
for i in num:
    if i == 45:
       continue
    print(i)
else:
    print('end')
output:
34
38
56
7
87
end
iii)pass

num = [34,38,45,56,7,87]
for i in num:
    pass
-----------------------
2.while loop
-------------------
ex:
num = 1
while num < 10:
    print(num)
    num += 1
-------------
i)assert
ex;
age = 35
assert age >= 18, 'not eligible'
print('eligible')


'''
marks_ = 565
assert marks_ >= 35, 'fail'
print('pass')





























