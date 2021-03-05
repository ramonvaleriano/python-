# Program: Algoritmo482_fun24.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 10/06/2020 - 15:02
# Upadated:

LISTA = list()

def ordem(lista):
    q = len(lista)
    cont = 0
    while cont<q:
        if lista[cont]>lista[cont+1]:
            lista[cont], lista[cont+1] = lista[cont+1], lista[cont]
        cont+=1
    return lista

lista_inicial = list()

for e in range(3):
    number = int(input("Digite %d numero: " %(e+1)))
    lista_inicial.append(number)

print(ordem(lista_inicial))

