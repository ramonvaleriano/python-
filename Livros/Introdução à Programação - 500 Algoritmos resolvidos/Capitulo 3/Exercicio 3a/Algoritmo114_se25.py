# Program: Algoritmo114_se25.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 17:46
# Updated:

number1 = float(input("Enter with first number: "))
number2 = float(input("Enter with second number: "))

if number1 != number2:
    if number1 > number2:
        aux = number1
        number1 = number2
        number2 = aux
else:
    print("Number equals!")
print(number2)
print(number1)
