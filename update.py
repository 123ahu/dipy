import sqlite3

conn = sqlite3.connect('base.db')
print("Opened database successfully")

conn.execute("update TEACHERS set SALARY=60000.00 where ID=1")
conn.commit()

data = conn.execute("select * from TEACHERS")
for teacher in data:
    print("ID:", teacher[0])
    print("Firstname:", teacher[1])
    print("Lastname:", teacher[2])
    print("Age:", teacher[3])
    print("Salary:", teacher[4])

print("Record updated successfully")
conn.close()