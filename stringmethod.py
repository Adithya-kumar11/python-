class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, year={self.year})"


car = Car("Toyota", "Corolla", 2025)
print(car)  # Output: Car(make=Toyota, model=Corolla, year=2025)