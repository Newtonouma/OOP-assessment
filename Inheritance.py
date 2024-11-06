# parent class of Animal
class Animal:
    def eat(self):
        print("This animal eatings.")

    def sleep(self):
        print("This animal sleepings.")

# child_class: Dog which inherits attributes from Animal
class Dog(Animal):
    def bark(self):
        print("The dog barkings.")

# an instance of Dog
my_dog = Dog()

# inherited methods
my_dog.eat()
my_dog.sleep()

# Using the new method made in the Dog child_class
my_dog.bark()
