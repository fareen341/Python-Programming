#Exception Handling
"""
1.Syntax error
2.Runtime error
  i)Runtime Error
  ii)ValueError
  iii)FileNotFoundError
  etc....

->Some unexpected,unwanted event that disturb the normal flow of the program are called as exceptions
->Handling exception does not mean fixing the error , it simply means avoiding Abnormal Termination of our program by defining alternative way

Eg:database connection
     open db conn
     read data from db <-------- if exception raised here the database will never closed, the program run first line and give runtime error
     close db conn
In this case our resource is wasting
We shoud not block and miss anything
"""

#DEFAULT EXCEPTION IN PYTHON
"""
Every exception in python is class
"""

#Python Exception Hirerchy(D drive png image)

#Customizing exception handling(try-except)
"""
1.it is not recommended to put every code in try-except block
2.only code which are risky which may give exception should be in try and catch block
"""

#1.it is not recommended to put every code in try-except block
try:
    print('Hello')
    print('Python')
    a=10
    b=0
    c=a/b
    print('This code will never run bcoz the moment exception come try will jump to except block that is why it is not recommended to put every code inside try-except block')
    print('I am wasted line')
except ZeroDivisionError as msg:
    print("Cannot divide by zero")

#2.only code which are risky which may give exception should be in try and except block
try:
    print('only risky code should be here, not recommended to put every code in here')
except ValueError as msg:
    print("Value error") 

#CONTROL FLOW IN TRY-EXCEPT
#1.if no exception then(NT)
try:
    print('stmt 1')
    print('stmt 2')
    print('stmt 3')
except ZeroDivisionError as msg:
    print("stmt 4")
print('stmt 5')
"""op---
stmt 1
stmt 2
stmt 3
stmt 5
"""
#2.if exception come at line 3 then(Normal Termination)
try:
    print('stmt 1')
    print('stmt 2')
    c=10/0
    print('stmt 3')
except ZeroDivisionError as msg:
    print("stmt 4")
print('stmt 5')
"""op---
stmt 1
stmt 2
stmt 4
stmt 5
"""
#if exception occured at exception line(Abnormal Termiantion)
try:
    print('stmt 1')
    print('stmt 2')
    c=10/0
    print('stmt 3')
except ZeroDivisionError as msg:
    print("stmt 4")
    print(int('hello'))
print('stmt 5')
"""op---During handling of the above exception, another exception occurred:
stmt 1
stmt 2
stmt 4
Traceback (most recent call last):
  File "D:\Python\practice.py", line 4, in <module>
    c=10/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Python\practice.py", line 8, in <module>
    print(int('hello'))
ValueError: invalid literal for int() with base 10: 'hello'
"""
#if exception occured outside the try-except block(AT)
try:
    print('stmt 1')
    print('stmt 2')
    c=10/0
    print('stmt 3')
except ZeroDivisionError as msg:
    print("stmt 4")
   
print(int('hello'))
print('stmt 5')
"""op---
stmt 1
stmt 2
stmt 4
Traceback (most recent call last):
  File "D:\Python\practice.py", line 9, in <module>
    print(int('hello'))
ValueError: invalid literal for int() with base 10: 'hello'
"""

#Printing the different info related to exception
"""
BaseException is the parent of all the exception class.
so parent can handle itself and childs too.

class = <class 'ZeroDivisionError'>
description = division by zero
"""
try:
    print('stmt 1')
    print('stmt 2')
    c=10/0
    print('stmt 3')
except BaseException as msg:
    print("Printing the description of exception:",msg)
    print("Exception type:",type(msg))
    print("The corresponding class object:",msg.__class__)
    print("Printing exception class name:",msg.__class__.__name__)
print('stmt 5')

                #OR
try:
    print('stmt 1')
    print('stmt 2')
    c=10/0
    print('stmt 3')
except ZeroDivisionError as msg:
    print("Printing the description of exception:",msg)
    print("Exception type:",type(msg))
    print("The corresponding class object:",msg.__class__)
    print("Printing exception class name:",msg.__class__.__name__)
