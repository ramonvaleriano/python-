# Program: Algoritmo309_Enq48.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 07/04/2020 - 08:58
# Updated:

dejection = 600
exempt = 0
value_total = 0
while True:
    cic = int(input("Enter with the personal code: "))
    if cic < 0:
        break
    dependents = int(input("Dependents number: "))
    gross_income = float(input("Enter with Gross Income: "))


    if dependents > 0:
        income = gross_income - (dependents*dejection)
    else:
        income = gross_income


    if income <= 1000:
        tax = 0
        value = income
        exempt+=1
    elif income > 1000 and income <= 5000:
        tax = 15
        value = (income*tax)/100
    elif income > 5000 :
        tax = 25
        value = (income*tax)/100
    else:
        print("Invalid Option!")
        tax = 0
        value = 0

    print(cic)
    print(value)
    print(tax)
    print()
    value_total+=value
print()
print(value_total)
print(exempt)
