# Program: desafio_066.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 17:45

soma = cont = 0

while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    cont+=1
    soma+=number
print(f'A quantidade de números {cont}')
print(f'A soma de todos os números digitados: {soma}')