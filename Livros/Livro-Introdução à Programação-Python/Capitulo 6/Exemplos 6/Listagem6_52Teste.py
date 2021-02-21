# Program: Listagem6_52Teste.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 22/04/2020 - 23:17
# Updated:

estoque = {"Tomate" : [100, 2.30],
           "Alface" : [500, 0.45],
           "Batata" : [2001, 1.20],
           "Feijão" : [100, 1.50] }

for test in estoque:
    print("Chave: ", test)
    print("Quantidade: ", estoque[test][0])
    print("Valor: ", estoque[test][1])
    print("\n")
