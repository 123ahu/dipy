class car:
    def __init__(self, make, model, year, engine, colour):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.colour = colour

    def order(self):
        print("The ordered car was a", self.make, self.model, self.year, "version", self.engine, "engine size", self.colour, "colours")


car1 = car("BMW", "320i", 2010, "2800cc", "Metallic Gray")
car1.order()
car2 = car("Nissan", "GTR", 2020, "3000cc", "Dark Gray, Orange Outlines")
car2.order()
car3 = car("Mitsubishi", "L200", 2015, "3200cc", "White, Black Bumpers")
car3.order()


# Devices
class devices:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def order(self):
        print(self.model, self.year, "version", "has crushed")


computer = devices("Hp", 2008)
computer.order()
laptop = devices("Dell", 2008)
laptop.order()