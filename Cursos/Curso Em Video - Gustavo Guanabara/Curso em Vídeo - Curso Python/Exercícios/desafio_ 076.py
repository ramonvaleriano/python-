# Program: desafio_076.py
# Author: Ramon R. Valeriano
# Descritption:
# Updated: 01/10/2020 - 22:47

tupla = ('Arroz', 20.00, 'Feijão', 15.00, 'Picanhar', 67.49)

for i in range(0, len(tupla), 2):
    print(f'{tupla[i]} -->  {tupla[i+1]}')
