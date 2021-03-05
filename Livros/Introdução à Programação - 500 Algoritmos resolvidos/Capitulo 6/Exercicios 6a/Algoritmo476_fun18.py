# Program: Algoritmo476_fun18.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/06/2020 - 15:09
# Updated:

def vogais(string):
    comparador = string.upper()
    comparador = list(comparador)
    string = list(string)
    quantity = len(string)
    final = list()
    for e in range(quantity):
        if comparador[e]==string[e]:
            final.append(1)
        else:
            final.append(0)
    return final

name = str(input("Digite um nome desejado: "))
print(vogais(name))
            
