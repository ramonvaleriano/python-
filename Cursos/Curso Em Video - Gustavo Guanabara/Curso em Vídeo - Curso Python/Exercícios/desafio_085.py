# Program: desafio_085.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 10:06

quantidade = 7
pares = list()
impares = list()
total = list()

for i in range(quantidade):
    numero = float(input('Digite um número: '))
    if numero%2==0:
        pares.append(numero)
        pares.sort()
    else:
        impares.append(numero)
        impares.sort()
total.append(pares)
total.append(impares)
print(total)
