class Person: 
    def __init__(self, name, wealth): 
        self.name = name 
        self.wealth = wealth

    def info(self): 
        return f"Person (name: {self.name}), wealth: {self.__wealth}"

    @property 
    def wealth(self): 
        return self.__wealth 

    @wealth.setter
    def wealth(self, new_value):
        self.__wealth = new_value 


p1 = Person("mr. Park", 32)
p2 = Person("Marshal", 1000)
print(p1.wealth)
p1.wealth = 1234
print(p1.info())

