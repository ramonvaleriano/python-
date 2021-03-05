# Program: desafio_22.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 26/09/2020 - 22:56

def maiuscula(entrada):
    nome_completo = entrada
    nome_completo = nome_completo.upper()
    return nome_completo

def minuscula(entrada):
    nome_completo = entrada
    nome_completo = nome_completo.lower()
    return nome_completo

def dividir(entrada):
    nome_completo = str(entrada)
    dividido = nome_completo.splint()
    return dividido

def contagem_letras(entrada, dividir):
    nome_completo = dividir(entrada)
    soma = 0
    for e in nome_completo:
        soma+=len(e)
    return soma

def contagem_first(entrada, dividir):
    nome_completo = dividir(entrada)
    first = nome_completo[0]
    quantidade = len(first)
    return quantidade

nome = str(input('Digite o nome completo da pessoa: '))
n_maiuscula = maiuscula(nome)
print(n_maiuscula)
n_minuscula = minuscula(nome)
print(n_minuscula)
n_quantidade_letras = contagem_letras(nome, dividir)
print(n_quantidade_letras)