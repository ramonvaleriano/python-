# Program: exercicio9_3.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 12:49

impares = open("impares.txt", "r")
pares = open("pares.txt", "r")
completa = open("completa.txt", "w")
lista = list()
for linha in pares.readlines():
    number = int(linha)
    lista.append(number)
for linha in impares.readlines():
    number = int(linha)
    lista.append(number)
lista.sort()
for linha in lista:
    completa.write(f'{linha}\n')
impares.close()
pares.close()
completa.close()