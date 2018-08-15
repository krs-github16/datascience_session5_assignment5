# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:14:38 2018

@author: disiz
"""
"""
-Session 5
-Assignment five
"""
##assignmnet 5 question 1
def division(n1,n2):
    try:
       # You do your operations here;
        e=int(n1)/int(n2)
    except ZeroDivisionError:
        #If there is Exception, then execute this block.
        print("-"*50)
        print("You are trying to divide a number by 0, i wasn't trained for this kind of scenario.I kindly request you not to divide any number by 0 in future.In python it would be treated as 'ZeroDivisionError'")
    else:
        # If there is no exception then execute this block.
        print("divison would be successful as long as denominator is not zero")
        print("o/p of division is %0.2f" %e)
    finally:
        # exception present or not ,this would be executed.
        print("-"*50)
        print("end of exception handling")
op=division(5,0)
print("-"*100)
print('\n')
##assignmnet 5 question 2
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
# list comprehension-lc
lc=[(i+' '+j+' '+k) for i in subjects for j in verbs for k in objects]
for l in lc:
    print(l)
print("-"*100)
print('\n')
print("End of assignment")
