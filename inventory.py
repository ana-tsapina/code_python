class Inventory: 
    def __init__(self, name, price = None, desc = None, quantity = None): 
        self.name = name
        self.price = price 
        self.desc = desc 
        self.quantity = quantity 

    @property 
    def name(self): 
        return self.__name

    @property 
    def price(self): 
        return self.__price

    @property 
    def desc(self): 
        return self.__desc

    @property 
    def quantity(self): 
        return self.__quantity 


    @name.setter
    def name(self, value): 
        self.__name = value 

    @price.setter
    def price(self, value): 
        try: 
            if not isinstance(value, int): 
                raise ValueError("Value must be a numeric value")
            self.__price = value 

        except ValueError as e: 
            print(f"Error: {e}")

    @desc.setter
    def desc(self, text): 
        try: 
            if not isinstance(text, str): 
                raise ValueError("Must be a string value")

            self.__desc = text 

        except ValueError as e: 
            print(f"Error: {e}")

        
    @quantity.setter
    def quantity(self, value): 
        try: 
            if not isinstance(value, int): 
                raise ValueError("Must be a int or float value")
            self.__quantity = value 

        except ValueError as e: 
            print(f"Error: {e}")


p1 = Inventory("Tea", 7, "hot", 3)
print(p1.name)
p1.price = 20
print(f"Product: {p1.name} | Price: {p1.price} | Description: {p1.desc} | Quantity: {p1.quantity}")