# Program: Algortimo375_Vetor23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 04/05/2020 - 22:21
# Updated:

lista1 = []
lista2 = []

quantity = 5

for e in range(quantity):
    number = float(input("Enter with %d° number: " %(e+1)))
    lista1.append(number)

for n in lista1:
    if n%2!=0:
        product=n**2
        lista2.append(product)
    else:
        conversion=n/2
        lista2.append(conversion)
print()

for v in lista1:
    print(v, end=" ")
print()
for v in lista2:
    print(v, end=" ")
