# Program: Algoritmo354_Vetor2.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 14:19
# Updated:

lista_numbers = list()
quantity = 4

for e in range(quantity):
    number = int(input("Enter with the %d° number: " %(e+1)))
    lista_numbers.append(number)
print("\n\n")
for n in lista_numbers:
    if n%2==0:
        message = "Never"
        print("%d - %s" %(n, message))
    else:
        message = "Odd"
        print("%d - %s" %(n, message))
