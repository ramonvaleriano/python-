# Program: exercicio8_5.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 21:28

import random

def pesquisa(lista, numero):
    for x, e in enumerate(lista):
        if e==numero:
            return x
    #return None

lista = list(range(1, 11))
random.shuffle(lista)
print(lista)
print('\n\n')
number = float(input("Digite o número que deseja pesquisar: "))

result = pesquisa(lista, number)
print('O númer {} está na posição {}'.format(number, result))