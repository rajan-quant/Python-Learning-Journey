#Questions and  solving related to funcition Module in 'Python'.

#🧠 PART 1: FUNCTIONS (Level: Beginner → Strong)
#🟢 Basic Level

# Q.Write a function that returns the square of a number.
"""
n = int(input('Enter a num:'))
def square(n):
    sqr = n*n
    return sqr

s = square(n)
print(s)"""

# Q. Write a function that takes two numbers and returns the larger one.
"""
num1 = int(input('Enter a num1: '))
num2 = int(input('Enter another num2: '))

def largeNum(num1,num2):
    if num1>num2:
        #print("NUM 1 is greater")
        return num1
    else:
       # print("Num2 is greater")
        return num2
    
large = largeNum(num1,num2)
print("Larger Number is",large)"""

# Q. Write a function that checks if a number is even or odd.
"""
num = int(input('Enter a num to check:'))

def Even_or_Odd(num):
    if num%2 ==0:
        print("Number is Even")
    else:
        print("Num is Odd")

Even_or_Odd(num)
"""

# Q. Write a function that returns the factorial of a number.
"""
num = int(input('Enter a num to check:'))

def factorial(num):
    if num ==0:
        return 1
    else:
        return num*factorial(num-1)

res = factorial(num)
print(res)
    """

# Q. Write a function that counts how many digits are in a number.
"""
num = int(input('Enter a num to check:'))
count = 0

def counts(num):
    num = abs(num)
    return len(str(num))

digit = counts(num)
print("Digits in a Number: ",digit)
"""

#🟡 Intermediate Level

# Q. Write a function that returns the reverse of a number and check it is a palindrome or not.
"""
num = int(input('Enter a num to reverse:'))
def reverse(num):
    rev = 0
    org = num
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num//=10
    if org == rev:
        print("It is palindrome")
    else:
        print("It is not a palindrome")
    return rev

res = reverse(num)
print("Reverse of a number: ",res)"""


# Q. Write a function that takes a list and returns the maximum value.
"""
lst = list(map(int,input('Enter values of list:').split()))

def max_value(lst):
    value = max(lst)
    return value
Max = max_value(lst)
print("Maximum Value in List: ",Max)
"""

# Q. Write a function that removes duplicates from a list.
"""
lst = list(map(int,input('Enter values of list: ').split()))

copy = []
dupli=[]

def duplicate(lst):
    for num in lst:
        if num in copy:
            dupli.append(num)
        else:
            copy.append(num)

duplicate(lst)
print("Removed Duplicate values list: ",copy)"""

