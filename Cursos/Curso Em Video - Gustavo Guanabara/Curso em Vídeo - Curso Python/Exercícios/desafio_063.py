# Program: desafio_063.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 14:33

number = int(input('Digite um número inteiro qualquer: '))
anterior = 0
atual = 1
posterior = anterior+atual
s = 0
while s<number:
    if s == 0:
        print(anterior, end=' ')
    else:
        print(atual, end=' ')
        anterior = atual
        atual = posterior
        posterior = anterior + atual
    s+=1