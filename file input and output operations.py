#File Handling
"""
useful for storing data like entering students name,age,gender.. in case without file these data will be lost after program closed 


1)Text File(.txt)
2)Binary File(.rtf)
    ->image
    ->video
"""

#HOW TO CREATE OR OPEN A TEXT FILE?
"""
open() function
open function returns a pointer to the beginning of the file, this is called file handler or file object

syntax:
        open('filename',mode='',buffering,encoding=None,errors=None,newline=None,closefd=True,opener=None)
        1.file                   - required
        2.mode                   - default(read mode)
        3.buffering              - default if not given
        4.encoding               - default(None)
        5.errors                 - default(None)
        6.newline                - default(None)
        7.closefd                - default(True)
        8.opener                 - default(None)        
        
open('filename(with path option if file availabe in same dir)', mode)   default mode is 'r'
"""
#default keyword argument in given sequence only(if anything is not specify it will take default value)
open('stu.txt','r',1,'utf-8')

#keyword argument in any sequence as long as keyword is defined
f=open(buffering=1,encoding='utf-8',mode='r',file='stu.txt')
print(f)

#valid(bcoz default argument is given first then keyword argument)
f=open('stu.txt','r',encoding='utf-8',buffering=1)

#not-valid(non-keyword argument is given first)
f=open(name='stu.txt','r',encoding='utf-8',buffering=1)
"""error:
positional argument follows keyword argument
"""

#the given keyword should not be blank(if we dont write "mode=''" it will take default r mode)
f=open('stu.txt',mode='',buffering=1,encoding='utf-8',errors=None,newline=None,closefd=True,opener=None)
print(f)
"""error:
mode cannot be blank
"""

#WRITING DATA TO FILE
"""
write()
->if file not exist it will create file itself with given name
->overwrites the data
->it returns the number of character written
->start overwriting from the blinking cursur(file handler or object) which is from the starting
->write only take string(write() argument must be str, not int)
Syntax:
        file_object.write(string)
        file_object-file which we opened
"""

#number of character print
f=open('stu.txt','w')
n=f.write('Hello')
print(n)
f.close()
"""op---stu.txt
Hello


op---
5
"""

#write() and writelines()
'''
write() takes only string argument no other arguments are allowed not even int,list,bool etc
writelines() takes list,tuple,set ,dict which have only str data no other are allowed
both takes only str datatype no other data type they takes
and they cannot be blank or gives error
'''

#\n is one character too
f=open('stu.txt','w')
n=f.write('Hello\n')
print(n)
f.close()
"""op---
6
"""

#start overwriting from the blinking cursur(file handler or object) which is from the starting
f=open('stu.txt','w')
f.write('Python')
f.close()
"""op---stu.txt
Python

we overright the above program so now Hello is overwritten by Python
"""

#Space newline \n in write mode
f=open('stu.txt','w')
f.write('Python\n')                                    #for newline
f.write('Java                      C++')               #for space
f.write('C++')
f.close()
"""stu.txt
Python
Java                      C++
"""

#exculsive(x) IT IS USED TO CREATE A NEW FILE, IF FILE EXIST ALREADY, THEN IT FAILS('x')
"""
->it needs file which does not exist(new file)
"""
f=open('stu1.txt','x')
f.write('Hello ')
f.write('Python')
f.close()
"""stu1.txt
Hello Python
"""

#running the same file again gives error (file exist)

#APPEND DATA IN YOUR FILE('a')
"""
->if file not exist it create the file with the given data
->It does not overright the data it append text at the end
"""

f=open('stu1.txt','a')
f.write('Hello')
f.close()
"""stu1.txt
Hello
"""

#running the same file again will append the particular given text at the end of the above given text "Hello"
"""stu1.txt
HelloHello
"""

#READING FILES

#By using for loop you can read a text file in python. It will print the whole file. Let’s see how to do it-

