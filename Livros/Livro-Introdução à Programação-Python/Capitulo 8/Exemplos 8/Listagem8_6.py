# Program: Listagem8_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 12:23
# Updated:

def soma(lista):
    total = 0
    for e in lista:
        total+=e
    return total

def media(lista):
    result = soma(lista)/len(lista)
    return result

l = [10, 20, 25, 30]
print(media(l))
