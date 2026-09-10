#1 example
i = 0

while i < 6:
    i += 1

    if i == 3:
        continue

    print(i)

#2 example

i = 0

while i < 8:
    i += 1

    if i == 5:
        continue

    print(i)

#3 example
i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue

    print(i)
#4 example

fruits = ["apple", "banana", "orange", "cherry"]

i = 0

while i < len(fruits):
    fruit = fruits[i]
    i += 1

    if fruit == "banana":
        continue

    print(fruit)

#5 example

numbers = [5, -2, 8, -1, 3]

i = 0

while i < len(numbers):
    number = numbers[i]
    i += 1

    if number < 0:
        continue

    print(number)