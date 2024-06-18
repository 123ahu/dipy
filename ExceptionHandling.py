try:
    x = 5
    print(x)
except:
    print("Error")
finally:
    print("Success")

num1 = 67
num2 = 0

try:
    print(num1 / num2)
except:
    print("Error: division by zero")
finally:
    print("Success")
