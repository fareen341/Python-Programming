#string formating
#replacement operator {}
print('hello{}'.format('python'))                #hellopython

#1.using index
print('Name:{2},Roll No:{1},Weight:{0}'.format(45.66,1,'fareen'))

#2.using keywords
print('Name:{name},Roll No:{r_num},Weight:{wt}'.format(wt=45.66,name='fareen',r_num=1))

#3.using keywords
name,roll='fareen',1
print('Name={},Roll num={}'.format(name,roll))

#Format string(%) %s=for string, list, tuple, set, dict----------------------------------------------------------------------------------------------
a="""My name is %s and roll number %d
            and my name starts with %c and weight is %f""" %('fareen',1,'f',55.56)                # cannot be done in replacement which is the specility of % operator
print(a)

print('Hello{%.2f}'%(77.888888))
print('Hello %s ,Your marks are:%s'%('fareen',[10,20]))

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


#f-string------------------------------------------------------------------------------------------------------------------------------------------------------------
n='fareen'
p=f"{n}"
'''
'fareen'
'''

#using '<' and '>'
n="""fareen"""
p=f"""{n:>7}"""
print(p)
'''
 fareen

one space and 6 chars =7
'''

#it gives only one bracket{}
n="""fareen"""
p=f"""{{{n}}}"""
print(p)
'''
{fareen}
'''
