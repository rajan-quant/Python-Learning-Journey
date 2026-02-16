"""
if condition:
   group of statement
"""
age = int(input('Enter Your age:'))
if age>=18:# only execute if the condition is true; othersie not execute.
    print('You are eligible to vote')
else:
    print('You are not eligible to vote:Your age is <18')
    