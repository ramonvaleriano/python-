# Program: Listagem6_53.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/04/2020 - 20:11
# Updated:

estoque = { "Tomate" : [1000, 2.30],
            "Alface" : [500, 0.45],
            "Batata" : [2001, 1.20],
            "Feijão" : [100, 1.50] }
venda = [["Tomate", 5], ["Alface", 10], ["Batata", 5]]
total = 0

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("%12s: %3d x %6.2f = %6.2f"
          %(produto, quantidade, preco, custo))
    estoque[produto][0]-=quantidade
    total+=custo
print("Custo total: %21.2f\n" %total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Valor: %6.2f\n" %dados[1])
    
