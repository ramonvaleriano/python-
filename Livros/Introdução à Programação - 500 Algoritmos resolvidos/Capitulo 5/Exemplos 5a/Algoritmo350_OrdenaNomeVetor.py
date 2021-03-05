# Program: Algoritmo350_OrdenaNomeVetor.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 12:48
# Updated:

lista = list()
quantity = 5
for e in range(quantity):
    name =  str(input("Enter with %d name: " %(e+1)))
    lista.append(name)

for n in range(quantity):
    for y in range((n+1), quantity):
        if lista[n]>lista[y]:
            aux = lista[n]
            lista[n] = lista[y]
            lista[y] = aux
print(lista)
