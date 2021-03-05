# Program: aula_18e.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 09:07

galera = list()
dado = list()
quantidade = 5

for pessoa in range(quantidade):
    nome = str(input(f'Digite o nome da pessoa {pessoa+1}: '))
    dado.append(nome)
    dado.append(int(input(f'Digite a idade dessa mesma pessoa: ')))
    galera.append(dado[:])
    dado.clear()
print()
print(galera)