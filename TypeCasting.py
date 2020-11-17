#Implicit Typecasting
x=10                        #Python itself convert it into int
y=10.5                      #Python itself convert it into float


#Explicit Typecasting(INT, FLOAT, STRING, BOOL, COMPLEX ALL ARE IMMUTABE)
"""(if we try to change this immutable object it will point to different location))
x=10
x=x+1 (this will point to different memory location)
"""

#Eg1 of immutable string
x=10
print(x)
print(id(x))
x=20
print(x)
print(id(x))
"""o/p---
10
2324384606800        
20
2324384607120

both are pointing to different memory location
"""
#Eg2 of immutable string
a="fareen"
print(a)
print(id(a))
a=a+"ansari"
print(a)
print(id(a))
"""o/p---
fareen
2209404885360
fareenansari
2209404207024

both are pointing to different memory location
"""

#INT
int(10)              #int to int
int(10.99)           #Int to float
#to convert int into string it.string should be numeric and integral(with base 10))
int("python")        #Error
int("10.5")          #Error(it must be base 10)
int(0B101)           #Binary literal to int
int(True)            #int to bool
int("nan")           #error
int("infinity")      #error

"""In the case where the second argument is specified for the int () function,
the first must always be a string. The second argument specifies the number system of the first argument.
The int() function returns its value in decimal notation."""
int('10',8)            #o/p-- 8
int('0b11',2)          #o/p-- 3

int(10,'20')           #Error(Second argument cannot be a string first only can be a string) 


#FLOAT
float(10)              #float to Int  
float(10.5)            #float to float  
float("String")        #Error
float("10.9")          #Float to float
float(0B11)            #Binarty literal to float
float(True)            #float to bool
float("nan")           #o/p--nan
float("infinity")      #o/p--inf

#String
str(10)                #int to string
str(10.5)              #float to string
str("python")          #string to string
str(0o66)              #string to octal literal


#BOOL
#The following will return True:
bool("python")
bool(10)
bool(10.5)
a,b=5,10
c=a<b               #Return True
bool(0.8)
bool(" ")           #Return True bcoz of space
#The following will return False else everything is True:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#Application
name=input("Enter ur name-")
married=bool(input("Married or not(T/F)-"))
print(name)
print(married)
"""o/p--
Enter ur name-fareen
Married or not(T/F)-False
fareen
True

Even tho it is false it is showing true bcoz bool of any string is true
To resolve this case use "eval"
"""

#Eval(it gives the output as data type peovided by programmer)
name=input("Enter ur name-")
married=eval(input("Married or not(T/F)-"))
print(name)
print(married)
"""o/p--
Enter ur name-fareen
Married or not(T/F)-False
fareen
False"""

