# Program: Algoritmo156_se5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 14:15
# Updated:

day = int(input("Enter with the day: "))
month = int(input("Enter with the month: "))
year = int(input("Enter with the year: "))

if(day>=1)and(day<=31)and(month>=1)and(month<=12)and(year>=1)and(year<=2020):
    if month == 2:
        if(day>=1)and(day<=28):
            result =  True
        else:
            result =  False
    elif(month == 4)or(month == 6)or(month == 9)or(month == 11):
        if(day>=1)and(day<=30):
            result =  True
        else:
            result = False
    elif((month == 1)or(month == 2)or(month == 3)or(month == 5)or(month == 7)or
    (month == 8)or(month == 10)or(month == 12)):
        if(day>=1)and(day<=31):
            result =  True
        else:
            result = False
    else:
        result = False
    print(result)
        
else:
    print("Invalido")

#-------------------------------------------------------------------------#

if result == True:
    print("Valido")
else:
    print("Invalido")
