#RANGE(Sequence of numbers) range(begin,end-1,step)  default(0,end-1,1)
'''
forward dirn(sub 1)
backward dirn(add 1)
'''


r=range(5)              #Starts with 0 end to end-1 4 
type(r)

#Indexing and slicing in range
r=range(10)             #o/p--(0,10)   
print(r[1])
print(r[ :5])
print(r[ : ])           #o/p--(0,10)
print(r[-1])            #o/p--(9)

#Range is immutable bcoz it is range
r[0]=7                  #TypeError


#Accessing range
r=range(10)
for x in r:  
    print(x)            #o/p--(0,1,2,3,4,5,6,7,8,9)


r=range(0,30,5)         #o/p--(0,5,10,15,20,25)
for x in r:  
    print(x)

#for printing negative values in range
s=range(-1,-10,-1)
for x in s:
    print(x)

"""op---
-1
-2
-3
-4
-5
-6
-7
-8
-9
"""

#printing reverse values
s=range(10,0,-1)
for x in s:
    print(x)
"""op---
10
9
8
7
6
5
4
3
2
1
"""
