# Program: listagem8_26.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 06:39

def soma(a, b):
    s = a + b
    return s

def subtracao(a, b):
    s = a - b
    return s

def imprime(a, b, foper):
    print(foper(a, b))

imprime(2, 3, soma)
imprime(4, 2, subtracao)