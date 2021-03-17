# Program: Listagem11_26.py
# Author: Ramon R. Valeriano
# Description: Solicitando o tratamento do tipo de Campos
# Developed: 17/03/2020 - 08:56

import sqlite3

with sqlite3.connect('brasil.db', detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    cursor = conexao.cursor()
    for feriado in cursor.execute("""
                                  select * from feriados
                                  """):
        print(feriado)

    cursor.close()