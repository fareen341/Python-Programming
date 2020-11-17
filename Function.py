#function
"""
1.defining the function
2.calling the function
You can call a function by using the following types of formal arguments −
Required arguments
Keyword arguments
Default arguments
Variable-length arguments

def fun(parameter)
    stmt

fun(argument)
"""
#Local and global variable
#local
def fun():
    a=10
    print(a)

fun()
print(a)
"""op---
10
NameError: name 'a' is not defined
"""

#global
global a
a=5
def fun():
    a=10
    print(a)                            #op---10,5

fun()
print(a)

#declaring global function inside local function
def fun():
    global a
    a=10
    print(a)                           #op---10,10

fun()
print(a)


#Required arguments
"""
the given amount of argument is required or it will give error
"""
def input_str(str):
    print (str)                         #TypeError: input_str() missing 1 required positional argument: 'str'
input_str()

def input_str(str):
    print (str)                         #op-- fareen
input_str('fareen')

#Keyword arguments
"""Keyword arguments are related to the function calls.
When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name."""

def stu_detail(name,roll_no,age,gender):
    print (name,roll_no,age,gender)
stu_detail(gender='female',name='fareen',roll_no=1,age=22)
"""op---
fareen 1 22 female"""

#Points to remember
"""default parameter should not come before required parameter"""
def fun(a=10,b):
    print(a+b)

fun(1,1)
"""
error: non default argument follows default argument
"""


#Default arguments
"""A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument."""

def stu_detail(name,age='18'):
    print (name,age)
stu_detail(name='fareen')                 #calling       op----fareen 18

#Variable-length arguments
"""You may need to process a function for more arguments than you specified while defining the function.
These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.
useful when no. of argument is unknown
TYpe of Variable-length arguments is TUPLE
it can name anything tho *args is best practice cuz it is easily recognizable that the function is Variable-length arguments,same with **kwargs
"""
#
def stu_marks(*args):                    #*args can be anything name,student, employee
    print(type(args))
    for i in args:
        print(i)
        
stu_marks(100,200,300)  
"""op---
<class 'tuple'>
100
200
300
"""

#Using Many Named Arguments with **kwargs
"""
gives output in dict
usefull when required multiple name arguments
"""
def stu_marks(**kwargs):
    print(kwargs)

stu_marks(python='200')
stu_marks(java='300',Cpp='200')
"""op---
{'python': '200'}
{'java': '300', 'Cpp': '200'}
"""

#Combining Varargs and Keyword Arguments
def stu_marks(*args,**kwargs):
    print(args)
    print(kwargs)

stu_marks(1,2,3,python='200')                    #*args value should come first the **kwargs according to the parameter given
"""op---
(1, 2, 3)
{'python': '200'}
"""

#changed order gives error it must be (*args,**kwargs)
def stu_marks(**kwargs,*args):
    print(args)
    print(kwargs)

stu_marks(python='200',1,2,3)

#Unpacking Arguments with *args and **kwargs
l=[1,2,3]
def add(x,y,z):
    print(x+y+z)                                 #op---6

add(*l)


#The Anonymous Functions(or lambda functn)
"""
1.one time use
2.nameless
3.keyword lambda

x=lambda x:x*x
print(2) |:|*|
         |:|*|
         |:|*|
         2 2 2

y=lambda x,y:x*y
print(y(2,3))         so x=2,y=3
lambda input_args:expression
lambda n:n*n
"""
def sqrt(n):
    print(n*n)
    
    #both are same
    
s=lambda n:n*n
print(s(2))
sqrt(2)

#1.Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
#2.An anonymous function cannot be a direct call to print because lambda requires an expression
s=lambda n:n+n
print(s)                          #op---<function <lambda> at 0x000002F1E1AB3F70>
"""
always using expression inside print bcoz it return value in the form of expresssion
i.e :print(s(2))"""

#Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.
s=lambda n:n+n
print(s(2))
print(n)
"""op--
4
NameError: name 'n' is not defined
"""

#return
"""
return always return to the function call
it terminates the function
def fun(x,y):
     return x+y-------------------
                                  |
fun(2,3)<-------------------------

1.The python return statement is used in a function to return something to the caller program.
2.We can use the return statement inside a function only.
3.In Python, every function returns something. If there are no return statements, then it returns None.
4.If the return statement contains an expression, it’s evaluated first and then the value is returned.
5.The return statement terminates the function execution.
6.A function can have multiple return statements. When any of them is executed, the function terminates.
7.A function can return multiple types of values.
8.Python function can return multiple values in a single return statement.
"""
#1.The python return statement is used in a function to return something to the caller program.
#2.We can use the return statement inside a function only.
def fun(a,b):
  return a+b                  #this 1+1 go to the caller and assign this value to x and then print x

x=fun(1,1)
print(x)

#3.In Python, every function returns something. If there are no return statements, then it returns None.
def fun(a,b):
  print(a+b)

x=fun(1,1)                    #in this case nothing is returning so python show none in output
print(x)

"""op--
2
None
Without a return stmt a function cannot communicate back to the caller of the function.
Therefore a variable cannot receive a value from a function
A return stmt replaces the function call with the return value."""

#
def foo():
  pass
print(foo())                  #op---none

#4.If the return statement contains an expression, it’s evaluated first and then the value is returned.
def fun(x,y):
  return x+y

print(fun(1,2))
x=fun(2,2)
print(x)

#5.The return statement terminates the function execution.
def fun(x,y):
  return x+y
  print('this is function')    

