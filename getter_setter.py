class Member: 
    def __init__(self, name, account_number): 
        self.name = name 
        self.__acc = self.__set_acc(account_number) 

    @property 
    def acc(self): 
            return self.__acc

    def __self_acc(self, value): 
        if isinstance(value, int): 
            return value
        else: 
            raise ValueError(f"{value} is not an integer.")


    def __str__(self): 
        return f"{self.acc}: {self.name}"


member1 = Member("Jasper Park", 1)
member1.name = "poopoo"
print(member1)
print(member1.acc)


