# Program: Algoritmo83_InversoAbsoluto.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 23/03/2020 - 16:59
# Updated:

number = float(input("Enter with a number:"))

if number >= 0:
    result = 1/number
else:
    result = number*(-1)
print(result)
