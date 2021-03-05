# Program: Algoritmo58_Lea31.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 15/03/2020 - 18:26
# Updated:

import math

number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
number3 = float(input("Enter with the third number: "))
number4 = float(input("Enter with the fourth number: "))

result = number1 + (number2/(number3+number2)) + (2*(number1-number2)) + (math.log(64)/math.log(2))

print(result)
