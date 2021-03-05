# Program: aula_16d.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 19:48

lanches = 'Hamburgues', 'Suco', 'Pizza', 'Pudim'

for i in range(0, len(lanches)):
    print(f'Eu comigo {lanches[i]}, na posição {i}')
print(f'\nEu comi muito!')
print('\n\n')
for i, r in enumerate(lanches):
    print(f'Eu comi: {r}, na posição: {i}')
print(f'\nEu comi muito!')
