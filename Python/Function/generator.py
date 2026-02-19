#yield
def count_down(num):
    while num>0:
        yield num #yield- value one at a time
        num -= 1

#using the generators
for numbers in count_down(5):
    print(numbers)
