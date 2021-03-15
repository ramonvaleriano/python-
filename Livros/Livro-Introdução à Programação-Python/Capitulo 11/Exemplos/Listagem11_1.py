# Program: Listagem11_1.py
# Author: Ramon R. Valeriano
# Description: Exemplo de Uso do SQlite, em python
# Developed: 15/03/2020 - 13:24

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute("""create table agenda(
                  nome text, telefone text)
                  """)

cursor.execute("""
                insert into agenda(nome, telefone) 
                values(?,?)
                """, ('Ramon', '71 9 9277-4903'))
conexao.commit()
cursor.close()
conexao.close()