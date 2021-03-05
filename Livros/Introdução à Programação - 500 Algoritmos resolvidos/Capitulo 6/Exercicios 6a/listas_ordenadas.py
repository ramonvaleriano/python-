# Program: listas_ordenadas.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 16:05
# Updated:

def crescente(lista):
    anterior = 0
    quantity = len(lista)
    while anterior<quantity:
        posterior = anterior+1
        while posterior<quantity:
            if(lista[anterior]>lista[posterior]):
                lista[anterior], lista[posterior] = lista[posterior], lista[anterior]
            posterior+=1
        anterior+=1
    return lista

def minimo(lista):
    cont = 0 
    menor = lista[cont]
    while cont<len(lista):
        if menor>lista[cont]:
            menor = lista[cont]
        cont+=1
    return menor


