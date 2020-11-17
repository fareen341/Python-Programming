#cONTROL FLOW
"""
1.Selection statement
if
if-else
if-elif-else
if-elif

2.Iterstive stmt
for
while

3.Transfer stmt
break continue

"""

#if
#1.Selection statement(decision making statements or branching statements)

#if
i=30
if i==30:
    print('i value is:',i)
print('Rest of the code')
"""o/p---
i value is: 30
Rest of the code"""

#if-else
i=30
if i==31:
    print('i value is:',i)
else:
    print('i is not equal to 30')
print('Rest of the code')
"""
i is not equal to 30
Rest of the code
"""

#if-elif-else
a=input('Enter a character:')
if a=='a':
    print(a,'is vovel')
elif a=='e':
    print(a,'is vovel')
elif a=='i':
    print(a,'is vovel')
elif a=='o':
    print(a,'is vovel')
elif a=='u':
    print(a,'is vovel')
else:
    print(a,'is consonent')

#if-elif
a=input('Enter a character:')
if a=='a':
    print(a,'is vovel')
elif a=='e':
    print(a,'is vovel')
elif a=='i':
    print(a,'is vovel')
elif a=='o':
    print(a,'is vovel')
elif a=='u':
    print(a,'is vovel')
print('rest of the code')

#Question
if():
    print('True')
else:
    print('False')                              #False
        #OR
if 1:
    print('True')
else:
    print('False')                              #True

"""
if takes boolean value any value except these values(null,0,empty parentahesis,False) everything will be true including -ve values will be true
"""

#remember the indentation
"""There will always be space after every if statement
The equal space represent the one single block
"""
i = 15
if(i==15):
    print("First Statement")
    if(i%3==0):
        print("Second Statement")
print('None of above will run')
"""o/p--
First Statement
Second Statement
None of above will run
"""

#else belongs to first if stmt
i = 18
if(i==15):
    print("First Statement")
    if(i%3==0):
        print("Second Statement")
else:
    print('This else belongs to first if stmt')
"""op--
This else belongs to first if stmt
"""


#else belongs to second if stmt
i = 15
if(i==15):
    print("First Statement")
    if(i%2==0):
        print("Second Statement")
    else:
        print('Cannot divided by 2')
"""op---
First Statement
Cannot divided by 2
"""

#if both if and else condition is true(if will be printed)
age=30
if age>20:
    print('if')
elif age>20:
    print('elif')
else:
    print('else')
"""op---
if

"""

#Program
if(0):
    print("NULL")
elif(False):
    print("TRUE")
else:
    print("FALSE")                                #o/p--False


#using set of conditions
"""
if any value in set of condition is false the output will be false
for true all statemnt must be true
"""
i,j=1,1
k=0
if i==j==k:
    print("True")
else:
    print("False")                               #op--False

i,j,k=1,2,3
if i<j<k:
    print("True")
else:
    print("False")                              #op---True


#using logical operator
i,j=1,9
if i or j:
    print("True")
else:
    print("False")                             #op--TRue(i and j both are non zero)
    
i,j=0,0
if i or j:
    print("True")
else:
    print("False")                              #op---false

#Program
"""
in this case True and False evaluate to False so it will become
if(False) which will print False 
"""
if True and False:
    print("True")
else:
    print("False")                             #op--- False


#using escape character
print(ord('\0'))
if('\0'):
    print('True')                             
else:
    print('False')
    
#Transfer stmt(break,continue)-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
break goes out of the stmt
for i in range():
   if:
      stmt
   break--------------------------------------
                                             |
print('')<------------------------------------

continue skip that particular stmt and come up
for i in range(): <------------------------------------
   if:                                                |
      stmt                                            |
   continue-------------------------------------------
print('')

