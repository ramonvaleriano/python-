# Program: Listagem11_16Testando.py
# Author: Ramon R. Valeriano
# Description: Criação de bando de dados com a população dos estados brasileiros.
# Developed: 16/03/2020 - 13:15

import sqlite3

conexao = sqlite3.connect('brasil.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

for registro in cursor.execute('select * from estados'):
    print(f'Id: {registro["id"]} - Nome: {registro["nome"]} - População: {registro["populacao"]}')

cursor.close()
conexao.close()