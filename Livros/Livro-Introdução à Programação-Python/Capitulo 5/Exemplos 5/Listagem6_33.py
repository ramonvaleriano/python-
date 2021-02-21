# Program: Listagem6_33.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 07:30
# Updated:

lista = [1, 7, 2, 4]
bigger = lista[0]
for number in lista:
    if number >= bigger:
        bigger = number
print(bigger)
