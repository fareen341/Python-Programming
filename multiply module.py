#USER DEFINED MODULE

'''
    This is mult module.

    This module can multiple the given numbers.
    It can have one number,two and n numbers.
'''


def mult(x=0):
    '''
        This function takes one argument and returns the multiply of it.
        If nothis is provide gives 0.
    '''
    return x*x


def mult_var_len(*l):
    '''
        This function takes n number of argument and return the multiply of all numbers.
    '''
    x=1
    for i in l:
        x=x*i
    return x

__author__='fareen'
__copyright__='copyright 2020'


#IMPORTING USER DEFINED MODULE IN ANOTHER FILE
#first import the module and than check the things related to it
import multiply

print(multiply.mult(3))                 #op---9


#USING help('multiply') GIVES THE DOCUMENTATION ON MULTIPLY MODULE
help(multiply)

#USINF dir() GIVES ALL THE MEMBERS RELATED TO multiply() FUNCTION
dir(multiply)

#USING doc GIVE THE DOCUMENTATION ON PARTICULAR FUNCTION
print(multiply.mult.__doc__)


