# Program: listagem8_27.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 06:45

def imprime(L, fimpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def impressao(number):
    print('Valor: {}'.format(number))

def ehpar(number):
    return(number%2==0)

def ehimpar(number):
    return(not ehpar(number))

lista = list(range(21))

imprime(lista, impressao, ehpar)
imprime(lista, impressao, ehimpar)