print('stmt 5')
"""op---
stmt 1
stmt 2
Printing the description of exception: division by zero
Exception type: <class 'ZeroDivisionError'>
The corresponding class object: <class 'ZeroDivisionError'>
Printing exception class name: ZeroDivisionError
stmt 5
"""

#if spelling mistake in exception name(it will give name error but if we define user define exception with the same name we will not get any error)
try:
    print('stmt 1')
    print('stmt 2')
    c=10/0
    print('stmt 3')
except ArithmeticErroring as msg:
    print("Printing the description of exception:",msg)
    print("Exception type:",type(msg))
    print("The corresponding class object:",msg.__class__)
    print("Printing exception class name:",msg.__class__.__name__)
print('stmt 5')
"""op---
stmt 1
stmt 2
Traceback (most recent call last):
  File "D:\Python\practice.py", line 4, in <module>
    c=10/0
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Python\practice.py", line 6, in <module>
    except ArithmeticErroring as msg:
NameError: name 'ArithmeticErroring' is not defined
"""


#Example 2
try:
    first_value=int(input("Enter First Number:"))
    second_value=int(input("Enter Second Number:"))
    print("The Result:",first_value/second_value)
except BaseException as result:
    print("Exception Type:", type(result))
    print("Exception Type:", type.__class__)
    print("Exception Class Name:", result.__class__.__name__)
    print("Description of Exception:", result)
"""OP---
Enter First Number:1
Enter Second Number:two
Exception Type: <class 'ValueError'>
Exception Type: <class 'type'>
Exception Class Name: ValueError
Description of Exception: invalid literal for int() with base 10: 'two'
"""

#TRY WITH MULTIPLE EXCEPT TWO WAYS
"""
1.using different except blocks
2. using single line with different exception inside the parenthesis seperated by comma(we can take any number of exception but parenthesis is important)
------in this except the order of except block is important-----
    If except block is defined for only one exception, then parenthesis is optional, and if except block is defined for more than one except block, then parenthesis is mandatory.
    If we use parenthesis then as keyword must be outside the parenthesis.
"""
#1.using different except blocks----------------------
#first way(Two possiblity user can enter 0 or string)
try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number:"))
    print("The Result:",x/y)
except ZeroDivisionError as msg:
    print("Cannot divide by zero")
except ValueError as msg:
    print('Enter integer value only')

