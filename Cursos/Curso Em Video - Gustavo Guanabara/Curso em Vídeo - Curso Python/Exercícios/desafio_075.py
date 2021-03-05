# Program: desafio_075.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 22:29

tupla = list()

n = 0
t = 4
while n<t:
    number = input(input('Digite um valor: '))
    tupla.append(number)
    n+=1
tupla = tuple(tupla)
if 9 in tupla:
    print(tupla.count(9))
if 3 in tupla:
    print(tupla.index(3))
for i in range(len(tupla)):
    if tupla[i]%2==0:
        print(f'{i}', end=' ')