x=fun(1,1)
print(x)
"""op---
2
print function will not print bcoz the return statement terminates the function execution
"""

#condition below the return terminate so it does not even gives error
def fun():
    return 'hello'
    oifhoiehfeif

fun()
'''
no error bcoz return terminates
'''

#6.A function can have multiple return statements. When any of them is executed, the function terminates.
def fun(x):
  if x%2==0:
    return 'even'
  else:
    return 'odd'

x=fun(2)
print(x)
print(type(x))
"""op---
even
<class 'str'>
"""

#8.Python function can return multiple values in a single return statement.
def func(x,y,z):
  return x,y,z

a=func(1,2,3)                          #op--tuple of(1,2,3)
print(a)


#pass
"""
function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.
it returns none
"""
def myfunction():
    pass

#it returns none
def myfunction():
    pass

x=myfunction()
print(x)

#recursive function
"""
recursion function run in infinite loop but the limit is 1000
after printing 1000 times it will stop itself
"""
def fun():
    print('hello')
    fun()
    
fun()

#recursion limit
import sys
print(sys.getrecursionlimit())

#changing recursion limit
import sys
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())

#factorial using function
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)                            #120

s=fact(5)
print(s)


#Practical questions-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)                 
    
x = 50
func(x)
print('x is now', x)
"""
x is 50
Changed local x to 2
x is now 50
"""

#
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

print('x=', x)
x = 50
func(x)
print('x is now', x)
"""
NameError: name 'x' is not defined

according to sequence of execution print('x=',x) will execute first that is why we got error
"""

#
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

global x
x=20
x = 50
x=0
func(x)
print('x is now', x)
"""op---
x is 0
Changed local x to 2
x is now 0

x is taking the last value which is first the value of x was x=20,then x=50 now x=0 so 0 will be global now
"""

#
x = 50
def func():
    global x
    x = 2
    print(x)
    x=0
    x=1
    x=13
    print(x)
    print('Changed global x to', x)
func()
print('Value of x is', x)

#(in this case the last value will become the global)
x = 50
def func():
    global x
    print(x)
    x=0
    print(x)
    x=1
    print(x)
    x=13
    print(x)
    print('Changed global x to', x)
func()
print('Value of x is', x)
"""op---
50
0
1
13
Changed global x to 13
Value of x is 13

according to the sequence of execution the value of global x is changing ,first the value of global x is x=0 then x=1 then x=13 now x=13 is the global value of x
"""

#default keyword
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
 
func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)
"""op---
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50

until the keyword is define it will not give the error unlike in default argument where we have to give value according to the argument,
in default argument the first stmt itself throw the error(one missing argument)
"""

#type function(it takes only one value inside and return the type)
print(type(str(10)))                          #class str
print(type(type(10)))                         #class type
print(type(type(type(type(10)))))             #class type

#
print(chr(ord('A')))                          #first ord of A=97 then chr(97) so A will be printed


#NESTED FUNCTION
#case 1:(inner function recursion, in this case fun2 must be called)
def fun1():
    print('Hello')
    
    def fun2():
        print('Bye')
        fun2()
    fun2()
        
fun1()

#2.inner function can access the variables of outer function
def fun1():
    a=1
    print(a)
    
    def fun2():
        print(a)
    fun2()
fun1()

#3.print belongs to outer statement
def fun1():
    a=1
    print(a)
    
    def fun2():
        a=2
        print(a)
    fun2()
    
    print(a)
    
fun1()
'''
1
2
1
'''

#4.Recursion in inner function
def fun1():
    print('Hello')
    
    def fun2():
        print('Bye')
        fun2()
        
fun1()
'''
Hello

bcoz function 2 is not called, and it must be called inside function or gives error.
'''

#5.Inner function must be called inside of outer function, inner function has its scope only inside that particular function.
def fun1():
    print('Hello')
    
    def fun2():
        print('Bye')
    fun2()
    
fun1()

#6.printing outer statement before calling inner function
def fun1():
    print('Hello')
    
    def fun2():
        print('Bye')
    print('Hii')
    fun2()
    
fun1()
'''
Hello
Hii
Bye
'''

#guessing the a value
a=20
def fun1():
    a=10
    print(a)
    
    def fun2():
        a=5
        print(a)
    fun2()
    
    print(a)
    
fun1()
print(a)
'''
10
5
10
20
'''

#we should not use return in outer statement bcoz return terminate the statement and come out of the function
def fun1():
    return 'out'
    def fun2():
        print('inn')
    fun2()
o=fun1()
print(o)
'''
out

inn will not printed bcoz the return statemnt terminated at line 2
'''

# this will print the inn statemnt bcoz return is after child function call
def fun1():
    def fun2():
        print('inn')
    fun2()
    return 'out'

o=fun1()
print(o)
'''
inn
out
'''

#an inner function can be the indentation of the outer statement
def fun1():
    def fun2():
        print('inn')

    fun2()
fun1()
'''
inn

here we did not give any statement to outer function still we got the op
'''

#same as above but without inner function
def fun():
fun()

#Invalid
a=20
def fun1():
    print(a)
    a=9
    print(a)

    
fun1()
print(a)

#invalid(only the parent can call the child function)
a=20
def fun1():
    print(a)

    def fun2():
        print(a)

        def fun3():
            print(a)
    fun3()
    
fun1()
print(a)
'''
bcoz fun2 is the parent of fun3 so it can only call in fun2.
'''

#
def fun(x,y):
    def fun2(a,b):
        return a+b
    return fun2(x,y)
print(fun(3,2))
'''
5
'''



