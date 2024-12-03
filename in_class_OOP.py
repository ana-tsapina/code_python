from random import randrange 

class Monster: 
    def __init__(self, name): 
        self.name = name 
        self.hp = 10 
        self.dmg = randrange(1, 10)

    def info(self):
        data = f"Monster ({self.name}, HP: {self.hp}, DMG: {self.dmg})"
        return data
    
    def attack(self, other_monster): 
        if other_monster.hp > 0: 
            other_monster.hp = other_monster.hp - self.dmg 
        else: 
            print("It's dead")

m1 = Monster("Megatron")
m2 = Monster("Expo Marker")
print(m1.info())
print(m2.info())
m1.attack(m2)
print(m2.info())


