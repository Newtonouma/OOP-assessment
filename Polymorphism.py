# Parent class Animal
class Animal:
    def make_sound(self):
        pass

# the Cat child_class
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Dog child_class
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Function to show polymorphism
def animal_sound(animal):
    animal.make_sound()

# instances of Cat and Dog child_classes
cat = Cat()
dog = Dog()

# Demonstrate polymorphism by passing both objects to the same function
animal_sound(cat)  # Outputs: Meow!
animal_sound(dog)  # Outputs: Woof!
