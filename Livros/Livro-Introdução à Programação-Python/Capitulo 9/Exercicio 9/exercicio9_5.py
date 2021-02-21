# Program: exercicio9_5.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 13:08

pares = open('pares.txt', 'r')
inverso = open('inverso_pares', 'w')
inverso_pares = list()
for linha in pares.readlines():
    number = int(linha)
    inverso_pares.append(number)
inverso_pares.sort(reverse=True)
print()
for linha in inverso_pares:
    inverso.write(f'{linha}\n')
pares.close()
inverso.close()
inverso.close()