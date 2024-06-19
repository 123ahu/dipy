# Class is a blueprint of an object
# Objects are instances of a class

class Person:
    # Properties/Attributes/Variables/Characteristics
    name = "James"
    age = 22
    gender = "M"

    # Methods/Functions/Behavior
    def move(self):
        print(self.name, "is moving")


farmer = Person()
farmer.move()
print(farmer.age)
