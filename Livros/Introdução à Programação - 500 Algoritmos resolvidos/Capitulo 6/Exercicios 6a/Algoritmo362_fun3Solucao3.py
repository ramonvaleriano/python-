# Programa: Algoritmo362_fun3Solucao3.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 21:33
# Updated:

import calculos

alunos = list()

for e in range(3):
    number = float(input("Digite o valor da %d nota: " %(e+1)))
    alunos.append(number)

print(calculos.media(alunos))
