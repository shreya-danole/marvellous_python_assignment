import os

def Check_file():
    print("Enter a file name : ")
    FileName = input()

    if os.path.exists(FileName):
        print("File exits in current directory")

    else:
        print("File doesn't exits in current directory")


def main():
    Check_file()

if __name__ == "__main__":
    main()
