# nested try - except eg:
try:
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter a number:'))
    try:
        result = num1/num2
        print(f'result: {result}')
    
    except ZeroDivisionError:
        print('You cannot divide by zero')

except ValueError:
    print('You must provide a valid input!')

     