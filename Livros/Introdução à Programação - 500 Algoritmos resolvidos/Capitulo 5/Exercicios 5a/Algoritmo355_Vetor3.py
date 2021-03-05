# Program: Algoritmo355_Vetor3.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 14:24
# Updated:

lista_numbers = list()
quantity = 4

for e in range(quantity):
    number = int(input("Enter with the %d° number: " %(e+1)))
    lista_numbers.append(number)
print("\n\n")
cont = 0
for n in lista_numbers:
    if n%6==0:
        cont+=1
    print(n, end=" ")
print("\n\n")
print(cont)
