# Program: desafio_17.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 21:00

from math import sqrt, pow

def hipotenusa():
    cateto_oposto = float(input('Digite o cateto Oposto: '))
    cateto_adjacente = float(input('Digite o cateto Adjacente: '))
    result = sqrt(pow(cateto_adjacente, 2)+pow(cateto_oposto, 2))
    return result

valor_final = hipotenusa()
print(valor_final)