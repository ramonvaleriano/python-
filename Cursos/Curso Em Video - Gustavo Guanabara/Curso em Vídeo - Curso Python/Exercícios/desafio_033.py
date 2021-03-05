# Program: desafio_033.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:49

quantidade = 3
numeros_tudo = list()
for e in range(quantidade):
    number = int(input("Digite o {}° número: ".format(e+1)))
    numeros_tudo.append(number)
maior = numeros_tudo[0]
menor = numeros_tudo[0]
for i in numeros_tudo:
    if i>=maior:
        maior = i
    if i<=menor:
        menor = i
print(maior)
print(menor)