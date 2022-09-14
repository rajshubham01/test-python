tenure = int(input("Enter tenure:\t"))
if tenure >=10:
    print("Bonus is 15%")
elif tenure<10 and tenure>=5:
    print("Bonus is 10%")
elif tenure<5 and tenure>=3:
    print("Bonus is 5%")
else:
    print("Not eligible for bonus!")