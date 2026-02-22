"""
 __init__()
"""
"""class car:
    def set_details(self,brand,color):
        self.brand = brand
        self.color = color

#creating object
car1 = car()
car1.set_details('RangeRover','White') 
print(car1.brand)
print(car1.color)
"""
#same progam with constructor

class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

car1 = car('RangeRover','White')
print(car1.brand)
print(car1.color)