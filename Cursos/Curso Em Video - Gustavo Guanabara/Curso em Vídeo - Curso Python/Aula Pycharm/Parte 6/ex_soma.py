# Program: ex_soma.py
# Author: Ramon R. Valeriano
# Desciption:
# Updated: 13/09/2020 - 16:00

def entrada():
    lista = list()
    cont = 0
    while cont<=1:
        number = float(input('Entre com %d° numero:' %(cont+1)))
        lista.append(number)
        cont+=1
    return lista

def soma(i_funcao):
    #lista1 = i_funcao()
    soma_elementos = 0
    for i in i_funcao():
        soma_elementos+=i
    return soma_elementos

def mensagem(i_funcao1, i_funcao2):
    #lista2 = i_funcao1()
    resultado = i_funcao2(i_funcao1)
    for e in i_funcao1():
        print(e, end=", ")
    print('Sua soma = {}'.format(resultado))

mensagem(entrada,soma)
