from functools import reduce

numbers = [1, 2, 3, 4, 5]

# len
print("Length:", len(numbers))

# sum
print("Sum:", sum(numbers))

# min
print("Minimum:", min(numbers))

# max
print("Maximum:", max(numbers))

# sorted
print("Sorted:", sorted(numbers, reverse=True))

# map
squared = list(map(lambda x: x * x, numbers))
print("Map:", squared)

# filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter:", even_numbers)

# reduce
product = reduce(lambda x, y: x * y, numbers)
print("Reduce:", product)

# Type conversion
number = "25"

print(int(number))
print(float(number))
print(str(100))
print(list("Python"))

# Type checking
print(type(numbers))
print(isinstance(numbers, list))