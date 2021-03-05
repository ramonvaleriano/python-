# Program: Algoritmo382_Vetor30.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/05/2020 - 21:18
# Updated:

lista1 = list()
lista2 = list()
quantity = 20

for e in range(quantity):
    number =  float(input("Enter with the %d° number: " %(e+1)))
    lista1.append(number)
print("\n")
cont = 0
lista2 = lista1[:]
while cont<len(lista2):
    cont2 = 0
    while cont2<len(lista2):
        if cont2 > cont:
            if lista2[cont]==lista2[cont2]:
                del lista2[cont2]
        cont2+=1
    cont+=1
print()
cont = 0
while cont<len(lista2):
    cont2 = 0
    while cont2<len(lista2):
        if lista2[cont]<lista2[cont2]:
            lista2[cont], lista2[cont2] = lista2[cont2], lista2[cont]
        cont2+=1
    cont+=1
print()
for n in lista2:
    print(n, end=" ")
