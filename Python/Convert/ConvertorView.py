from ConvertorPresenter import Presenter


class View:
   
    def __init__(self):
        self.presenter = Presenter()

    def toBinRegister(self):
        try:
            b_input = int(input("Введите число для перевода в двоичную систему: "))
            print(self.presenter.toBinResult(b_input))
        except ValueError:
            print("Error value 'View 0x001'")

    def toDecRegister(self):
        b_input = input("Введите число (в двоичной/шестнадцатеричной системе) для перевода в десятичную: ")
        print(self.presenter.toDecResult(b_input))

    def toHexRegister(self):
        try:
            b_input = int(input("Введите число для перевода в шестнадцатеричную систему: "))
            print(self.presenter.toHexResult(b_input))
        except ValueError:
            print("Error value 'View 0x002'")
    def start(self):
        
        while True:
            print("Выбирете действие : \n "
                  "1. toBin \n"
                  "2. toDec \n"
                  "3. toHex \n"
                  "4. exit \n"
            )
            try:
                aInput = int(input("Введите число : "))
            except ValueError:
                print("Error value 'View 0x003'")
                self.start()

            match(aInput):
                case 1:
                    self.toBinRegister()
                case 2:
                    self.toDecRegister()
                case 3:
                    self.toHexRegister()
                case 4:
                    print("Exit from program")
                    exit(0)




