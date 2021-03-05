# Program: TrianguloSuperiorDaDP.Py
# Author: Ramon R. Valeriano
# Description:
# Developed: 13/05/2020 - 19:54
# Updated:

lista1 = list(range(1, 5))
lista2= list(range(1, 5))
listat = list()
listat.append(lista1)
listat.append(lista2)

for e in range(1, 5):
    for n in range(e+1, 5):
        print("\t", listat[e][n], end=" ")
    print()
    for g in range(e):
        print()
    
