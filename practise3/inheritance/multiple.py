# Here is the first parent class.
class Father:

    # Here is a method from the Father class.
    def father_skill(self):
        print("Father can drive a car.")


# Here is the second parent class.
class Mother:

    # Here is a method from the Mother class.
    def mother_skill(self):
        print("Mother can cook well.")


# Here is a child class that inherits from two classes.
class Child(Father, Mother):

    # Here is a method from the Child class.
    def child_skill(self):
        print("The child can play football.")


# Here is an object created from the Child class.
child = Child()


# Here is an inherited method from Father.
child.father_skill()


# Here is an inherited method from Mother.
child.mother_skill()


# Here is a method from Child.
child.child_skill()