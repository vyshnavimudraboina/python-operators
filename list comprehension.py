'''

list comprehension
--------------
-->the comprehension is the short form of syntax used to generate a new list from the old list....

syntax:
[expression loop]

ex:

num = [1,2,3,4,5]
new_ = [j for j in num]
print(new_)

ex:

num = [1,2,3,4,5]
new_ = [j if j%2==0 else 'odd' for j in num]
print(new_)

ex:

num = [1,2,3,4,5]
nel_ = [i for i in num if i%2!=0]
print(nel_)
------------------------------------
nested comprehension
----------------------
-->nested comprehension means an comprehension inside the another comprehension is called nested comprehension
sytax:
[expression loop_1 and loop_2]

match = [[1,2,3],[4,5,6],[7,8,9]]
all_ = [j for j in match]
print(all_)


match = [[1,2,3],[4,5,6],[7,8,9]]
any_ = [i for i in match]
all_ = [num for j in match for num in j]
print(any_)
print(all_)


new_ = [[i*j for j in range(1,6)] for i in range(1,6)]
ne = [i for i in range(1,6)]
print(ne)
print(new_)


output

[1, 2, 3, 4, 5]
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
--------------------------------

generator 
--------------
-->this generator will generate value one at a time and th pause it on the position when we are using yield keyword
---> here we use yield to get the value
--->   this yield is used to get the value and will only gives one value and pauses ther itself
--->if you want remainig values use get the next()

ex:

def gen(n):
    for i in range(1,n+1):
        yield i*i
a = gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
  

function and ganerator differences
--------------------
function             
-------------
return when the return is executed,it will exit for the function

ganerator
-----------------
--->yield
--->when the yield id executed, it will pause the function and the next yield is called then it will resume again
---> in ganerator will get one at a time .....

'''
def gen(n):
    for i in range(1,n+1):
        yield i*i
a = gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))






































    











