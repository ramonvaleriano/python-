# Program: Exercicio8_1.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 11:24
# Updated:

def maximo(number1, number2):
    large = number1
    if number2>number1:
        large = number2
    return large
print(maximo(5,6))
print(maximo(2,1))
print(maximo(7,7))
print()
print()
print(max(5,6))
print(max(2,1))
print(max(7,7))
