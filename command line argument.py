#COMMAND LINE ARGUMENT
"""
->Without using input function,using command line.
->It always take string type.
always take string argument
indexing >>>test.py 10,20 
               0    1  2
import from sys module
->sys is a module and argv is a variable(which is present in sys module)
->argv is list type

Uses:
custimize the behaviour of application
eg: file merge application
    f1=open(argv[1])
    f2=open(argv[2])
    f3=open(argv[3])
    for x in f1:
        f3.write(x)
    for x in f2:
        f3.write(x)

Output: work even if the file name changes
no need to hardcode

from sys import argv
print(argv[0])


->py test.py 10 20
      |       |
      |     arg[1] and so on
      |
      first argument arg[0]

"""

from sys import argv
print(argv[0])
"""op--
example.py
"""

#Printing info of command line arguments
from sys import argv
print (argv[0])
print(argv[1])
print(argv[2])
print('Length of argv',len(argv))
print('List of args',argv)
for x in argv:
    print(x)
"""op--
D:\Python>py sample3.py 10 20
example.py
10
20
Length of argv 3
List of args ['sample3.py', '10', '20']
sample3.py
10
20
"""

#USing sys
import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print('Length of argv',len(sys.argv))
print('List of args',sys.argv)
for x in sys.argv:
    print(x)
"""same output as above"""

#It always take string type.
from sys import argv
c=argv[1]+argv[2]
print(c)
"""op---
D:\Python>py sample3.py 10 20
1020
"""

#convert to int type
from sys import argv
c=int(argv[1])+int(argv[2])
print(c)

print(type(c))
"""op---
D:\Python>py sample3.py 10 20
30
<class 'int'>
"""

#(to consider fareen ansari as one argument put it inside double quotes)
from sys import argv
print(argv[1])
"""op---
->it consider single quote as seperate argument
D:\Python>py sample3.py 'fareen ansari'
'fareen


->D:\Python>py sample3.py fareen ansari
                            |    |
                            |   2nd argument
                            first argument

->Using double quote
D:\Python>py sample3.py "fareen ansari"
fareen ansari
""" 

#Use of command line argument:
"""
file merger application

f1=open(file1.txt)
f2=open(file1.txt)
for x in f1:
    f3.write(x)
for x in f2:
    f3.write(x)
(this program is only available for file1 and file2, if other day the file name changes we need to update the program)
instead use command line argument:

f1=open(argv[1])
f2=open(argv[2])
for x in f1:
    f3.write(x)
for x in f2:
    f3.write(x)
(customize the behaviour of appln)

"""

#Index error
from sys import argv
print(argv[100])
"""op--
D:\Python>py sample3.py "fareen ansari"
Traceback (most recent call last):
  File "D:\Python\sample3.py", line 2, in <module>
    print(argv[100])
IndexError: list index out of range
"""





















