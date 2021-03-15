# Program: Listagem11_5.py
# Author: Ramon R. Valeriano
# Description: Consulta, registro por registro.
# Developed: 15/03/2020 - 14:32

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')
cursor.close()
conexao.close()

