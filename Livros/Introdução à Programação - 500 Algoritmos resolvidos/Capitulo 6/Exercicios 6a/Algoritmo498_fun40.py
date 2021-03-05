# Program: Algoritmo498_fun40.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 11/06/2020 - 12:04 
# Updated:

import random

def crescente(lista):
    new_lista = sorted(lista[:])
    return new_lista

def contador(lista, ordem):
    repetidos = list()
    lista_o = ordem(lista[:])
    for e in lista_o:
        dados = list()
        quantity = lista_o.count(e)
        if(quantity>1):
            dados.append(e)
            dados.append(quantity)
            repetidos.append(dados[:])
    return repetidos

numeros = list()
quantity = 1000

for n in range(quantity):
    number = random.randint(1, 100)
    numeros.append(number)

n_repetidos = contador(numeros, crescente)
em_ordem = crescente(numeros)

for o in em_ordem:
    print(o)
print("\n\n")

for r in n_repetidos:
    print("%5d - %5d" %(r[0], r[1]))
print()
        
    
