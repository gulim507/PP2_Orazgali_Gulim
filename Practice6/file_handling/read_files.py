# Read the whole file
with open("sample.txt", "r") as file:
    content = file.read()

print(content)

# Read one line
with open("sample.txt", "r") as file:
    first_line = file.readline()

print(first_line)

# Read all 
with open("sample.txt", "r") as file:
    lines = file.readlines()

print(lines)

# Count the number of lines
with open("sample.txt", "r") as file:
    line_count = len(file.readlines())

print("Number of lines:", line_count)