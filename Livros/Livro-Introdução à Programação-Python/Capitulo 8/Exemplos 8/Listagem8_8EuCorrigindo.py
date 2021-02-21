# Program: Listagem8_8EuCorrigindo.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 12:40
# Updated:

def soma(lista):
    q = len(lista)
    total = 0
    cont = 0
    while cont<q:
        total+=lista[cont]
        cont+=1
    return total

l = [1,7,2,9,15]
print("{0}".format(soma(l)))
print("{0}".format(soma([7,9,12,3,100,20,4])))

