def main():
    print("Enter the file name:")
    file_name = input()

    search = input("Enter the string you want to search: ")

    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        frequency = words.count(search)
        print(f"The string '{search}' appears {frequency} times.")

if __name__ == "__main__":
    main()
