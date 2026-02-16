#Methods
#1 - get()
profile ={
    "name":"raju",'age':21,'salary':'30lakh',
}
"""age = profile.get('age1','Not Found')#if value is not in dict.. ie. Not Found is given
print(age)"""

#2- keys()
#keys = profile.keys()
#print(keys)#this returns a touple of keys
#print(list(keys)) #this will return a list of keys

#3- values() if i just want to get the values 
"""values = profile.values()
print(list(values))
"""

#4. items() to access both key and values
"""
items = profile.items()
print(list(items))"""

#5.pop() to delete a key from the dictionary
"""poped = profile.pop('age','Not Found')
print(poped)
print(profile)"""

#6.popitems() - delete the last key:pair of our dictionary
 
"""
popped_i = profile.popitem()
print(popped_i)
print(profile)"""

#7.clear() - to delete all the key:value paris form the list
cleared = profile.clear()
print(cleared)
print(profile)