#int float and bool (juputer nootbook)
#int
int(10)                     #int
int(10.67)                  #float
int('python')               #string
int('10.78')                #string
int('199')                  #string with base 10
int(False)                  #bool


#float
float(1)
float(1.1)
float(True)
float('fareen')
float('NaN')                #nan
float('Inf')   #OR          #op--inf
float('inf')                #op--inf

#1.2-1.0=0.19999999999999996
'''
it is bcoz float calculate values to base 2
this can be solve by decimal module
'''

#Exponent and power
2**2=4
2.3**2=5.289999999999999
        #Or
pow(2.3,2)
pow(1.5,-1)
0.6666666666666666)

#bool
#only these condition will give false rest all are true
bool(0)
bool(False)
bool('')
bool()
bool(not True)
bool(0j)
import decimal
decimal.Decimal(0)
#bool of triple quote string
bool('''''')
#empty list tuple set and dict
bool()
bool([])
bool({})
bool(set())
bool(None)

#rest all are true including NaN
bool('NaN')
bool(bool)


#String Data Types
x="Python is great programming language"
y='Python is great programming language'
z='''Python is great
programming language'''   #Multiline string        
print(x)
print(y)
print(z)


"""two uses of multiline strings
1.to display multiline string
2.to display single or double quoted string(we can use \ too to display single or double quoted string)"""

#1
z='''Python is great
programming language'''   #Multiline string        
print(z)

#2
z='Python is \'great\' programming language'   
print(z)

z='''Python is \'great\' programming language'''
print(z)

z='''Python is 'great' "programming language"'''
print(z)

z='''Python is 'great(\tspeed\t)' \n"programming language"'''   #Adding tab(\t) and newline(\n)
print(z)

#RAW STRING (Raw strings do not treat the backslash as a special character at all. Every character you put into a raw string stays the way you wrote it)(r or R)
x="Python is great programming language sail by \neil"
print(x)
"""Output - Python is great programming language sail by 
eil"""

y=r'Python is great programming language said by \neil \u'
print(y)
         #OR   
y=R'Python is great programming language said by \neil \u'
print(y)

y='C:User\\n\t\done'
print(y)
""" OUtput-
C:User\n	\done"""


#Strings are immutable(cannot be modified)
x="Hello World!"
y=x[ :6]+"Python"
print(y)                          #O/P-Hello Python (but if u print the value of x it will be "Hello Python" bcoz strings are immutable, it simply makes the copy)


#To print the last character as capital
"""String has both positive and negative indexing
    -6 -5 -4 -3 -2 -1
str= f  a  r  e  e  n
     0  1  2  3  4  5"""

x="Hello World"
y=x[ :len(x)-1]+x[-1].upper()
print(y)                         #O/P-Hello WorlD


#STRING SPECIAL OPERATOR
#1.Concatination(+)

a="fareen"
b="ansari"
c=(a+b)
print(c)

#Repetition(*)
a="fareen"
b=(a*6)
   #OR
b=(6*a)
print(b)


#Indexing and slicing
#Index(getting index value)
a="fareen"                             #len=6 not including 0
y=(a[0])
z=(a[-1])
l=(a[len(a)-1]) 
print(y)
print(z)
print(l)

#Slicing(getting a range of value) [begin:end-1:step]
a="fareen"
y=a[ :6]                                 #default value of begin is 0
print(y)

y=a[0: ]                                 #default value of end is len-1
print(y)

y=a[ : :2]                               #step is to count after every given step eg- 0,1,2,3,4 and step is 2 output will be-0,2,4
print(y)

y=a[ : ]                                 #OUtput- fareen
print(y)

a="fareen"
print(a[-5:-2])                          #Negative slicing


#Membership( in and not in which gives boolean value)
a="fareen"
y="r" in a                 #True      
print(y)

a="fareen"
y="r" not in a             #False
print(y)

#String Modulo Operator(%s,%d,%f or %F,%c,%e or %E,g or %G)
a="""My name is %s and roll number %d
            and my name starts with %c and weight is %f""" %('fareen',1,'f',55.56)
print(a)
"""Output ---- (My name is fareen and roll number 1
            and my name starts with f and weight is 55.560000)"""

