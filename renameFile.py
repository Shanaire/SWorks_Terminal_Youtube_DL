import sys
import os
import string

# Get the file path as a command-line argument
file_path = sys.argv[1]
new_file_name = ""
new_file_path = "/"

def main():
    # Remove special characters and replace colons with hyphens
    dirPath = os.path.dirname(file_path)
    new_file_name = os.path.basename(file_path)
    if new_file_name.startswith("."):
        new_file_name = new_file_name[1:]
    
    new_file_path = os.path.join(dirPath, new_file_name)

    print("Updated fileName: ", new_file_name)
    # Rename the file
    os.rename(file_path, new_file_path)



if __name__ == "__main__":
    main()
