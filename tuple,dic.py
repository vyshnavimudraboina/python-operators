'''
        ***tuple***
--->tuple is a collection different datatype that are represented in () and separated by
--->tuple is immuttable
index;
---->variable_name.index(item)
ex;
go = (1,'java',[3,6],('python',63))
print(go.index('java'))
------------------------------------
count;
syntax----->variable_name.count(item)
ex;
go = (1,'java',[3,4],('python',78))
print(go.count(('python',78)))
print(go.count('python',))
--------------------------------
       ***dictionary***
----->dict is key:value pair
----->keys and values separated by
------>dict is represented by {}
1.keys
--> sytanx; dict.keys()
ex;
details  = {'name':'vyshnavi',
            'AC':12345678,
            'plan':345678,
            'adhr':87655432}
print(details.keys())
2.values
--->sytanx; dict.values()
details  = {'name':'vyshnavi',
            'AC':12345678,
            'plan':345678,
            'adhr':87655432}
print(details.keys())
3.items
----->
ex;
details  = {'name':'vyshnavi',
            'AC':12345678,
            'plan':345678,
            'adhr':87655432}
print(details.items())
4.update
--->dict.update({})
details  = {'name':'vyshnavi',
            'AC':12345678,
            'plan':345678,
            'adhr':87655432}
details.update({'adhr':9876543212345})
print(details)
5.clear
---->dict.clear()



--------------------------------

'''
details  = {'name':'vyshnavi',
            'AC':12345678,
            'plan':345678,
            'adhr':87655432}
print(details.keys('name'))




