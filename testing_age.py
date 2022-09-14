age=input("Enter Your Age : ")
while len(age)==0 or int(age)<20 or int(age)>100  or age.isnumeric()==False:
    age=(input("Enter Valid Age : "))