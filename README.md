<h1>If else checking condition short way</h1>
<pre>
If the given condn is marks should be less than or equal to 350 and greater than or equal to 450
then:
print(350<=marks<=450)

instead of writing:
marks <=350 and marks >=450
</pre>

<h1>Random Module</h1>
<pre>
import random

#random() : to get randome values between 0 and 1.
x=random.random()

#randint() : to get random intigers(eg to get random number in dice)
x=random.randint(1,6)   #return random intiger value, including 1 and 6
print(x)

#randrange() : returns a number between 3 (included) and 9 (not included), 9-1=8, so 3 to 8
print(random.randrange(3, 9))

#unique() to get the random floating point value between 1 and 10 use uniform
x=random.uniform(1,10)   #random floating values between 1 and 10
x=random.uniform(0,1)   #random floating value between 0 and 1, it can be like 0.603094.. etc

#choice() : picks random values from a list of value
vehicle=['car','bike','bus']
print(random.choice(vehicle))

#choices() : here it will pick choices in the given list based on the k value provided
vehicle=['car','bike','bus']
print(random.choices(vehicle, k=10))

#adding weight in choices
vehicle=['red','blue','green']
print(random.choices(vehicle, weights=[18,18,2], k=10))  #red and blue has 18 chance to be randomly selected, but green has only 2 chance to get randomly secelted.

#shuffle()
deck = list(range(1, 53))
random.shuffle(deck)    #this will randomly shuffle the elements
print(deck)

#sample() : gives the unique values no number will repeat
hand = random.sample(deck, k=5)         #get the 5 unique values
print(hand)
</pre>


<h1>Exception</h1>

![exception](https://user-images.githubusercontent.com/59610617/146680494-251995ff-b7cc-4e07-a2da-c456c9622378.png)

<h1>UPLOADING CSV DATA TO MYSQL DATABASE</h1>
<pre>
1)Create database.
2)Use database;
3)Write code in proper format
def csv_sql(request):
    df = pd.read_csv('D:/userdata.csv')
    x=df.head()
    print(type(x))
    print(x)
    # format: mysql://user:password@host/db
    engine = create_engine('mysql://root:@localhost/csvdb')
    x.to_sql('userdatatable', con=engine)
    return HttpResponse("done")
   
Output: userdatatable is a table name, we dont need to create table just create database and use it, then whatever name we provide in the to_sql parameter that name will be the name of the table.
Note: if the file is xlsx then change pd.read_xlxs
link followed: https://syntaxbytetutorials.com/sql-import-excel-file-to-table-with-python-pandas/
</pre>











# Python Concept
1. Differentiate between .py and .pyc files?
<pre>
.py files contain human-readable Python source code, while .pyc files contain compiled Python bytecode used for more efficient execution.
And which is understadable by intepreter.

IN short: .py file contains actual code, whereas .pyc is a complied file which intepreter understand.
</pre>

# Python Basics
We have str, list, tuple, set and dict. </br>
<b>Operations on list</b>
<pre>
Functions of list:
li = [1,2,8,4,9,3]

1. copy() function:
eg: new_li = li.copy()        # new_li will be same as li

2. reverse() function:
eg: li.reverse()        # [3, 9, 4, 8, 2, 1]

3. sort() function:
eg: li.sort()         # [1, 2, 3, 4, 8, 9]

4. remove() function:    it'll remove one item at a time, if we have two '3''s then it'll remove the first occurance from left to right.
li.remove(1)        # [2, 3, 4, 8, 9]

5. count() function:
li.count(3)            # 1

6. len()
len(li)        # 7

Other functions: remove, pop, index, extend, append, insert, clear

Functions on tuple:
count, index

<b>Differentiate between append() and extend().</b>
append() adds a single element to the end of a list, while extend() adds multiple elements from an iterable to the end of a list.
Example:

nums = [1,2,3,4]
nums.append(4)
print(nums)                 #  [1,2,3,4,4]
nums.extend([5,6])
print(nums)                 #  [1,2,3,4,4,5,6]
</pre>

<b>Operations on set, frozenset</b>
1. insertion order are not preserved
2. duplicate are not allowed
3. indicated by{}
4. set item are not indexed so slicing and indexing not allowed
5. immutable
6. we can add and remove item in set but cannot change the value by using index.
7. main fucntionality of set is, union, difference & intersetion</br>

<b>The difference in set and frozenset is, in a short way set is kind of like a list and frozenset is kind of like a tuple.</b>
<pre>
Example:
Union:
a={1,2,3,4,5}
b={4,5,6,7,8,9}
c = a | b      # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

Intersetion:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

Difference:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
</pre>

<b>Operations on dict</b>
1. duplicated keys are not allowed
2. indexing and slicing not allowed
3. we can check the value of a perticuar key by giving its key

Other functions: add, update, remove, pop, discard
<pre>

d = {"red": 1, "blue": 2, "pink": 3, "black": 4}

<b>Get the keys.</b>
d.keys()         # dict_keys(['red', 'blue', 'pink', 'black'])

<b>Get the values.</b>
d.values()        # dict_values([1, 2, 3, 4])

<b>Get the values using get().</b>
d.get("red", "black")        # 1
d.get("cyan", "black")       # black

<b>Update the value of a key, or update the dict.</b>
d["red"] = 55                           # {'red': 55, 'blue': 2, 'pink': 3, 'black': 4}
d.update({"new_color": "green"})        # {'red': 5, 'blue': 2, 'pink': 3, 'black': 4, 'new_color': 'green'}

<b>Get the tuple from the dict, using items()</b>
d.items()		# dict_items([('red', 1), ('blue', 2), ('pink', 3), ('black', 4)])
</pre>

<b>Map, Filter, Reduce</b>
1. Map: Used when we want to do operation on all items on a list.
2. Filter: Used when we want to do operations to get a single values, example to get the greatest value etc.
3. Reduce: When we want to get one values, example sum etc.

<b>Operations on string</b>
<pre>
Slicing:

name = "fareen"
name[::-1]    # reverse string neeraf

In positive i.e from left to right it add -1, and for negative from right to left it does +1
Example:
name[0:3]        # far
name[0:-3]        # far

String methods:
use help(str)
</pre>

<b>Operators</b>
<pre>
<b>1. Arithmetic operator: </b>
/ is used for getting the actual division like we get in calculator, // is used to get quotent and % is used for getting the reminder. 

/ : used for divide		# always give floating value, will calculate the normal division
Example:
a=10
b=3
print(a / b)			# 3.3333333333333335

