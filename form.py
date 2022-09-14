from datetime import date, datetime

fn = input("Enter first name ")
mn = input("Enter middle name ")
ln = input("Enter last name ")

print("Enter date of birth:")
dob = date(int(input("Year")),int(input("Month")),int(input("date")))
print("Age :",int((date.today()-dob).days/365))

ph = input("Enter contact number ")
area = input("Enter area ")
city = input("Enter city ")
state = input("Enter state ")

company = input("Enter where you work ")

today = date.today()

print("\nFull Name:",fn,mn,ln,"\nAge:",today.year - dob.year - ((today.month,today.day) < (dob.month,dob.day)))
print("\nContact Details:\n"+"Address:",area,city,state,"\nPhone:",ph)
print("\nCompany working in:",company)