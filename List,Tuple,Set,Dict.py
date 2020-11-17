#LIST
"""
LIST--------- represent with []
1.Order will be preserved
2.mutable
3.duplicates are allowed
4indexing and slicing are allowed
5.use for changing values like height and weight
6.different kind of values can be stored(int,float,str,bool,complex)
"""
#Order is fixed
a=[]
a.append(10)
a.append(20.666)
a.append("fareen")
a.append(False)
a.append(10+20j)
print(a)

#Mutable
a[0]=30
print(a)

#Duplicate
a.append(10)
print(a)

#Indexing and slicing
print(a[0])
print(a[0:])
print(a[-1:-4:-1])

#Nasted list
b=[1,[1,2,3],'fareen',[1,2,3]]
print(b)

#how to access the nasted list?
"""
        0 1 2 3 4 5 
list =  f a r e e n
              |
              |
              0 1
              m y
                |
                |
                0 1 2 3
                n a m e

list['f''a','r','e',['m','y',['n','a','m','e']],'e','n']

list[3][1][0]
"""
a=['f','a','r','e',['m','y',['n','a','m','e']],'e','n']
print(a)
print(a[4][2][0])           #o/p--n

#
l=[1,2,3,[0,1,[2,3]],4,[2,3]]
print(l[3][2][1])

#slicing in nested list
l=[1,2,3,[0,1,[2,3,4,5]],4,[2,3]]
print(l[3][2][0:2])

#Range inside a list
li=list(range(10))

#Methods of list...
"""

2	len(list)
Gives the total length of the list(number of elemnt).

3	max(list)
Returns item from the list with max value.

4	min(list)
Returns item from the list with min value.

5	list(seq)
Converts a tuple into list.
"""

h=[10,20,30,40]
print(len(h))
print(max(h))
print(min(h))
print(list(h))

o=(10,20)
print(list(o))


"""
append()	Adds an element at the end of the list

insert()	Adds an element at the specified position

clear()	Removes all the elements from the list  & del detele list along with elements

copy()	Returns a copy of the list

count()	Returns the number of elements with the specified value

extend()	Add the elements of a list (or any iterable), to the end of the current list

index()	Returns the index of the first element with the specified value

pop()	Removes the element at the specified position

remove()	Removes the first item with the specified value

reverse()	Reverses the order of the list

sort()	Sorts the list
"""
#
l=[99,98,False,'100']
l.insert(0,'python')

l=[99,98,False,'100']
l.clear()

l=[1,2,3,4]
p=l.copy()

l=[99,98,False,'100']
print(l.count('100'))

l=[99,98,False,'100']
o=[1,2,3]
o.extend(l)
print(o)

#if pop is empty it removes the last element
l=[1,2,3,4]
l.pop(2)

l=[99,98,False,'100']
print(l.index('100'))

l=[1,2,3,4,5]
l.reverse()

l=['b','a','  ']
l.sort()

#difference in remove ,pop, del
#remove(remove the first matcing VALUE),pop(remove the item at specific INDEX and returns it), and del(remove the item at specific INDEX)
l=[1,2,3,4,4]
l.remove(4)                           # remove the first occurance of ELEMENT NOT INDEX o/p--[1,2,3,4]
print(l)

l.pop(0)                              #o/p-- [2,3,4]
print(l)

del l[0]                              #o/p--[3,4]
print(l)


#TUPLES-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""TUPLES---------- represent with ()
same as list except-
1.tuples are immutable
2.latitude and longatitude of ur home which is fixec
"""

a=(10,20.666,'fareen',False,10+20j)
print(a)

#immutable
a[0]=30
print(a)                           #TypeError: 'tuple' object does not support item assignment"""


b=(10)                             #Int
#All belo are tuple
b=(10,)
b=()
b=10,

#methods
"""count()	Returns the number of times a specified value occurs in a tuple
   index()	Searches the tuple for a specified value and returns the position of where it was found"""
