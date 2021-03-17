# Program: Listagem11_27.py
# Author: Ramon R. Valeriano
# Description: Trabalhando com datas
# Developed: 17/03/2020 - 09:42

import sqlite3
from datetime import datetime

with sqlite3.connect('brasil.db', detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    for feriado in cursor.execute('select * from feriados'):
        print(f'{feriado["data"].strftime("%d/%m")} {feriado["descricao"]}')

    cursor.close()