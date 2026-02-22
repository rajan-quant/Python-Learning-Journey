

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #no implamentation

class car(Vehicle):
    def start(self):
        print('CAR STARTS WITH A KEY')

class Bike(Vehicle):
    def start(self):
        print('Bike start with a button')

Car = car()
bike = Bike()

Car.start()
bike.start()