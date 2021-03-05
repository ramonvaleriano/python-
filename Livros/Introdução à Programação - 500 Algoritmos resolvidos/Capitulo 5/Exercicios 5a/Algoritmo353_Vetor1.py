# Program: Algoritmo353_Vetor1.py 
# Author: Ramon R. Valeriano
# Description:
# Developed: 25/04/2020 - 13:50
# Updated:

nomes = list()
quantity = 10

for e in range(quantity):
    name = str(input("Enter with the %d° name: " %(e+1)))
    name = name.upper()
    nomes.append(name)
print("\n\n")
for x, n in enumerate(nomes):
    print("%2d - %s" %((x+1), n))
