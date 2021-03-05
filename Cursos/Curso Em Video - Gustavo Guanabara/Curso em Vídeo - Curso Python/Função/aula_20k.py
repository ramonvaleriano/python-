# Program: aula_20k.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 13:21

def soma(*numeros):
    soma = 0
    for n in numeros:
        soma+=n
    print(soma)

soma(2, 5, 6)
soma(1, 4)
soma(1, 7, 0, 2, 5, 6)