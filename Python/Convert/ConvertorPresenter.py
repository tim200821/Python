from ConvertorModel import toBinary, toDecimal, toHexadecimal

class Presenter:

    
    def toBinResult(self, inputNumber):
        try:
            result = toBinary(inputNumber).convert()
            return result.getInfo()
        except Exception as e:
            print(f"Error Presenter 0x001: {e}")
        
    def toDecResult(self, inputNumber):
        try:
            result = toDecimal(inputNumber).convert()
            return result.getInfo()
        except Exception as e:
            print(f"Error Presenter 0x002: {e}")
        
    def toHexResult(self, inputNumber):
        try:
            result = toHexadecimal(inputNumber).convert()
            return result.getInfo()
        except Exception as e:
            print(f"Error Presenter 0x003: {e}")
        
