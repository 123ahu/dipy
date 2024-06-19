class student:
    def __init__(self, name, course, gender):
        self.name = name
        self.course = course
        self.gender = gender

    def study(self):
        print(self.name, "is studying", self.course, ".")


Stud1 = student("Sam", "Cybersecurity", "M")
Stud1.study()
Stud2 = student("Neema", "Data Science", "F")
Stud2.study()
Stud3 = student("Makena", "MIT", "F")
Stud3.study()
