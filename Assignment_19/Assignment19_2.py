import os
import sys

def DirectoryWatcher(DirectoryName, Extension1, Extension2):
    # Convert to absolute path if not already
    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)

    # Validate path
    if not os.path.exists(DirectoryName):
        print("Path is invalid")
        sys.exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but target is not a directory")
        sys.exit()

    print("Absolute path is: " + DirectoryName)

    # Traverse directory
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            full_file_path = os.path.join(FolderName, fname)

            if os.path.isfile(full_file_path) and fname.endswith(Extension1):
                print("Found file:", fname)

                # Get base name without extension
                basename, _ = os.path.splitext(fname)
                new_filename = basename + Extension2

                old_file_path = os.path.join(FolderName, fname)
                new_file_path = os.path.join(FolderName, new_filename)

                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"File '{old_file_path}' renamed to '{new_file_path}' successfully.")
                except FileNotFoundError:
                    print(f"Error: File '{old_file_path}' not found.")
                except PermissionError:
                    print(f"Error: Permission denied to rename '{old_file_path}'.")

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <DirectoryPath> <OldExtension> <NewExtension>")
        sys.exit()

    DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