t=1,2,3,4,5,5
print(t.count(5))
print(t.index(4))


#SET------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
1.insertion order are not preserved
2.duplicate are not allowed
3.indicated by{}
4.set item are not indexed so slicing and indexing not allowed
5.immutable
6.we can add and remove item in set tho, but cannot change the value by using index
"""

i={}                              #By default it is dict bcoz we dont use set as much as dict

#we can declare empty set as
i=set()

#insertion order are not preserved
i=set()
i.add(10)
i.add(20.6)
i.add(True)
i.add("hello")
"""o/p---
{True, 10, 20.6, 'hello'}
"""

#duplicate are not allowed
i=set()
i.add(10)
i.add(20.6)
i.add(True)
i.add("hello")
i.add("hello")
"""o/p--
{True, 10, 20.6, 'hello'}
"""

#methods
"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item (just like remove method in list)
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set any item
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""
#difference
x = {"apple", "banana", "cherry"}                               #return only x value compared with y and o
y = {"google", "microsoft", "apple"}
o = {"google", "microsoft", "apple","banana"}
z=x.difference(y,o)
print(z)

#update x value
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
x1.difference_update(y1)
print(x1)

#remove the specified ELEMENT 
c={'1','2'}
c.discard('1')

#intersection(common element)
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
z2=x2.intersection(y2)
print(z2)

x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}
x3.intersection_update(y3)
print(x3)

#Disjoint(if a intersection b is zero)
x4 = {"apple", "banana", "cherry"}
y4 = {"google", "microsoft", "apple"}
z4=x4.isdisjoint(y4)                              #false
print(z4)

#Subset(Return True if all items set x are present in set y
x5 = {"a", "b", "c"}
y5 = {"f", "e", "d", "c", "b", "a"}             #true
z5 = x5.issubset(y5)
print(z5)

x0 = {"f", "e", "d", "c", "b", "a"}             #false
y0 = {"a", "b", "c"}
z0 = x0.issubset(y0)
print(z0)

#Superset(Return True if all items set y are present in set x
x6 = {"f", "e", "d", "c", "b", "a"}           #true
y6 = {"a", "b", "c"}
z6 = x6.issuperset(y6)
print(z6)

x7 = {"a", "b", "c"}                           #false
y7 = {"f", "e", "d", "c", "b", "a"} 
z7 = x7.issuperset(y7)
print(z7)

#Pop (remove any random element and return the removed element)
"""p={2,3,4}                       #error
p.pop(1)
print(p)"""

p={2,3,4,0}
k=p.pop()
print(k)                                #0 

#remove(ELEMENT not index)(if not found gives keyerror)
q={1,2,3,4}
q.remove(4)
print(q)

#symmetric_difference(Return a set that contains all items from both sets, except items that are present in both sets))
x8 = {"apple", "banana", "cherry"}
y8 = {"google", "microsoft", "apple"}                  #o/p:{'banana', 'microsoft', 'google', 'cherry'}
z8 = x8.symmetric_difference(y8)
print(z8)

x8 = {"apple", "banana", "cherry"}
y8 = {"google", "microsoft", "apple"}                  #Updated the x8 value
x8.symmetric_difference_update(y8)
print(x8)

#union(Return a set that contains all items from both sets, duplicates are excluded)
#difference between union and symmetric_difference is union give the o/p including the element which present in both)
x8 = {"apple", "banana", "cherry"}
y8 = {"google", "microsoft", "apple"}                  #o/p:{'cherry', 'microsoft', 'google', 'banana', 'apple'}
z8 = x8.union(y8)
print(z8)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}                   #simply update x 
x.update(y)
print(x)
"""o/p
first x={"apple", "banana", "cherry"}
after update x={'google', 'microsoft', 'cherry', 'banana', 'apple'}
"""

#difference in discard and remove
'''
discard dont give error if iten not found but remove gives keyerror if item not found.
'''

#DICTIONARY--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
1.duplicated not allowed
2.indexing and slicing not allowed
3.we can check the value of a perticuar key by giving its key
'''
#Points to remember
#1.Duplicate key not allowed(key must be unique)
""" More than one entry per key not allowed. Which means no duplicate key is allowed.
When duplicate keys encountered during assignment, the last assignment wins. """"
l={1:1,2:2,3:3,1:4}
print(l)
"""o/p---
{1: 4, 2: 2, 3: 3}
"""
#Empty Dict
k={}
type(k)

#Key-Value pair
k={1:'fareen',2:'anamika'}
print(k)

for i in k:                               #This gives only keys   
    print(i)

#if access 'c' this gives "keyerror" to avoid this use get
j={'a':97,'b':98}
print(j)
print(j['a'])
j.get('b')
j.get('c')

#key can be int,float,bool,str,tuple
l={1:'int',10.5:'float',False:'bool','str':'str',(2):'python'}
print(l)

#Mutable
l={1:1,2:2,3:3}
l[2]=4
print(l)

#2.cannot use list in dict, int,float,str,tuples allowed
dict = {['Name']: 'fareen', 'Age': 22}                               #error
print(dict['Name'])

dict = {('Name'): 'fareen', 'Age': 22}
print(dict['Name'])

#methods of dict
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""



#fromkey
#Create a dictionary with 3 keys, all with the value 0
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#Same example as above, but without specifying the value
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

x=(1,2)
y=(0,1)
z=dict.fromkeys(x,y)

#get(The get() method returns the value of the item with the specified key)
"""
Try to return the value of an item that do not exist:gives none not error
"""
d={1:'a',2:'b'}
s=d.get(2)
print(s)

#item(The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list)
d={1:'a',2:'b'}
z=d.items()
print(z)
"""o/p:
dict_items([(1, 'a'), (2, 'b')])
"""

#keys(The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.)
d={1:'a',2:'b'}
z=d.keys()
print(z)
"""o/p:
dict_keys([1, 2])
"""
#values(return all the values, The view object contains the values of the dictionary, as a list.)
d={1:'a',2:'b'}
z=d.values()
print(z)
"""o/p:list of values
dict_values(['a', 'b'])
"""

#pop(if default value is not specified it will give keyerror)
d={1:'a',2:'b',3:'c'}
z=d.pop(2)                           #pop(keyname,defaultvalue(optional))
print(z)

d={1:'a',2:'b',3:'c'}
z=d.pop(4,'not exist')                           #pop(keyname,defaultvalue(optional))
print(z)

#Popitem(Remove the last item from the dictionary)
d={1:'a',2:'b',3:'c'}
z=d.popitem()                           #pop(no value)
print(z)

#setdefault(Returns the value of the specified key. If the key does not exist: insert the key, with the specified value)
d={1:'a',2:'b',3:'c'}
z=d.setdefault(1,'g')                            #o/p: a(a which is alredy abailable)
print(z)

d={1:'a',2:'b',3:'c'}
z=d.setdefault(4,'d')                            #o/p: 4 with value inserted at the end
print(z)

#Updates the dictionary with the specified key-value pairs (if the key value not availabe insert key-value at the end)
d={1:'a',2:'b'}
z=d.update({3:'c'})                      
print(d)




#POINTS TO REMEMBER
'''
Nested list has no effect on method
in the below method the reverse opreation only worked on list not on nested list tho , same for all method
operation will only be performed on outer list
'''
l=['f','a',['a','e','i',['p','o','o'],'o'],'r','e','e','n']
print(l.reverse())
'''op--
['n', 'e', 'e', 'r', ['a', 'e', 'i', ['p', 'o', 'o'], 'o'], 'a', 'f']'''

#sort
'''
in case of character it sort by ascii
'''
l=['a','b','A','*',' ']
l.sort()
'''
[' ', '*', 'A', 'a', 'b']
'''










