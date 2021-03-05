# Program: Algoritmo483_fun25.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 16:15
# Updated:

import random

def soma1(lista):
    soma = sum(lista)
    return soma

def soma2(lista):
    soma = sum(lista)
    return soma

def total(lista1, lista2, funcao1, funcao2):
    soma_total = funcao1(lista1) + funcao2(lista2)
    return soma_total

lista1 = list(range(1, 11))
random.shuffle(lista1)
lista2 = list(range(1, 11))
random.shuffle(lista2)

print(total(lista1, lista2, soma1, soma2))
