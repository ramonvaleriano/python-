# Program: listagem9_2OutraForma.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 11:46

aquivo = open('números.txt')
dados = aquivo.read("números.txt")
aquivo.close()
for registro in dados.split().lines():
    print(registro)