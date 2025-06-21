import os
import sys
import time
import hashlib

def CalculateChecksum(path, ):
    with open(path, 'rb') as fobj:
        hobj = hashlib.md5()
        while True:
            buffer = fobj.read()
            if not buffer:
                break
            hobj.update(buffer)
    return hobj.hexdigest()

def FindDuplicate(DirectoryName="Marvellous"):
    # Normalize path
    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)

    if not os.path.exists(DirectoryName):
        print("The path is invalid")
        sys.exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but the target is not a directory")
        sys.exit()

    Duplicate = {}

    # Scan and collect checksums
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


def main():
    border = "-" * 60
    print(border)
    print("Marvellous Duplicate File Finder")
    print(border)

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg.lower() == "--h":
            print("Help: This script identifies duplicate files based on checksum.")
            print("Usage: python script.py <DirectoryPath>")
        elif arg.lower() == "--u":
            print("Usage: python script.py <DirectoryPath>")
            print("Make sure to provide a valid absolute or relative path.")
        else:
            FindDuplicate(arg)
    else:
        print("Invalid number of command line arguments.")
        print("Use '--h' for help or '--u' for usage instructions.")

    print(border)
    print("Thank you for using Marvellous Infosystems")
    print(border)

if __name__ == "__main__":
    main()
