#IDENTITY OPERATOR is used to compare memeory of two objects
"""
is- Return 'True' if     the memory location is same
is not - Return 'True' if the memeory location in not same
"""

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)
print(a is not c)