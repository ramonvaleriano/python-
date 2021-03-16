# Program: Listagem11_25.py
# Author: Ramon R. Valeriano
# Description: Acessando um campo do tipo data
# Developed: 16/03/2020 - 16:39

import sqlite3

with sqlite3.connect('brasil.db') as conexao:
    cursor = conexao.cursor()
    for feriado in cursor.execute('select * from feriados'):
        print(feriado)

    cursor.close()