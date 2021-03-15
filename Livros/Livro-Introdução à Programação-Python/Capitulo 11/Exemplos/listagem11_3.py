# Program: Listagem11_3.py
# Author: Ramon R. Valeriano
# Description: Exemplo de Uso do SQlite, em python
# Developed: 15/03/2020 - 14:11

import sqlite3

dados = [
    ('Milla', '789456-45689'),
    ('Chata', '654987-456789'),
    ('Linda', '1233221-456987')
]

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.executemany("""
                    insert into agenda(nome, telefone)
                    values(?,?)
                    """, dados)
conexao.commit()
cursor.close()
conexao.close()