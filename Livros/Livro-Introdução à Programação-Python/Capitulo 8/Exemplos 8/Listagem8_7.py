# Program: Listagem8_7.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 12:31
# Updated:

def media(lista):
    total = 0
    for e in lista:
        total+=e
    result = total/len(lista)
    return result
l = [10, 25, 20, 45]
print(media(l))
