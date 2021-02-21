# Program: Listagem4_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 13:36
# Updated:

minutes = float(input("Enter with quantity of minutes: "))

if minutes > 0:
    if minutes <= 200:
        tax = 0.20
    elif((minutes>200)and(minutes<=400)):
        tax = 0.18
    else:
        tax = 0.15
    value = minutes*tax
    print(value)
else:
    print("You are an asshole!")
