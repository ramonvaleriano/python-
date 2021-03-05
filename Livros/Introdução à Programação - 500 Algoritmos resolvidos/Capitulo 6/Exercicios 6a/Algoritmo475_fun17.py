# Program: Algoritmo475_fun17.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 09/06/2020 - 15:06
# Updated:

def vogais(string):
    #string = string.lower()
    transformar = list(string)
    transformado = list()
    for e in transformar:
        if((e == "a")or(e == "e")or(e == "i")or(e == "o")or(e == "u")):
            transformado.append(1)
        else:
            transformado.append(0)
    return transformado

name = str(input("Digite um nome: "))
print(vogais(name))

