# Program: Listagem6_42.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 13:12
# Updated:

produto1 = ["Maçã", 10 , 0.30]
produto2 = ["Pera", 5 , 0.75]
produto3 = ["Kiwi", 4 , 0.98]

compras = [produto1,produto2,produto3]

for e in compras:
    print("Produto: %s" %e[0])
    print("Quantidade: %02d" %e[1])
    print("Valor: %5.2f" %e[2])
    print("\n\n")
    
