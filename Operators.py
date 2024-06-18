num1 = 56
num2 = 8

# Arithmetic Operators -- used for simple calculations

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)  # Modulus(%) returns the value of the remainder

# Comparison Operators -- compare values

print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not Equal to

# Assignment Operators -- Assign values to variables

a = 200
print(a)

a += 20  # Addition assignment
print(a)

# Logic Operators -- and, or, not. They work on basis of conditions

x = 100
print(200 > x > 2000)
print(x < 200 or x > 2000)
print(not(x < 200 or x >2000))

# Operator Precedence -- order in which operations get executed
output = (100 - 4 * 3 / 1)
print(int(output))

# Write a simple python program that returns the area of a trapezium (1/2(a+b)h)
a = 12
b = 7
h = 5
Area_of_Trapezium = 0.5*h*(a + b)
print("The Area is", Area_of_Trapezium, "units squared")