#1.append method
#if i want to add element on the end of the list - append method is used
"""a = [1,2,3,4]
a.append(5)
print(a)"""

#2.extend method
"""if i have two list and i want the elements of 2nd list in 1st list
 or vice versa then i will use extend method"""
#eg:-
"""lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.extend(lst2)
print(lst1)"""

#3.insert method
"""
if i want to insert an element in any position 
i will use insert method

this will not delete or remove any thing just insert that element on that position
"""

"""
lst1 = [1,2,3,4,5]
lst1.insert(0,'hello')
print(lst1)
"""

#4.remove method
# if i want to remove any element from list - i will use remove method
"""lst = [1,2,3,4,5]
lst.remove(3)
print(lst)"""

#5.pop method
"""
if i want to remove element using indexing - i will use pop method
pop - returns the element which is removed.
 """
"""a = [ 1,2,3,4,5]
popped = a.pop(0)
print(popped,a)"""

#6.clear method
"""
if i want to clear all elements from the list
i will use clear method"""

"""lst = [ 1,2,3,4,5]
lst.clear()
print(lst)"""

#7- index method
"""
if i want to know the index of a specific element from a list 
i will use index method
"""
"""lst = [1,2,3,4,5,6,7]
index = "index is:",lst.index(6)
print(index)"""

#8.count method
"""
if i want to count how many same elements are in a list
i will use count method
"""
"""
lst = [1,2,3,4,1,1,2,3,4,3,4,5,6,34,56,4,6,7,7]
count = lst.count(10)
print(count)"""


#9- sort method
"""lst = [99,35,27,39,73,938,0,873,-736,983,-743,]
lst.sort()
#lst.reverse()
print(lst)"""

#10. reverse method
"""a = [2,34,64,75,333,-736,0,35]
a.reverse()
print(a)"""

#11-copy method

"""a = [ 1,2,3,4]
a1 = a.copy()
a1.append(5)

print(a,a1)
"""

#12- min and max method
#-used to find minimum and maxinum value in list
"""lst = [99,35,27,39,73,938,0,873,-736,983,-743,]
print('min:',min(lst))
print('max:',max(lst))"""

