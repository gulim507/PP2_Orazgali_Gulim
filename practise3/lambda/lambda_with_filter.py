# Here is a list of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Here is a lambda function that selects even numbers.
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)


# Here is a lambda function that selects numbers greater than 5.
large_numbers = list(
    filter(lambda number: number > 5, numbers)
)


# Here is the list of even numbers.
print("Even numbers:", even_numbers)

# Here is the list of numbers greater than 5.
print("Numbers greater than 5:", large_numbers)