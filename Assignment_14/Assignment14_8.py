
#methode overiding 

class Vehicle:
    def Start(self):
        print("inside Base display")

class Car(Vehicle):
    def Start(self):      #overrided method
        print("inside Derived display")


def main():
    bobj =  Vehicle()
    dobj = Car()

    bobj.Start()
    dobj.Start()


if __name__=="__main__":
    main()
