# Program: Algoritmo93_se4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/03/2020 - 08:57
# Updated:

import math

number = float(input("Enter with a number: "))

if number >= 0:
    result = math.sqrt(number)
else:
    result = number**2
print(result)
