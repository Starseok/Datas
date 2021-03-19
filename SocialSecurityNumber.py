# Korea Social Security Number Input Then Sex and Age output program (born in 1921~ 2020)
from datetime import datetime
SSN = input("Korea Social Security Number : ")

if int(SSN[6]) == 1 or int(SSN[6]) == 3:
    sex = "male"
    print("Sex :", sex)
elif int(SSN[6]) == 2 or int(SSN[6]) == 4:
    sex = "female"
    print("Sex :", sex)
else:
    print("Foreign?")

your_year = int(SSN[0:2])
your_month = int(SSN[2:4])
your_day = int(SSN[4:6])

now_year = str(datetime.today().year)
now_year = int(now_year[2:4])
now_month = datetime.today().month
now_day = datetime.today().day

if now_year <= your_year:
    Age = 100 + now_year - your_year
else:
    Age = now_year - your_year

if now_month > your_month:
    print("Age :", Age)
elif now_month == your_month and now_day >= your_day:
    print("Age :", Age)
else:
    print("Age :", Age-1)
