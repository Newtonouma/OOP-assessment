# Engine parent_class
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            print(f"{self.type_of_engine} engine started.")
        else:
            print(f"The {self.type_of_engine} engine is running already.")

    def stop(self):
        if self.running:
            self.running = False
            print(f"{self.type_of_engine} engine stopped.")
        else:
            print(f"The {self.type_of_engine} engine is already off.")

# Car parent_class with an Engine instance as a member
class Car:
    def __init__(self, make, model, engine_type):
        self.make = make
        self.model = model
        self.engine = Engine(engine_type)

    def start_car(self):
        print(f"Starting the {self.make} {self.model} car...")
        self.engine.start()

    def stop_car(self):
        print(f"Stopping the {self.make} {self.model} car...")
        self.engine.stop()

# Create a Car object with a specific Engine
my_car = Car("VolksWagen", "Tiguan", "V8")

# Start and stop the car
my_car.start_car()
my_car.stop_car()
