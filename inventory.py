class Inventory: 
    def __init__(self, name, price, description, quanitity): 
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
        reutrn self.__desc

    @property 
    def quantity(self): 
        return self.__quantity 


    @price_setter
        def price(self, value): 
            try: 
                if not isinstance(text, str): 
                    raise ValueError("Value must be a numeric value")
            self.__price = value 
            except ValueError as e: 
                print(f"Error: {e}")

    @desc_setter
        def desc(self, str): 
            try: 
                if not isinstance(text, str): 
                    raise ValueError("Must be a string value")

            self.__desc = text 

            except ValueError as e: 
                print(f"Error: {e}")

        
    @quantity.setter
        def quantity(self, value): 

