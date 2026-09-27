
# 1. Simple generator

def show_numbers():
    yield 10
    yield 20
    yield 30


for number in show_numbers():
    print(number)


# 2. Generator with a loop

def even_numbers(limit):
    number = 2

    while number <= limit:
        yield number
        number += 2


for value in even_numbers(10):
    print(value)


# 3. Using next()

def colors():
    yield "red"
    yield "green"
    yield "blue"


color_gen = colors()

print(next(color_gen))
print(next(color_gen))
print(next(color_gen))


# 4. Iterator with a list

fruits = ["apple", "orange", "kiwi"]
fruit_iterator = iter(fruits)

print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))


# 5. Iterator with a string

word = "python"
letter_iterator = iter(word)

print(next(letter_iterator))
print(next(letter_iterator))
print(next(letter_iterator))
print(next(letter_iterator))
print(next(letter_iterator))
print(next(letter_iterator))
