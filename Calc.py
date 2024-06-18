a = float(input("Enter first number: "))
choice = input("Enter operand (+,-,*,/): ")
b = float(input("Enter second number: "))

if choice == '+':
    print("Result:", a + b)
elif choice == '-':
    print("Result:", a - b)
elif choice == '*':
    print("Result:", a * b)
elif choice == '/':
    if b == 0:
        print("# Error: number cannot be divided by zero")
    else:
        print("Result:", a / b)

else:
    print("Invalid input")