#%s can take any value int,float,bool ,list ,tuple,dict ,set
s='%s %s %s %s'%(10,4.9,[1,2,4],False)
print(s)


#%E or %e(exponent)
n='hello %e'%(0.0001)           #e-4
m='hello %E'%(100.000)          #E+2

#capital F gives capital inf
i=float('Inf')
s='%F, %f'%(i,i)                #'INF, inf'

#%g or %G(floating point or exponential point)
x=float('NaN')
s='%g, %G, %e, %E'%(x,x,x,x)
print(s)

i='expo:%f,%g'%(1.1,0.00000001)
print(i)
"""op---
nan, NAN, nan, NAN
expo:1.100000,1e-08
"""
#
s='%s,%d,%c,%f,%e,%g'%('fareen',9,'f',1.1,0000.01,10000.0)
print(s)
"""op--
fareen,9,f,1.100000,1.000000e-02,10000
"""

#Built-in String Methods

"""       
1	capitalize()
Capitalizes first letter of string

2	center(width, fillchar)
Returns a space-padded string with the original string centered to a total of width columns.

3	count(str, beg= 0,end=len(string))
Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.


6	endswith(suffix, beg=0, end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.

7	expandtabs(tabsize=8)
Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

8	find(str, beg=0 end=len(string))
Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.

9	index(str, beg=0, end=len(string))
Same as find(), but raises an exception if str not found.

10	isalnum()
Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

11	isalpha()
Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

12	isdigit()
Returns true if string contains only digits and false otherwise.

13	islower()
Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

14	isnumeric()
Returns true if a unicode string contains only numeric characters and false otherwise.

15	isspace()
Returns true if string contains only whitespace characters and false otherwise.

16	istitle()
Returns true if string is properly "titlecased" and false otherwise.

17	isupper()
Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

18	join(seq)
Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

19	len(string)
Returns the length of the string

20	ljust(width[, fillchar])
Returns a space-padded string with the original string left-justified to a total of width columns.

21	lower()
Converts all uppercase letters in string to lowercase.

22	lstrip()
Removes all leading whitespace in string.

23	maketrans()
Returns a translation table to be used in translate function.


25.partition()
26	replace(old, new [, max])
Replaces all occurrences of old in string with new or at most max occurrences if max given.

27	rfind(str, beg=0,end=len(string))
Same as find(), but search backwards in string.

28	rindex( str, beg=0, end=len(string))
Same as index(), but search backwards in string.

29	rjust(width,[, fillchar])
Returns a space-padded string with the original string right-justified to a total of width columns.

30	rstrip()
Removes all trailing whitespace of string.

31	split(str="", num=string.count(str))
Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.

32	splitlines(self, /, keepends=False)
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

33	startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

34	strip([chars])
Performs both lstrip() and rstrip() on string.

35	swapcase()
Inverts case for all letters in string.

36	title()
Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

37	translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing those in the del string.

38	upper()
Converts lowercase letters in string to uppercase.

39	zfill (width)
Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).

40	isdecimal()
Returns true if a unicode string contains only decimal characters and false otherwise."""


s='Fareen'
print(s.capitalize())
s='fareen'
print(s.casefold())
s='Fareen'
print(s.center(20))
s='Fareen'
print(s.count('e'))
s='Faree@'
print(s.encode())
s='Fareen'
print(s.endswith('n'))
print(s.startswith('F'))
s='Fareen\tAnsari'
print(s.expandtabs(20))
s='Fareen'
print(s.find('n'))
s='My name is {:s}, roll no:{:d}, weight{:f}'
print(s.format('fareen',1,49))
s='Fareen'
print(s.index('n'))
s=' Fareen'
print(s.isalnum())
print(s.isalpha())
print(s.isdecimal())
print(s.isdigit())
print(s.isidentifier())
print(s.islower())
print(s.isnumeric())
print(s.isprintable())
print(s.isspace())
print(s.istitle())
print(s.isupper())
s='Fareen'
k='#'.join(s)
print(k)
s='Fareen'
k=s.ljust(10,'o')        #o including given characters
print(k)
print(k,'my name')
s='Fareen'
k=s.rjust(10,'o')        #o including given characters counting with char not wth index
print(k)
f='    fareen     '
print(f.lstrip())
print(f.rstrip())
print(f.strip())
f='fareen'
x=f.maketrans('f','a')
print(f.translate(x))

