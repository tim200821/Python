inputNumber = int(input(" :"))
outputNumber = int(bin(inputNumber)[2:])


#print(outputNumber)

def getInfo():
        info = "\n InputNumber : %s\n OutputNumber : %i" % (inputNumber, outputNumber)
        print(info)
        return info

def start():
        
    while(True):
        print("Выбирете действие : \n "
              "1. toBin \n"
              "2. toDec \n"
              "3. toHex \n"
              "4. exit \n"
        )
        try:
            aInput = int(input(":"))
        except:
            exit(0) 
            
        match(aInput):
            case 1:
                getInfo()
                start()

            case _:
                exit(0)  

start()