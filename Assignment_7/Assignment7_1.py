square = lambda no : (no**2)
cube  = lambda no : (no**3)

def main():
    num = int(input("enter a number: "))
    ret1 = square(num)
    ret2 = cube(num)

    print("square: ",ret1)

    print("cube:", ret2)
if __name__=="__main__":
    main()
