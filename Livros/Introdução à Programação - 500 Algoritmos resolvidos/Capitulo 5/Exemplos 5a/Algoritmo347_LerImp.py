# Program: Algoritmo347_LerImp_.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 10:54
# Updated:

lista = list()
quantity = 10
for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    lista.append(name)
for n in lista:
    print(n, end=" ")
