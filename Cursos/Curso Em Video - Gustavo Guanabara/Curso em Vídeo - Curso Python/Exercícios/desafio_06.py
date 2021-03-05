# Programa: desafio_06.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:06

numero = 0

def entrada():
    global numero
    numero = float(input("Digite um número qualquer: "))
    return numero

def dobro(num):
    num*=2
    return num

def triplo(num):
    num*=3
    return num

def raiz(num):
    result = num**(1/2)
    return result

teste = entrada()
print(dobro(teste))
print(triplo(teste))
print(raiz(teste))