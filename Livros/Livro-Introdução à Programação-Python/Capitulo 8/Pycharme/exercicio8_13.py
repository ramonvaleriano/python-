# Program: exercicio8_13.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 23/09/2020 - 06:50

import random
number = random.randint(1, 10)
for e in range(3):
    num = int(input('Digite um número: '))
    if num == number:
        print('Você acertou!')
        break
    else:
        print('Você errou!')
print('O número sorteado foi: {0}'.format(number))