"""
#break
for i in range(10):
    if i==5:
        break
    print(i)
print('Came out of statement')
"""op---
0
1
2
3
4
Came out of statement
"""
#Program
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')

print('Loop is Terminated')
"""op---
Siya
Tiya
Guru
Found the name Guru
Loop is Terminated
"""

#continue
for i in range(10):
    if i==5:
        continue
    print(i)
print('Came out of statement')
"""op---
0
1
2
3
4
6
7
8
9
Came out of statement
"""

#Program
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        continue
        print('After break statement')

print('Loop is Terminated')
"""o/p:
Siya
Tiya
Guru
Found the name Guru
Daksh
Riya
Guru
Found the name Guru
Loop is Terminated"""

#Iterstive stmt(while, for)----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#while
"""
as long as the condition is true in while it will run
it will only stop on false condition
while also take boolean value
"""

#infinite loop
n=1
print("Infinite loop starts")                #run infinite bcoz it will always be true
while n>0:
    n=n+1
    print(n)


i=1
n=10
while(i<n):
    if(i%2==0): 
        print('Even:',i)                     #infinite loop printing(Odd:1)
    else:
        print('Odd:',i)

#stopping the infinite loop with break stmt
while(1):
    print('hello')                           #op--hello (without break it is infinite loop)
    break

#while with if and else
i=1
n=10
while(i<n):
    if(i%2==0):
        print('Even:',i)                    
        i+=1
    else:
        print('Odd:',i)
        i+=1
"""op----
Odd: 1
Even: 2
Odd: 3
Even: 4
Odd: 5
Even: 6
Odd: 7
Even: 8
Odd: 9
"""
#nested while
i=1
while(i<3):
    print(i)
    i+=1
    j=1
    while(j<3):
        print(j)
        j+=1

#printing star in nested loop
"""
    ****
    ****
    ****
    ****
"""
i=1
while(i<5):
    i+=1
    print()
    j=1
    while(j<5):
        print('*',end="")
        j+=1
        
#while with else stmt(else will run after while complete)
i=1
while(i<5):
    print(i)
    i+=1  
else:
    print('this is else')
"""op---
1
2
3
4
this is else
"""

#While (if) with break stmt
i=1
while(i<10):
    if i==4:
        break                                  #op---1 2 3
    print(i,end=" ")
    i+=1

#while (if) with continue stmt
i = 0
while i <= 20 :
    i += 1
    if i % 2 == 1 :
        continue
    print(i)
"""o/p:
2
4
6
8
10
12
14
16
18
20
"""

#Group of stmt
"""
while(stmt1, stmt2, stmt3)
run as long as all the condition is true 
"""
a,b,c=1,2,3
while(a<b<c):
    print('ok')
    b+=1
print('out of loop')
"""op---
ok
out of loop
"""

#PROGRAMS
#1.comparing id's
a=4
b=4
while(id(a)==id(b)):
    print('equal a and b value')                          #op--equal a and b value
    break
     #OR
a=4
b=4
while(a is b):
    print('equal a and b value')                          #
    break
     #OR
a=4,5
b=4
while(b in a):
    print('equal a and b value')                          #using membership
    break 

#2.using not
while(not 0):
    print('equal a and b value')                          #op---equal a and b value
    break  
else:
    print('false condition')

#3.using ascii value
while('a'>'0'):
    print('equal a and b value')                          #op---equal a and b value
    break  
else:
    print('false condition')

#4.
    i=1
while(i==2):
    print('equal')
    while(i==2):
        print('equal2')
print('false')

#5.
i=1
while(i==1):
    print('equal')
    while(i==2):
        print('equal2')
    else:
        print('inner while')
    break
else:
    print('outer while')
"""op--
equal
inner while
"""

#for loop
"""
for must be string, range or list
int,float,bool is not itrable

"""
#for loop in list
li=[1,2,3,4]
for x in li:
    print(x)                                             #op----1,2,3,4

#loop in range
for x in range(5):
    print(x)                                             #op---0,1,2,3,4

#loop in string
s="fareen"
for i in s:
    print(i)
"""op--
f
a
r
e
e
n
"""
#
s="fareen"
for i in s:
    print(i,end=" ")                                     #op---print fareen 5 times
"""op---
f a r e e n 
"""

#nested loop
for i in range(2):
    for j in range(3):
        print(i,j)
"""op---
0 0
0 1
0 2
1 0
1 1
1 2
"""

#Using step in range
x=range(1,10,2)
for i in x:                                              #op---1,3,5,7,9
    print(i)

#op---(-1,-2,-3,-4,-5,-6,-7,-8,-9)
x=range(-1,-10,-1)
print(x)
for i in x:
    print(i)

#op----(10,8,6,4,2)
x=range(10,1,-2)
print(x)
for i in x:
    print(i)

#for with break:
s="programming"
for i in s:
    if i=='m':
        break
    print(i)

#for with continue
s="programming"
for i in s:
    if i=='m':
        continue
    print(i,end='')
"""op---
prograing
"""

#for with else
for i in range(0,9):
    print(i)
else:
    print('print else too')
"""op---
0
1
2
3
4
5
6
7
8
print else toof
"""
#for with list(running two for loop simultaneously)
color = ["blue", "white"]
vehicle = ['car', 'bike', 'truck'] 
color_comb = [(x,y) for x in color for y in vehicle] 
print(color_comb)

#
i=[1,2,3]
j=[1,2,3]
for x in i:
    for y in j:
        print(x,y)

        #OR

z=[(x,y) for x in i for y in j]
print(z)

#
l=[1,2]
l2=[2,3]
combo=[(x,y) for x in l for y in l2]
print(combo)
"""op--
[(1, 2), (1, 3), (2, 2), (2, 3)]
"""

#printing pattern
"""
when i=0  i=1    i=2
     j=1  j=1,2  j=1,2,3

