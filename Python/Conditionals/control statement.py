"""
control statement
1. break
2. continue
3. pass
"""
#1. break
"""for num in range(1,10,1):
    if num == 5:
        break
    print(num) """ 

#2. continue
"""for num in range(1,10,1):
    if ( num % 2 == 0):
        continue
    print(num)"""

#3. pass - it does nothing 
for num in range(1,10):
    if num == 5:
        pass
    print(num)