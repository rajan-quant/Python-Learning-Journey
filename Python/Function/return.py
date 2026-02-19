#return in function is used to stop the function and come out from the function
def get_full_name (first_name,last_name):
    '''RETURN THE FULL NAME IN A NEATED FORMAT'''
    full_name = f'{first_name}{last_name}'
    return full_name #return statement

final_name = get_full_name("Rajan","Thakur")     
print("Full Name:",final_name)

"""
1- function name should be meaningful
2- length of function should be short
3- avoid global variables  

"""