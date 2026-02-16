#used if we have multiple conditions to check

age = int(input('Enter Your age:'))
if age>=18 and age<=100:# only execute if the condition is true; othersie not execute.
    print('You are eligible to vote')
elif age<=0:
    print('Invalid age:')    
elif age>=200:
    print('Age is more than 100!')    
else:
    print('You are not eligible to vote:Your age is <18')
    