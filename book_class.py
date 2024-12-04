class Book: 
    def __init__(self, title, author, pages, year, type): 
        self.title = title 
        self.author = author 
        self.pages = pages 
        self.year = year 
        self.type = type 

    def info(self): 
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}, Year: {self.year}, Type: {self.type}"
        

b1 = Book("Anna Karenina", "Leo Tolstoy", 800, 1878, "Fiction")


print(b1.info())