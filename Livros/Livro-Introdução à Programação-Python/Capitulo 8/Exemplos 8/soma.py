# Program: soma.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 20:03
# Updated:

import Entrada

l = []

for x in range(10):
    l.append(Entrada.valida_inteiro("Digite um Número: ", 0, 20))
print("Soma %d" %(sum(l)))
