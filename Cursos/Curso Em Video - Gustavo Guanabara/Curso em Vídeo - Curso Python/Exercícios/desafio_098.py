# Program: desafio_098.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 14:19

from time import sleep

def linha():
    print('-='*20)

def contagem(inicio, fim, salto, linha):
    linha()
    print(f'Contagem de {inicio} a {fim}:')
    for n in range(inicio, fim+1, salto):
        sleep(1)
        print(n, end=' ')
    print()
    linha()

contagem(1, 10, 1, linha)
contagem(10, -2, -2, linha)
