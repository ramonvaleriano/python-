# Program: aula_18e.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 22:50

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

for e in range(inicio, fim+1, passo):
    print(e)
print()
print('Fim!')