# Program: aula_16a.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 07:53

lanches = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanches)
print()
for l in lanches:
    print(l, end='...')

print('\n')
numeros = 1, 2, 3, 4, 5
print(numeros)
print(type(numeros))
""" As tuplas são totalmente imutáveis, até para formar adicionar novos elementos.  
novo = 'Coxinha'
lanches.append(novo)
print(lanches)
"""