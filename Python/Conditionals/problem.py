#Take two number form user and ask to perform operation based on four coice +,-,*,/

"""num_1 = int(input('Enter a number:'))
num_2 = int(input('Enter another number:'))

choice = input('Enter your choice of operation : +,-,*,/ : ')

if choice == '+':
    add = num_1+num_2
    print(add)

elif choice == '-':
    sub = num_1-num_2
    print(sub)
elif choice == '*':
    mult = num_1*num_2
    print(mult) 
elif choice == '/':
    div = num_1/num_2
    print(div) 
else:
    print('INVALID CHOICE!')    

"""
# problem for loop
# print even number from 1-10
"""for num in range(1,11):
    if num % 2 == 0:
        print('even',num)
   # else:
      #  print('odd',num)    

for num in range(1,11):
    if num %2 != 0:
        print('odd',num)
"""
#program to skip number in the given range of num
#conditions: 
#1.starting num should be smaller than stoping num if not print invalid choice!
#2.skip num should be in range of nums if not then print invalid choice!s
"""
start = int(input('Enter the starting num:'))       
stop = int(input('Enter stoping num: '))
skip = int(input('Enter a number to skip in the range of numbers:'))


if start > stop:
    print('INVALID CHOICE! starting num should not be greater than stoping num.')
        

elif skip not in range(start,stop):
    print('INVALID CHOICE! skip num is not in range')
         
else:
     for num in range(start,stop):
        if num == skip:
                continue
        print(num)
"""

# Questions
"""
Take an integer input n.
If n is divisible by both 3 and 5, print "FizzBuzz"
If only divisible by 3, print "Fizz"
If only divisible by 5, print "Buzz"
Else print the number itself
📌 Focus: if / elif / else, logical operators

"""

"""num = int(input('Enter a number to check:'))

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')       """


"""n = int(input())
i = 0
while i<n:
    print(i**2) 
    i +=1"""
"""
n = int(input())
for i in range(n):
    print(i**2)    """