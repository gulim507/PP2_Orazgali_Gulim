# Here is a function with positional arguments.
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)


# Here is a function with a default argument.
def greet(name="Student"):
    print("Hello,", name)


# Here is an example of positional arguments.
student_info("Gulim", 18)

# Here is an example of a default argument.
greet()
greet("Aruzhan")