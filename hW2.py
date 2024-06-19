# Program that checks whether a number is prime or not
# Defining prime numbers formula
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Using the formula
num = int(input("Enter a number: "))
if prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
