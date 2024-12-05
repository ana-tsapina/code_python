class Animal: 
    def __init__(self,name): 
        self.name = name
    
    def __str__(self): 
        return f"Animal ({self.name})"

    def __repr__(self):
        return self.__str()

    def sound(self): 
        return "Urf!"

class Dog(Animal): 
    def info(self): 
        return "I am actually a dog"
    
    def sound(self): 
        return "bark bark"

a1 = Animal("Seal")
d1 = Dog("Marshall")

print(d1.sound())
print(a1.sound())