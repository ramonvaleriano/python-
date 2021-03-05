# Program: DiagonalPrincipal.Py
# Author: Ramon R. Valeriano
# Description:
# Developed: 13/05/2020 - 19:35
# Updated:

lista1 = list(range(1, 6))
lista2= list(range(1, 6))
listat = list()
listat.append(lista1)
listat.append(lista2)
print(listat)


for e in range(1, ((len(listat[0])+1))):
    print(e,e)
    for n in range(1, e+1):
        print("\t", end=" ")
        
