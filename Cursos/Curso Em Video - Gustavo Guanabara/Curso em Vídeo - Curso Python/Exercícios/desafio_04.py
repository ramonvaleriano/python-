# Programa: desafio_04.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 19:58

def entrada():
    dado = input('Digite algum tipo de informação: ')
    return dado

def verificacao(variavel):
    teste = variavel
    print(type(teste))

numero = entrada()
verificacao(numero)
