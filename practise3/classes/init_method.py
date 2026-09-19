# Here is a Student class with an __init__ method.
class Student:

    # Here is the constructor that saves student information.
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Here is a method that displays student information.
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Here is an object created with values.
student1 = Student("Gulim", 18)


# Here is an example of calling the method.
student1.show_info()