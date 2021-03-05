# Program: Algoritmo103_se14.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 12:08
# Updated:

year = int(input("Enter with your year of birth: "))
year_c = int(input("Enter with the current year: "))

if ((year >= year_c)and((year >= 0)and(year <= 9999)):
    result = int(year - year_c)
else:
    reult = 0
    print("You are asshole!")
print(result)