#read(),readline() tell() and seek() METHODS IN PYTHON
"""
->This method is usefull for find the current position of the file pointer from beginning of the file, position starts from 0.->
->usefull when u want to append the data , so before appending check the cursor pointer.
"""

#read()(read single character)
"""
>read from the current curser point starts with blinking cursur
>if nothing is given inside parenthesis or negative value it will print entire file
>if file not exist gives error
"""

"""
number.txt has
12345
6789
"""
f=open('number.txt','r')
r1=f.read(7)
print(r1)

print()
r2=f.read(3)
print(r2)
"""op---
12345
6

789

first 7 character will be printed +1 for new line ,now curser is at point before 7 so the next 3 character will be printed.
"""
#readline()(read the whole line)
"""
only read data in a single line
number.txt
12345
6789
print the output along with a new line \n
"""
f=open('number.txt','r')
r1=f.readline()
print(type(r1))
print(r1)
"""op--
<class 'str'>
12345

"""

#
"""
now number.text has only one line so it won't go to new line
number.txt
12345
"""
f=open('number.txt','r')
r1=f.readline()
print(type(r1))
print(r1)
"""op---
<class 'str'>
12345
"""

#readline with parameter (only read data in a single line)
f=open('number.txt','r')
r1=f.readline(9)
print(type(r1))
print(r1)

#readlines() 
"""
read the whole lines and returns a list
"""
f=open('number.txt','r')
r1=f.readlines()
print(r1)
"""op--
['12345\n', '6789']
"""

#
f=open('file.txt','r')
r=f.readlines()
for i in r:
    print(i)

"""op---
Python

Jupyter

Java

C#

space is bcoz after Python there is one \n
as in:
l=['f\n','y\n']
for i in l:
    print(i)

    op---
    f

    y
    
"""

#tell()
"""
tells the cursor position

number.txt
12345
6789
000
"""
f=open('number.txt','r')
r1=f.read(13)
print(r1)
print(f.tell())
"""op--
12345
6789
00
15
"""

#seek()
"""
takes the cursor position to particular given place

number.txt
12345
6789
000


for new line add 2 then print data, for the same line no need to add
"""
f=open('number.txt','r')
print(f.seek(8))
print(f.tell())
print(f.read())
"""op---
8
8
789
000
first the cursor position is at 0 after seek it takes cursor to 2.
"""

f=open('number.txt','r')
print(f.seek(8))
print(f.tell())
print(f.read())

print()
print(f.seek(2))
print(f.read())
"""op---
8
8
789
000

2
345
6789
000
"""

f=open('number.txt','r')
f.seek(2)                #for same line 
print(f.read())

print()
f.seek(8)         
print(f.read())
"""op--
345
6789
000

789
000
"""

#example:
"""
number.txt
hello!!!
this is python file
hope you are ok
"""
f=open('number.txt','r')
f.seek(2)               
print(f.read())

print()
f.seek(8)         
print(f.read())

print()
f.seek(10)         
print(f.read())

print()
f.seek(31)         
print(f.read())
"""op---
llo!!!
this is python file
hope you are ok


this is python file
hope you are ok

this is python file
hope you are ok

hope you are ok
"""

#r+(first read and then write)
"""
->it does not create new file ,give error if file not found
file.txt
Python

first the program read Python now the cursor is pointing to Python| then it will start writing from cursor point.

points to remember:
in case of write it overwrite all the data
in case of r+ it will start with cursur point and start overwriting
f=open('prac.txt','r+')
f.write('A')
o=f.read()
print(o)
f.close()

adter executing the avove program prac.txt will be Arogramming ,it does not overwrite the whole file unlike in w mode 

prac.txt
Programming

after execution the below program it will be
PythonProgramming
"""
#
f=open('file.txt','r+')
r=f.read()
f.write('Programming')
f.close()
print(r)
"""op--
PythonProgramming
"""

