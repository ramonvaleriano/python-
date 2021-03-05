# Program: Algoritmo146_se57.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 26/03/2020 - 09:40
# Updated:

distance = float(input("Enter with the distance: "))
type_car = input("Type of car: ")

type_car = type_car[0].upper()
print(type_car)
if type_car == "A":
    value = distance/12
    print(value)
elif type_car == "B":
    value = distance/9
    print(value)
elif type_car == "C":
    value = distance/8
    print(value)
else:
    print("You are asshole!")
