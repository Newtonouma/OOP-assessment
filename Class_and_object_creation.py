#Car class
class Car:
    def __init__(self, make, model, year):
        # attributes
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
            print(f"Car Details: {self.year} {self.make} {self.model}")

# this is an instance of the Car class
my_car = Car("VolksWagen", "Tiguan", 2024)

my_car.display_info()
