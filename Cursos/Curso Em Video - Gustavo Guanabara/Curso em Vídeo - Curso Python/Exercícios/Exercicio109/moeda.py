# Program: moeda.py
# Author: Ramon R. Valeriano
# Description: Modulo Criado para alimentar exercícios
# Developed: 09/10/2020 - 11:37
# Updated: 09/10/2020 - 12:34

def aumento(numero, valor, formato=False):
    result = numero + ((numero*valor)/100)
    return result if formato is False else conversao(result)


def diminuir(numero, valor, formato=False):
    result = numero - ((numero*valor)/100)
    return result if formato is False else conversao(result)


def dobro(numero, formato=False):
    result = numero*2
    return result if formato is False else conversao(result)


def triplo(numero, formato=False):
    result = numero*3
    return result if formato is False else conversao(result)


def metade(numero, formato=False):
    result = (numero/2)
    return result if formato is False else conversao(result)


def conversao(preço = 0, tipo = 'R$'):
    result = f'{tipo}{preço:.2f}'.replace('.',',')
    return result

