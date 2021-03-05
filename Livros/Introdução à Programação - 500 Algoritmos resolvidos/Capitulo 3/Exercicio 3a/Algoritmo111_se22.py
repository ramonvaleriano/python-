# Program: Algoritmo111_se22.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:36
# Updated:

number1 = float(input("Enter with first number: "))
number2 = float(input("Enter with second number: "))

if number1 != number2:
    if number1 < number2:
        smaller = number1
    else:
        smaller = number2
else:
    print("Number equals")
print("\n\n%5.2f" %smaller)
