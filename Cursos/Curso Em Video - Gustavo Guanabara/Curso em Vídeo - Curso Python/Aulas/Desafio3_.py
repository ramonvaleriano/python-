# Program: Desafio3.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 13/09/2020 - 12:44

def entrada():
    numeros = list()
    number1 = int(input("Entre com o primeiro Número: "))
    numeros.append(number1)
    number2 = int(input("Entre com o segundo Número: "))
    numeros.append(number2)
    return numeros

def soma(i_funcao):
    soma = 0
    lista = i_funcao()
    for i, e in enumerate(lista):
        soma+=e
    return soma

def mensagem(i_funcao1, i_funcao2):
    lista1 = i_funcao1()
    print('Os número digitados foram: ')
    for i in lista1:
        print(i, end=",")
    soma = i_funcao2()
    print('Sua Soma: ',soma)

entrada()
mensagem(entrada, soma(entrada))


    
    
