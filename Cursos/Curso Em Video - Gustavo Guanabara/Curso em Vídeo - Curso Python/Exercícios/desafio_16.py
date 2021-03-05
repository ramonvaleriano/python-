# Program: desafio_16.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 20:59

from math import trunc

def entrada():
    number = float(input('Digite um número: '))
    return number

def truncando(funcao):
    number = funcao()
    result = trunc(number)
    return result

print(truncando(entrada))