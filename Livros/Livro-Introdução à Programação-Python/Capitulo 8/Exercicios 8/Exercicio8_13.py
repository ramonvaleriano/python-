# Program: Exercicio8_13.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 20:24
# Updated:

import random

erros = 0
acertos = 0
aleatorio = random.randint(1, 10)
while erros<3 or acertos<3:
    test = int(input("Entre com um número: "))
    if test == aleatorio:
        acertos+=1
    else:
        erros+=1
