# Program: Algoritmo115_se26.py
# Author: Ramon R. Valeriano
# Descritption:
# Developed: 24/03/2020 - 22:04
# Updated:

import math

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))

if number1>=number2:
    bigger = number1
    smaller = number2
else:
    bigger = number2
    smaller = number1
root = math.sqrt(bigger)
square= smaller**2

print(root)
print(square)
