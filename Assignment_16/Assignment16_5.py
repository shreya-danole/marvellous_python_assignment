import os

def main():
    print("Enter the name of the file you want to read:")
    file_name = input()

    if os.path.exists(file_name):
        print("File is present in the current directory.")
        with open(file_name, "r") as fobj:
            for line in fobj:
                word_count = len(line.split())
                if word_count > 5:
                    print(line.strip())
    else:
        print("File does not exist in the current directory.")

if __name__ == "__main__":
    main()
