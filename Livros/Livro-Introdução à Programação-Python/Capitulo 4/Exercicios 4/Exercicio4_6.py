# Program: Exercicio4_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 13:30
# Updated:

distance = float(input("Enter with the distance: "))

if distance > 0:
    if distance <= 200:
        tax = 0.50
    else:
        tax = 0.45
    value = distance*tax
    print(value)
else:
    print("You are an asshole!")
