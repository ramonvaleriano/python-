# Program: Listagem11_10_1.py
# Author: Ramon R. Valeriano
# Description: Atualizando todo os telefones de uma só vez.
# Developed: 16/03/2020 - 09:25

import sqlite3

dados = [
    ('Ramon', '071 9 9277-4903'),
    ('Milla', '123456-654987'),
    ('Chatona', '3216547-89456')
]

conexao = sqlite3.connect('agendaTeste.db')
cursor = conexao.cursor()

cursor.execute("""
                create table agendaTeste(
                nome text, telefone text)
                """)

cursor.executemany("""
                    insert into agendaTeste(nome, telefone)
                    values(?,?)
                    """, dados)

cursor.execute('update agendaTeste set telefone = "123-456"')

conexao.commit()
cursor.close()
conexao.close()