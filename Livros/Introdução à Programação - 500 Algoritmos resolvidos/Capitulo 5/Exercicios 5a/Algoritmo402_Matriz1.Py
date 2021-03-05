# Program: Algoritmo402_Matriz1.Py
# Author: Ramon R. Valeriano
# Description:
# Developed: 13/05/2020 - 20:00
# Updated:

quantity = 5
lista1 = list(range(quantity))
lista2= list(range(quantity))
listat = list()
listat.append(lista1)
listat.append(lista2)

for e in range(quantity):
    for n in range(quantity):
        number = int(input("Entre com um número para a linha %d  e a coluna %d: "%((e+1),(n+1))))
        listat[e][n]=number
print("-"*15+"Diagonal Principal"+"-"*15)
for e in range(quantity):
    print(listat[e][e])
    for n in range(0, e):
        print("\t", end=" ")
        
