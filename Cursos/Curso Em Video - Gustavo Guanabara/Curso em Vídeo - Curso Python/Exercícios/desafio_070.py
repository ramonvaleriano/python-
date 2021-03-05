# Program: desafio_070.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 18:37

soma = 0
produtos_superiores = 0
nome_barato = 0

while True:
    nome_produto = str(input('Digite o nome do produto: ')).upper().strip()
    valor = float(input('Digite o valor do produto: '))
    if soma == 0:
        nome_barato = nome_produto
        menor = valor
    soma+=valor

    if valor>=1000:
        produtos_superiores+=1
    elif valor<=menor:
        menor = valor
        nome_barato = nome_produto

    opcao = str(input('Deseja adicionar mais algum produto a sacola[S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        print('Gastando mais')
    else:
        print('Opçaõ Invalida!')

print(soma)
print(produtos_superiores)
print(nome_barato)