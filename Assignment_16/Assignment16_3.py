import os 

def main():
    print("Enter the name of that you want to read:")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in the current directory")
        line_count = 0
        with open(FileName, 'r') as file:
            for line in file:
                line_count += 1
        print("Number of lines: ",line_count)
        
        c = 0
        with open(FileName, 'r') as file:
            data = file.read()
            w = data.split()
            c = c + len(w)
        print("Number of words: ", c)

        with open(FileName, 'r') as file:
            content = file.read()
            char = len(content)
        print("Number of characters:" , char)
    


if __name__ == "__main__":
    main()
