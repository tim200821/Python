myobject = {}
def personal(obj): 
    FIO = input("Set Your fullname: ")
    age = int (input("Set your age: "))
    phone = input("Set Your phone: ")
    obj={}
    obj["personal"]={"Name":FIO,"age":age, "CallTo":phone}
    return obj

def adress(obj):
    street = input("Your street: ")
    building = input("Your home number: ")
    apartment = input("yout apartment: ")
    obj["address"] = {"Street": street, "Building": building, "appartment":apartment} 

def stade

myobject = personal(myobject)
adress(myobject)

print(myobject)






 
#def showme(): 
#    print(ObjectToString (myobject))