from math import sqrt 

class Vector: 
    def __init__(self, x, y): 
        self._x = x 
        self._y = y 

    @property 
    def x(self): 
        return self._x

    @property
    def y(self): 
        return self._y


    def __str__(self): 
        return f"Vector: {self.x}, {self.y}"
    
    def __repr__(self): 
        return self.__str()

    def __add__(self, other_vector): 
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __mul__(self, scalar): 
        return Vector(self.x * scalar, scalar*self.y)

    def dot_product(self, other_vector): 
        return (self.x*other_vector.x) + (self.y * other_vector.y)

    def is_orthogonal(self, other_vector): 
        return self.dot_product(other_vector) == 0 

    def distance(self, other_vector): 
        return sqrt((self.x - other_vector.x)**2 + (self.y - other_vector.y)**2)

    def magnitude(self): 
        return self.distance(Vector(0,0))

v1 = Vector(1,2)
v2 = Vector(5,10)
print(v1)
print(v2)

print(f"distance from {v1} to {v2} is {v1.distance(v2)}")
print(f"magintude of {v2} is : {v2.magnitude()}")

v3 = v1 + v2 
print(f"{v1} + {v2} = {v3}")

v4 = v1 * 3
print(f"{v1} * 3 = {v4}")

dp = v1.dot_product(v2)
print(f"{v1} dot_product with {v2}: {dp}")

ortho = v1.is_orthogonal(v2)
print(f"Is v1 orthogonal to v2?: {ortho}")
print(ortho)