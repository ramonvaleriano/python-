# Program: Listagem6_43.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 13:15
# Updated:


compras = []

while True:
    produto = input("Produto: ")
    produto = produto.upper()
    if produto == "FIM":
        break
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor: "))
    compras.append([produto, quantidade, valor])
sum_=0
for e in compras:
    print("%20s = %05d x %5.2f = %6.2f "
          %(e[0], e[1], e[2], (e[1]*e[2])))
    sum_+=(e[1]*e[2])
print("Total: %7.2f" %sum_)
