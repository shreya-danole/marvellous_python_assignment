class Circle:
    PI = 3.14

    def __init__(self):
        print("inside constructor")
        self.Radius = 0.0     # instances varibale
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("enter a radius"))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumferences(self):
        self.Circumference = 2 * Circle.PI * self.Radius 

    def Display(self):
        print("Radius of circle:",self.Radius)
        print("area of circle:",self.Area)
        print("Circumferences of circle is:",self.Circumference)


    
    
def main():
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumferences()
    obj.Display()

    
if __name__=="__main__":
    main()
