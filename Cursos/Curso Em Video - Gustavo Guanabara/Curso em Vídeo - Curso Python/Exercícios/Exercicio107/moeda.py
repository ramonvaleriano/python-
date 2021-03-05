# Program: moeda.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 09/10/2020 - 11:37

def aumento(numero, valor):
    result = numero + ((numero*valor)/100)
    return result

def diminuir(numero, valor):
    result = numero - ((numero*valor)/100)
    return result

def dobro(numero):
    result = numero*2
    return result

def triplo(numero):
    result = numero*3
    return result

def metade(numero):
    result = (numero/2)
    return result
