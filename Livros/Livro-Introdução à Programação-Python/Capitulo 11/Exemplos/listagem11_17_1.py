# Program: Listagem11_17_1.py
# Author: Ramon R. Valeriano
# Description: Consulta dos estados brasileiros, ordenados por nome.
# Developed: 16/03/2020 - 13:21

import sqlite3

conexao = sqlite3.connect('brasil.db')
conexao.row_factory = sqlite3.Row

cursor = conexao.cursor()
print('%3s %-20s %12s' %('Id', 'Estado', 'População'))
print('='*37)
for estado in cursor.execute('select * from estados order by nome'):
    print(f'Id: {estado["id"]:3} - Nome: {estado["nome"]:20} - População: {estado["populacao"]:12}')

cursor.close()
conexao.close()