f='fareen'
x=f.maketrans('far','joy')              #using many characters together
print(f.translate(x))
p='python is great language'
print(p.partition('great'))
p='python is great language'
print(p.partition('fareen'))
p='python is great language great great'
print(p.rpartition('great'))
p='python is great language great great'
print(p.replace('great','perfect'))
print(p.replace('great','perfect',2))      #only first 2 occurance
p='python is great language great great'
print(p.rfind('great'))                              #last occurance
print(p.rindex('great'))               # same as above
print(p.find('great'))                  #find from right

p='python is great, language, great great'
print(p.split())
print(p.rsplit(',',1))            #maxsplit=1 whic is 1+1=2
p='python is great\n language\n great great'
print(p.split())
print(p.splitlines())
p='python is great language great great'
print(p.title())
p='fareen'
print(p.zfill(10))                       # fill with 0 including characters from left
h='abcbcaPythonabc'
print(h.removeprefix('abc'))                 #does not remove the repeat unlike in lstrip
print(h.lstrip('abc'))

h='Pythonabcaabc'
print(h.removesuffix('abc'))                 #suffix consider string ans rstrip consider each characters
print(h.rstrip('abc'))

"""o/p---
areen
fareen
       Fareen       
2
b'Faree@'
True
True
Fareen              Ansari
5
My name is fareen, roll no:1, weight49.000000
5
False
False
False
False
False
False
False
True
False
True
False
F#a#r#e#e#n
Fareenoooo
Fareenoooo my name
ooooFareen
fareen     
    fareen
fareen
aareen
joyeen
('python is ', 'great', ' language')
('python is great language', '', '')
('python is great language great ', 'great', '')
python is perfect language perfect perfect
python is perfect language perfect great
31
31
10
['python', 'is', 'great,', 'language,', 'great', 'great']
['python is great, language', ' great great']
['python', 'is', 'great', 'language', 'great', 'great']
['python is great', ' language', ' great great']
Python Is Great Language Great Great
0000fareen
bcaPythonabc
Pythonabc
Pythonabca
Python
"""

#POINTS TO REMEMBER:
'''
1.raw string with old number of backslahes(backslesh not the forward slash) at the end are invalid only even number of blacksleshes are valid which are at the end.
'''
#valid:
s='C:/'
print(s)
s='C:/'
print(s)
s='C:\python'
print(s)
s='C:\python\\'

#invalid
s='C:\'
print(s)

'''
\\ is represented by single \
and single is represented by single slash \

\\-->\
\--->\
'''

#raw too print the new line
k=r'''python
great
'''
print(k[0:7])
'''
python

space bcoz there is one new line
'''

#points to remember related to str methods
'''
every counting starts with ,counting with character and start counting from 1 not 0
eg:below eg give tab size of 8 including the character 
'''
#expandtab(if nothig is given in() it will take 8 tabs) count including the left chrs
k='fareen\thello'                                   #op--fareen  hello
print(k.expandtabs())

#alnum
k='ll01'
print(k.isalnum())
'''
if we use space anywhere it will give false otherwise true take only chars or only nums no matter but space is false
'''
#capitalize(it will create the first letter as capital, rest all be lower)
k='PYTHON'
print(k.capitalize())                               #op---Python

#center
k='PYTHOn'
print(k.center(8))
'''
space before and after python
( PYTHOn )
'''
#isalpha
k='PYTHO n'
print(k.isalpha())
'''
False
bcoz of space
'''
#isascii
k='PYTHO n'
print(k.isascii())
'''
True

return true if all characters have ascii value
'''
#isidentifier
k=' else'
print(k.isidentifier())
'''
False
return true if charachter is keyword
above case is false cuz it has space
'''

#count (str,start,end-1)
s='Fareen'.count('a',1,3)
print(s)

s='Fareen'.count('e',0,-2)
print(s)

#endswith('str',start, end)
s='Fareeneennn'.endswith('e',0,4)
print(s)

#splitlines(keepends=False).............default=False
k='''python
is
great
language'''
print(k.splitlines(keepends=True))
'''
['python\n', 'is\n', 'great\n', 'language']

cahracter counting always starts with char i.e 1 and index count starts with 0
as in zfill counts with chars
'''





