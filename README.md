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













# Python Basics:
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
</pre>

<b>Operations on set</b>
1. insertion order are not preserved
2. duplicate are not allowed
3. indicated by{}
4. set item are not indexed so slicing and indexing not allowed
5. immutable
6. we can add and remove item in set but cannot change the value by using index.
7. main fucntionality of set is, union, difference & intersetion
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

<b>Extra functions:</b>
<pre>
1. Memory location
a = 10
id(a)			# will give memory location of a

2. chr() function, to get number from unicode
chr(65)			# A

3. ord() function to get unicode from character
ord('A')		# 65

4. floor and ceil
from math import floor, ceil

floor(4.5)		# 4
floor(4.8)		# 4

ceil(4.5)		# 5
ceil(4.1)		# 5
</pre>

<b>Extra points</b>
<pre>
1. Floating point error:
0.1 + 0.2			# 0.30000000000000004

Getting wong error, we should get 0.3

2. When we do -4 // 3, we should get one as quotent, but we get -2, 
-4 // 3		# -2

This is cuz it does the floor division, in case of minus floor acts as ceil and vice versa.

3. The __init__ method: it is called automatically when you create a new instance of a class (an object). 
It is the constructor for the class, and it allows you to perform any necessary setup or initialization for the object.
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

