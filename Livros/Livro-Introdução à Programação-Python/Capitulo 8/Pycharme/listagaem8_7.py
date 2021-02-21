# Program: listagem8_7.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 22:31

import random

def soma(lista):
    total = 0
    for e in lista:
        total+=e
    return total

def media(lista, i_funcao):
    soma = (i_funcao(lista))
    quantidade = len(lista)
    media = (soma/quantidade)
    return media

lista = list(range(1, 46))
random.shuffle(lista)
print(lista)
print('\n\n')
print('Média dessa lista é: {}'.format(media(lista, soma)))