from Model import *
from view import *
import sys
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
            sys.exit()