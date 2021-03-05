# Programa: Algoritmo365_fun6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 21:51
# Updated:

import maior_e_menor_listas

def entrada():
    quantity = int(input("Quantos números você deseja comparar: "))
    return quantity

def coletando(quantity):
    numeros = list()
    for e in range(quantity):
        number = float(input("Digite o %d número a ser coletado: " %(e+1)))
        numeros.append(number)
    return numeros
n = entrada()
coletando(n)
print("O maior número é: %7.3f" %(maior_e_menor_listas.maior(coletando(n))))