//: used for quotent
Example:
a=10
b=3
print(a // b)			# 3

%: used for reminder
a=8
b=3
print(a % b)			# 2

<b>Logical Operator: and, or and not</b>
If we do:
a = 10
b = 20

print(a and b)		# 20

It gave left hand value, we need to give condition in both side, like a > 10 and b < 20, likewise.

<b>Opeartor and precedence in python. All have left to right</b>
1. ()
2. **			# only this have right to left precedence
3. * / % //
4. + -

Question: 5 * 2 // 2 * (2 + 3)
So going for bracket first:	5 * 2 // 2 * 5
Now braket done, now go from left to right cuz all have same precedence.
So o/p:  10 // 2 = 5,   5 * 5 = 25

<b>in and is in python.</b>
For string: name = "fareen",  
'a' in name		# True

For lits: nums = [1,2,3,4,5,6]
1 in nums		# True

is is used to check for memory location, two values such as:
a = 10, b = 10
print(a is b)			# True, cuz values is same but when b = 20 the it'll be False
</pre>

# Deep vs Shallow copy
Deep copy creates the entirely new object which is independent of original object, where as shallow copy does not creates new object instead it refer the same original object.
<pre>
import copy

# Original nested list
original_list = [1, [2, [3, 4], [5, 6], 7]]

# Shallow copy
shallow_copied = copy.copy(original_list)

# Deep copy
deep_copied = copy.deepcopy(original_list)

# Modify the copied lists
shallow_copied[1][0] = 'X'
deep_copied[1][0] = 'Y'

# Print the results
print("Original List:", original_list)
print("Shallow Copy:", shallow_copied)
print("Deep Copy:", deep_copied)

output:
Original List: [1, ['X', [3, 4], [5, 6], 7]]
Shallow Copy: [1, ['X', [3, 4], [5, 6], 7]]
Deep Copy: [1, ['Y', [3, 4], [5, 6], 7]]


<b>Deep copy did not touch the original list, where as shallow copy change both the list</b>
</pre>

# Conditional Execution
<pre>
Marks should be less than or equal to 350 and greater than or equal to 450
if marks <= 350 and marks <= 450:
	pass

Instead of above use:
if `50<= marks <=450`:
	pass	
</pre>


# Function in python.
1. Required arguments: it is must we need to pass it.
<pre>
def calc_sum(a, b):
	sum = a + b
	return sum

Not giving a, b gives missing required parameter error.
</pre>

2. Keyword arguments: It checks the keyword passed.
<pre>
def create_dict(key, value):
    sum = {key: value}
    return sum

result = create_dict(value=20, key="Fareen")
</pre>

3. Default arguments: value = 20 is default value.
Non default argument should be after. Example: def sum(x, y, z=10).
<pre>
def create_dict(key, value=20):
    sum = {key: value}
    return sum

result = create_dict("Fareen")
</pre>

4. Variable-length arguments: In case of args and kwargs, args should come first then kwargs, args support list, tuple, kwargs support python dict. def nums(*args, **kwargs)

5. Function scope, local & global variable.</br>
i. Function have local space, meaning its variable value will be available inside that function only.</br>
ii. If we use global variable it'll become global, now we can use it anywhere it'll be global, even if we give global inside the function that'll become global.</br>
iii. In short: if we give global val even if it's inside the function, that'll become global, rest it has local space.</br>
iv. Consider below example and give output:</br>
<pre>
<b>Program 1:</b>
global val
val = 10

def print_val():
    val = 20
    return val

result = print_val()
print(result)
print(val)

<b>Program 2:</b>
def print_val():
    global val
    val = 20
    return val

result = print_val()
print(result)
print(val)
</pre>

6. Anonymous/Lambda Functions.
<pre>
add = lambda x,y: x + y
print(add(3,3))			# 6
</pre>

7. Higher order function.
<pre>
<b>i. Accepting argument as function.</b>
def add(sqrt, y):
    return sqrt(2) + y

def sqrt(val):
    result = val ** val
    return result

final = add(sqrt, 20)
print(final)

<b>ii. Returning function as result.</b>
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double)			# will return function, cuz it's returning a function
result1 = double(5)		# will pass 5 as argument in multiplier
print(result1)  		# Output: 10

# Another great example, this is called as function currying in javascript:
def sum1(num1):
    def sum2(num2):
        def sum3(num3):
            return num1 + num2 + num3
        return sum3
    return sum2

rest = sum1(1)(1)(1)
print(rest)			# 3
</pre>

7. Recursive Function: </br>
i. A recursive function in Python is a function that calls itself in order to solve a problem. Recursive functions are useful for solving problems that can be broken down into smaller, similar sub-problems. It is different from above function, above function calling another function, here it'll call itself.</br>
ii. To stop a function to to reach it recursion dept, we should give it a stop/break consition.</br>
iii. It has base/stop case and recurssion case.
<pre>
def calc_sum(n):
    if n == 1:		
        return 1			# base/break case
    n = n + calc_sum(n - 1)		# recursion case
    return n

res = calc_sum(5)
print(res)

In above code when we call calc_sum inside the function it gets minus 1 
i.e calc_sum(n - 1) = calc_sum(4), so here n becomes 4, i.e n = 4, so n = n + calc_sum() in this it gets n value which is 4
</pre>

8. Decorators in Function.
In Python, decorators are a powerful and flexible way to modify or enhance the behavior of functions or methods without changing their source code.</br>
In Python, a decorator is a function that takes another function as an argument and adds some functionality to it without modifying its source code. Decorators are often used to modify the behavior of functions or methods.
<pre>
Example:
def my_decorator(say_hello):
    def wrapper():
        print("Something is happening before the function is called.")
        say_hello()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

O/p:
Something is happening before the function is called.
Hello!
Something is happening after the function is called.

<b>BEST EXAMPLE OF DECORATOR: use this in interview</b>
class UnauthorizedUser(Exception):
    def __init__(self, message="You are Unauthorized!"):
        self.message = message
        super().__init__(self.message)

# super user check, if not super user then return exception
def super_user_check(get_all_users):
    def wrapper(request, *args, **kwargs):
        if request == "Fareen":
            return get_all_users(request, *args, **kwargs)
        else:
            raise UnauthorizedUser
    return wrapper

@super_user_check
def get_all_users(request):
    # uers = User.objects.all()
    return f"Hello {request}, you are authorized!"
	
result = get_all_users("Fareen")
print(result)
</pre>

9. What will be the output of the following function?
<pre>
def power_function(exponent):
    # This is the function factory
    def power(x):
        return x ** exponent
    return power

result = power_function(3)(2)
print(result)
</pre>

<b>Extra functions</b></br>
1. Memory location
<pre>
a = 10
id(a)			# will give memory location of a
</pre>

2. chr() function, to get number from unicode
<pre>
chr(65)			# A
</pre>

3. ord() function to get unicode from character
<pre>
ord('A')		# 65
</pre>

4. math module
<pre>
import math

# with positive numbers 
print(math.floor(3.9))		# 3
print(math.ceil(3.1))		# 4
	
# with negative numbers 
The above become vice versa, 3 become 4 and 4 becomes 3.
That is because it rounds to the closest floor number. 
-4 -3 -2 -1 0 1 2 3 4
</pre>

5. enumerate(): enumerate() is a built-in function in Python that is used to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index or position of each item. It returns an iterator that generates pairs of the form (index, item) for each item in the sequence.
<pre>
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
</pre>

6. eval() & exec()</br>
eval(): Essentially, it allows you to run Python code from a string.</br>
exec(): It is used for block of string.
<pre>
# eval()
nums_list = "[1,2,3,4]"
print(type(nums_list))			# <class 'str'>
result = eval(nums_list)
print(type(result))			# <class 'list'>

# exec()
code = """
x = 10
y = 20
result = x + y
print(result)
"""
exec(code)			# 30


Difference in eval and exec is:
eval for oe line stmt, exec is for multiple line of statement. Both uses string eval use one line str and exce uses multi-line string.
</pre>

7. range() and xrange() function
<pre>
xrange(): (Python 2 only)
range(): (Python 2 and Python 3)

Example:
Print reverse number using range from 10 to 0.
Print number in negative in range from -1 to -10.
</pre>

8. To get binary, bin function.
<pre>
bin(3)		# 0b11
</pre>

9. isinstance() 
<pre>
isinstance is a built-in Python function used to check if an object belongs to a specified class or type.
Example:
$ isinstance("fareen", (list, str))		# True
</pre>

# Extra points
<pre>
1. Floating point error:
0.3 - 0.1			# 0.19999999999999998

Getting wong error, we should get 0.3

