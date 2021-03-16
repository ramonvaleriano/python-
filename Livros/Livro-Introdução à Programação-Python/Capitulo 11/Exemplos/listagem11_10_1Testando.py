# Program: Listagem11_10_1Testando.py
# Author: Ramon R. Valeriano
# Description: Atualizando o Telefone
# Developed: 16/03/2020 - 09:32

import sqlite3

name = str(input('Digite o nome que deseja procurar: '))
name = name.strip().title()

conexao = sqlite3.connect('agendaTeste.db')
cursor = conexao.cursor()

cursor.execute('select * from agendaTeste where nome = ?', (name,))
x = 0
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        if x == 0:
            print('Nome não encontrado!')
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}\n\n')
    x += 1

cursor.execute('select * from agendaTeste')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')

cursor.close()
conexao.close()



