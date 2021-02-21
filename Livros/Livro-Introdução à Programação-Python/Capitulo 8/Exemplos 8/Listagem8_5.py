# Program: Listagem8_5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 12:13
# Updated:

def pesquisa(lista, valor):
    for x,e in enumerate(lista):
        if valor == e:
            return x
    return None

l = [10, 20, 25, 30]

print(pesquisa(l, 25))
print(pesquisa(l, 27))
print(pesquisa(l, 10))
