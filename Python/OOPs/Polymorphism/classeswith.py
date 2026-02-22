#polymorphism with class method overriding

class Bird:
    def sound(self):
        print('Birds make sound')

class Crow(Bird):
    def sound(self):
        print("crow says 'caw caw'")

class parrot(Bird):
    def sound(self):
        print('parrot sounds "squawk"')

bird1 = Crow()
bird2 = parrot()

bird1.sound()
bird2.sound()