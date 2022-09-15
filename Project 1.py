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




print(f"\nFull Name: {fname} {lname}")
print(f"Age: {age}")
print(f"Phone Number: {ph}")
print(f"City: {city}")
print(f"Salary: {salary}")
print(f"Department: {dept}")