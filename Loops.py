# While Loop
# Incrementing
number = 25
while number <= 30:
    print(number)
    number += 1
# Decrementing
count = 10
while count >= 1:
    print(count)
    count -= 1

# Break and continue statements
x = 100
while x <= 105:
    print(x)
    if x == 103:
        break
    x += 1

y = 34
while y < 40:
    y += 1
    if y == 38:
        continue
    print(y)

# For Loop
for num in range(70, 80):
    print(num)

for e in range(100, 110, 3):
    print(e)

Languages = ["Python", "Java", "C++", "Javascript"]
for lang in Languages:
    print(lang)
