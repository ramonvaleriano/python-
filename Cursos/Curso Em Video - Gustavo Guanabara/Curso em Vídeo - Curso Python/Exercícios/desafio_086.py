# Program: desafio_086.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 10:17

matriz = list()

for i in range(3):
    dado = list()
    for e in range(3):
        number = int(input(f'[{i}][{e}]: '))
        dado.append(number)
    matriz.append(dado[:])
    dado.clear()

for i in matriz:
    for g in i:
        print(f'[ {g} ]', end='')
    print()
