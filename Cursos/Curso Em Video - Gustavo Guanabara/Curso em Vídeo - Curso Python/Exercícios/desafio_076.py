# Program: desafio_076.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 02/10/2020 - 19:29

def guardar():
    numeros = list()
    quantidade = 5
    for indice in range(quantidade):
        numeros.append(int(input(f'Digite o {indice+1}° número: ')))
    return numeros

def maior_menor(funcao):
    numeros = funcao()
    indice_maior = 0
    indice_menor = 0
    maior = numeros[0]
    menor = numeros[0]
    for indice, valor in enumerate(numeros):
        if valor >= maior:
            maior = valor
            indice_maior = indice
        elif valor <= menor:
            menor = valor
            indice_menor = indice
    print(f'O maior númeror {maior}, se encontra na posição {indice_maior}')
    print(f'O menor númeror {menor}, se encontra na posição {indice_menor}')

maior_menor(guardar)