# Program: listagem8_8.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 22:37

import random

def soma_lista(lista):
    total = 0
    for e in lista:
        total+=e
    return total

lista = list(range(1,25))
random.shuffle(lista)

print(soma_lista(lista))
