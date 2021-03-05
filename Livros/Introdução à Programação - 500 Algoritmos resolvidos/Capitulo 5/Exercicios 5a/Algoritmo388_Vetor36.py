# Program: Algoritmo388_Vetor36.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/05/2020 - 21:17
# Updated:

quantity = 10
lista = list()

for e in range(quantity):
    number = int(input("Entre com um número: "))
    lista.append(number)
    if e != 0:
        cont = 0
        while cont<len(lista):
            cont2 = 0
            while cont2<len(lista):
                if lista[cont]>lista[cont2]:
                    lista[cont], lista[cont2] = lista[cont2], lista[cont]
                cont2+=1
            cont+=1
        for n in lista:
            print(n)
    print()
