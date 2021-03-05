# Program: aula_18f.py
# Author: Ramon R. Valeriano
# Description:
# Updated:  06/10/2020 - 09:17

galera = list()
dado = list()
quantidade = 3
total_maior = total_menor = 0

for pessoa in range(quantidade):
    nome = str(input(f'Digite o nome da pessoa {pessoa+1}: '))
    dado.append(nome)
    dado.append(int(input(f'Digite a idade dessa mesma pessoa: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1]>=18:
        print(f'{pessoa[0]} é maior de idade!')
        total_maior+=1
    else:
        print(f'{pessoa[0]} é menor de idade!')
        total_menor+=1
print(f'Quantidade de pesoas de maior: {total_maior}')
print(f'Quantidade de pesoas de menor: {total_menor}')