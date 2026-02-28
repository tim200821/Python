import abc
class Animal(abc.ABC):
    def __init__(self, name,  age):
        self.name = name
        self.age = age

    def GetInfo(self):
        A = "\n Name : %s\n Age : %i " % (self.name, self.age)
        return A
class Dog(Animal):
    def GetInfo(self):
        A = super().GetInfo(self) + "\nAnimal is Dog"
    def Type(self):
        return "dog"
    def toString(self):
        print("dog %s" % self.name)

class Cat(Animal):
    def GetInfo(self):
        A = super().GetInfo(self) + "\nAnimal is Cat"
    def Type(self):
        return "cat"
    def toString(self):
        print("cat %s" % self.name)
        
animalList = []
def AddtoList(animal):
    animalList.append(animal)