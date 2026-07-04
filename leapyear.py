#Check leap year

year = int (input("enter year : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400==0 :
    print("its a leap year")
else:
    print("not leap year")