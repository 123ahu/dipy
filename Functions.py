# In-built functions

y = min(23, 56, 100, 458)
print("The smallest number is", y)

x = max(33, 98, 54, 10)
print("The largest number is", x)

z = pow(2, 3)
print("The value is", z)


# User-defined functions

def multiply(a, b):
    print("Answer =", a * b)


multiply(2, 3)  # Calling the function


# Parameters and arguments

def add(i, j):
    print("The sum is", i + j)


add(12, 13)
add(30, 143)
add(82, 11)


def Workers(Fullnames, Age, Salary, Phonenumber, Position):
    print(Fullnames, Age, Salary, Phonenumber, Position)


Workers("Job Kamau", 45, 500000, +254712345678, "Managing director")
Workers("Sasha Marie", 25, 45000, +25471238754, "Secretary")
Workers("Nicholas Jackson", 30, 50000, +254712388395, "Accounts Clerk")




