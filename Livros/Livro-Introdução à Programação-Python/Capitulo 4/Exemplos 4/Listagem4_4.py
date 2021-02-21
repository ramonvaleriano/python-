# Program: Listagem4_4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 11:15
# Updated:

salary = float(input("Enter with your salary: "))

base = salary
tax = 0

if base > 3000:
    tax = tax + (((base - 3000)*35)/100)
    base = 3000
if base > 1000:
    tax =  tax + (((base - 1000)*20)/100)
print("The salary: R$ %5.2f \nThe Tax: R$ %5.2f" %(salary, tax))
