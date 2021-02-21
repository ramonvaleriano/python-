# Program: Listagem8_35.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 20:13
# Updated:

from Entrada import valida_inteiro

l = []

for x in range(10):
    l.append(valida_inteiro("Digite um Número: ", 0, 20))
print("Soma %d" %(sum(l)))
