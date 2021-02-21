# Program: Listagem6_51.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 22/04/2020 - 23:06
# Updated:

tabela = { "Alface" : 0.45,
           "Batata" : 1.20,
           "Tomate" : 2.30,
           "Feijão" : 1.50 }
print(tabela, "\n")
del tabela["Tomate"]
print(tabela, "\n")
tabela.pop("Batata")
print(tabela, "\n")
tabela["Cebola"] = 1.28
print(tabela, "\n")
tabela.pop("Alface")
print(tabela, "\n")
#tabela.append("Caralho")
#print(tabela, "\n")
