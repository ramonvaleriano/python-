# Program: Listagem8_8.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 12:35
# Updated:

def soma(lista):
    total = 0
    x = 0
    while x<5:
        total+=lista[x]
        x+=1
    return total

l = [1,7, 2,8, 15]
print(soma(l))
print(soma([7,9,12,3,100,20,4]))
