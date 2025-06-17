def main():
    print("Enter ten numbers:")
    data = []

    for i in range(10):
        num = int(input())
        data.append(num)

    with open('number.txt', 'w') as file:
        for number in data:
            file.write(str(number) + '\n')

    print("Numbers written to number.txt")

if __name__ == "__main__":
    main()
