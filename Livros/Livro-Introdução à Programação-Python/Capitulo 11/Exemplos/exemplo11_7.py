# Program: Listagem11_7.py
# Author: Ramon R. Valeriano
# Description: Consulta com filtro
# Developed: 15/03/2020 - 15:50

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = "Ramon"')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')
cursor.close()
conexao.close()

