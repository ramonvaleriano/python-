# Program: desafio_062.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 14:21

first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
t = 10
while True:
    n = 0
    while n<=t:
        a = first + ((n-1)*razao)
        print(a, end=' ')
        n+=1
    print('\n')
    q = int(input('Você deseja mostar mais quantos termos: '))
    if q == 0:
        break
    t+=q