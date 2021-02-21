# Program: Listagem8_27.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 19:05
# Updated:

def imprime_lista(L, fimpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            fimpressao(e)

def imprime_elemento(e):
    print("Valor: %d" %e)

def ehpar(x):
    return(x%2==0)

def ehimpar(x):
    return not ehpar(x)

L = [1,7,9,2,11,0]

imprime_lista(L, imprime_elemento, ehpar)
print()
imprime_lista(L, imprime_elemento, ehimpar)