2. When we do -4 // 3, we should get one as quotent, but we get -2, 
-4 // 3		# -2

This is cuz it does the floor division, in case of minus floor acts as ceil and vice versa.
</pre>


# Getting Help In Python(help, dir & docstring).
<pre>
# Use of help
For example if i want to get help for a module, i'll simply use:
$ help(functools)
If i want to get access of its one of the function as in i want to get help of reduce of functools.
$ help(functools.reduce)

# Use of dir function:
The dir() function in Python is used to list all the attributes (including methods, properties, and other attributes) 
of an object. It can be applied to various types of objects, including modules, classes, instances, and more. 
$ dir(functools)

# doc string
def sum_func(a, b):
	'''
	This is sum func.
	'''
	return a + b

$ sum_func.__doc__				# for custom module

import functools
$ functools.reduce.__doc__			# will print the doc string of reduce
</pre>

# OOPs In Python.

<b>Python Classes and Objects.</b>
<pre>
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f"Hello {self.name}, your age is {self.age}")

p1 = Person("Fareen", 26)
print(p1.name)				# Fareen		
p1.__str__()				# Hello Fareen, your age is 26

# likewise create many objects
</pre>

<b>Constructors in Python.</b></br>
In python `__init__()` function is acts as constructir and can be used to pass initial values. Consider the above example.

<b>Destructor in python using del, `__del__()` method:</b>
<pre>
In python `__del__()` is used to delete an object,
Example: below example print the statement before deleting the object.
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"This is going to delete: {self.name}")
	
p1 = Person("Fareen")
print(p1.name)				# Fareen
del p1
print(p1.name)				# NameError: name 'p1' is not defined


<b>There are other methods in class like `__len__()`, `__setitem__()`, `__getitem__()` but they are not very imp.</b>
</pre>

<b>Inheritance in Python</b>
1. Single Inheritance.
2. Multiple Inheritance: Method Resolution Order (MRO), It helps resolve potential ambiguities in multiple inheritance situations and provides a clear sequence for method lookup. You can access the MRO of a class using ClassName.__mro__, which will show you the order in which the classes are considered during method lookup.

