import sys, abc
class Animal(abc.ABC):
    def __init__(self, name,  age):
        self.animal = name
        self.age = age

    def speak(self):
        pass 
    
    def GetInfo(self):
        A = "\n Кличка : %s\n Возраст : %i " % (self.animal, self.age)
        return A
class Dog(Animal):
    def speak(self):
        return f"{self.animal} говорит : Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.animal} говорит : Мяу!"
    
class Drago(Animal):
    def speak(self):
        return f"{self.animal} говорит : Аррррр!"
