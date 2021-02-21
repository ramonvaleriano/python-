# Program: listagem8_37.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 23/09/2020 - 06:46

import random

m = random.randint(1, 10)
x = int(input('Escolha um número entra 1 a 10: '))
if x == m:
    print('Você acertou o número!')
else:
    print('Você errou o número!')
