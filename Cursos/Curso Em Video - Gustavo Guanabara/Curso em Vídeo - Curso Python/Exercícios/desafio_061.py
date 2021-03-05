# Program: desafio_061.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 14:21

first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 0
while n<=10:
    a = first + ((n-1)*razao)
    print(a, end=' ')
    n+=1