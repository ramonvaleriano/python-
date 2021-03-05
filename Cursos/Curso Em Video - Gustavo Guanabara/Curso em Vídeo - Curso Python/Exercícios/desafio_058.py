# Program: desafio_058.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 08:26

import random

sorteio = random.randint(0, 10)
number = -1
cont = 0
while sorteio != number:
    sorteio = random.randint(0, 10)
    number = int(input('Digite um número inteiro, entre 0 a 10: '))
    print('O número sortiado foi: {}'.format(sorteio))
    cont+=1
    if sorteio == number:
        print('Parabéns!')
    else:
        print('Tentei mais uma vez!')
print('O jogador teve que tentar {} vezes.'.format(cont))