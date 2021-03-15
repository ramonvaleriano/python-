# Program: Listagem11_6.py
# Author: Ramon R. Valeriano
# Description: Uso de with para fechar a conexão.
# Developed: 15/03/2020 - 14:39

import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from agenda')
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')

