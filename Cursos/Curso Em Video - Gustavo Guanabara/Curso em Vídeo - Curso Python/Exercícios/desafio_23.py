# Program: desafio_23.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 09:43

def contador(f_leitura):
    quantidade = len(f_leitura)
    lista_numeros = list(f_leitura)
    for e in range((quantidade-1),-1,-1):
        print(lista_numeros[e])

numero = str(input('Digite um número qualquer: '))
contador(numero)