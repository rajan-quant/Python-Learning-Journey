"""
parameters - placeholders for the values
arguments - values that we pass
"""
"""def greet(name):     #parameters
    '''display HI to the user'''
    print("Hi",name)

greet("Rajan Thakur") #arguments"""

"""
Type of arguments
1- positional argument
2-keyword argument
3-default argument
"""
#1-positional argument

"""def greet(name ,city):     #parameters
    '''display HI to the user'''
    print(f'Welcome {name} to the {city}')

greet("Rajan Thakur","janakpurdham-07") #arguments"""

#2-keyword arguments

"""def greet(name,city):     #parameters
    '''display HI to the user'''
    print(f'Welcome {name} to the {city}')

greet(name = "Rajan Thakur",city ="janakpurdham-07") #arguments"""
#this is key argument example.

#3-default arguments 

def greet(name='rajan',city='janakpur'):     #parameters
    '''display HI to the user'''
    print(f'Welcome {name} to the {city}')

#greet(name = "Rajan Thakur",city ="janakpurdham-07") #arguments
greet("rajanthakur","banglore")#if arguments is given then this works
greet()#if i dont pass any argument then default parameter arguments works