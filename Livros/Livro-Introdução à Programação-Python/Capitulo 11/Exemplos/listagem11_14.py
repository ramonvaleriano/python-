# Program: Listagem11_14.py
# Author: Ramon R. Valeriano
# Description: Acesso Simplificado.
# Developed: 16/03/2020 - 11:35

import sqlite3

with sqlite3.connect('agendaTeste.db') as conexao:
    for registro in conexao.execute('select * from agendaTeste'):
        print(f'Nome: {registro[0]} Telefone {registro[1]}')