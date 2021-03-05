# Program: desafio_084.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 09:39

cont_pessoas = 0
dados = list()
pessoas = list()
while True:
    if cont_pessoas == 0:
        nome = str(input('Digite o nome de uma pessoa: '))
        peso = float(input(f'Digite o pesoa de {nome}: '))
        dados.append(nome)
        dados.append(peso)
        pessoas.append(dados[:])
        dados.clear()
        opcao = str(input('Deseja adionar os dados de mais uma pessoa[S/N]: ')).strip().upper()[0]
    if opcao == 'S':
        nome = str(input('Digite o nome de uma pessoa: '))
        peso = float(input(f'Digite o pesoa de {nome}: '))
        dados.append(nome)
        dados.append(peso)
        pessoas.append(dados[:])
        dados.clear()
        cont_pessoas+=1
    elif opcao == 'N':
        break
    else:
        print('Opção invalida: ')
        continue
mais_pesadas = list()
mais_leves = list()
for pessoa in pessoas:
    if pessoa[1]>=100:
        mais_pesadas.append(pessoa[:])
    else:
        mais_leves.append(pessoa[:])
print()
print(cont_pessoas)
print(pessoas)
print(mais_pesadas)
print(mais_leves)