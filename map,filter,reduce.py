#map() function
'''
The map() function is going to apply the given function on all the items inside the iterator and return an iterable map object i.e a tuple, a list, etc.
map(function, iterator1,iterator2 ...iteratorN)
function : necessary
iteraror : necessary
'''
#Example:find the square of the number in the givrn list
def sqr(x):
        return x*x

l=[1,2,3,4,5,6,7,8,9,10]
m=list(map(sqr,l))
print(m)
'''apply square on the given list l'''

#same eg with lambda function
l=[1,2,3,4,5,6,7,8,9,10]
m=list(map(lambda x:x*x,l))
print(m)

#EXAMPLES:
fun=list(map(lambda x:x*x,range(10)))
print(fun)
'''op:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''


-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#reduce
'''Applies function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
Syntax
reduce (function, iterable [, initializer])

function
Required. A function of two arguments.
iterable
Required. An iterable sequence.
initializer
Optional. Value placed before the iterable; default value if iterable is empty.
'''
import functools
list1=[1,2,3,4]
print(functools.reduce(lambda x,y:x+y,list1))
'''
op:10
 x, is the accumulated value and the right argument, y, is the update value from the iterable.'''

#using operator
import functools
import operator
list1=[1,2,3,4]
print(functools.reduce(operator.add,list1))
'''
op:10
first it will take 1,2 combine them and store in x and the x+newxt val and so on'''
        OR
import functools
import operator
list1=[1,2,3,4]
print(functools.reduce(operator.add,[1,2,3,4]))

#using iitializer
import functools
list1=[1,2,3,4]
print(functools.reduce(lambda x,y:x+y,[20,30,40],100))
'''op:
100+20+30+40
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#filter
li=[1,2,3,4,5,6,7,8,9,10]
def gre(num):
    return num>5

l=list(filter(gre,li))
print(l)
        #OR
l=list(filter(lambda x:x>5,li))
print(l)

#return all the +ve number in the given range
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)





































