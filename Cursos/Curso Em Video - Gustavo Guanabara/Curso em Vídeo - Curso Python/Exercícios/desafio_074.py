# Program: desafio_074.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 22:18

from random import randint

tupla = list()

for i in range(5):
    tupla.append(randint(0, 100))

tupla = tuple(tupla)
print(tupla)
maior = max(tupla)
menor = min(tupla)
print(f'O maior número: {maior}')
print(f'O menor número: {menor}')