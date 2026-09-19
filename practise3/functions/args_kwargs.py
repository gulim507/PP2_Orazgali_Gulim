# Here is a function that accepts many positional arguments.
def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


# Here is a function that accepts many keyword arguments.
def show_student(**information):
    for key, value in information.items():
        print(key, ":", value)


# Here is an example of using *args.
print("Sum:", calculate_sum(1, 2, 3, 4, 5))

# Here is an example of using **kwargs.
show_student(
    name="Gulim",
    age=18,
    university="KBTU"
)