# Program: Algoritmo383_Vetor31.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/05/2020 - 21:36
# Updated:

lista = list()
quantity = 5
troca = list()
for e in range(quantity):
    number =  float(input("Enter with %d° number: " %(e+1)))
    lista.append(number)
for n in range((quantity-1), -1, -1):
    troca.append(lista[n])

lista = troca[:]
print(lista)
