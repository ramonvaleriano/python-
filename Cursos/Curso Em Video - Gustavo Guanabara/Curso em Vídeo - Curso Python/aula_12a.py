# Program: aula_12a.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 17:06

nome = str(input('Qual é o seu nome: '))
if nome == 'Ramon':
    print('Qua nome bonito!')
elif nome == 'Maria' or nome == 'José' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))