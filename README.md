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

# shallow copy
original_list = [1,2,3]
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[1] = 88
print(shallow_copied_list)
print(original_list)

# deep copy
original_list = [1,2,3]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[1] = 88
print(original_list)
print(deep_copied_list)
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
In Python, decorators are a powerful and flexible way to modify or enhance the behavior of functions or methods without changing their source code.
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

6. eval(): Essentially, it allows you to run Python code from a string.
<pre>
nums_list = "[1,2,3,4]"
print(type(nums_list))			# <class 'str'>
result = eval(nums_list)
print(type(result))			# <class 'list'>
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
0.1 + 0.2			# 0.30000000000000004

Getting wong error, we should get 0.3

2. When we do -4 // 3, we should get one as quotent, but we get -2, 
-4 // 3		# -2

This is cuz it does the floor division, in case of minus floor acts as ceil and vice versa.
</pre>


# Getting Help In Python(help, dir & pydoc).
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

# Use of pydoc module.
So it is a module, this command will not work on shell, get outside of shell and run:
$ python3 -m pydoc list
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

# Json dump and load
1. json.dump - serializer, converting python complex data type into json format.
2. json.load - deserializer, converting json data back to python complex data type.
<pre>
import json

data = {"name": "Fareen", "age": 25}

with open("data.json", 'w') as file:
    json.dump(data, file)

with open("data.json", 'r') as file:
    json_data = json.load(file)

print(json_data)
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

# Programs Practice
1. Get the 2nd larget value in a list
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
</pre>
7. Remove duplicate from a list num_list = [3,4,6,3,4,7].
8. Length of last word str = "python is great, it has many features".
9. In the given list arr = [5, 32, 45, 4, 12, 18, 25], do minus of first element with second.
10. Find all the pairs which has sum = 17 in the given list arr = [5, 7, 4, 3, 9, 8, 19, 21].
11. Find all the missing values in list arr = [1,2,3,5,6,7,8,10,17].
12. Convert two list into dict x = [1,2,3,4], y = ["a", "b", "c", "d"].
13. Find the count of word "python" in the given string, str = "python is great, it has many features, python".
14. Find the common element in two str, name = "Seema" and name = "FarEen", by repetation of words and without repetation also. Also ignoring the case.
15. Calculate sum of all numbers in a list using recursion nums = [1,2,3,4,5,6] also print sum as fibonacci series like 1+2 = 3 so on.

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


# Programming Answers
15. Calculate sum of all numbers in a list using recursion nums = [1,2,3,4,5,6] also print sum as fibonacci series like 1+2 = 3 so on.
<pre>
def recursive_sum(n):
    if not n:  # Base case: the list is empty
        return 0
    else:
        rec = recursive_sum(n[1:])
        sum = n[0] + rec
        print(f'{n[0]} + {rec} = {sum}')
        return sum

n = [1, 2, 7, 1, 9]
x = n.reverse()
result = recursive_sum(n)
print(result)

Note: taking rec in a variable cuz, if we take recursive_sum(n[1:]) it'll call the self function again
</pre>
