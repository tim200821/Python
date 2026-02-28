import  abc
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

while(True):
    print('Выберите животное' '\n'
        '1. Собака' '\n'
        '2. Кошка'    '\n'
        '3. Дракон' '\n'
        '4. все')
    InputNumber = int(input('Введите число : '))
    
    match InputNumber:
        case 1:
            dog = Dog("Собака" ,7)
            print(dog.GetInfo())
            break
        case 2:
            cat = Cat("Кошка" , 8)
            print(cat.GetInfo())
            break
        case 3:
            drag = Drago("Дракон" , 125)
            print(drag.GetInfo())
            break
        case 4:
            dog = Dog("Собака" ,7)
            print(dog.GetInfo())
            cat = Cat("Кошка" , 8)
            print(cat.GetInfo())
            drag = Drago("Дракон" , 125)
            print(drag.GetInfo())
        case _:
            exit(0)

a = [1, 2 ,3, 4]
a = arr.array([1, 2, 3, 4])

            

    



