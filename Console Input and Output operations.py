#Input statement and Output stmt
"""
input ---> input method
output---> print() method
"""
#Output stmt
'''
print()

print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
a=input("Enter numer 1:")
b=input("Enter numer 2:")
print(a+b)
"""o/p--
Enter numer 1:10
Enter numer 2:20
1020"""

#input always take str value
'''
If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
'''

print("Enter your name:")
x = input()                                           #Hello fareen
print("Hello, " + x)

#eval(this function convert user data type into the given data type)
a=eval(input("Enter a number:"))
print(a,type(a))                                      #Enter a number:5

                                                      #5 <class 'int'>

#taking 2 user input using single line
#1.using default split value
a,b=[int(x) for x in (input('Enter 2 numbers:')).split()]
print(a+b)
#1.using comma split value
a,b=[int(x) for x in (input('Enter 2 numbers:')).split(',')]
print(a+b)

#output statement(print)-------------------------------------------------------------------------------------------------------------------------------------------------------------
#1.blank line space
print('hello')
print()
print('python')
"""o/p:
hello

python"""

#2.escape character
print('py'+'thon')
print('Hello'*3)
"""o/p---
python
HelloHelloHello"""

#3.take space after every argument by default print has space ( sep=' ') and one new line(end='\n')
a,b,c=1,2,3
print(a,b,c)                                     #1 2 3

#4.Sep(seperator, which seperate values by provided seperator)
a,b,c=1,2,3
print(a,b,c,sep=':')                             #1:2:3

a,b,c=1,2,3
print(a,b,c,sep='#')                             #1#2#3

print(1,2,3,sep='')                              #123

#end attribute(default \n)
a,b,c=1,2,3
print(a,b,c,end=':')                             #o/p---1 2 3:5 6 7
print(5,6,7)

print('hello' end='')                            #hellopython
print('python')

#using sep and end together
a='python'
b='java'
print(a,b,sep='&',end='***')
print('are great',end='***')
print('language')                                #o/p---python&java***are great***language

#Python(object)= can be list ,tuple,set
l=[10,20]                                        #o/p---[10, 20]
print(l)

