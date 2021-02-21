# Program: exercicio9_5.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 12:44

multiplos_4 = open("Multiplos de 4.txt", "w")
pares = open("pares.txt", "r")

for linha in pares.readlines():
    if int(linha) % 4 == 0:
        multiplos_4.write(f'{linha}')
pares.close()
multiplos_4.close()
