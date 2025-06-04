
class BookStore:
    NoOfBooks = 0    
     
    def __init__(self):
        print("inside constructor")
        self.Name = input("enter name of book:")
        self.Author = input("enter a author of book:")
        BookStore.NoOfBooks = BookStore.NoOfBooks+1

    def Display(self):
        print("name of book:"+self.Name)
        print("author of book:"+self.Author)
        print("number of books:",BookStore.NoOfBooks)

def main():
    obj1 = BookStore()
    obj1.Display()

    obj2 = BookStore()
    obj2.Display()
    
if __name__=="__main__":
    main()
