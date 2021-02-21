# Program: listagem9_2.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 11:43

arquivo = open('números.txt', 'r')
for linha in arquivo.readlines():
    print(f'{linha}')
arquivo.close()