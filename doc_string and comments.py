#COMMENTS AND WHITE SPACE

#invalid() (in this case if become one stmt and print() become one stmt)
if True:
print('true')

#valid
if True:print('True')

#valid
if True:
                                        print('True')

#valid
def sum(x,y):return x+y
k=sum(1,1)
print(k)

#valid
#one tab
if 1:
    print('false')

#one space
if 1:
 print('false')


#DOCUMENTATION STRING IN PYTHON
"""
->The doc string line should begin with a capital letter and end with a period.
->The first line should be a short description.
->If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.
"""

#documentation on build in function
print(max.__doc__)
"""
max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its biggest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more arguments, return the largest argument.

>>> help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
"""

#dir() vs help()
'''
dir()
returns members related to that module in list(including function,variable,methods)
'''

#
dir(10)
'''
this dir gives the member related to int function
dir(str,int,float,bool)
'''

#help
help(math)
provide the documantation


#documemtation on user define module
'''
    # name= This is the calculation module, which can perform basic calculation operatios.
    
    # description = Like add and subtract
'''

a=10
b=20


def add(a,b):
    '''
    This function adds numbers.
    It has two arguments a,b.
    '''
    print(a+b)

def sub(a,b):
    '''
    This function subtracts numbers.
    It has two arguments a,b.
    '''
    print(a-b)


__author__='fareen'
__cpoyright__='copy right'

"""op--
import calc
help('calc')

============================= RESTART: D:\Python\sample3.py =============================
Help on module calc:

NAME
    calc

DESCRIPTION
    This is the calculation module, which can perform basic calculation operatios.
    Like add and subtract

FUNCTIONS
    add(a, b)
        This function adds numbers.
        It takes two arguments a,b.
    
    sub(a, b)
        This function subtracts numbers.
        It takes two arguments a,b.

DATA
    __cpoyright__ = 'copy right'
    a = 10
    b = 20

AUTHOR
    fareen

FILE
    d:\python\calc.py
"""

#Documentation related to particular member
print(calc.add.__doc__)
"""op---

     This function adds numbers.
     
     It takes two arguments a,b.
"""


#getting documentation using doc
print(add.__doc__)
"""op--

     This function adds numbers.

     It takes two arguments a,b.
"""

#getting documentation using help

print(help(add))
"""op---
Help on function add in module __main__:

add(x, y)
    This function adds numbers.

    It takes two arguments a,b.
"""



#doc string in python using pydoc(python documentation tool)-----------------------------------------------------------------------------------------------------------------
"""
-->when running help() on cmd it wont recognize for this use pydoc -m
-->without using import we got documentation of any module
D:\Python>help(math)
This command is not supported by the help utility.  Try "(math) /?".

D:\Python>import math
'import' is not recognized as an internal or external command,
operable program or batch file.

"""


##Documentation -m pydoc
'''
D:\Python>py -m pydoc
pydoc - the Python documentation tool

pydoc <name> ...
    Show text documentation on something.  <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package.  If <name> contains a '\', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.

pydoc -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.

pydoc -n <hostname>
    Start an HTTP server with the given hostname (default: localhost).

pydoc -p <port>
    Start an HTTP server on the given port on the local machine.  Port
    number 0 can be used to get an arbitrary unused port.

pydoc -b
    Start an HTTP server on an arbitrary unused port and open a Web browser
    to interactively browse documentation.  This option can be used in
    combination with -n and/or -p.

pydoc -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '\', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.
'''

#pydoc <name>

D:\Python>py -m pydoc calc
'''
Help on module calc:

NAME
    calc

DESCRIPTION
    This is the calculation module, which can perform basic calculation operatios.
    Like add and subtract

FUNCTIONS
    add(a, b)
        This function adds numbers.
        It takes two arguments a,b.

    sub(a, b)
        This function subtracts numbers.
        It takes two arguments a,b.

DATA
    __cpoyright__ = 'copy right'
    a = 10
    b = 20

AUTHOR
    fareen

FILE
    d:\python\calc.py
'''

            #OR

D:\Python>py -m pydoc calc.add
'''
Help on function add in calc:

calc.add = add(a, b)
    This function adds numbers.
    It takes two arguments a,b.
'''

#pydoc -k <keyword>
'''
D:\Python>py -m pydoc -k calc
calc
'''

#pydoc -p <port>
D:\Python>py -m pydoc -p 9999
'''
Server ready at http://localhost:9999/
Server commands: [b]rowser, [q]uit
server>
'''
                #OR

D:\Python>py -m pydoc -p 0
'''
Server ready at http://localhost:64307/
Server commands: [b]rowser, [q]uit
server>

click b and you will see the list of all modeules and everything on browser
'''

#pydoc -w <name>(to save the documentation in html)

D:\Python>py -m pydoc -w calc
'''
wrote calc.html

'''