![multiple](https://github.com/fareen341/Python-Programming/assets/59610617/90db5532-df97-4021-bf79-4236fbbf9f3e)


<pre>
# Base classes
class A:
    def __init__(self):
        self.name = "Fareen"

class B:
    def __init__(self):
        self.name = "Anamika"

# Derived class with multiple inheritance
class C(B, A):
    def __init__(self):
        self.name = "Roma"

    def __str__(self):
        print(f"Name: {self.name}")

obj = C()
obj.__str__()


Python support multiple inheritance, In above class, class C is getting property from A and B also
So here python resolve this conflict by checking the first class given inside C class which is B so 'Anamika' will be printed.print
If it'd be A class first then it'd be Fareen
And if child has own name property the it'd be Roma.
</pre>

3. Multi-Level Inheritance.

![multilevel](https://github.com/fareen341/Python-Programming/assets/59610617/96e866d5-acc9-40a3-a8ad-b5df4b002912)

4. Hierarchical Inheritance.

![hirarchical](https://github.com/fareen341/Python-Programming/assets/59610617/331315e8-6fb6-4be6-85f6-bed5825a9b64)

<b>Encapsulation in Python.</b>
It's important to note that encapsulation in Python is more of a convention than a strict enforcement. Access to protected and private members is still possible, but it's considered non-standard practice and should be avoided unless you have a compelling reason to access them directly. Encapsulation helps make code more maintainable and less error-prone by restricting direct access to internal implementation details of a class.
<pre>
class Student:
    def __init__(self, name, aadhar, pswd):
        self.name = name
        self._aadhar = aadhar
        self.__pswd = pswd

    def display(self):
        print(f"Name is: {self.name}, aadhar is: {self._aadhar}, pswd is: {self.__pswd}")

stu_obj = Student("Fareen", 223, "Someval@val")
print(stu_obj.name)
print(stu_obj._aadhar)
print(stu_obj._Student__pswd)
stu_obj.display()

Purpose: This is used to prevent subclassing issues or to ensure that the attribute is not accidentally overridden or accessed directly.
</pre>

5. Diamond Problem.
i. To address this issue, programming languages that support multiple inheritance typically provide rules and mechanisms for method resolution, such as the C3 linearization algorithm used in Python's method resolution order (MRO).</br>
ii. This is same as multiple inheritance.
<pre>
   A
  / \
 B   C
  \ /
   D


</pre>

<b>Overloading & Overriding in Python.</b>
<pre>
<b>Method Overriding: Same name of method but different definition.</b>
class A:
    def __init__(self):
        self.name = "Fareen"

    def print_name(self):
        print(f"Name is: {self.name}")

class C(A):
    def print_name(self):
        print(f"Name is: {self.name}")

obj_A = A()
obj_A.print_name()
obj = C()
obj.print_name()
	
<b>Overloading: Same method name with different number of parameters.</b>
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
</pre>

<b>Use of super() method in python.</b></br>
In Python, super() is a built-in function that is used to call a method from a parent or superclass. It is particularly useful in the context of method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass. super() allows you to invoke the parent class's version of a method while extending or modifying its behavior in the child class.</br>

The primary use of super() is to ensure that the parent class's implementation of a method is called before adding or extending functionality in the child class. This is important to maintain code reusability and to avoid duplicating code that already exists in the parent class.</br>

In below example we extend the parent function addition in child by using the same function with adding child's functionality too.
<pre>
class Parent:
    def show(self):
        sum = 10 + 10
        print(f"This is the parent class sum {sum}")
        return sum

class Child(Parent):
    def show(self):
        parent_sum = super().show()  # Call the parent class's show method
        child_sum = parent_sum + 10
        print(f"This is the parent class sum {child_sum}")
        return child_sum

child = Child()
child.show()


<b>super in constructor</b>
class Vehicle:
    def __init__(self, name):
        self.name = name

class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the base class
        self.color = color

my_car = Car("Sedan", "Blue")
</pre>

<b>Duck Typing.</b></br>
1. Duck typing is a concept in dynamic programming languages like Python that focuses on the behavior of an object rather than its type or class.
2. In below example, the get_length function does not check the type of the obj parameter. Instead, it relies on the fact that various objects (strings, lists, tuples) all support the len() function. As long as an object behaves like it has a length, it can be passed to this function.
3. Duck typing promotes flexibility and code reusability by allowing you to work with a wide range of objects without being overly concerned with their specific types. However, it also places responsibility on the developer to ensure that objects passed to functions or methods behave as expected.
4. The term "duck typing" comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
<pre>
def get_length(obj):
    return len(obj)

# You can pass different types, and it will work as long as they support len().
string_length = get_length("Hello, World!")  # Works
list_length = get_length([1, 2, 3])           # Works
tuple_length = get_length((4, 5, 6))          # Works

a = "937937"
print(type(a))			# str
print(int(a))			# even tho type is string it checks the behaviour

# There are no type checks; it works based on behavior.
</pre>

<b>Abstract Base Classes.</b></br>
1. This is same as which we have in django Abstract class.
2. Here also this class acts as a structure only and dont allow us to cannot create object of this class. Likewise in django it does'nt create class for Abstract base class.
3. We use Meta class in django to make it Abstract class. Likewise in python we use abstractmethod to make a method as abstractmethod.
<pre>
from abc import ABC, abstractclassmethod


class Person(ABC):

    @abstractclassmethod
    def common_details(self):
        pass

class Student(Person):
    def common_details(self, name):
        self.name = name
        print(name)

class Teacher(Person):
    def common_details(self):
        pass

    def salary_details(self, salary):
        print(salary)

# p_obj = Person()                # TypeError: Can't instantiate abstract class Person with abstract methods common_details

st_obj = Student()
st_obj.common_details("Fareen")


te_obj = Teacher()
te_obj.salary_details(400000)

<b>Concrete Methods in Abstract Base Classes</b>
In above clas if we dont override common_details function in child class, it'll give error.
So we need not to override Concrete Methods, this have definition in Abstract/Common class only.

Example:

from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def common_details(self):
        pass

    def description(self):
        print("This if from common class.")

class Student(Person):
    def common_details(self):
        print("This if from child.")

st_obj = Student()
st_obj.common_details()
st_obj.description()
</pre>

<b>Decorators in Class</b></br>
<pre>
Check out decorators in function
Decorators is also called as Metaprogramming.

Example:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the method is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the method is called.")
        return result
    return wrapper

class MyClass:
    def __init__(self, value):
        self.value = value

    @my_decorator
    def greet(self):
        print(f"Hello, my value is {self.value}")

# Creating an instance of the class
obj = MyClass(42)

# Calling the decorated method
obj.greet()
</pre>

<b>Class Method & Static Method</b></br>
In summary, `@classmethod` is used when you need to work with or modify class-specific attributes and methods, while `@staticmethod` is used for utility functions that are related to a class but don't need access to class or instance-specific data. Both decorators help organize and encapsulate code within a class and make it more readable and maintainable.
<pre>
<b>Class Method</b>
class Person:
    age = 20

    def __init__(self, age):
        self.age = age

    @classmethod
    def age_increment(cls):
        inc = cls.age + 4
        print(inc)

    def age_decrement(cls):
        dec = cls.age - 2
        print(dec)

p = Person(30)
p.age_increment()
p.age_decrement()

In above code when we can access/modify class variable by using classmethod, we use cls for class method.isinstance
In age_decrement function we have taken cls, but that does not mean it is class method instead it is self only.
It gets class method only after using that decorator

<b>Static Method</b>
It is a regular function which is inside class.
In below example we must pass self or cls, to make it a class method, but if we have requirement to make it a 
regular function and inside the class then use decorator staticmethod.
class Person:
    age = 20

    def __init__(self, age):
        self.age = age

    @classmethod
    def age_increment(cls):
        inc = cls.age + 4
        print(inc)

    def age_decrement(cls):
        dec = cls.age - 2
        print(dec)

    @staticmethod
    def display_greetings():
        print("Hello!")

p = Person(30)
p.age_increment()
p.age_decrement()
p.display_greetings()
</pre>

# Module
<pre>
There are built-in module, eg math. 
import math

to create user-defined module:
Step 1: create a module file eg, multiply_module.py
Step 2: create a function with multiply functionality, accepting parameters.
Step 3: import multiply_module
</pre>

# Logger
1. We do print statement but that is limited to terminal, meaning it's not getting stored in some file. We log statements to get infor eg: we use logger.error() in exception to check what is causing the error in live using the log file.
2. Below example will created a app.log file and store all the log info in that file only.
3. By default, Python's logging module does not automatically manage log retention, so logs will accumulate in the log file until the file system runs out of space or you manually manage log rotation.
<pre>
import logging
# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)


logger.info("STMT")
logger.error("raised error")

Output:
2023-10-13 11:11:49,363 - __main__ - INFO - STMT
2023-10-13 11:16:02,165 - __main__ - ERROR - raised error
</pre>

# Date & Time
For this refer jupyter notebook.

# Closures
1. Basically closure store the state of outer function. It is same in javascript.
2. Inner function can access data of outer/parent function with the help of closure.
<pre>
def outer_func(x):
    def inner_func(y):              # it holds the value of x in the closure
        return x + y
    return inner_func

res = outer_func(4)(4)
print(res)
</pre>

# Monkey Patching
1. Monkey patching is a programming technique in which you modify or extend the behavior of existing classes or modules at runtime, typically without altering the source code of those classes or modules. It's called "monkey patching" because you're making changes to code in a way that might be considered as a "monkey" playing with it.
2. This technique is often used when you need to fix bugs or add functionality to libraries or modules for which you don't have access to the source code. Monkey patching can be a quick and convenient solution, but it also has some potential downsides, such as introducing unexpected behavior or making your code less maintainable.
<pre>
class Person:
    def __init__(self, value):
        self.value = value

# creating a class method outside of the class
def new_method(self):
    print(f'Valis is {self.value}')


# # Monkey patch the method into the class
Person.new_method = new_method

per1 = Person(44)
per1.new_method()
</pre>

# Regular Expression
<b>Match & Search</b>: The match() function in Python's re module is used to determine whether a regular expression pattern matches at the beginning of a string. It attempts to match the pattern from the start of the string, and if a match is found at the beginning, it returns a match object; otherwise, it returns None.
<pre>
import re

text = "The python is a great language, it has many modules, python is my fav."
pattern = "python"
# match
match = re.match(pattern, text)				# check the first occurance, so it'll search for python in first match

# search
match = re.search(pattern, text)			# check the entire string and return the first occurance
if match:
    print(f"Match Found: {match.group()}")		# blank outout
</pre>

<b>Split</b>
<pre>
text = "The python is a great language, it has many modules, python is my fav @python."
pattern = r"[@, p]"			# this means split by @ or comma or space or p
match = re.split(pattern, text)
print(match)				
	
Output:
['The', '', 'ython', 'is', 'a', 'great', 'language', '', 'it', 'has', 'many', 'modules', '', '', 'ython', 'is', 'my', 'fav', '', '', 'ython.']

Note: wherever it finds the given patten like 'p' it'll consided it as '', same for all.
</pre>

<b>Creating pattern</b>
<pre>
pattern for indian mobile number.
r'^9\d{9}$'

To be continue
</pre>

# Pickling and Unpicling
1. Serializer is converting python complex datatype into json.
2. Pickling is converting python complex datatype into binary format.
<pre>
import pickle

# Serialize (pickling)
data = [1, 2, 3, 4, 5]
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize (unpickling)
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: [1, 2, 3, 4, 5]
</pre>

# Json dump, dumps and load, loads. 
1. json.dump - serializer, converting python complex data type into json format.
2. json.load - deserializer, converting json data back to python complex data type.
<pre>
import json

data = {"name": "Fareen", "age": 25}

# writing
file = open("data.json", 'w')
json.dump(data, file)
file.close()

# reading
file = open("data.json", 'r')
json_data = json.load(file)
print(json_data)
file.close()

<b>Difference between load and loads</b>
1. In loads or dumps, `s` stands for string, if i have a string data in python and i want to convert it into json use loads.
2. Use load and dump when working with files.

# this is json data, which takes string, in python it'll print as str
json_data = '{"US": 100, "IND": 200}'
print(type(json_data))                                  # str, basically json

# loads
converted_python_dt = json.loads(json_data)             # {"US": 100, "IND": 200}'
print(type(converted_python_dt))                        # dict

# dumps
python_dt = converted_python_dt                         # python dict
converted_json_dt = json.dumps(python_dt)               # str
print(type(converted_json_dt))                          # {"US": 100, "IND": 200}
</pre>

# MultiTasking & MultiThreading
1. Multitasking involves running multiple processes, which are separate and isolated instances of a program, while multithreading involves running multiple threads within a single process, which share the same memory space. Multitasking provides strong isolation but has higher overhead, while multithreading has lower overhead but requires careful management of shared resources and synchronization.

![1](https://github.com/fareen341/Python-Programming/assets/59610617/20e1cdc5-6318-495c-b9fb-8a122c95b1f1)

2. MultiTasking Example: below program will run parallely utiling the different core of the CPU.
<pre>
import multiprocessing

def worker1():
    for i in range(5):
        print("Worker 1: Task", i)

def worker2():
    for i in range(5):
        print("Worker 2: Task", i)

# Create two separate processes for multitasking
process1 = multiprocessing.Process(target=worker1)
process2 = multiprocessing.Process(target=worker2)

# Start the processes
process1.start()
process2.start()

# Wait for the processes to finish
process1.join()
process2.join()

print("Multitasking complete")

Output:
Worker 1: Task 0
Worker 2: Task 0
Worker 1: Task 1
Worker 2: Task 1
Worker 1: Task 2
Worker 2: Task 2
Worker 1: Task 3
Worker 2: Task 3
Worker 1: Task 4
Worker 2: Task 4
Multitasking complete
</pre>

3. Multi-Threading Example:
<pre>
import threading
import time

def worker1():
    for i in range(5):
        print("Worker 1: Task", i)
        time.sleep(0.1)

def worker2():
    for i in range(5):
        print("Worker 2: Task", i)
        time.sleep(0.1)

# Create two separate threads for multithreading
thread1 = threading.Thread(target=worker1)
thread2 = threading.Thread(target=worker2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Multithreading complete")

O/p: same as above

In this example, we define two worker functions, worker1 and worker2, which perform tasks. 
We create two separate threads using threading.Thread and assign each worker function to a thread. 
We start the threads, and they run concurrently. The join method is used to wait for both threads to complete.
</pre>

# Method Chaining
Method chaining is a programming technique where you can call multiple methods on an object one after the other in a single line of code. This is often used for building more concise and readable code.
<pre>
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self

    def subtract(self, x):
        self.value -= x
        return self

    def get_result(self):
        return self.value

# Using method chaining
result = Calculator(10).add(5).subtract(2).get_result()

print("Result:", result)			# Result: 13
</pre>

# Function Factory
1. Function Factory is the function which return another function as its output. It is higher order function.
2. For example, check above higher order function.

# Working with OS module.
<pre>
<b>Get current working dir.</b>
os.getcwd()		
	
<b>mkdir() vs makedirs()</b>
# will give error if Python dir is not present in current dir	
os.mkdir('Python/Django')	
	
# will not give error if Python dir is not present in current dir and create dir accordingly
# will create Python first and inside it DJango	
os.mkdir('Python/Django')			

<b>rmdir() vs removedirs()</b>
Same like make directory.

<b>List directory</b>
# we need to give full path here
print(os.listdir('/home/fareen/Desktop/Python'))
	
# whatever it prints we need to give that path inside listdir
print(os.getcwd())

<b>Check for file existance. isfile() & exists()</b>
print(os.path.isfile("output.csv"))				# True
print(os.path.exists("output.csv"))				# True

print(os.path.isfile("/home/fareen/Desktop/Python/output.csv"))		# True
print(os.path.exists("/home/fareen/Desktop/Python/output.csv"))		# True
</pre>

# Working with file.
<pre>
import json

# Writing data
d = {"UN": 30, "INT": 40}

file = open("data.json", "w")		# we can also use with keyword
json.dump(d, file)
file.close()

# Reading Data
file = open("data.json", "r")	
read = json.load(file)
print(read)
file.close()
</pre>

# Advance Python
# Pandas
In pandas we have series and dataframe, input/output, data cleaning like missing and null value, merging and joinig and plot.
<b>1. DataFrame</b>
<pre>

import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)

O/p:
      Name  Age           City
0    Alice   25       New York
1      Bob   30  San Francisco
2  Charlie   35    Los Angeles
</pre>

<b>2. Series</b>
<pre>
import pandas as pd
# Creating a Series with custom index labels
data = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
my_series = pd.Series(data)

# Print the Series
print(my_series)

O/p:
Alice      25
Bob        30
Charlie    35
dtype: int64
</pre>

<b> Input/Output in pandas</b>
<pre>
Reading:
1. read_csv:
eg: df = pd.read_csv('data.csv')

2. read_excel
3. read_json
4. read_sql

Writing:
same functions like above but instead of read it is to_csv, to_sql etc

Example: to_csv
import pandas as pd
df = {
        'alpha' : ['a', 'b', 'c', 'd'],
        'data' : [10, 20, 30, 40]
     }
my_series = pd.DataFrame(df)
my_series.to_csv('output.csv', index=False)
</pre>

<b>loc & iloc in pandas</b>
<pre>
Indexing:
<b>loc example:</b>

import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['apple', 'banana', 'cherry', 'date', 'elderberry']}

df = pd.DataFrame(data, index=['row1', 'row2', 'row3', 'row4', 'row5'])

O/p:
        A   B          C
row1  1  10      apple
row2  2  20    banana
row3  3  30    cherry
row4  4  40    date
row5  5  50    elderberry

selected_data = df.loc[[row], [column]]
selected_data = df.loc[['row1', 'row3'], ['A', 'C']]

O/p:
      A   B      C
row1  1  10  apple

selected_column = df.loc[:, 'B']

<b>iloc: select by integer position.</b>
Example:
selected_column = df.iloc[:, 1]

O/p:
row1    10
row2    20
row3    30
row4    40
row5    50
Name: B, dtype: int64
</pre>

<b>Data Visualization</b>
<pre>
Built-in plotting methods like plot(), hist(), boxplot(), etc.
For this to work we need matplotlab module.

Step 1: Create or load data.
Step 2: Convert into dataframe/series.
Step 3: Plot, using df.plot(kind)

Example:
bar plot:
import pandas as pd
import matplotlib.pyplot as plt
data = {'Category': ['A', 'B', 'C'], 'Value': [10, 20, 15]}
df = pd.DataFrame(data)
df.plot(x='Category', y='Value', kind='bar')
OR
plt.show()

histogram:
import pandas as pd
import matplotlib.pyplot as plt
series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5])
series.plot(kind='hist', bins=5)
</pre>

<b>Data Merging and Joining</b>
<pre>
1. We can perform sql like join of two dataframe:
2. The how parameter specifies the type of join (inner, outer, left, right).
3. You can also join multiple DataFrames by chaining .join().

import pandas as pd
left = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                    'value_left': [1, 2, 3]})
right = pd.DataFrame({'key': ['K1', 'K2', 'K3'],
                     'value_right': [4, 5, 6]})
