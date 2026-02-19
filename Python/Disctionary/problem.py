#Questions solved for dictionary

#Easy(1,2,and 3)
#1-Create a dictionary with 5 country-capital pairs and print all keys. 
"""
my_dict = {
    'nepal':'kathmandu','india':'delhi','china':'Bejing','japan':'tokyo','usa':'NewYork'
}
keys = my_dict.keys()
print(list(keys))
"""
#2.Write code to update the value of a specific key.
"""
my_dict = {
    'nepal':'kathmandu','india':'delhi','china':'Bejing','japan':'tokyo','usa':'NewYork'
}
print(my_dict)
my_dict.update({input('Enter a key to update:'):input('enter a value to update:')})
result = my_dict.items()
print(list(result))"""

#3.Delete a key form a dictionary
"""
my_dict = {
    'nepal':'kathmandu','india':'delhi','china':'Bejing','japan':'tokyo','usa':'NewYork'
}
print(my_dict)
my_dict.pop(input("Enter a key to delete:"),'Not found')
print(my_dict)"""

#medium(4 and 5)
#4.count how many keys are in a dictioary without using len().
"""
my_dict = {
    'nepal':'kathmandu','india':'delhi','china':'Bejing','japan':'tokyo','usa':'NewYork'
    ,'UK':'London'
}
count = 0
for i in my_dict:
    count +=1
print("No.of keys: ",count)"""

#5.Create a dictionary from two lists:
#keys = ["a","b","c"]
#values = [1,2,3]
"""
keys = ["a","b","c"]
values = [1,2,3]

my_Dict = dict(zip(keys,values))
print(my_Dict)"""

#Hard(6 and 7)
#6-Find the key with the maximu values in a dictionary

"""my_dict = {
    'a':1,'b':2,'c':3,'d':4,'e':5
}"""

#day 2 

#🧠 PART: DICTIONARIES
#🟢 Basic Level

# Q. Create a dictionary of 5 students and their marks. Print all names.
"""
my_dict = {
    'std1':56,'std2':60,'std3':69,'std4':47,'std5':90
}
result = my_dict.values()
print(list(result))"""

# Q. Write a function that takes a dictionary and returns the sum of all values.

"""
def sumOfElem(my_dict):
    result = 0
    for value in my_dict.values():
        result += value
    return result
my_dict = {
    'std1':56,'std2':60,'std3':69,'std4':47,'std5':90
}
sum = sumOfElem(my_dict)
print(sum)"""

# Q. Check if a key exists in a dictionary.
"""
my_dict = {
    'std1':56,'std2':60,'std3':69,'std4':47,'std5':90
}
if my_dict.keys() == input("Enter a key to check: "):
    print('Key is present')
else:
    print("Key is not present")"""

# Q .Count how many times each character appears in a string using dictionary.
"""
str = input('Enter any string: ').lower()
#str = input('Enter any string: ').lower().replace(" ","")
my_dict = {}

for i in str:
    if i == " ":
        continue
    
    if i not in my_dict:
        my_dict[i] = 1 
        
    elif i in my_dict:
        my_dict[i] +=1 
        
print(my_dict)"""

# Q.Merge two dictionaries.
"""
std1 ={
    'name':'Rajan','semester':'2nd'
}
std2 = {
    'name1':'Suman','semester':'2nd'
}
for i in std2:
    std1[i]=std2[i]

print(std1)"""

#🟡 Intermediate Level
#Create a dictionary from two lists (keys list and values list).

"""key = ['name','section','semester']
value = ['Rajan','CSE-14','2nd']
dis ={}

if len(key)!=len(value):
        print("Not appropriate arrangement of data!!")

for i in range(len(key)):
            
        dis[key[i]] = value[i]

print (dis)"""

# or
"""
keys = ['name','section','semester']
values = ['Rajan','CSE-14','2nd']

dis = dict(zip(keys, values))
print(dis)"""
"""
d1 = {'a': 2, 'b': 3}
d2 = {'a': 5, 'c': 4}

def merge_and_add(d1,d2):   
  for key in d2:
    if key in d1:
        d1[key] += d2[key]
    else:
        d1[key] = d2[key]
    return d1
dirt = merge_and_add(d1,d2)
print(dirt)"""


