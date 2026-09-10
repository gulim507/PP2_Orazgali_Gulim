# 1 example
i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1

# 2 example
number = 1

while number <= 10:
    if number == 7:
        break

    print(number)
    number += 1

#3 example
i = 1

while True:
    print(i)

    if i == 3:
        break

    i += 1

#4 example
password = ""

while True:
    password = input("Enter password: ")

    if password == "1234":
        print("Correct!")
        break

    print("Wrong password")

#5 example
number = 1

while number <= 20:
    print(number)

    if number == 10:
        break

    number += 1