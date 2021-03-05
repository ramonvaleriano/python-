# Programa: Algoritmo130_se41.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/03/2020 - 12:06
# Updated:

value = float(input("Enter with the value: "))

if value > 0:
    if value<=20:
        tax = 45
    else:
        tax = 30
else:
    tax = 0
    print("What fuck is this?!")

discount = value + ((value*tax)/100)
print(discount)
