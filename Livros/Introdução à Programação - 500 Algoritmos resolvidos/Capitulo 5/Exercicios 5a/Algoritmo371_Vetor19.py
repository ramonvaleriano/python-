# Program: Algoritmo371_Vetor19.py 
# Author: Ramon R. Valeriano
# Description: 
# Developed: 28/04/2020 - 20:28
# Updated:

quantity1 = 5
quantity2 = 7
lista1 = list()
lista2 = list()
lista3 = list()

for e in range(quantity1):
    number1 = int(input("Enter with %d° number: " %(e+1)))
    lista1.append(number1)
for n in range(quantity2):
    number2 = int(input("Enter with %d° number: " %(n+1)))
    lista2.append(number2)
lista3 = lista1[:]+lista2[:]
quantity3 = len(lista3)
cont = quantity3
while cont>0:
    g = 0
    quantity3 = len(lista3)
    for h in range(quantity3):
        if lista3[g] == lista3[h]:
            del lista3[h]
        h+=1
    cont-=1
print(lista3)
            
    
