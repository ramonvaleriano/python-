# Program: desafio_028.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:20

from random import randint

sorteado = randint(0, 5)
number = int(input('Digite um número inteiro: '))
print(sorteado)
if number>0:
    if number==sorteado:
        print('Parabéns, você acertou!')
    else:
        print('Você errou!')
else:
    print('Você tem problemas.')