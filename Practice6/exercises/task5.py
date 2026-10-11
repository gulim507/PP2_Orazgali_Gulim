names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as file:
    file.writelines(name + "\n" for name in names)

print("List written to file.")