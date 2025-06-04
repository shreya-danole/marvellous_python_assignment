class Rectangle:

    def __init__(self,A,B):
        self.length = A
        self.width = B

    def CalculateArea(self):
        Ans = self.width *self.length
        return Ans
    
    def CalculatePerimeter(self):
        Ans = (2*(self.width +self.length))
        return Ans


def main():
    obj = Rectangle(50,30)
    ret = obj.CalculateArea()
    ret1 = obj.CalculatePerimeter()
    print("Area of reactangle:",ret)
    print("perimeter of reactangle:",ret1)

if __name__=="__main__":
    main()
