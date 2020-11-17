"""Slicing---------------------------------------------

         -ve         -6  -5  -4  -3  -2  -1
        STRING=       P   Y   T   H   O   N
         +ve          0   1   2   3   4   5

Syntax
(begin,,end,step)
Step decide whether to move forward or backword direction
eg--(1:5:2)-----
1.move forward direction
2.minus -1 to end i.e (end-1)

eg--(1:5:-2)-----
1.move backword direction
2.add +1 to end i.e (end+1)

In forward always move no matter -ve and +ve index   ,default value is(0,len-1,1)       -------------> 
In backward always move no matter -ve and +ve index                                     <-------------

Points to remember--
1.end and step can never be zero
2.slicing never give index error

Indexing------------------------------------------------
It have be -ve and +ve as well

"""

#Indexing
a="python"
print(a[0])
print(a[-1])

#DEfault value of backword direction is eg---
a="python"
print(a[-1: :-1])
print(a[ :-7:-1])

#Slicing
a="python"
print(a[0:-1:2])
print(a[-5:-1])

print(a[-1:-5])                #Error(bcoz it is forward direction we cannot move backword)
print(a[-6:-2:-1])             #Error(bcoz it is backword direction we cannot move forward)

a="programming" 
print(a[6:2:-1])               #o/p---marg
print(a[-6:-2:1])              #o/p---ammi




#Program examples------------------------------------------------------------------------
#To get the last 3 letters in the string "programming"
a="programming"
print(a[8: ])
print(a[-3: ])

#To skip the first and last character
a="programming"
print(a[1:-1])
print(a[1:10])

#To print the last 3 letter in reverse direction
print(a[-1:-4:-1])
print(a[ :-4:-1])

#To print the whole string in reverse direction
a="python"
print(a[-1: :-1])
print(a[ :-7:-1])
print(a[5: :-1])
print(a[ : :-1])

#Using step 2 in backward
a="PythonProgramming"            
print(a[ : :-2]) 

#slicing in multi line string
a='''hello
Python'''
k=a[0:7]
print(list(k))
print(k)
'''
including one \n for new line
['h', 'e', 'l', 'l', 'o', '\n', 'P']
hello
P
'''

