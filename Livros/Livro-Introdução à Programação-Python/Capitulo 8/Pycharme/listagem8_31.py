# Program: listagem8_31.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 07:04

def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior == None or maior < e:
            maior = e
    print(mensagem, maior)
imprime_maior('Maior', 1,2,3,4,5)
imprime_maior('Max', *[1, 4, 6])