#1- square bracket
'''my_list = [1,2,3,4.5,'PYthon',True]
print(my_list)
'''
#2- using list constructors
"""my_list1 = list((1,2,3,4.5,'python',False))
print(my_list1)
"""
#3,4.- list comprehension and range()

#using range 
"""
start-1
stop-100
step-1
it is exclusive
"""
"""num = list(range(1,101,1))
print(num)
"""

#4 - list comprehension

"""
syntax:-
[expression for item in iterable if condition]
expression - x*2 or 2+3 ....
item - range(1,11,1)
condition (optional) 

"""
"""square = []
for i in range(1,11):
    square.append(i**2)
print(square)"""

square = [i**2 for i in range(1,15) if i%2 == 0]
print(square)