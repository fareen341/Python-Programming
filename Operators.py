#Arithmetic Operators(+,-,/,*,//,**,%)
"""
/- only this always provide float value rest a both(int and float)
//,** - both int and float
//-floor division
"""

#/- always provide float value
a=10
b=5
print(a/b)

#'+' in string concatination (both value must be str type)
a='fareen'
b=10                       #error
c=a+b
print(c)

#%,//
9//10
9%10
'''
   0
   -
10]9
   0
   -
   9

so remainder(%)=9 and quotent(//) will be =0
'''

#//
a=10
b=3
print(a//b)                #int value output

a=10.0
b=3
print(a//b)                #float value output

#%
a=10
b=3
print(a%b)                 #int value output

a=10.0
b=3
print(a%b)                 #float value output

#** or pow
a=2**2

import math
print(pow(2,2))

#'*' in string repetation(any one must be str and one must be int)
a='Fareen'*3
     #OR
a=3*'Fareen'


#RELATIONAL OPERATOR OR COMPARISON(<,<=,>,>=,==,=,!)--------------------------------------------------------------------------------------------------------------------------------------
"""
ASCII VALUE
32-space
33-47- special character
0=48  9=57
a=97  z=122
A=65  Z=90

"""

#To get ascii value use ord() and chararcter related to ascii use chr()
print(ord('a'))
print(chr(97))

#string comparison
c='a'<'b'
print(c)

c='fareen'<'fareena'
print(c)

c='fareen'<'anamika'                         #False (it start comparing from first value 'a' is less than 'f')
print(c)

c='fareen'<'fanamika'                        #False
print(c)


#Comparing a list of values(it gives true if all condition is true ,but give false if any condtion fails)
a,b,c=1,2,3
c=a<b<c                                      #True
print(c)

a,b,c,d=1,2,3,0
c=a<b<c<d
print(c)                                     #False

c=' '>'a'                                    #False(ascii value of space is 32 and 'a' 97)
print(c)

#Equality operator(==,!=, identity operator(is and is not))--------------------------------------------------------------------------------------------------------------
"""
==(use to compare to content)
is(use to reference compare or address comparison)
"""
a=10
b=20
c=a==b
print(c)


#is and is not(order does not matter "a is b" OR "b is a" is same)
a=10
b=20
c=a is b                                    #False(address of a and b are different)
print(c)

a=10
b=10
c=a is b                                    #True
print(c)

a=10
b=a
c=a is b                                    #True
print(c)

#In case of list the id are different 
l1=[1]
l2=[1]
print(l1 is l2)           #False

#but in list id of every element is different, but the element which are same have the same id
a=[1,2,3,1,1,1]
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
print(id(a[4]))
print(id(a[5]))
"""
OP:
1597228033856
1597219694896
1597219694928
1597219694960
1597219694896
1597219694896
1597219694896

Here id of 0,3,4,5 position element has same id and rest all have different id
"""



#Python Assignment Operators(+=, -=, *=, //= and so on)-----------------------------------------------------------------------------------------------------------------------------
"""
+=
c += a is equivalent to c = c + a
-=
c -= a is equivalent to c = c + a
and so on
"""
a=10
b=10
b+=a
print(b)


#Python Bitwise Operators(& ,|, ~, ^, << Binary Left Shift, >> Binary Right Shift)------------------------------------------------------------------------------------------------
"""
this gives the binary calclation
1.AND(&)
 T,T = T (rest all F)

2.OR(|)
 F,F = F (rest all T)

3.XOR(^)
 T,T = F
 F,F = F  (rest all are true)

4.Compliment(~)
formula(~a = -a-1)
~True -> False

5.<< Binary Left Shift
formula-
value << no. of shifts
4 << 2
calcutaion--
binary of 4----------0 0 0 0 0 1 0 0

shift 2 zero         0 0 0 1 0 0 0 0----->16
(discard 2 zero from left and add 2 '0' in the right)

6.>> Binary Right Shift
formula-
value >> no. of shifts
4 >> 2
calcutaion--
binary of 4----------0 0 0 0 0 1 0 0

shift 2 zero         0 0 0 0 0 0 0 1----->1
(discard 2 zero from rght and add 2 '0' in the left)
(2**0=1)
"""

#Always add 0 to the number shifted
example:
bin(8): 0000 1000
8>>4
so it will be 0000 0000  (convert all the shifted nymbers to zero)
"""
answer :0
"""


#AND
a=20
b=4
c=a & b
print(c)
"""o/p--- 4
calculation--
&(T,T = T)
20 in binary is---0 0 0 1 0 1 0 0
4  in binary is---0 0 0 0 0 1 0 0
                 -----------------
                  0 0 0 0 0 1 0 0      --------> 4
"""

#xOR
a=20
b=4
c=a ^ b                                  #16
print(c)

#compliment(~)(flip the binary form of 0 to 1 and 1 to 0)
a=20
print(~a)                                #-21(according to formula -20-1=-21)
~True                                    #-2

#Left shift(<<) <-----left shift
4 << 2                                   #16

#Right shift(>>) ----->right side
4 << 2                                   #1


#Python Logical Operators(AND,OR,NOT)---------------------------------------------------------------------------------------------------------------------------------------------
"""
AND
if T,T = T (rest all F)

OR
if F,F = F (rest all T)

Logical Not(reverse)
"""

a=True         
b=False
c=a and b
print(c)                                  #False

a=True
print(not a)                              #False

bool(not 10)                              #False

bool(not ' ')                             #False

#Membership operstor(in and not in)-----------------------------------------------------------------------------------------------------------------------------------------------------
"""
a in b
 if a is the member of b

 a='fa'
 b='a'

 a is the superset of be
 so, b in a --> True
 and a in b --> False

 
"""

a='fareen'
c='a' in a                               
print(c)                                  #True

a='fareen'
c='a' not in a                               
print(c)                                  #False

'' in 'abc'                              #True

#Terniry operator------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
k=a if b else c
"""
a=20
b=30
c=10
k=a if b<c else c                         #10   
print(k)


#Operator Precedence
"""


highest priority----->() -left to r
1)	
**
Exponent (raise to the power)----->IMPORTANT (RIGHT TO LEFT)
exponent is RIGHT TO LEFT Eg:
2 + 3 ** 4 ** 2
here the output is 43046723 and not 6563 bcoz it is right to left


2)	
~ + -
Complement, unary plus and minus (ex:+4 or -4)(method names for the last two are +@ and -@)

3)	
* / % //
Multiply, divide, modulo and floor division

4)
+ -
Addition and subtraction

5)	
>> <<
Right and left bitwise shift

6)	
&
Bitwise 'AND'

7)	
^ |
Bitwise exclusive `OR' and regular `OR'

8)	
<= < > >=
Comparison operators

9)
<> == !=
Equality operators

10)
= %= /= //= -= += *= **=
Assignment operators--------------------->IMPORTANT(RIGHT TO LEFT)

11)
is is not
Identity operators

12)
in not in
Membership operators

13)
not or and
Logical operators

logical not ------------------------------------->IMPORTANT(RIGHT TO LEFT)

AND has associtivity more than OR
first AND then OR
"""
