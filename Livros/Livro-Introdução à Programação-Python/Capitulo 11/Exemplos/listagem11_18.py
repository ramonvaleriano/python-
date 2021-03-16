# Program: Listagem11_18.py
# Author: Ramon R. Valeriano
# Description: Alterando a tabela
# Developed: 16/03/2020 - 14:17

import sqlite3

conexao = sqlite3.connect('brasil.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("""
                alter table estados 
                add sigla text
                """)
cursor.execute("""
                alter table estados
                add regiao text
                """)
cursor.close()
conexao.close()