# Program: exercicio11_1Teste1.py
# Author: Ramon R. Valeriano
# Description: Segundo Exercicio
# Developed: 15/03/2020 - 15:19

import sqlite3
from contextlib import closing

dados = [
    ('ka', '59000'),
    ('HB20', '65000')
]

with sqlite3.connect('preco1.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""
                        create table preco1(
                        nome text, valor text
                        """)

        cursor.executemany("""
                            insert into preco1(nome, valor)
                            values(?,?)
                            """, dados)
    conexao.commit()