result = pd.merge(left, right, on='key', how='left')  # Left join

O/p:
key	value_left	value_right
0	K0	1	NaN
1	K1	2	4.0
2	K2	3	5.0


Example 2: using .join()
  
import pandas as pd
left = pd.DataFrame({'A': ['A0', 'A1', 'A2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'B': ['B0', 'B1', 'B2']},
                     index=['K1', 'K2', 'K3'])
result = left.join(right, how='inner')

O/p:
	A	B
K1	A1	B0
K2	A2	B1
</pre>

# Numpy
Numpy is all about numeric calculations, it works well with array, we get maths functions easily in numpy like sqrt, add, sin, power etc, generate range, generate random number.
<pre>
import numpy as np

# Creating an array from a Python list
my_list = [1, 2, 3, 4, 5]
arr_from_list = np.array(my_list)

# Creating an array filled with zeros
zeros_array = np.zeros(5)

# Creating a 2D array filled with ones
ones_array = np.ones((2, 3))

# Creating an array with a range of values
range_array = np.arange(0, 10, 2)

# Creating a linearly spaced array
linspace_array = np.linspace(0, 1, 5)

# Creating a random array with values between 0 and 1
random_array = np.random.rand(3, 4)
</pre>


# Matplotlib & Seaborn
Both are used for data visualization.
<pre>
We need to import Matplotlib for plotting

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Country": ["UN", "US", "IND", "EU", "CHINA"],
    "SCore": [100, 20, 40, 50, 100]
}

df = pd.DataFrame(data)
df.plot(kind='hist', bins=2)
plt.show()
</pre>

# What is pep8 and flake8?
1. PEP 8 is the Python Enhancement Proposal that defines the style guide for writing Python code. It provides guidelines and recommendations on how to format Python code for improved readability and consistency.
2. Some key component of pep8 is, Maximum Line Length: Limit lines to 79 characters for code and 72 characters for docstrings and comments.
3. flake8 is a tool that checks your Python code against PEP 8 style guide conventions and detects violations. It enforces PEP 8 rules and helps ensure that your code follows the recommended coding standards.
4. We can use flake8 vs code extension.
5. Difference between composition and inheritance?
- Composition is when a class is composed of one or more objects from other classes and uses their functionality without altering their internal workings.
- In inheritance we can alter the behaviour of parent class in child class.
- This is same like in django we pass request to the method which does not have request, self.request = request. But this is not composition this is attribute assignment.
```python
class Engine:
    def start(self):
        return f'Engine started!'

class Car:
    def __init__(self):
        self.engine = Engine()

    def engine_status(self):
        return self.engine.start()

eng = Car()
print(eng.engine_status())
```   
 

# String formatting in python.
<pre>
<b>print statement syntax</b>
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Example:
a = "Hello"
b =  "World"
c = "AND Python"
print(a, b, sep="*", end="**")
print(c)

Output:
Hello*World**AND Python

<b>f string in python</b>
print(f'2 + 2 = {2 + 2}')		# 4
	
<b>Usinh modulus</b>
print("2 + 2 = %s" % (2 + 2))		# 4
</pre>

# Programs Practice
1. Get the 2nd larget value in a list.
2. The given list ["abc", "def"] convert the list in [["a", "b", "c"], ["d", "e", "f"]].
3. Reverse the name "fareen".
4. Fine a pallindrome.
5. Print pattern:
<pre>
*
**
***
****
*****
</pre>
6. What is the output: 
<pre>
1. 2 + 3 * 4 ** 2 / 2
2. 3 ** 3 ** 2
</pre>
7. Find a number is armstrong or not.
<pre>
Cube of all numbers and addition will give the same number.
For example, let's take the 3-digit number 153:

Calculate each digit raised to the third power, it is pow of 3 not num ** 3:

1^3 = 1
5^3 = 125
3^3 = 27

1 + 125 + 27 = 153

i. Using recursion
ii. Using simple logic

<b>SOLUTION:</b>
# Using recursion
def find_armstrong(num, total=0):
    if num <= 0:
        return total
    total = total + pow(num % 10, 3)
    return find_armstrong(num // 10, total)

res = find_armstrong(407)
print("ARM: %s" % res)

# uisng simple logic
total = 0
num = "158"
for i in num:
    total = total + pow(int(i), 3)
print(total)
</pre>
7. Remove duplicate from a list num_list = [3,4,6,3,4,7].
<pre>
i. Using simple set.
ii. Using simple logic.

ii.
for i in num_list:
    if num_list.count(i) > 1:
        num_list.remove(i)
print(num_list)
</pre>

8. Length of last word str = "python is great, it has many features".
9. In the given list arr = [5, 32, 45, 4, 12, 18, 25], do minus of first element with second.
10. Find all the pairs which has sum = 17 in the given list arr = [5, 7, 4, 3, 9, 8, 19, 21].
11. Find all the missing values in list arr = [1,2,3,5,6,7,8,10,17].
12. Convert two list into dict x = [1,2,3,4], y = ["a", "b", "c", "d"].
13. Find the count of word "python" in the given string, str = "python is great, it has many features, python".
14. Find the common element in two str, name = "Seema" and name = "FarEen", by repetation of words and without repetation also. Also ignoring the case.
15. Calculate sum of all numbers in a list using recursion nums = [1,2,3,4,5,6].
16. In a given list l=[1,1,1,4,5,6,5,6], count the occurance of all elements, also count the occurance of just one element `4`?</br>
i. using collections module. </br>
ii. using logic. </br>
<pre>
<b>SOLUTION</b>
<b>Using collection module</b>
import collections

l=[1,1,1,4,5,6,5,6]
result = collections.Count(l)
print(result)

<b>Using simple logic</b>
l=[1,1,1,4,5,6,5,6]
d = {}
for i in l:
    d.update({i, l.count(i)})
print(d)
</pre>
17. Write a program which can compute the factorial of a given numbers.</br>
i. Using Recursion.</br>
ii. Using Loop.
<pre>
<b>SOLUTION</b>


<b>Using recursion</b>
def calc_fact(num, factorial=1):
    if num <= 1:
        return factorial
    factorial = factorial * num
    return calc_fact(num - 1, factorial)

res = calc_fact(5)
print(res)
</pre>
18. Question: towns = [{'name': 'Manchester', 'population': 58241}, {'name': 'Coventry', 'population': 12435}, {'name': 'South Windsor', 'population': 25709}] 
<pre>
Create a new list of the town names using for loops... using list comprehensions... using the map() function.
Create two lists, one of the town names and one of the town populations using for loops... using list comprehensions... using the zip() function.
Given the two lists (names and populations), combine them back into a list of dictionaries using for loops... using list comprehensions.
Using the list of towns, find the total combined population using for loops... using the sum() function... using the reduce() function.
</pre>
19. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
<pre>
Example:
0100,0011,1010,1001
Then the output should be:
1010
</pre>
20. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
21. Write a program that accepts a sentence and calculate the number of letters and digits.
22. Suppose the following input is supplied to the program:
<pre>
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

<b>SOLUTION:</b>

text = "hello world! 123"
str_count = 0
int_count = 0
for i in text:
    try:
        if int(i):
            int_count = int_count + 1
    except ValueError as e:
        if not i == " " and isinstance(i, str):
            str_count = str_count + 1

print(str_count)
print(int_count)
</pre>

23. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
<pre>
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
</pre>
23. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
<pre>
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7
Then, the output should be:
1,9,25,49
</pre>
24. How can you replace string space with a given character in Python?
25. Count the sum of all elemenet in list = [1,2,3,4] also sum of range of 5 numbers using recursion?
26. Find febonacci series using recursion and without recursion?
27. Give list l=[1,2,3,[9,9,9],10, [2,3], [3]] 
<pre>
i. count the sum of all elements in the given list.
ii. count the sum of all elements in the given list only if they are even number.
iii. with using list comphrension, if possible.
</pre>
28. Find the pallindrom using recursion?
<pre>
<b>SOLUTION:</b>

num = 1234
def find_palindrom(num, reverse=0):
    if num <= 0:
        return reverse
    reverse = reverse * 10 + num % 10
    return find_palindrom(num // 10, reverse)

res = find_palindrom(num)
print("res %s" % res)

<b>Points to remember when solving the recursion program.</b>
1. Always give stop condition.
2. If we need to initialize the variable for counter always use it in parameter which initialize with 0, see above.
3. Understand the recursion loop first.
4. Return statement should return itself. Base condition should return the value. 
</pre>

29. Give example of Decorator program?
30. Give example of Higher order function?
31. Find armstrong number.
<pre>
i. with using list method.
ii. without using list method, i.e with logic.
</pre>
32. Sum of all element in a given range, for eg if i give 5 then calculate `5 + 4 + 3 + 2 + 1` using recursion?
<pre>
<b>SOLUTION</b>
def find_sum(num, total=0):
    if num <= 0:            # base condition
        return total
    total = total + num
    return find_sum(num - 1, total)

res = find_sum(5)
print(f"Result is : {res}")
</pre>
33. Print the following pattern:
<pre>
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

<b>SOLUTION</b>
incr = 1
for i in range(0, 5):
    # print space
    for j in range(1, (5 - i)):
        print(' ', end=" ")
    if i >= 1:
        incr = i+i+1
    # print star
    for k in range(0, (incr)):
        print("*", end=" ")
    print()
</pre>

34. Give the output of the following division.</br>
 i. 5 * 2 // 2 ** (2 + 3)</br>
 ii. 10 / 32
<pre>

<b>SOLUTION</b>
i. 

5 * 2 // 2 ** (2 + 3)

5 * 2 // 2 ** 5

5 * 2 // 32

10 // 32    =  0


ii. 

    0.3125
32 | 10
     32
     ===
     100
     96
     ===
     40
     32
     ==
     80
     64
     ==
     160
     160
     ==
</pre>
35. Calculate the largest element of a list using recursion, lst = [2,3,5,9,4,8,3,1,10, 3, 2, 38, 21, 3]?</br>
i. Using recursion.</br>
ii. Using loop.
<pre>
<b>SOLUTION</b>

<b>Uisng recursion</b>
lst = [2,3,5,9,4,8,3,1,10, 3, 2, 38, 21, 3]

def calc_largest(lst, lar=lst[0]):
    if not lst:
        return lar
    if lst[0] > lar:
        lar = lst[0]
    return calc_largest(lst[1:], lar)

res = calc_largest(lst)
print(res)

<b>Using Loop</b>
fir = lst[0]
for i in lst[1:]:
    if i > fir:
        lar = i
        fir = i

print(lar)
</pre>

36. Write a program to convert the below data into key value pair  of json, data is like:
<pre>
pdf_data = [
    "12-04-2012 JHKWm KUHYk PCS 20000.456 8,4432.09 3,545.55 CR",
    "12-04-2012 KUHKDNFKNFKLIOOUJI 80700.456 8,4432.09 2,545.55 CR",
    "12-04-2012 KHHDJHDDKJHD KDUH/KLDIUYH PCS 50000.456 1,4432.09 4,545.55 CR",
    "12-04-2012 KIUGHDIK KJUDGHJKAH 90000.456 8,4432.09 4,545.55 CR"
]

output should be: list of dict of all elements of above list
{
    data: 12-04-2012,
    acno: JHKWm KUHYk PCS,
    credit: 20000.456,
    debit: 8,4432.09,
    total: 3,545.55 CR    
}
</pre>
<pre>
In above string the data in all list elements are same except the acno, 2nd string
<b>SOLUTION</b>
account_list = []
for i in pdf_data:
    final_acno = ""
    d = {}
    data = i.split(" ")
    acno = data[1:-4]
    for i in acno:
        final_acno = final_acno + " " + i
    d.update({"date": data[0], "acno": final_acno, "credit": data[-4], "debit": data[-3], "total": data[-2] + " " + data[-1]})
    account_list.append(d)

file = open("account.csv", "w")
json.dump(account_list, file)
file.close()
</pre>

37. calculate fibonacci series of given number.
<pre>
i. Uisng simple loop.
ii. Uinsg recursion.
</pre>

<pre>
Understanding below series.
# 0, 1, 1, 2, 3, 5, 8, 13

# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13

In above:
n0 = 0
n1 = 1
total = 0

n0 + n1 = total
n0 = n1
n1 = total

print(n1)	# will print the series
</pre>

<pre>
<b>SOLUTION</b>
i. Using for loop:

n = 10
n0 = 0
n1 = 1
total = 0
lst = [n0, n1]
for i in range(n):
    total = n0 + n1
    n0 = n1
    n1 = total
    lst.append(n1)
print(lst)


ii. Using recursion:
def fino_series(num, n0=0, n1=1, total=0, lst =[0, 1]):
    if num < 0:
        return lst
    total = n0 + n1
    n0 = n1
    n1 = total
    lst.append(n1)
    return fino_series(num - 1, n0, n1, total)

res = fino_series(10)
print(res)
</pre>

38. Calculate sum of all elements in the list = [1, 2, [3, 4, [4, 5]]].
<pre>
def calculate_nested_list_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total = total + calculate_nested_list_sum(element)
        else:
            total = total + element
    return total

original_list = [1, 2, [3, 4, [4, 5]]]
result = calculate_nested_list_sum(original_list)
print("Sum of elements in the nested list:", result)
</pre>

39. Calculate prime number in 50 range.
<pre>
i. Using loop
ii.Using recursion

So prime number is number which is divisible by 1 and itself, like:
2, 3, 4, .. 19 and so on, is prime number cuz it is divisible by itself and no other number.
</pre>

<pre>
<b>SOLUTION</b>

i. Using loop
lst = []
num = 50
for i in range(2, num):
    for j in range(2, 10):
        if i == j:
            continue
        if i % j == 0:
            lst.append(i)
            break

res = [i for i in range(1, num) if i not in lst]
print(res)


ii. Using recursion
def prime_calc(num, lst=[]):
    if num < 3:
        return lst
    for i in range(2,10):
        if num == i:
            continue
        if num % i == 0:
            lst.append(num)
            break
    return prime_calc(num - 1)

num = 50
res = prime_calc(num)
result = [i for i in range(1, num) if i not in res]
print(result)

<b> Also we can do:</b>
res = set(lst) - set(non_prime)
print("res", res)
</pre>

39. Calculate prime number in the given list.
<pre>
non_prime = []
lst = [3, 4, 6, 5, 87, 3, 34, 346, 227]
for i in lst:
    for j in range(2, 10):
        if i == j:
            continue
        if i % j == 0:
            # print(i)
            non_prime.append(i)
            break

res = set(lst) - set(non_prime)
print("res", res)

# if we need repeating numbers also, we need to use loop, see above
</pre>


# Program with solution
1. Shortest way to check for pallindrome.
<pre>
name = "madam"
if name == name[::-1]:
	print("pallindrome")
else:
	print("not a pallindrome")	
</pre>

# Interview Questions
<b>Python</b>
1. Difference between method and class?
2. What is dunder method?
3. What is `__init__()` in python?
4. Difference betweeb `__init__()` method and `__init__.py` file?
5. What is self in class?
6. What is MetaProgramming?
7. What is self, cls & static in class method?
8. What is static method, class method & instance method?
9. Difference in exec() and eval ()?
10. What is os and explain few operations on os?
11. What is MultiProcessing & MultiThreading? Give example program?
12. Different types of inheritance?
13. What is regular expression, explain match(), search() & findall()?
14. Create a pattern for IND mobile number extraction, email and url?
15. Working with file, give example of read and write file?
16. Difference in json load and dump? and how it is different from load vs loads & dump vs dumps?
17. Difference in .py and .pyc?
18. What is the difference between deep and shallow copying in Python?
19. What is the difference between range and xrange? How has this changed over time?
20. How do you iterate over a list and pull element indices at the same time?
21. I'm getting a maximum recursion depth error for a function. What does this mean? How can I mitigate the problem?
22. How does Python's list.sort work at a high level? Is it stable? What's the runtime?
23. What does this list comprehension do? Give one example of dictionary?
24. What is monkeypatching? How can you do it in Python?
25. Difference in pickling and unpicling? How it id differ from Serializer and Deserializer?
26. What is the use of enumerate() in Python?
27. Differentiate between append() and extend() methods ?
28. What is the different between range () and xrange () functions in Python?
29. What is the difference between del() and remove() methods of list?
30. What are the tools that help to find bugs or perform static analysis?
31. How Python is interpreted?
32. What is docstring in Python? How do you access/see the doc string?
33. List vs Tuple?
34. Set vs Frozenset?
35. What is a Module in a python?
36. What is Scope in function, explain global keyword?
37. Decorators? Give example?
38. Explain Python Logging?
39. What are higher ordered functions.
i. passing function as an argument.
ii. returning function on return statement.
40. Explain isinstance()
41. Nested function, Explain Closure in Python?
42. What is polymorphism?
```python
# Method Overloading (same method name, different parameter types or numbers)
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_op = MathOperations()
print(math_op.add(1, 2))      # Calls the method with 2 arguments
print(math_op.add(1, 2, 3))   # Calls the method with 3 arguments
```
44. What is Overriding? Explain Constructor Overriding?
45. Explain super() keyword?
46. What is Duck Typing?
47. What is Abstract Base Class. Explain concrete Methods in Abstract Base Classes?
48. Difference between Abstraction & Encapsulation?
49. How to raise a custom exception?
<pre>
class UnauthorizedUser(Exception):
    def __init__(self, message="You are Unauthorized!"):
        self.message = message
        super().__init__(self.message)

<b>Raise an error:</b>b>

name = "Fareen"
if name != "FareenAns":
        raise UnauthorizedUser

<b>Handling above exception</b>
name = "Fareen"
try:
    if name != "FareenAns":
        raise UnauthorizedUser
except UnauthorizedUser as e:
    print("ERROR %s" % e)
</pre>

49. What is yield?
<pre>
yield is a keyword in Python used in the context of creating generators. It's used within a function to indicate that the function 
should return a generator, which can be iterated over to produce a sequence of values one at a time. When yield is encountered, 
the current state of the function is saved, and a value is sent to the caller. The function can later be resumed from where it left off, 
continuing its execution.
</pre>

50. What is Generator?
<pre>
Example 1: generator

def my_generator():
    for i in range(100):
        yield i
gen = my_generator()

for item in gen:
    print(item)

 In this example, my_generator is a generator function that yields values one at a time. When you loop over the gen object,
 it processes one value at a time, just as you mentioned, which is more memory-efficient for large datasets.


Example 2:  normal function

def my_func():
    for i in range(100):
        return i

for loop that iterates over the range from 0 to 99. In this case, the entire range is generated in memory.
It doesn't load the entire range into memory at once, but it generates the values one at a time as needed by the loop.
</pre>

51. Iterator vs Iterable?
<pre>
Iterable: python list, tuple, dict are iterable, which is able to iterate.
Iterator: 
1. An "iterator" is an object used to iterate through an iterable.
2. It keeps track of the current state and knows how to access the next value.
3. An iterator is obtained from an iterable using the iter() function.
4. When no item left, it'll give StopIteration
5. Example:
lst = [1,2,3]
it = iter(lst)

print(next(it))
print(next(it))
print(next(it))         # 3, It keeps track of the current state and knows how to access the next value.
print(next(it))         # StopIteration
</pre>

52. What is context manager in python?
- In Python, context managers are a way to properly manage resources by ensuring that certain actions are taken before and after a block of code runs. They are typically used to manage resources like file handling, database connections, locks, etc., ensuring that setup and cleanup operations are automatically handled.
```python
with open('example.txt', 'r') as file:
    content = file.read()
# No need to call file.close(), it is done automatically after
```
53. Exception?
- Why exception: So when exception is not handled it'll show error and exit, when handled it'll show handled msg and dont exit.
- Eg: When reading file, try to open not existing file, will show error FileNotFoundError error and exit, when handled it'll show proper msg.
```python

x = 10
y = 0
try:
    z = x/y
except Exception as e:
    print('Exception occured:', e)
except ZeroDivisionError as e:        # this is invalid, code will never go in cuz it'll always run its parent exception above
    print('Exception occured ZeroDivisionError:', e)
except:
    print('This is default exception, if no other exception matched then this will run.')
else:
    print('No exception run else.', z)      # if no exception come this will run.
finally:
    print('This will always run no matter exception come or not.')
``` 

PENDING TOPICS:
1. What is property in class?
2. What is GC and how does GC works?
3. Is all the memory freed when Python exits?
4. How memory is managed in Python?



# Interview Questions with answer:
<b>Python</b>
1. What is dunder method?
<pre>
A method has double underscore before and after, these are special methods in python.
Example, __str__(), __init__(), __repr__() etc
</pre>

2. What is `__init__()` method?
<pre>
It is the first method which is called in python, it constructor in python. 
Use it when you want to pass some initial values in python.
</pre>

3. Difference betweeb `__init__()` method and `__init__.py` file?
<pre>
init method: In Python, the __init__ method is often referred to as the constructor method, and it's used to initialize
 the attributes or properties of an object when an instance of a class is created. You can use it to set some initial 
values for those attributes.
	
init file: In Django, the __init__.py file is a special file that indicates to Python that the directory 
containing it should be considered a Python package or module.
</pre>

5. What is self in class?
In Python, self is a convention, and not a reserved keyword, used to represent the instance of a class within the class itself. It is the first parameter of instance methods in Python. When you define a method within a class, the method should accept self as its first parameter.

6. What is MetaProgramming?
Metaprogramming, as mentioned earlier, involves writing code that generates, modifies, or analyzes other code at runtime. Example decorator.

7. What is self, cls & static in class method? 8. What is static method, class method & instance method?
<pre>
Static method: it is regular method having decorator to make it normal method.
Class Method: Class Method can directly access class variables. It also have decorator
Instance Method: Method of the class, which uses self.
</pre>

9. Difference in exec() and eval ()?
10. What is os and explain few operations on os?

11. What is MultiProcessing & MultiThreading?
<pre>
Difference in MultiProcessing & MultiThreading is MultiProcessing involves multiple processes and MultiThreading use different shards in one single process.
Give example program: see above
</pre>

20. How do you iterate over a list and pull element index at the same time?
<pre>
We can use enumerate() funtion.
</pre>

22. How does Python's list.sort work at a high level? Is it stable? What's the runtime?
<pre>
list.sort uses TimSort, which is a hybrid sorting algorithm derived from merge sort and insertion sort.
</pre>

30. What are the tools that help to find bugs or perform static analysis?
<pre>
There are many one of them is flake8. I use flake8.
</pre>

31. How Python is interpreted?
<pre>
Python is an interpreted language, which means that the Python code is executed line by line by an interpreter.
</pre>



================================================================================================================
# Extra Programming Excercise
This excercise is for practice, above excercise is enough for interview. This is extra.</br></br>

1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
<pre>
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
</pre>

<pre>
<b>SOLUTION</b>
import collections

lst = [19, 19, 15, 5, 3, 5, 5, 2, 5]
res = collections.Counter(lst)
if res[19] == 2 and res[5] == 3:
    print(True)
else:
    print(False)
</pre>

# To check what all parameters a class method accept
```python
import inspect

class Car:
    def get_car_details(self, a, b):
        return f'A: {a}, B:{b}'

c = Car()
res = inspect.signature(Car.get_car_details)
for res in res.parameters.values():
    print(res)

'''
self
a
b
'''

# Likewise for existing method like list
import inspect

res = inspect.signature(list.sort)
for res in res.parameters.values():
    print(res)

'''
self
key=None
reverse=False
'''
```

