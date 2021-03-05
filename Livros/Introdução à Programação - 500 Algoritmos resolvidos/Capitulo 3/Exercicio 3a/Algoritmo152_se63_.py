# Program: Algoritmo152_se63_.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 13:29
# Updated:

age = int(input("Enter with the your age: "))
weight = int(input("Enter with the your weight: "))

if(age>0)and(weight>0):
    if age >= 12:
        if weight >= 60:
            tax = 1000
        else:
            tax = 875
    elif age < 12:
        if(weight>=5)and(weight<=9):
            tax = 125
        elif(weight>9)and(weight<=16):
            tax = 250
        elif(weight>16)and(weight<=24):
            tax = 375
        elif(weight>24)and(weight<=30):
            tax = 500
        elif weight>30:
            tax = 750
        else:
            tax=0
    print(tax)
else:
    print("Pouco me importa!")
