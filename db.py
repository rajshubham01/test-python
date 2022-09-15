from logging import exception
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="admin",
        host="localhost",
        port=3306,
        database="employees"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
conn.autocommit=True

try:
    cur.execute("create table newemployees (name varchar(30),lname varchar(30),phone integer,age integer,city varchar(30),salary integer,dept varchar(30))")
except exception as y:
    print(y)

from asyncio.windows_events import NULL
from contextlib import nullcontext
from inspect import _empty
import numbers
from queue import Empty
from unicodedata import name


while True:
    fname = input("Enter first name:")
    if fname.isalpha()==False or len(fname)==0:
        print("Check your input!")
        pass
    else:
        break

while True:
    lname = input("Enter last name:")
    if lname.isalpha()==False or len(lname)==0:
        print("Check your input!")
        pass
    else:
        break

while True:
    ph = input("Enter phone number:")
    if ph.isnumeric()==False or len(ph)<10:
        print("Check your input!")
        pass
    else:
        break

while True:
    age = input("Enter age:")
    if age=="" or int(age)<20 or age.isnumeric()==False:
        print("Check your input!")
        pass
    else:
        break

while True:
    city = input("Enter city:")
    if len(city)==0 or city.isalpha()==False:
        print("Check your input!")
        pass
    else:
        break

while True:
    salary = float(input("Enter salary:"))
    if salary==NULL or salary<0:
        print("Check your input!")
        pass
    else:
        break

while True:
    dept = input("Enter department:")
    if len(dept)==0 or dept.isalpha()==False:
        print("Check your input!")
        pass
    else:
        break

#cur.execute("insert into table values (fname,lname,phone,age,city,salary,dept)")

cur.execute("select * from newemployees")

for i in cur:
    print(i)

'''
print(f"\nFull Name: {fname} {lname}")
print(f"Age: {age}")
print(f"Phone Number: {ph}")
print(f"City: {city}")
print(f"Salary: {salary}")
print(f"Department: {dept}")'''