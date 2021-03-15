# Program: Listagem11_3testando.py
# Author: Ramon R. Valeriano
# Description: Exemplo de Uso do SQlite, em python
# Developed: 15/03/2020 - 14:15

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall()
print(resultado)
#print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')
cursor.close()
conexao.close()