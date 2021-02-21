# Program: Listagem8_9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 12:48
# Updated:

def fatorial(number):
    fat = 1
    while number>1:
        fat*=number
        number-=1
    return fat
print(fatorial(5))
