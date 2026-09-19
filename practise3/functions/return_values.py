# Here is a function that returns the sum of two numbers.
def add_numbers(a, b):
    return a + b


# Here is a function that returns the square of a number.
def square(number):
    return number * number


# Here is a function that returns the larger number.
def find_larger(a, b):
    if a > b:
        return a
    else:
        return b


# Here is an example of using a return value.
result = add_numbers(10, 20)
print("Sum:", result)

# Here is another example of using a return value.
print("Square:", square(5))

# Here is an example of finding the larger number.
print("Larger number:", find_larger(15, 8))