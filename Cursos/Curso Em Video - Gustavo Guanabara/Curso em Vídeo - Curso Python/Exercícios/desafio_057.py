# Program: desafio_057.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 29/09/2020 - 08:17

while True:
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Seu sexo é Masculino!')
        break
    elif sexo == 'F':
        print('Seu sexo é Feminino!')
        break
    else:
        print('Opção Invalida, digite um sexo de verdade!')