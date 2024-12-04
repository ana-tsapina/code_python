from math import pi 

class Circle:  
    def __init__(self, radius, diameter): 
        self.__radius = radius 
        self.__diameter = diameter 

    def info(self): 
        return f"radius: {self.radius}, diameter: {self.diameter}"

    def cir(self): 
        return 2 * pi * self.radius 

    def area(self): 
        return pi * self.radius * self.radius

    @property 
    def radius(self): 
        return self.__radius
    @property 
    def diameter(self): 
        return self.__diameter

c1 = Circle(8, 16)


print(c1.info())
print(c1.diameter)
print(c1.area(), c1.cir())

    