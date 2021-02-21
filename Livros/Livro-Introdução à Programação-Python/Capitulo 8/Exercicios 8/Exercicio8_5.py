# Program: Exercicio8_5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 13:21
# Updated:

def pesquisa(lista, aprocurar):
    if aprocurar in lista:
        local = lista.index(aprocurar)
        return local
    else:
        return None
    
def verificando(lista, testando):
    teste_local = pesquisa(lista, testando)
    if teste_local != None:
        number = teste_local
        message = "Número está dentro da Lista. Na posição:"
    else:
        number = None
        message = "Número não existe"
    print("{0}\n{1}".format(message, number))
    
l = [10, 20, 25, 30]

verificando(l, 20)
