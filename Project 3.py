import cal

print("Enter your details:\n")

fname = input("Enter first name:")
lname = input("Enter last name:")
salary = int(input("Enter basic salary:"))

print(f"Full Name: {fname}{lname}")
print("HRA is",cal.hra(salary))
print("DA is",cal.da(salary))
print("Bonus is",cal.bonus(salary))

ctc = salary+cal.hra(salary)+cal.da(salary)+cal.bonus(salary)
print("\nYour CTC is:",ctc)