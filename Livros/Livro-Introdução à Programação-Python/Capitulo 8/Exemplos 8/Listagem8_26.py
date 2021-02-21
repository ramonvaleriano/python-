# Program: Listagem8_26.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 19:00
# Updated:

def soma(a, b):
    return(a+b)

def subtracao(a, b):
    return(a-b)

def imprime(a, b, foper):
    print(foper(a, b))

imprime(5, 4, soma)
imprime(10, 1, subtracao)
