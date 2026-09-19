# Here is a Calculator class.
class Calculator:

    # Here is a method that adds two numbers.
    def add(self, a, b):
        return a + b


    # Here is a method that subtracts two numbers.
    def subtract(self, a, b):
        return a - b


    # Here is a method that multiplies two numbers.
    def multiply(self, a, b):
        return a * b


# Here is an object created from the Calculator class.
calculator = Calculator()


# Here is an example of using the class methods.
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))