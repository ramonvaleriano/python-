# Program: teste_continue.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 02/10/2020 - 20:00

lista = list(range(0, 11))

for e in lista:
    if e%2==0:
        continue
    else:
        print(e)