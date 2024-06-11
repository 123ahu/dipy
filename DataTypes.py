# Data types
number = 78  # int
num = 45.09  # float
greeting = "Hi, how r u"  # str
Is_Programming_Interesting = True  # bool
devices = ["laptop", "phone", "computer", "tablet"]  # list
Browsers = ("Chrome", "Firefox", "Opera", "Safari")  # tuple
Countries = {"Kenya", "Uganda", "Tanzania"}  # set
Employee = {
    "<NAME>": "Jane",
    "<AGE>" : 29,
    "<NATIONALITY>" : "Kenyan",
    "<email>": "jane@gmail.com"
}  # Dictionary

print(num)
print(Countries)
print(Employee["<NAME>"])

# Determining data types
print(type(Employee))

# Type Casting
# Is the process of converting one data type to another
print(int(num))
print(float(number))
