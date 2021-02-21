# Program: Listagem6_45Test.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 22/04/2020 - 22:16
# Updated:

tabela = { "Alface" : 0.45,
           "Batata" : 1.20,
           "Tomate" : 2.30,
           "Feijão" : 1.50 }

for e in tabela:
    print(e)

print()
for e in tabela:
    print(tabela[e])
    
print()
for e in tabela:
    print(e, tabela[e])
print()
print(tabela["Alface"])
