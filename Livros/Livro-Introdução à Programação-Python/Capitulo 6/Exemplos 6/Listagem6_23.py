# Program: Listagem6_23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 20/04/2020 - 21:11
# Updated:

l=[15,7,27,39]
number = int(input("Entre com o número a ser pesqusiado: "))
achou = False
cont = 0
while cont<len(l):
    if l[cont]==number:
        achou = True
        break
    cont+=1
if achou:
    print("%d achado na posição %d." %(number, cont))
else:
    print("Número não encontrado.")
