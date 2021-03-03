What is List Comprehensions?
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) 
using sequences which have been already defined.

#List Comprehension
l=[i for i in range(10)]
'''op-[0,1,2,3,4,5,6,7,8,9]'''

#eg1
l=[i for i in range(10) if i%2==0]
print(l)
'''op:
[0,2,4,6,8]'''

#eg2
k=[(i,j) for i in range(3) for j in range(3)]
print(k)
'''op--
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]'''

#eg3
k=[i.lower() for i in 'HELLO']
print(k)

'''[print, for loop , condition]'''

#practical problems:
1)Given a list of numbers, write a list comprehension that produces a list of each number doubled.
num=[1, 2, 3, 4, 5]
k=[i*2 for i in num]
print(k)

2)printing only even numbers
num=[1, 2, 3, 4, 5]
k=[i for i in num if i%2==0]
print(k)

3)printing only +ve numbers
num=[1, 2, 3, 4, 5,-5]
k=[i for i in num if i>0]
print(k)

4)pringing the number which is divisible by 5
num=[5,10,25,6,9]
k=[i for i in num if i%5==0]
print(k)

5)cartesion product
k=[(i,j) for i in range(3) for j in range(3)]
print(k)

6)Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.
a='fareen'
j=[i for i in a if i=='a' or i=='e' or i=='i' or i=='o'  or i=='u']
print(set(j))

