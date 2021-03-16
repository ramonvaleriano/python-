# Program: Listagem11_15.py
# Author: Ramon R. Valeriano
# Description: Acessando os campos pelo nome
# Developed: 16/03/2020 - 11:40

import sqlite3

conexao = sqlite3.connect('agendaTeste.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()
for registro in cursor.execute('select * from agendaTeste'):
    print(f'Nome: {registro["nome"]} Telefone: {registro["telefone"]}')
cursor.close()
conexao.close()