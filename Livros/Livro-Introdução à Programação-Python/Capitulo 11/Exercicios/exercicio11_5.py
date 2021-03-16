# Program: exercicio11_5.py
# Author: Ramon R. Valeriano
# Description: 5° Exercicio
# Developed: 16/03/2020 - 10:16

import sqlite3

dados = [
    ('ka', 59000),
    ('HB20', 65000),
    ('Celta', 12000),
    ('Onix', 70000)
]

conexao = sqlite3.connect('precoNovo.db')
cursor = conexao.cursor()

cursor.execute("""
                create table precoNovo(
                nome text, valor float)
                """)

cursor.executemany("""
                insert into precoNovo(nome, valor)
                values(?,?)
                """, dados)

cursor.execute("""
                update precoNovo set valor = (valor*1.10)
                """)
print(f'Quantidade de alterações: {cursor.rowcount}')

conexao.commit()
cursor.close()
conexao.close()


