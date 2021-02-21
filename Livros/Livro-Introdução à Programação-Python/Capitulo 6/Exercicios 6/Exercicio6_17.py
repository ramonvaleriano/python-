# Program: Exercicio6_17.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 24/04/2020 - 20:29
# Updated:

estoque = { "Tomate" : [1000, 2.30],
            "Alface" : [500, 0.45],
            "Batata" : [2001, 1.20],
            "Feijão" : [100, 1.50] }

total = 0

produto = input("Digite o produto desejado: ")
produto = produto[0].upper()+produto[1:].lower()
print(produto)
quantidade = int(input("Entre com a quantiadde que deseja: "))
venda = [[produto, quantidade], ]
if (produto in estoque):
    for operacao in estoque:
        #produto, quantidade = operacao
        preco = estoque[produto][1]
        custo = preco * quantidade
        print("%12s: %3d x %6.2f = %6.2f"
              %(produto, quantidade, preco, custo))
        estoque[produto][0]-=quantidade
        quantidade = 0
        total+=custo
        custo = 0
    print("Custo total: %21.2f\n" %total)
    print("Estoque:\n")
else:
    print("Produto Invalido!\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Valor: %6.2f\n" %dados[1])
    
