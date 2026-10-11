import string

for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as file:
        file.write(letter)

print("26 files created.")