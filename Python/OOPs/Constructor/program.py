#programming example of constructor
class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

std1 = student('Rajan',21,"A+")
std2 = student('Chandan',20,'A+')

print(std1.name,std1.age,std1.grade)
print(std2.name,std2.age,std2.grade)

