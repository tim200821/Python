import abc

class model(abc.ABC):

    def __init__(self, inputNumber, outputNumber = None):
        self.inputNumber = inputNumber
        self.outputNumber = outputNumber
        pass

    def getInfo(self):
        info = "\n InputNumber : %s\n OutputNumber : %i" % (self.inputNumber, self.outputNumber)
        print(info)
        return info

class toBinary(model):
    def convert(self):
        self.outputNumber = int(bin(self.inputNumber)[2:])
        return self
class toDecimal(model):
    def convert(self):
        #decimalNumber = int(self.inputNumber, 0)
        try:
            if isinstance(self.inputNumber, int):
                self.outputNumber = str(self.inputNumber)
                tmp = int(self.outputNumber, 0)
            else:
                self.outputNumber = self.inputNumber
            return self
        except ValueError:
            print("Error value 'model 0x001'")


class toHexadecimal(model):
    def convert(self):
        self.outputNumbers = hex(self.inputNumber)[2:].upper()
        return self



    
