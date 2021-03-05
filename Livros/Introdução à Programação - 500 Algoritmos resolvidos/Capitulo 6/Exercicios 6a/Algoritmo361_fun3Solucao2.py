# Programa: Algoritmo361_fun3Solucao2.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 21:00
# Updated:

def dobro(number):
    result = number*2
    return result

def mostrar(lista, execucao):
    #quantity = len(lista)
    for x in lista:
        print("{0} X 2 = {1}".format(x, execucao(x)))

numeros = list()

for e in range(3):
    adicionar = float(input("Digite o número que deseja: "))
    numeros.append(adicionar)

mostrar(numeros,dobro)
