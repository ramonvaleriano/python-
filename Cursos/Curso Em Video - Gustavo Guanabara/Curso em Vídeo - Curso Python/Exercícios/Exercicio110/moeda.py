# Program: moeda.py
# Author: Ramon R. Valeriano
# Description: Modulo Criado para alimentar exercícios
# Developed: 09/10/2020 - 11:37
# Updated: 09/10/2020 - 15:21

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

def linha(quantidade=30):
    print('-'*quantidade)

def resumo(preço=0, valor_c=0, valor_b=0):
    linha()
    print('Resumo do Valor'.center(30))
    linha()
    print(f'Preço Analisado: {conversao(preço)}')
    linha()
    print(f'Dobro do Preço: {dobro(preço, True)}')
    linha()
    print(f'O valor do aumento: {aumento(preço, valor_c, True)}')
    linha()
    print(f'O valor do queda: {diminuir(preço, valor_b, True)}')
    linha()
    print(f'O valor da metade: {metade(preço, True)}')