#w+(first write then read)
"""
write always overwrite

file.txt
Python
"""
f=open('file.txt','w+')
r=f.read()
f.write('\nIs a great language')
print(r)
f.close()
print(r)
"""op--


we got blank output bcoz w+ first then read while writing the cursur point is moving from Is till 'e' of language and it will now point on 'e' after e there is nothing
so we got blank output
"""
#
f=open('file.txt','w+')
r=f.read()
f.write('Is a great language')
print(f.tell())
print(r)
f.close()
print(r)
"""op--
19


"""

#use seek to print data in w+
f=open('file.txt','w+')
f.write('Is a great language')
f.seek(0)
r=f.read()
print(r)
f.close()
"""op--
Is a great language
"""

#a+(append and then read)
"""
file.txt
Is a great language
"""
f=open('file.txt','a+')
f.write('Easy for beginners')
r=f.read()
print(r)
f.close()
"""op--


same we got blank screen ,cursur position in append is at the end of the written line so appending starts at 'e' of language and cursor stops at 's' of bignners so we got blank op.
file.txt
Is a great languageEasy for beginners
"""

#using seek in a+
f=open('file.txt','a+')
f.write('Easy for beginners')
f.seek(0)
r=f.read()
print(r)
f.close()
"""op--
Is a great languageEasy for beginners

file.txt
Is a great languageEasy for beginners
"""

#PRINTING INFO USING IN-BUILD FUNCTION AND VARIABLE
#variable(f.name,f.mode,f.encoading) functions(f.close,f.readable(),f.writable())
f=open('nnnn.txt','r+')
print('name:',f.name)
print('name:',f.mode)
print('writabe:',f.writable())
print('readable:',f.readable())
print('encoading:',f.encoding)
f.close()
'''
name: nnnn.txt
name: r+
writabe: True
readable: True
encoading: cp1252
'''

#with STATEMENT IN FILE HANDLING
"""
->it is used while opening a file
->when we open a file using with stmt there is no need to close the file explicitly.
 SYNTAX:
      with open('filename','mode') as file_object:              mode default is read
      stmt
"""
with open('file.txt','r') as f:
    r=f.read()
    print(r)
    print(f.closed)
print(f.closed)
"""op--
Is a great language
False
True


1nd stmt gave false bcoz we are still in file
"""


#BINARY FILES--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ZIPPING AND UNZIPPING...(zipfile module, have class : ZipFile)
'''
BY creating the object of the ZipFile we can zip and unzip our files...

my_zipfile = zipfile.ZipFile("F:/NewZipfile.zip", mode='w', compression=zipfile.ZIP_DEFLATED)
f=ZipFile('MyTextFile.zip','r',ZIP_STORED)


1.FILENAME
2.MODE
3.COMPRESSION --> default (ZIP_STORED)

'''
from zipfile import *
f=ZipFile('MyTextFile.zip','w',ZIP_DEFLATED)
f.write('PythonSite.txt')
f.write('questions.txt')

print('Zip file created successfullt!!!')
"""op---
Zip file created successfullt!!!
"""

#unzipping and reading the content of the file
from zipfile import *
f=ZipFile('MyTextFile.zip','r',ZIP_STORED)
names=f.namelist()
for x in names:
    print('File name:',name)
    print('Content of this file:')
    f1=open('name','r')
    print(f1.read())
    f1.close()
    print()


#BINARY DATA------------------------------------------------------------------------------------------------------------------------------------------------
'''
modes in binary: rb,wb,ab,r+b,w+b,a+b,xb
 To handle binary data use bytes,bytearray

 for image .jpg
 for audio mp4
 for video

 to perform more operation in python use pillow library
 
'''
f1=open('flower.jpg','rb')
data=f1.read()
f2=open('new_flower.jpg','wb')
f2.write(data)
f1.close()
f2.close
print('new image is available:')
'''op---
new image is available:
'''


#DELETING THE FILE-----------------------------------------------------------------------------------------------------------------------------------------
import os
os.remove('number.txt')





































