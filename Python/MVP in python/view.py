import Present
class view:
    
    def __init__(self):
        self.presenter = Present.presenter()

    def dogRegister(self):
        caption = input("enter dog name : ")
        age = int(input("Dogs age : "))
        return self.presenter.dogRegisterResualt(caption, age)

    def catRegister(self):
        caption = input("enter cat name : ")
        age = int(input("Cats age : "))
        return self.presenter.catRegisterResualt(caption, age)

    def start(self):
        while(True):
            print('Выберите животное' '\n'
            '1. Собака' '\n'
            '2. Кошка'    '\n'
            '3. Список животных' '\n'
            )
            try:
                InputNumber = int(input('Введите число : '))
            except:
                print("Error value")
                self.start()
           

            match(InputNumber):
                case 1:
                    self.dogRegister()
                    self.start()
                case 2:
                    self.catRegister()
                    self.start()
                case 3:
                    aList = self.presenter.getAnimalList()
                    for animal in aList:
                        animal.toString()
                case _:
                    exit(0)


