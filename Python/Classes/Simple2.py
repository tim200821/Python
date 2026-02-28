#class Person:
# 
#    def __init__(self, name, age):
#        self.name = name        # имя человека
#        self.age = age          # возраст человека
#     
#    def display_info(self):
#        print(f"Name: {self.name}  Age: {self.age}")
# 
# 
#tom = Person("Tom", 22)
#tom.display_info()      # Name: Tom  Age: 22
# 
#bob = Person("Bob", 43)
##bob.display_info()      # Name: Bob  Age: 43
#
#class Person:
#  
#    def __init__(self, name):
#        self.name = name
#        print("Создан человек с именем", self.name)
#        #конструктор класса, создает экземпляр класса
#     
#    def __del__(self):
#        print("Удален человек с именем", self.name)
#        #деструктор класса, уничтожает экземпляр класса
#  
#tom = Person("Tom")
#
#class Person:
#    def __init__(self, name, age):
#        self.name = name    # устанавливаем имя
#        self.age = age      # устанавливаем возраст
#                 
#    def print_person(self):
#        print(f"Имя: {self.name}\tВозраст: {self.age}")
#         
# 
#tom = Person("Tom", 39)         # создает экземляр класса "Person"
#tom.name = "Человек-паук"       # изменяем атрибут name
#tom.age = -129                  # изменяем атрибут age
#tom.print_person()              # Имя: Человек-паук     Возраст: -129
#
#class Person:
#    def init__(self, name, age): # отрибуты с __Имя_отрибута инкапсулированный и являются приватными
#        self.__name = name    # устанавливаем имя
#        self.__age = age       # устанавливаем возраст
#                  
#    def print_person(self):
#        print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#          
#  
#tom = Person("Tom", 39)
#tom.__name = "Человек-паук"     # пытаемся изменить атрибут __name
#tom.__age = -129                # пытаемся изменить атрибут 
#tom.print_person()              # Имя: Tom        Возраст: 39
#
#class Person:
#    def __init__(self, name, age):
#        self.__name = name    # устанавливаем имя
#        self.__age = age       # устанавливаем возраст
#                  
#    def print_person(self):
#        print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#          
#  
#tom = Person("Tom", 39)
#tom._Person__name = "Человек-паук"     # изменяем атрибут __name
#tom.print_person()              # Имя: Человек-паук        Возраст: 39
#
class Person:
    def __init__(self, name, age):
        self.__name = name    # устанавливаем имя
        self.__age = age       # устанавливаем возраст
 
    # сеттер для установки возраста
    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")
 
    # геттер для получения возраста
    def get_age(self):
        return self.__age
 
    # геттер для получения имени
    def get_name(self):
        return self.__name
     
    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")
          
  
tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.print_person()  # Имя: Tom  Возраст: 25