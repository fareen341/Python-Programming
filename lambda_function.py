#Lambda Function
#normal function
def name(fname,lname):
    return (f'Full name:{fname.title()}{lname.title()}')

#lambda function
n=lambda fname,lname:f'Full name:{fname.title()}{lname.title()}'
print(n('fareen','ansari'))
'''op-
Full name:fareenansari
'''

#*args, **kwargs
fun=lambda *args:args
print(fun(1,2,3,4))

fun=lambda **kwargs:kwargs
print(fun(python=20,java=30))
'''op:
(1, 2, 3, 4)
{'python': 20, 'java': 30}
'''

#sorting a list using lambda function
subject_marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key = lambda x: x[1])
print(subject_marks)
'''op
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

#sorting dict
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)

#even,odd using lambda
fun=lambda x:x%2 and 'odd' or 'even'
k=int(input())
print(fun(k))

#Maximum number of a list using lambda
import functools
l=[10,20,50,30,40]
print(functools.reduce(lambda x,y:x if x>y else y,l))
'''op-50'''
