#example of try and except 

try:
    num = int(input('Enter a number: '))
    res = 10/num
    print(f'result: {res}')

except ZeroDivisionError:
    print('You cannot divide with zero (0)')

except ValueError:
    print('you cannot divide with strig')