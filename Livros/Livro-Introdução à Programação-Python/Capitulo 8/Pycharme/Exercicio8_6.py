# Program: exercicio8_6.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 22:55

def pesquisa(lista, number):
    for i, n in enumerate(lista):
        if number == n:
            return i

def montando():
    import random
    lista = list()
    for e in range(10):
        lista.append(random.randint(1,20))
    return lista

numero = int(input("Digite um número: "))
lista1 = montando()
print(lista1)
print(pesquisa(lista1, numero))
