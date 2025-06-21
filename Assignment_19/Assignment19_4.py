import os
import sys
import shutil

def DirectoryWatcher(DirectoryName1, DirectoryName2, Extension):

    flag = os.path.isabs(DirectoryName1)

    if(flag == False):
        DirectoryName1 = os.path.abspath(DirectoryName1)

    flag = os.path.exists(DirectoryName1)

    if(flag == False):
        print("Path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName1)
    
    if(flag==False):
        print("Path is valid but target is not directory")
        exit()
    print("Absloute apth is:"+DirectoryName1)

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName1):
        # Create corresponding subfolder in target
        relative_path = os.path.relpath(FolderName, DirectoryName1)
        target_folder_path = os.path.join(DirectoryName2, relative_path)

        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)

        for fname in FileNames:
            source_file = os.path.join(FolderName, fname)
            target_file = os.path.join(target_folder_path, fname)
            if(fname.endswith(Extension)):
                try:
                    shutil.copy2(source_file, target_file)
                    print(f"Copied: {source_file} -> {target_file}")
                except Exception as e:
                    print(f"Error copying {source_file}: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <SourceDirectory> <TargetDirectory>")
        sys.exit()

    DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
