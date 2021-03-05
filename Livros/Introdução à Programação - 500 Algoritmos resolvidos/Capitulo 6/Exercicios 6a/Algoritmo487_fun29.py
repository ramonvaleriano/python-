# Program: Algoritmo487_fun29.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 20:45
# Updated: 11/06/2020 - 08:54

import random

def inverter(lista):
    quantity = len(lista)   
    new_lista = list()
    for e in range((quantity-1), -1, -1):
        number = lista[e]
        new_lista.append(number)
    return new_lista

numeros = list()
quantity = 10

for e in range(quantity):
    number = random.randint(0, 101)
    numeros.append(number)

for n in numeros:
    print(n, end=" ")
print()
inverso = inverter(numeros)
for i in inverso:
    print(i, end=" ")