in 2nd case
     i=0 i=1     i=2
     j=1 j=1,2,3 j=1,2,3,4,5
     so
     k=1
     k=k+2
"""
#1.
k=1
for  i in range(0,5):
    for j in range(0,k):
        print('*',end='')
    k=k+1
    print()

"""op---
*
**
***
****
*****
"""
#2.
k=1
for  i in range(0,5):
    for j in range(0,k):
        print('*',end='')
    k=k+2
    print()
    #OR
for  i in range(0,5):
    for j in range(0,i+1):
        print('*',end='')
    print()
"""op--
*
***
*****
*******
*********
"""
#3.
n=1
for  i in range(0,5):
    for j in range(0,i+1):
        print(n,end=' ')
        n=n+1
    print()
"""op---
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
"""

#4.
n=1
for  i in range(0,5):
    for j in range(0,i+1):
        print(n,end=' ')
    n=n+1
    print()
"""o/p--
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""

#5.
n=97
for  i in range(0,5):
    for j in range(0,i+1):
        print(chr(n),end=' ')
        n=n+1
    print()
"""op--
a 
b c 
d e f 
g h i j 
k l m n o 
"""

#6.
n=97
for  i in range(0,5):
    for j in range(0,i+1):
        print(chr(n),end=' ')
    n=n+1
    print()
"""op---
a 
b b 
c c c 
d d d d 
e e e e e 
"""

#7.
k=5
for  i in range(0,5):
    for j in range(0,k):
        print('*',end=' ')
    k=k-1
    print()
"""op--
* * * * * 
* * * * 
* * * 
* * 
*
"""
#8.
a=97
k=5
for  i in range(0,5):
    for j in range(0,k):
        print(chr(a),end=' ')
        a=a+1
    k=k-1
    print()
"""op---
a b c d e 
f g h i 
j k l 
m n 
o
"""

#9.
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
"""op---
Second Number Pattern 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

#10.
"""
first print space
then star which start with j=0,1
"""
k=3
for i in range(0,k):
    for j in range(0,k-i-1):
        print(' ',end='')
    for j in range(0,i+1):
        print('*',end=" ")
    print()
"""
  * 
 * * 
* * * 
"""

#11.
k=3
for i in range(0,k):
    for j in range(0,k-i-1):
        print(' ',end='')
    for j in range(0,2*i+1):
        print('*',end="")
    print()

"""
  *
 ***
*****
"""

#.12.
k=3
for i in range(0,k):
    for j in range(0,k-i-1):
        print(' ',end='')
    for j in range(0,i+1):
        print('*',end="")
    print()
"""
  *
 **
***
"""

#13.
k=5
for i in range(0,5):
    for j in range(0,5):
        print('*',end='')
    print()
"""
*****
*****
*****
*****
*****
"""

#14.
k=5
num=1
for i in range(0,5):
    for j in range(0,5):
        print(num,end='')
    num=num+1
    print()
"""
11111
22222
33333
44444
55555
"""

#15.
k=5
num=1
for i in range(1,6):
    for j in range(1,6):
        print(j,end='')
    print()
"""
12345
12345
12345
12345
12345
"""

#16
for i in range(1,6):
    num=5
    for j in range(1,6):
        print(num,end='')
        num=num-1
    print()
"""
54321
54321
54321
54321
54321
"""

#17.
k=5
num=1
for i in range(1,6):
    for j in range(1,k):
        print(num,end='')
    num=num+1
    k=k-1
    print()
"""
1111
222
33
4
"""


#POINTS TO REMEMBER
'''
1.break and continue cannot be used with if-else and if stmt
it should be with loop only
.....(invalid)
    if:
        break
    else:
......(valid)
    while 1:
    if:
        break
    else:
'''


#CONTROL FLOW IN IF ELSE
#only if
if 1:
    print('if')


#nested if
if 1:
    if 1:
        print('inner if')
    print('outer if')

#outer else
if 0:
    if 1:
        print('inner if')
    print('outer if')
else:
    print('outer else')

#True and False is intrepreted as (0 1 in python)
if 1 != True:
    if not True:
         print('inner if')
print('outer if')
































