# Parent class/ Base class/ Super class
class Animal:
    hasblood = True

    def bleeds(self):
        print("Bleedss")

# Child class/ Derived class/ Sub class
class Reptile(Animal):
    hasscales = True

    def sound(self):
        print("Reptile is talking")


class Birds:
    haswings = True

    def move(self):
        print("Moves by flying")


class Insects:
    def move(self):
        print("Moves by crawling")


r = Reptile()

b = Birds()

i = Insects()
