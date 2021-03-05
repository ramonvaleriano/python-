# Program: Algoritmo110_se21.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:32
# Updated:

number1 = float(input("Enter with first number: "))
number2 = float(input("Enter with second number: "))

if number1 != number2:
    if number1 > number2:
        bigger = number1
    else:
        bigger = number2
else:
    print("Number equals")
print("\n\n%5.2f" %bigger)
