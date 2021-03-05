# Program: Algortimo376_Vetor24.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/05/2020 - 22:33
# Updated:

quantity = 25
lista1 = list()
lista2 = list()
lista3 = list()

for e in range(quantity):
    number = int(input("Enter with %d° number: " %(e+1)))
    lista1.append(number)
print()
for n in range(quantity):
    number = int(input("Enter with %d° number: " %(n+1)))
    lista2.append(number)
print("\n\n")
for g in range(quantity):
    lista3.append(lista1[g])
    lista3.append(lista2[g])
print(lista3)
