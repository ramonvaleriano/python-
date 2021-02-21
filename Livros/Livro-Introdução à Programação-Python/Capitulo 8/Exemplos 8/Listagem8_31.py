# Program: Listagem8_31.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 19:37
# Updated:

def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior == None or maior<e:
            maior = e
        return maior
    print(mensagem, maior)

imprime_maior("Maior: ", 5,4,3,1)
imprime_maior("Máximo: ", *[1, 7, 9])
