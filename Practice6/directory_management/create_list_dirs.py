import os
from pathlib import Path

print("Current directory:", os.getcwd())

if not os.path.exists("single_folder"):
    os.mkdir("single_folder")

os.makedirs("test_folder/subfolder", exist_ok=True)

print("All files and directories:")
print(os.listdir("."))

print("Directories:")
for item in os.listdir("."):
    if os.path.isdir(item):
        print(item)

print("Files:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(item)

print("Python files:")
for file in Path(".").glob("*.py"):
    print(file)

path = Path("sample.txt")

if path.exists():
    print("Path exists.")
    print("Filename:", path.name)
    print("Directory:", path.parent)
else:
    print("Path does not exist.")

print("Exists:", os.path.exists("sample.txt"))
print("Readable:", os.access("sample.txt", os.R_OK))
print("Writable:", os.access("sample.txt", os.W_OK))
print("Executable:", os.access("sample.txt", os.X_OK))

original_directory = os.getcwd()
os.chdir("test_folder")
print("Changed directory:", os.getcwd())
os.chdir(original_directory)
print("Returned to:", os.getcwd())
