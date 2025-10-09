class Car:
    # Class variable to count number of cars
    count = 0

    def __init__(self, model):
        self.model = model
        Car.count += 1  # Increment count whenever a new car is created


car1 = Car("Toyota")
car2 = Car("Honda")
car3 = Car("Ford")

print(Car.count)  # Output: 3