#Second way(the order of except block is important)
try:
    print(20/0)
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
"""op---
ArithmeticError

ArithmeticError is the parent of ZeroDivisionError
the priority will give to top to bottom so ArithmeticError will get the first priority bcoz it is on top.
so ZeroDivisionError will never run in this case, it will run if it is given on top of ArithmeticError
"""
try:
    print(20/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
"""op---
ZeroDivisionError
"""

#2. using single line with different exception inside the parenthesis seperated by comma.--------------
try:
    x=int(input("Enter First Number:"))
    y=int(input("Enter Second Number:"))
    print("The Result:",x/y)
except (ZeroDivisionError,ValueError) as exp:
    print("Exception:",type(exp))
"""op---
Enter First Number:1
Enter Second Number:0
Exception: <class 'ZeroDivisionError'>
"""

#DEFAULT EXCEPT BLOCK IN PYTHON
"""
1.if no other except block matches it'll run
2.print basic information liking printing
3.handle any type of exception
4.it is compulsory defined at last after all exception of python or it will give error
"""
#1.if no other except block matches it'll run
try:
    c=10/0
    print(c)
except FileNotFoundError as msg:
    print('File not found')
except IndexError as msg:
    print('Index Error')
except:
    print('This line will run bcoz no above given exception matches')
"""op---
This line will run bcoz no above given exception matches
"""

#2.print basic information liking printing
try:
    c=10/0
    print(c)
except:
    print('This line will run bcoz of exception')
"""op---
This line will run bcoz of exception
"""

#4.it is compulsory defined at last after all exception of python or it will give error
try:
    c=10/0
    print(c)
except:
    print('This line will run bcoz no above given exception matches')
except FileNotFoundError as msg:
    print('File not found')
except IndexError as msg:
    print('Index Error')
"""op--
error: default except must be at last
"""

#FINALLY, BLOCK IN PYTHON
"""
1.The moment control comes in try block, finally will always run no matter exception come or not
2.Useful for maintailning cleaning of code in try except block
3.useful in example like db close
4.only at one condition finally won't run if we give os._exit(0) before finally ,os._exit(0) shut down our PVM 

eg :
        open db conn
        read data from db <--------------------if exception come at this line the our database will never be close
        db close conn

        for this use finally block, so eg exception arise at reading databse so use finally which will close database conn
        finally:
        db close conn

It is not recommended to place a cleanup code inside the try block because there is no guarantee for the execution of every statement inside the try block.
And also, it is not recommended to place a cleanup code inside the except block, because if there is no exception then except block won't be executed.
We required someplace to define a cleanup code which executes irrespective of whether the exception raised or not raised and whether the exception is handled or not handled, the best place is nothing but a finally block.
The main purpose of the finally code is to maintain a cleanup code.

----Syntax

            try:
                 risky code
            except:
                handling code
            finally:
                cleanup code
"""

#Exception came(AT)
try:
    print('open db conn')
    print('read data from db')
    c=1/0
    print('close db conn')
except TypeError as te:
    print('Type error occured in your code')
finally:
    print('close db conn')
"""op---
open db conn
read data from db
close db conn
Traceback (most recent call last):
  File "D:\Python\practice.py", line 4, in <module>
    c=1/0
ZeroDivisionError: division by zero

"""

#No exception
try:
    print('open db conn')
    print('read data from db')
    c=1/0
    print('close db conn')
except ZeroDivisionError as te:
    print('Type error occured in your code')
finally:
    print('close db conn')    
"""op---
open db conn
read data from db
Type error occured in your code
close db conn
"""

#os._exit(0) vs Finally Block in python (only at one condition finally won't run if we give os._exit(0) before finally)
"""
OS._exit(0)
Here Zero represents the status Code.Zero means normal termination.
Non-zero means abnormal termination
The python virtual machine internally uses this status code.
Whether it is zero or non zero, there is no difference in the result of the program.
"""
import os
try:
    print("try")
    os._exit(0)
except ValueError:
    print("except")
finally:
    print("finally")
"""op---
try

"""

#DIFFERENCE BETWEEN FINALLY BLOCK AND DESTRUCTOR
"""
->Finally Block	
Finally block is meant for cleanup activities related to the try block, i.e., whatever the resources we opened as part of try block will be cleaned inside the finally block.
->Destructor
Destructor is meant for cleanup activities related to the object; whatever the resources related to the object should be deallocated inside the destructor which will be executed
before destroying the object.
"""

#CONTROL FLOW OF TRY-EXCEPT-FINALLY
#1.If there is no exception occur
try:
    print('statement-1')
    print('statement-2')
    print('statement-3')
except ValueError as v:
    print('statement-4')
finally:
    print('statement-5')
print('statement-6')
"""op--
then 1,2,3,5,6 will run normal termination:
statement-1
statement-2
statement-3
statement-5
statement-6
"""
#2.If an exception raised at the statement-2 and corresponding except block matched
try:
    print('statement-1')
    c=1/0
    print('statement-2')
    print('statement-3')
except ZeroDivisionError as v:
    print('statement-4')
finally:
    print('statement-5')
print('statement-6')
"""op---NT
statement-1
statement-4
statement-5
statement-6
"""
#3.If an exception raised at the statement-2 and the corresponding except block not matched
try:
    print('statement-1')
    c=1/0
    print('statement-2')
    print('statement-3')
except ValueError as v:
    print('statement-4')
finally:
    print('statement-5')
print('statement-6')
"""op-- AT
statement-1
statement-5
Traceback (most recent call last):
  File "D:\Python\practice.py", line 3, in <module>
    c=1/0
ZeroDivisionError: division by zero
"""
#4.If an exception raised at the statement-4 if an exception raised at the exception block
try:
    print('statement-1')
    c=1/0
    print('statement-2')
    print('statement-3')
except ValueError as v:
    d=1/0
    print('statement-4')
finally:
    print('statement-5')
print('statement-6')
"""op---AT
statement-1
statement-5
Traceback (most recent call last):
  File "D:\Python\practice.py", line 3, in <module>
    c=1/0
ZeroDivisionError: division by zero
"""
#5.If an exception raised at statements 5 or 6 then it is always abnormal termination.
try:
    print('statement-1')
    print('statement-2')
    print('statement-3')
except ValueError as v:
    print('statement-4')
finally:
    c=1/0
    print('statement-5')
print('statement-6')
"""op---
statement-1
statement-2
statement-3
Traceback (most recent call last):
  File "D:\Python\practice.py", line 8, in <module>
    c=1/0
ZeroDivisionError: division by zero
"""
       #OR
try:
    print('statement-1')
    print('statement-2')
    print('statement-3')
except ValueError as v:
    print('statement-4')
finally:
    print('statement-5')
    
c=1/0
print('statement-6')
"""op---
statement-1
statement-2
statement-3
statement-5
Traceback (most recent call last):
  File "D:\Python\practice.py", line 10, in <module>
    c=1/0
ZeroDivisionError: division by zero
"""
       #OR
try:
    print('statement-1')
    print('statement-2')
    print('statement-3')
except ValueError as v:
    print('statement-4')
finally:
    print('statement-5')    
    c=1/0
    
print('statement-6')
"""op--
statement-1
statement-2
statement-3
statement-5
Traceback (most recent call last):
  File "D:\Python\practice.py", line 9, in <module>
    c=1/0
ZeroDivisionError: division by zero
"""

#NESTED, TRY-EXCEPT-FINALLY BLOCK
"""
->We can take try-except-finally blocks inside the try or except or finally or else block. Hence nesting of try-except-finally blocks is possible.
        SYNTAX
        nested try
        try:
        stmt1
            try:
            stmt2
            except:
            stmt3
            finally:
            stmt4
        stmt5
        catch:
        stmt6
        finally:
        stmt7

        nested catch
        try:
        stmt1
        catch:
            try:
            stmt2
            except:
            stmt3
            finally:
            stmt4
        stmt6
        finally:
        stmt7

        nested finally
        try:
        stmt1
        catch:
        stmt6
        finally:
            try:
            stmt2
            except:
            stmt3
            finally:
            stmt4
        stmt7

nested else
try:
    print('try')
except:
    print('except')
else:
    try:
        print('else-try')
    except:
        print('else-except')
        
->The general risky code we have to take inside the outer try block and too much risky code we have to take inside the inner try block.
->Inside the inner try block if an exception is raised, then the inner except block is responsible to handle it; if it is unable to handle,
then the outer except block is responsible for handling it.

real life corona virus , example there is in all maharashtra, but mumbai is in higher risk so maharashtra is in try block and mumbai is inside the nasted try 

eg:
    try:
    use conn
        try:
        use conn:
        except:
        use postcore(other db)
        finally:
    except:
    stmt
    finally:
    stmt
"""
#nested try
try:
    print("outer try block")
    try:
        print("Inner try block")
    except ZeroDivisionError as e:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
"""op--
there is no execption in inner or outer block so ot is normal termination
outer try block
Inner try block
Inner finally block
outer finally block
"""

#case 1:If an exception is raised in the inner try block and the inner except block will match then
try:
    print("outer try block")
    try:
        print("Inner try block")
        a=1/0
    except ZeroDivisionError as e:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
"""op---
outer try block
Inner try block
Inner except block
Inner finally block
outer finally block
"""

#case 2:if exception is raised in the inner try block but the corresponding except block not matched
try:
    print("outer try block")
    try:
        print("Inner try block")
        int('python')
    except ZeroDivisionError as e:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
"""op---NA
outer try block
Inner try block
Inner finally block
outer except block
outer finally block
"""

#case 3:If an exception is raised in the outer try block
try:
    print("outer try block")
    int('python')
    try:
        print("Inner try block")
    except ZeroDivisionError as e:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")
"""op---
outer try block
outer except block
outer finally block
"""

#else,BLOCK WITH TRY-EXCEPT-FINALLY IN PYTHON EXCEPTION HANDLING
"""
There is no chance of executing both except block and else simultaneously If we want to use the else block then compulsory the except block should be there

try:
    Risky code
except:
    Handling code
    will be executed if an exception inside try
else:
    will be executed if there is no exception inside try
finally:
    cleanup code
    will be executed whether exception raised or not raised and handled or not handled

else will run if and only if there is no exception in try block ,then else will run
"""
#case 1: no error in try
try:
    print('try')
except ValueError as v:
    print('except')
else:
    print('else')
finally:
    print('finally')

"""op---
try
else
finally
"""
#case 2: error in try
try:
    print('try')
    int('python')
except ValueError as v:
    print('except')
else:
    print('else')
finally:
    print('finally')

"""op--
try
except
finally
"""

#case 3:try without except keyword and only with else , this will give error
try:
   print("try")
else:
     print("Else")
finally:
      print("Finally")                     #error


#practical eg:
file=None
try:
    file=open("info.txt","r")
except:
    print("Some problem while locating and opening the file")
else:
     print("File opened successfully")
     print("The data present in the file is:")
     print("#",*30)
     print(file.read())
finally:
    if file is not None:
        file.close()

#this will give error (but not when we tak "print('stmt')" in else)
try:
   print("try")
   
except ValueError as v:
     print("Else")
     
print('stmt')
finally:
      print("Finally")

#The Various Possible Combinations of try-except-else-finally Block
#1.only try(invalid)
try:
    print('try')
"""op---
error it must be with except or finally block
"""

#2.only except(invalid, try must be there)
except:
    print('except')
    
#3.try with else(invalid, for else along with try except must be there) 
try:
    print('try')
else:
    print('else')

#4.only finally(invalid , with finally try must be there)
finally:
    print('finally')

    #valid
try:
    print('try')
finally:
    print('finally')
    
#5.try-else-except(invalid, order is important (try-except-else-finally))
try:
    print('try')
else:
    print('else')
except:
    print('except')
    
#6.try-else-finally(invalid (for else except must be there))
try:
    print('try')
else:
    print('else')    
finally:
    print('finally')
    
#7.try-except and try-finally(valid(1st :try-except is one block, 2nd: try-finally is one block))
try:
    print('try')
except:
    print('except')

try:
    print('try')
finally:
    print('finally')

#8.more than one else(invalid(it can have more than one except but not else))
try:
    print('try')
except:
    print('except')
else:
    print('else')
else:
    print('else')

#9.more than one finally(invalid)
try:
    print('try')
finally:
    print('finally')   
finally:
    print('finally')
    
#10.try- with independent stmt -except(invalid, try-except is a single stmt, in this case try will become alone and except too)
try:
    print('try')
print('hello')
except:
    print('except')    

#11.try-except with independent stmt again except(invalid, bcoz of that independent stmt try-except become one stmt and except became alone)
try:
    print('try')
except:
    print('except') 
print('hello')
except:
    print('except')

#12.try-except with one independent stmt- else(invalid,bcoz of this try-except become one stmt and else became alone)
try:
    print('try')
except:
    print('except')
print('hello')
else:
    print('else')

#13..try-except with one independent stmt- finally
try:
    print('try')
except:
    print('except')
print('hello')
finally:
    print('finally')

#14.nested try-except-finally with else stmt(valid)
try:
    print('try')
except:
    print('except')
else:
    print('else')
    try:
        print('try')
    except:
        print('except')
    finally:
        print('finally')

    

#TYPES OF EXCEPTIONS IN PYTHON EXCEPTION HANDLING
"""
1.Predefined Exceptions(all BaseException are predifine exception)
    ->ValueError
    ->ZeroDivisionError
    etc....

2.User-Defined Exceptions
"""

#2.User-Defined Exceptions
"""
1.Every exception in python is a class, and it should be a child class of BaseException.
2.The TooYoungException is our exception class name, and it is the child class Exception, and we can raise an exception by using the raise keyword.
3.raise will stop the execution, the statements after raise will not run.

class TooYongException(Exception):
      def __init__(self,msg):
            self.msg=msg
The TooYoungException is our exception class name, and it is the child class Exception, and we can raise an exception by using the raise keyword.
"""
class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input("Enter Age:"))
if age<=17:
    raise TooYoungException("Please Wait some more time, definitely you will get chance to vote")
