# Program: desafio_087.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 10:27

matriz = list()
soma_ = 0

for i in range(3):
    dado = list()
    for e in range(3):
        number = int(input(f'[{i}][{e}]: '))
        if number%2==0:
            soma_+=number
        dado.append(number)
    matriz.append(dado[:])
    dado.clear()

for i in matriz:
    for g in i:
        print(f'[ {g} ]', end='')
    print()

soma_coluna = 0
for i, e in enumerate(matriz):
    for indice, elemento in enumerate(e):
        if indice == 2:
            print(elemento, end=' ')
            soma_coluna+=elemento
print()

maior = matriz[1][0]
comparação = sum(matriz[:][2])

print(f'A soma de todo os números pares: {soma_}')
print(f'A soma da terceira coluna por forumala: {comparação}')
print(f'A soma por algoritomo: {soma_coluna}')