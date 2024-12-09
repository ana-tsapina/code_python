class Dog: 

    def __init__(self, name, breed, age): 
        self.name = name
        self.breed = breed
        self.age = age 

    def bark(self): 
        print("Bark! ")

    def sniff(self, object): 
        if object.name: 
            print(f"{self.name} is curious about {object.name}")
        else: 
            print(f"{self.name} is curious about {object.name}")

class Cat: 

    def __init__(self, name , breed, age): 
        self.name = name
        self.breed = breed
        self.age = age 

    def meow(self): 
        print("meow! ")

    def __str__(self): 
        return f"{self.breed} named {self.name}."

    def __repr__(self): 
        return f"Cat(name = {self.name}, breed = {self.breed}, age = {self.age})"

dog1 = Dog("Marshall", "Westie", 3) # instance of dog class 
print(f"{dog1.name} is a {dog1.breed}")

dog1.bark()

cat1 = Cat("Garfield", "Tabby", 10)
print(f"{cat1.name} is a {cat1.breed}")

cat1.meow()

dog1.sniff(cat1)

text = str(cat1)
print(text)

print(repr(cat1))