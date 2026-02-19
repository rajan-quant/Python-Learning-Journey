"""
burger - function
extra cheese - extra features

main function>function add
without changing the main function code
"""
#decorator creation
def my_decorator(func):
    def wrapped():
        print("something is happening before function is called")
        func()
        print("something is happening after function is called" )
    return wrapped
@my_decorator
def say_hello():
    print("hello")

say_hello()