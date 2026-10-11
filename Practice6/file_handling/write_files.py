import string

with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is Practice 6.\n")

with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

try:
    with open("exclusive_sample.txt", "x") as file:
        file.write("This file was created using x mode.\n")
except FileExistsError:
    print("File already exists.")

names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as file:
        file.write("This is file " + letter)

print("Files were created successfully.")
