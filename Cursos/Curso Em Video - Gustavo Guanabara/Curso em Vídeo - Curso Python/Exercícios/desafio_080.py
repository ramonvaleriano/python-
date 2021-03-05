# Program: desafio_080.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 14:42

lista= []
lista_ordenada = list()

quantidade = 5

for n in range(quantidade):
    number = int(input('Digite o %d° número: ' %(n+1)))
    lista.append(number)
#print(lista_normal)
c = 0
while c<quantidade:
    #atual = lista[c]
    s = 0
    #proximo = lista[c+1]
    while s<(quantidade-1):
        if lista[c]<=lista[s]:
            lista[c], lista[s] = lista[s], lista[c]
        s+=1
    c+=1
print(lista)
