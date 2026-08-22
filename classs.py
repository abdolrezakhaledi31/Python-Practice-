class Car:
    def __init__(self, brand, year, country):
        self.brand = brand
        self.year = year
        self.country = country

    def show_info(self):
        print(self.brand, self.year, self.country)

    def __str__(self):
        return self.brand + "-" + str(self.year) + "-" + self.country


car1 = Car("benz", 1999, "Germany")
car2 = Car("bmw", 2000, "Germany")
print(car1)
print(car2)
