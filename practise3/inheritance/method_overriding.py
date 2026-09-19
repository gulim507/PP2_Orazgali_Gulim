# Here is a parent class called Animal.
class Animal:

    # Here is a method from the parent class.
    def sound(self):
        print("The animal makes a sound.")


# Here is a Dog class that overrides the parent method.
class Dog(Animal):

    # Here is the overridden sound method.
    def sound(self):
        print("The dog says: Woof!")


# Here is a Cat class that overrides the parent method.
class Cat(Animal):

    # Here is the overridden sound method.
    def sound(self):
        print("The cat says: Meow!")


# Here is a Dog object.
dog = Dog()


# Here is a Cat object.
cat = Cat()


# Here is an example of method overriding.
dog.sound()
cat.sound()