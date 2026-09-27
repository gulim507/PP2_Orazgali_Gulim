# PYTHON ITERATORS

# Iterator from tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Iterator from string
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Loop through tuple
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


# Loop through string
mystr = "banana"

for x in mystr:
    print(x)


# Create an iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()

for x in myclass:
    print(x)


# GENERATORS

# Simple generator
def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)


# Generator with a loop
def count_up_to(n):
    count = 1

    while count <= n:
        yield count
        count += 1


for num in count_up_to(5):
    print(num)


# Large sequence generator
def large_sequence(n):
    for i in range(n):
        yield i


gen = large_sequence(1000000)

print(next(gen))
print(next(gen))
print(next(gen))


# Using next() with generator
def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"


gen = simple_gen()

print(next(gen))
print(next(gen))
print(next(gen))


# Generator expression
list_comp = [x * x for x in range(5)]
print(list_comp)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))


# Sum of squares
total = sum(x * x for x in range(10))
print(total)


# Fibonacci generator
def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()

for _ in range(10):
    print(next(gen))


# Generator send()
def echo_generator():
    while True:
        received = yield
        print("Received:", received)


gen = echo_generator()

next(gen)
gen.send("Hello")
gen.send("World")


# Generator close()
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")


gen = my_gen()

print(next(gen))
gen.close()


# PYTHON DATES

import datetime

# Current date and time
x = datetime.datetime.now()
print(x)


# Current year and weekday
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# Creating date object
x = datetime.datetime(2020, 5, 17)
print(x)


# Month name
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


# Date formatting
x = datetime.datetime.now()

print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%S"))


# PYTHON MATH

# Built-in functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# Absolute value
x = abs(-7.25)
print(x)


# Power
x = pow(4, 3)
print(x)


# Math module
import math

x = math.sqrt(64)
print(x)


# Ceil and floor
x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)


# Pi
x = math.pi
print(x)


# PYTHON JSON

import json

# Parse JSON
x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])


# Convert Python to JSON
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)


# Convert different Python objects to JSON
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Complex Python object
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))


# Format JSON
print(json.dumps(x, indent=4))


# JSON separators
print(json.dumps(x, indent=4, separators=(". ", " = ")))


# Sort JSON keys
print(json.dumps(x, indent=4, sort_keys=True))