source = input("Enter source file: ")
destination = input("Enter destination file: ")

with open(source, "r") as file:
    content = file.read()

with open(destination, "w") as file:
    file.write(content)

print("File copied successfully.")