elif age>=18 and age<100:
   raise TooOldException("Now, you are eligible to vote")
else:
    print("As per the gov rules the age should 18 to participate in voting")
"""op--
it will raise error when if condition is True
Enter Age:101
As per the gov rules the age should 18 to participate in voting
"""

#it will raise error when if condition is True
x=1
y='fareen'
if x==1:
    raise ZeroDivisionError('Zero Division Error')
elif int(y):
    raise ValueError('Value error')
    print('else')

'''
print('else') won't run 
'''

#3.raise will stop the execution, the statements after raise will not run.
while 1:
    print('hello')
    raise ZeroDivisionError('zero error')
print('bye')


#Predefined Errors:


#TYPES OF ERROR--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
1.Syntax(parsing error) and sematic error(logical error)
2.Out of memory error
3.Recursion Error
4.Indentation Error
"""

#1.Syntax(parsing error) and sematic error
"""
occur when we give wrong typo.
semantic error:logical error and does not give error but the result is different
"""

#semantic error example:
x=10
y=20
average=x+y/2
print(average)
"""op---
the average should be 15 but bcoz of python precedence rule we got 20

this logical error can be solve using parenthesis
i.e (x+y)/2
"""


#2.Out of memory error
"""
->Unexpected Memory Error in Python
If you get an unexpected Python Memory Error and you think you should have plenty of rams available, it might be because you are using a 32-bit python installation.

