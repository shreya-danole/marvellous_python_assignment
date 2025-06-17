def create_marks_file():
    # Creating the marks.txt file with sample data
    with open("marks.txt", "w") as f:
        f.write("Alice 82\n")
        f.write("Bob 67\n")
        f.write("Charlie 90\n")
        f.write("David 74\n")
        f.write("Eva 78\n")
        f.write("Frank 50\n")
        f.write("Grace 88\n")


def display():
    print("Students who scored more than 75:")
    with open("marks.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                name, mark = parts[0], int(parts[1])
                if mark > 75:
                    print(f"{name}: {mark}")


def main():
    create_marks_file()       
    display()  


if __name__ == "__main__":
    main()
