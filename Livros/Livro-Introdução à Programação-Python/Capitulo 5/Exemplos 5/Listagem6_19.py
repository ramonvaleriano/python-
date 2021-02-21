# Program: Listagem6_19.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 11:22
# Updated:

lista = ["a","b","c","d","e","f"]
print(lista, end=" ")
del lista[1]
print("\n\n")
print(lista, end=" ")
del lista[0]
print("\n\n")
print(lista, end=" ")
print("\n\n")
lista2 = ["a","b","c","d","e"]
retira = lista2.pop(0)
print(lista2, end=" ")
print("\n\n")
retira = lista2.pop(-2)
print(lista2, end=" ")
print("\n\n")
