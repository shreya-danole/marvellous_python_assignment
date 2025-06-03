def print_triangle(n, i=1):
    if i > n:
        return
    print('* ' * i)
    print_triangle(n, i + 1)

def main():
    num = int(input("enter a number"))
    print_triangle(num)


if __name__=="__main__":
    main()
