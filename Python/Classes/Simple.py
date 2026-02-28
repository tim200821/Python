# У класса могут быть (Фукций, методы и свойства)
# А задовать свойства и получать их можно тремя способами (1) через конструктор , (2) зделать свойства публичными , (3) через get(гетторы) set(сетторы))




#Пример 1
#Класс простейщий 
#pass Ничего не делать (передать)
class Simple:
    pass

sample1 = Simple()
sample2 = Simple()

print(sample1, sample2)
#выводит  <__main__.Simple object at 0x00000198650E86E0> <__main__.Simple object at 0x00000198650EC550>

#Пример 2
class Simple:

#def init это конструктор    
    def __init__(self):
        print("Создание объекта Simple")
        

sample1 = Simple()
sample2 = Simple()

print(sample1, sample2)
#Выводит
#Создание объекта Simple
#Создание объекта Simple
#<__main__.Simple object at 0x000001CB6D5B8830> <__main__.Simple object at 0x000001CB6D5BC690>

#Пример 3
class Person:
 
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
    def say_hello(self):
        print("Hello")
    def say(self, message):     # метод 
        print(message)
    
 
 
tom = Person("Tom", 22)
 
# обращение к атрибутам
# получение значений
print(tom.name)     # Tom
print(tom.age)      # 22
# изменение значения
tom.age = 37
print(tom.age)      # 37


#------------------------------------------------
#Особенность Python (Динамическое создание)
tom.family = "Ivanoff"
print (tom.family)
#------------------------------------------------
tom.say_hello()
tom.say("O my god")


#Пример 4
