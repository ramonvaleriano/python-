# Program: Algoritmo380_Vetor28.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/05/2020 - 21:01
# Updated:


quantity = 5
lista = list()

for e in range(quantity):
    number =  int(input("Enter with the %d° number: " %(e+1)))
    lista.append(number)
print("\n\n")
quantity = len(lista)
for n in range((quantity-1), -1, -1):
    print(lista[n], end=" ")
print("\n")
