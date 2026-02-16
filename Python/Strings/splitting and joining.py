# split
# string.split(",")

"""str = 'a,b,c'
s = str.split(",")
print('after spliting:',s)

# join(iterable)
result = ",".join(s)
print("after joiningr",result)

"""

line = input()
def split_and_join(line):
    s = line.split(" ")
    j = "-".join(s)
    return j
result = split_and_join(line)
print(result)