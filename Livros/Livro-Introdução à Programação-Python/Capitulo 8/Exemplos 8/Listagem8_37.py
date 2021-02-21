# Program: Listagem8_37.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 20:20
# Updated:

import random

n = random.randint(1,10)
x = int(input("Escolha um número entre 1 e 10: "))

if x == n:
    print("Você acertou!")
else:
    print("Você errou!")
