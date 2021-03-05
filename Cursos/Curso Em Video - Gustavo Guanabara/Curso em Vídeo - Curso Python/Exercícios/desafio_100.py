# Program: desafio_100.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 14:43

from random import randint

def sorteio(numeros):
    for n in range(5):
        numeros.append(randint(1, 100))

def somapar(numeros):
    soma = 0
    for n in numeros:
        if n%2==0:
            soma+=n
    print(f'A soma dos números pares é: {soma}')

numeros = list()
sorteio(numeros)
print(numeros)
somapar(numeros)
