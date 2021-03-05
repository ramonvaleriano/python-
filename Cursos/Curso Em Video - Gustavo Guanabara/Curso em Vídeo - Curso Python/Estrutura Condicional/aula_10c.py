# Program: Aula_10c.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:03

nome = str(input('Qual é o seu nome: '))
if nome == 'Ramon':
    print('Que nome do caralho você tem!')
print('Bom dia {}!'.format(nome))
print('\n\n\n')
frase = ('Nome Lindo' if nome == 'Ramon' else 'Nome muito normal esse seu')
print(frase)