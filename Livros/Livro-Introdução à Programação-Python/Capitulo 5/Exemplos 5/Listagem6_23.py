# Program: Listagem6_23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 31/03/2020 - 14:10
# Updated:

lista = [15, 7, 27, 39]
number = int(input("Entre com um número para ser pesquisado na lista: "))
achou = False
cont = 0
while cont<=len(lista):
    if lista[cont]==number:
        achou=True
        break
    cont+=1
if achou:
    print("%d achado na posição %d." %(number, cont))
else:
    print("%d não encontrado." %number)
