# Here is a list of numbers.
numbers = [1, 2, 3, 4, 5]


# Here is a lambda function that doubles every number.
doubled_numbers = list(
    map(lambda number: number * 2, numbers)
)


# Here is a lambda function that squares every number.
squared_numbers = list(
    map(lambda number: number * number, numbers)
)


# Here is the result of doubling the numbers.
print("Doubled:", doubled_numbers)

# Here is the result of squaring the numbers.
print("Squared:", squared_numbers)