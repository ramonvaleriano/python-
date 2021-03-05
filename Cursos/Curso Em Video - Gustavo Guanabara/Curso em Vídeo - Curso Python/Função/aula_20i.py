# Program: aula_20i.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 13:07

def contado(*numeros):
    tamanho = len(numeros)
    print(f'Eu recebi {tamanho} número: {numeros}')
    print()

# Programa Principal
contado(2, 5, 8)
contado(4, 2)
contado(3, 7, 9, 1)