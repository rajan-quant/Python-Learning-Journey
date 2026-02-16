"""a = [1,2,3]
a.pop(1)
print(a)"""

#list comprehension problems
#Q.1 list of odd numbers:
"""
result = [x for x in range(1,7) if x%2 !=0]
print(result)"""

#Q.2 list of constants:
"""
result = [x for x in "machinelearning" if x not in "aeiouAEIOU"]
print(result)"""

#Q.3 list of square of numbers divided by three
"""
result = [x**2 for x in range(1,21) if x%3 == 0]
print(result)"""

#Q.4 Replace even num with 'e' and odd num with 'o' from 1 to 10
 
"""
result = ['e' if x%2 == 0 else 'o' for x in range (1,11)]
print(result)"""

#5.Extract digits from a string
"""
result = [x for x in "abc123def45" if x in ('0123456789')]
print(result)"""

#6.From a list, keep numbers greater than average
"""
lst = [10,20,30,40,50]
result = [x for x in lst if x > (sum(lst)/len(lst))]
print(result)"""

#7.convert a list of words into their lenghh
#eg- ['ml','python','learn'] - [2,6,5]

lst = ['ml','python','learn']
result = [len(x.split()) for x in lst if len(x.split(",")) in range(0,101)]
print(result)
