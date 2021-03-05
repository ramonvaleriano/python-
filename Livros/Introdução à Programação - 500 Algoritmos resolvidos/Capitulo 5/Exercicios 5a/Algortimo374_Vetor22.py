# Program: Algortimo374_Vetor22.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/05/2020 - 22:13
# Updated:

lista1 = []
lista2 = []

quantity = 12

for e in range(quantity):
    number = float(input("Enter with %d° number: " %(e+1)))
    lista1.append(number)
print("\n")
for n in lista1:
    converstion = n**2
    lista2.append(converstion)
print()
print(lista2)
