# Program: desafio_037.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 17:33

numero = int(input('Digite o número: '))
escolha = int(input('Digite o tipo de dado que deseja: '))

if escolha == 1:
    print('{:b}'.format(numero))
elif escolha == 2:
    print('{:o}'.format(numero))
elif escolha == 3:
    print('{:X}'.format(numero))
else:
    print('Opção Invalida!')