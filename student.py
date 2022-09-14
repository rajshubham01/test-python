total = int(input("Total classes:"))
attend = int(input("Classes Attended:"))
perc = (attend/total)*100
print("Attendance is:\t",perc+"%")
if perc>70:
    print("Eligible")
else:
    print("Not Eligible")