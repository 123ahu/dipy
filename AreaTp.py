# Python program for getting the area of a trapezium
# Area formula is 0.5(a + b)*h

a = int(input("Enter value for side a: "))
b = int(input("Enter value for side b: "))
h = int(input("Enter value for height: "))

Area = 0.5*h*(a + b)
print("The area of the trapezium is ", int(Area), "units squared")

# Program that determines the smallest number

first = int(input("Enter the first value: "))
second = int(input("Enter the second value: "))
third = int(input("Enter the third value: "))
fourth = int(input("Enter the fourth value: "))

if (
        first < second and first < third and first < fourth):
    print(first, "is the smallest number")
elif (
        second < first and second < third and second < fourth):
    print(second, "is the smallest number")
elif (
        third < first and third < second and third < fourth):
    print(third, "is the smallest number")
else:
    print(fourth, "is the smallest number")
