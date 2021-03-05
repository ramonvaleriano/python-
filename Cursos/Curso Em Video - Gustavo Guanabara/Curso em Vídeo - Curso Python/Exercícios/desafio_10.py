# Programa: desafio_10.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:36

dollar = float(input('Qual o valor do dolar: '))
carteira = float(input('Quanto você tem an carteira: '))

digite = int(input('Qual tabuada você deseja: '))

quantos = carteira/dollar
print('Você tem ${} dollares'.format(quantos))

x = 0
while x<=10:
    result = digite + x
    print('{} + {} = {}'.format(x, digite, result))
    x+=1

