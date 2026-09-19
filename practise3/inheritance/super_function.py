# Here is a parent class called Person.
class Person:

    # Here is the constructor of the parent class.
    def __init__(self, name):
        self.name = name


    # Here is a method from the parent class.
    def introduce(self):
        print("My name is", self.name)


# Here is a child class that inherits from Person.
class Student(Person):

    # Here is the constructor of the child class.
    def __init__(self, name, university):

        # Here is super() calling the parent constructor.
        super().__init__(name)

        self.university = university


    # Here is a method from the child class.
    def show_student(self):

        # Here is super() calling the parent method.
        super().introduce()

        print("I study at", self.university)


# Here is an object created from the Student class.
student = Student("Gulim", "KBTU")


# Here is an example of calling the child method.
student.show_student()