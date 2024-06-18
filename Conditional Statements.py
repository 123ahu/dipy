Temperature = 46
if Temperature < 25:
    print("It is cold")
elif Temperature > 25:
    print("It is Hot")
else:
    print("It is normal")

# A simple program to return the largest number among three numbers
First = 90
Second = 45
Third = 69
if First > Second and First > Third:
    print(First, "Is the largest number")
elif Second > Third and Second > First:
    print(Second, " Is the largest number")
else:
    print(Third, " Is the largest number")


# Write a Python program to check whether a number is even or odd

even_odd_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in even_odd_numbers:
    if number % 2 == 0:
        print(number, "is an even number")
    elif 0 == number:
        print(number, "is neutral")
    else:
        print(number, " is an odd number")