->Loading a large dataset
Loading a large dataset directly into memory and performing computations on it and saving intermediate results of those computations can quickly fill up your memory
"""

#3.Recursion Error
"""
when we cross the recursion limit wjich is set by python(1000) it will give error:

    RecursionError: maximum recursion depth exceeded in comparison

to avoid this use:
1.iterative method(while loop)
2.increase the recursion limit(not recommended it may cause stack overflow)
"""

#CHANCES OF GETTING BUILD IN ERRORS:

#import error
"""
when the imported module not found
"""
import OS
print('before')
"""
ModuleNotFoundError: No module named 'OS'
"""

#Assertion error
"""
not used in preogram ,used for debugging
test condition and trigger an error when the condition is false
syntax:
 assert condition, optional message
"""
#handling assertion error
def age(y):
    try:
        assert age==0,'age cannot be zero'
        print(y)
    except AssertionError as e:
        print('assert error')

age(0)
print('hello')
"""
age cannot be zero
hello
"""

#
def age():
    try:
        assert True,'this will run'
        print('this will not run if above is true')
    except AssertionError as e:
        print('assertion error')
        print('bye')

age()
print('hello')


#Attribute error
s='fareen'
print(s.maximum())

"""error:

AttributeError: 'str' object has no attribute 'maximum'
"""

#assertion erros
def age(y):
        assert age==0,'age cannot be zero'
        print(y)
        
age(0)


#EOF Error
occur when press ctrl+D in input stmt
  
#NamaError
"""
when code refers a name that does not exist
"""
n=int(input('Enter number'))
print(k)
"""op---
it will run till line one and give name error on 2nd stmt
"""

#Lookup Error
"""
Somethig cant be find

1.Index error
2.Key error
"""
#1.Index error
l=[1,2,3]
print(l[4])

#2.Key error
k={1:'fareen',2:'ansari',3:'anamika'}
print(k[4])
"""
KeyError: 4
"""

#OS Error
"""
1.FileNotFound
2.Interrupted Error
3.Permission error
4.TimeOut error
"""

#1.FileNotFound
f=open('fareen','r')
"""
FileNotFoundError: [Errno 2] No such file or directory: 'fareen'
"""

#3.Permission error
f=open('D:/Python','r')
"""
PermissionError: [Errno 13] Permission denied: 'D:/Python'
"""

#TypeError
"""
when operation or function is applied of an inapproprite type
"""
c='2'+2
#
o='Python'
o.count(9)


#ValueError
"""
it is thrown when a function argument is of inappropriate type
"""
int('fareen')
"""
ValueError: invalid literal for int() with base 10: 'fareen'
"""

#Keyboard Interupt
"""
normally ctrl+c
"""
g=int(input('enter name:'))
"""
KeyboardInterrupt
"""

#SystemExit
import os

try:
    print('before')
    os.sys.exit()
    print('after')
except SystemExit as s:
    print('continue the program')
print('hello')
"""
before
continue the program
hello
"""

















































