# Program: Exercicio8_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 13:45
# Updated:

def soma(lista):
    total = 0
    for e in lista:
        total+=e
    return total
l=[1,7,2,9,15]
print(soma(l))
print(soma([7,9,12,3,100,20,4]))
