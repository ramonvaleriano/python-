# Program: desafio_082.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 06/10/2020 - 07:20

def entrada_dados():
    geral = list()
    number = float(input('Digite um número: '))
    geral.append(number)
    while True:
        opcao = str(input('Deseja por mais um número[S/N]: ')).strip().upper()[0]
        if opcao == 'N':
            break
        elif opcao == 'S':
            number = float(input('Digite um número: '))
            geral.append(number)
        else:
            print('Opção Invalida!')
    return geral

def par(entrada):
    completa = entrada
    pares = list()
    for numero in completa:
        if numero%2==0:
            pares.append(numero)
    return pares

def impar(entrada):
    completa = entrada
    impares = list()
    for numero in completa:
        if numero%2!=0:
            impares.append(numero)
    return impares

total = entrada_dados()
pares = par(total)
impares = impar(total)
print(total)
print(pares)
print(impares)

