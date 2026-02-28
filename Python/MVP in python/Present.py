import Model
class presenter:

    def __init__(self):
        self.commonList = Model.animalList

    def dogRegisterResualt(self, name, age):
        try:
            dog = Model.Dog(name, age)
            self.commonList.append(dog)
            return dog.GetInfo()
        except:
            return "Creation Error"
        
    def catRegisterResualt(self, name, age):
        try:
            cat = Model.Cat(name, age)
            self.commonList.append(cat)
            return cat.GetInfo()
        except:
            return "Creation Error"
        
    def getAnimalList(self):
        return self.commonList
    
    