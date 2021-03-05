# Program: Algoritmo103_se14.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 12:31
# Updated: 24/03/2020 - 17:00

year = int(input("Enter with your year of birth: "))
c_year = int(input("Enter with the current year: "))

if((type(year) is int)and(type(c_year) is int)):
    if ((year<=c_year)and((year>=0)and(year<=9999))):
        result = int(c_year-year)
    else:
        result = 0
        print("You are asshole!")
    print(result)
else:
    print("Your are asshole!")
