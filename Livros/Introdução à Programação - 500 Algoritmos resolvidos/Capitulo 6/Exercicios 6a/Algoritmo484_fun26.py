# Program: Algoritmo484_fun26.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 16:35
# Updated:

import random
import listas_ordenadas

numeros = list()
quantity = 10

for e in range(quantity):
    number = random.randint(1, 100)
    numeros.append(number)
print(numeros)
print(listas_ordenadas.minimo(numeros))
