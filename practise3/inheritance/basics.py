# Here is a parent class called Animal.
class Animal:

    # Here is a method from the parent class.
    def eat(self):
        print("The animal is eating.")


# Here is a child class that inherits from Animal.
class Dog(Animal):

    # Here is a method from the child class.
    def bark(self):
        print("The dog is barking.")


# Here is an object created from the Dog class.
dog = Dog()


# Here is an inherited method from Animal.
dog.eat()


# Here is a method from Dog.
dog.bark()