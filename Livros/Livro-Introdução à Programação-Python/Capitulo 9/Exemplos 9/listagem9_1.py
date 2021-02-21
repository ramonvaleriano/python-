# Program: listagem9_1.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 11:30

arquivo = open("números.txt", "w")
for linha in range(1, 101):
    arquivo.write(f'{linha}\n')
arquivo.close()
