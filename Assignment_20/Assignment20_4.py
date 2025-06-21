import os
import sys
import time
import hashlib

def CalculateChecksum(path,BlockSize=1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(BlockSize)

    while(len(Buffer)>0):
         hobj.update(Buffer)
         Buffer = fobj.read(BlockSize)

    fobj.close

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)
            print("file name: "+fname)
            print("Checksum: ",checksum)
            print()
            
    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,"w")

    Border = "-"*54
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectory Cleaner Script\n")

    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")


def FindDuplicate(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    
    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            filepath = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(filepath)

            if checksum in Duplicate:
                Duplicate[checksum].append(filepath)
            else:
                Duplicate[checksum] = [filepath]

    # Generate log file with duplicate files
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"DuplicateLog_{timestamp}.log"

    with open(log_filename, "w") as fobj:
        border = "-" * 60
        fobj.write(border + "\n")
        fobj.write("Duplicate File Report\n")
        fobj.write(f"Directory Scanned: {DirectoryName}\n")
        fobj.write(f"Created on: {time.ctime()}\n")
        fobj.write(border + "\n\n")

        dup_found = False
        for checksum, files in Duplicate.items():
            if len(files) > 1:
                dup_found = True
                fobj.write(f"Checksum: {checksum}\n")
                for filepath in files:
                    fobj.write(f"  {filepath}\n")
                fobj.write("\n")

        if not dup_found:
            fobj.write("No duplicate files found.\n")

    print(f"\nDuplicate file log created: {log_filename}")
    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    count  = 0
     
    for value in Result:
        for subvalue in value:
            count = count + 1
            print(subvalue)
            
        print("----------------------------------------")
        print("value of count is:",count)
        print("----------------------------------------")
        count = 0

def DeleteDuplicate(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    count  = 0
     
    for value in Result:
        for subvalue in value:
            count = count + 1
            if(count > 1):
                os.remove(subvalue)
        count = 0

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    start_time = time.time()  # Start timing

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            # DirectoryWatcher(sys.argv[1])
            Result = FindDuplicate(sys.argv[1])
            # DisplayResult(Result)
            DeleteDuplicate(Result)

        end_time = time.time()  # End timing
        execution_time = end_time - start_time
    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print(f"Script execution time: {execution_time:.2f} seconds")
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()
