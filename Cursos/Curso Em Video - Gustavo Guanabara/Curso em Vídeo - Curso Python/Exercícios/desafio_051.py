# Program: desafio_051.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 23:21

first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for n in range(10):
    a = first + ((n-1)*razao)
    print(a)
