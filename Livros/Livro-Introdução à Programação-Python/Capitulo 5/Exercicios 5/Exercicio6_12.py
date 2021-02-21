# Program: Exercicio6_12.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 07:33
# Updated:

lista = [1, 7, 2, 4]
smaller = lista[0]
for e in lista:
    if e<=smaller:
        smaller = e
print(smaller)
