# Program: desafio_088.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 10:56

from random import randint
from time import sleep


matriz = list()

quantidade = int(input('Digite a quantidade de sorteios que deseja: '))

for s in range(quantidade):
    sorteio = list()
    for n in range(6):
        numero = randint(1, 60)
        sorteio.append(numero)
    matriz.append(sorteio[:])
    sorteio.clear()

for indice, elemento in enumerate(matriz):
    sleep(1)
    print(f'Jogo: {indice+1}: {elemento}')
