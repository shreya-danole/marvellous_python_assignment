
class Book:
    def __init__(self,A):
        self.__Price = A  #private

    def display(self):
        print(self.__Price)
        
obj = Book(2490)
obj.display()
