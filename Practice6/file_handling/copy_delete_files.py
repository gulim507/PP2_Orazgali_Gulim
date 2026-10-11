import os
import shutil

# Copy a file
shutil.copy("sample.txt", "sample_backup.txt")
print("File copied successfully.")


with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("Contents copied successfully.")


file_path = "copy.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File is not writable.")
else:
    print("File does not exist.") 