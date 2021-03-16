# Program: Listagem11_13.py
# Author: Ramon R. Valeriano
# Description: Apagando Registros
# Developed: 16/03/2020 - 10:58

import sqlite3

dados = [
    ('Maria', '45632-78945'),
    ('José', '6549-789456')
]

conexao = sqlite3.connect('agendaTeste.db')
cursor = conexao.cursor()

cursor.executemany("""
                insert into agendaTeste(nome, telefone)
                values(?,?)
                """, dados)

cursor.execute('select * from agendaTeste')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')

cursor.execute("""
                delete from agendaTeste where nome = 'José'
                """)
print(f'Quantidade de Registros Deletados: {cursor.rowcount}' )


if cursor.rowcount == 1:
    print("Registro Deletado!")
    conexao.commit()
else:
    print("Operação Abortada!")
    conexao.rollback()


cursor.execute('select * from agendaTeste')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')

#conexao.commit()
cursor.close()
conexao.close()