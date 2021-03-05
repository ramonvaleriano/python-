# Program: Algoritmo497_fun39.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 12:02 
# Updated:

import random

def verifica(lista, number):
    return(number in lista)

def crescente(lista):
    new_lista = sorted(lista)
    return new_lista

def mensagem(lista, ordem, number, teste):
    l_lista = ordem(lista)
    if(teste(lista, number)):
        print("Esse número está na lista!")
        for x, e in enumerate(l_lista):
            print("%3d - %3d" %(x, e))
    else:
        print("Esse número não está na lista!")
        for x, e in enumerate(l_lista):
            print("%3d - %3d" %(x, e))

numeros = list()
quantity = 10
for n in range(quantity):
    number = random.randint(0, 100)
    numeros.append(number)
print()
numero = int(input("Entre com o número que deseja procurar: "))
print()
mensagem(numeros, crescente, numero, verifica)
