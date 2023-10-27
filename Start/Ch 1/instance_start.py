# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, price):
        self.title = title
        # TODO: add properties
        self.price = price
        self.__secret = "This is a secret attribute"
    # TODO: create instance methods
    def getprice(self):
        if (hasattr(self, "_discount")):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", 9.99)
b2 = Book("The Catcher in the Rye", 22.05)

# TODO: print the price of book1
print(b1.price)
print(b2.price)
print(b2.getprice())

# TODO: try setting the discount
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
# print(b1.__secret)
print(b2._Book__secret)
