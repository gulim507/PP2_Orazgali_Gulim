file_path = input("Enter file name: ")

with open(file_path, "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))