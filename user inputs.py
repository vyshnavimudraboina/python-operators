'''
**input formating**
int--->int(input())
---
ex;
num = int(input("enter a number:"))
print(num+4)
print(type(num))

string--->input()
-----
ex;
num = (input("enter a name:"))
print(num)
print(type(num))

list--->using map take user input
-----
ex;
nums = list(map(int,input('enter nums: ').split()))
print(nums)

list using string
ex
nums = input('enter nums: ').split()
print(nums)

tuple
--------
ex
nums = tuple(map(int,input('enter nums: ').split()))
print(nums)

nums = eval(input('enter nums: '))
print(type(nums))
24h clock problem
program


'''
time_ = input("enter a 24h clock: ")
parts_ = time_.split(':')
hours_ = int(parts_[0])-12
print(hours_,':',parts_[1],'pm')

