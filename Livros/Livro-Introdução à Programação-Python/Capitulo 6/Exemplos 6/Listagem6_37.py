# Program: Listagem6_37.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 12:46
# Updated:

compras=[]

while True:
    produto = input("Entre com o nome do produto: ")
    produto = produto.upper()
    if produto == "FIM":
        break
    compras.append(produto)
for x,e in enumerate(compras):
    print((x+1),e)
    
