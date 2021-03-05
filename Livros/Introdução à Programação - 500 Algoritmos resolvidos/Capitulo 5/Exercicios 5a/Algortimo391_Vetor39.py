# Program: Algortimo391_Vetor39.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/05/2020 - 10:17
# Updated:

quantity = 10
lista = list()
for e in range(quantity):
    number = float(input("Enter with %d° number: " %(e+1)))
    lista.append(number)
maior = 0
cont = 0
point = 0
while cont<len(lista):
    test = cont+1
    if test<len(lista):
        if lista[test]>lista[cont]:
            point+=1
        else:
            point = 0
        if point > maior:
            maior = point
    cont+=1
print("\n\n")
print(maior)
    
    
