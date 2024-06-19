import sqlite3

conn = sqlite3.connect('base.db')
print("Opened database successfully")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Joe',34,50000.00) ")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Alice','Dean',37,57000.00) ")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Sam','Siler',23,40000.00) ")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Steven','Gerad',44,46000.00) ")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Cole','Ashley',39,53000.00) ")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Monroe','Mason',24,40000.00) ")

conn.commit()
print("Information inserted successfully")

conn.close()
