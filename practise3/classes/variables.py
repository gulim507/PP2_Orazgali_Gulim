# Here is a Student class.
class Student:

    # Here is a class variable shared by all students.
    university = "KBTU"


    # Here is the constructor with an instance variable.
    def __init__(self, name):
        self.name = name


# Here is the first Student object.
student1 = Student("Gulim")


# Here is the second Student object.
student2 = Student("Aruzhan")


# Here is an example of the shared class variable.
print(student1.university)
print(student2.university)


# Here is an example of instance variables.
print(student1.name)
print(student2.name)


# Here is an example of changing an instance variable.
student1.name = "Dana"

print("New name:", student1.name)