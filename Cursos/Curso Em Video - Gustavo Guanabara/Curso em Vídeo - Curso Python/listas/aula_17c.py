# Program: aula_17c.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 02/10/2020 - 19:20

valores = list()

for cont in range(3):
    valores.append(int(input(f'Digite o {cont+1}° valor: ')))
print()
for i, v in enumerate(valores):
    print(f'No indice: {i} tem o valor {v}')
print('Cheguei ao fínal da lista')