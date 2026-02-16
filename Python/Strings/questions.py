"""password = str(input('Enter a password:'))

if len(password)>5:
    print('login successful')
else:
    print('login fail !!! length of password is < 5')"""


#question realated to memeber operatior for string

"""email = str(input('Enter you email:'))

if '@' in email:
    print('Valid Email')
else:
    print('Invalid email')"""

#Questions to solve:-
"""
Question 2 (Strings)
Problem:
Take a string input.
Count how many vowels are present in the string
Print the count
📌 Focus: strings, loops, in operator

"""
"""str = input('Enter a string to check:')
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for i in str:
    if i in vowels:
        count += 1

print(count)"""

#OR

"""str = input('Enter a string to check:').lower()
vowels = 'aeiou'
count = 0
for i in str:
    if i in vowels:
        count += 1

print(count)  """     
#both the logic are correct but the below one is more practical


"""
Question 3 (Conditionals + Strings)
Problem:
Take a string input.
If the string is a palindrome, print "Yes"
Else print "No"
(A palindrome reads the same forward and backward, e.g. madam, level)
📌 Focus: string slicing, condition checkingQuestion 3 (Conditionals + Strings)

"""
"""str = input('Enter a string to check :')

if str == str[::-1]:
    print('Palindrom')
else:
    print('Not Palindrom')    

"""
#or

"""print("Palindrome" if (s := input()) == s[::-1] else "Not Palindrome")
"""

"""
Write a Python progam:
input a string
if length is even - print "Even Length:
Else - print "Odd Length"

"""

"""str = input('Enter a string:')

if len(str) % 2 == 0:
    print("Even Length")
else:
    print('Odd Length')    """



