# Program: exercicio11_1.py
# Author: Ramon R. Valeriano
# Description: Primeiro Exercicio
# Developed: 15/03/2020 - 14:44

import sqlite3

dados = [
    ('ka', '59000'),
    ('HB20', '65000')
]

conexao = sqlite3.connect('preco.db')
cursor = conexao.cursor()
cursor.execute("""
                create table preco(
                nome text, valor text) 
                """)

cursor.executemany("""
                insert into preco(nome, valor)
                values(?,?)
                """, dados)
conexao.commit()
cursor.close()
conexao.close()