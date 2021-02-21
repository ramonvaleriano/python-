# Program: listagem8_35.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 23/09/2020 - 06:38

import entrada

lista = list()

for x in range(3):
    lista.append(entrada.valida_inteiro("Digite um número desejado: ", 0, 20))
soma = sum(lista)
print('A soma total = {:*^20}'.format(soma))
