# Program: Algoritmo398_Vetor46.py
# Author: Ramon R. Valeriano
# Description: 
# Developed: 11/05/2020 - 21:30
# Updated:

estoque = list()
quantity = 50
for e in range(quantity):
    dados = list()
    code = int(input("Entre com o código do produto: "))
    if code == -1:
        break
    quantidade = int(input("Digite a quantidade que há no estoque: "))
    dados.append(quantidade)
    value = float(input("Digite o valor unitário: "))
    dados.append(value)
    estoque.append(dados[:])
while True:
    for e in estoque:
        for v in e:
            print(e, end=" ")
        print("\n")
    procurar = int(input("Digite o codigo do produto que você deseja procurar: "))
    cont = 0
    sum_=0
    while cont<len(estoque):
        if procura == estoque[cont][0]:
            unidades = int(input("Quantas Unidades deseja comprar: "))
            if unidades <= estoque[cont][1]:
                apagar = unidade*estoque[cont][2]
                sum_+=apagar
                estoque[cont][1]-=unidades
                break
            else:
                print("Não há essa quantidade disponivel!")
                print("Quantidade disponível: %d" %estoque[cont][1])
                break
        cont+=1
    if cont>=len(estoque):
        print("Produto não encontrado")
    print("\n")
print("\n\n")
print("Lucro do dia: R$%7.2f" %sum_)
print("\n\n")
cont1 = 0
while cont1<len(estoque):
    cont2 = 0
    while cont2<len(estoque):
        if estoque[cont1][1]<estoque[cont2]:
            estoque[cont1], estoque[cont2] = estoque[cont2], estoque[cont1]
        cont2+=1
    cont1+=1
for e in estoque:
    for v in e:
        print(e, end=" ")
    print("\n")
