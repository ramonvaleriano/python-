# Program: Algoritmo482_fun24Tentativa.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 15:34
# Updated:

import listas_ordenadas

numeros = list()

for e in range(3):
    number = int(input("Entre com o %d número: " %(e+1)))
    numeros.append(number)

print(listas_ordenadas.crescente(numeros))
