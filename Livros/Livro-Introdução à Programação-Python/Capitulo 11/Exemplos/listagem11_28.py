# Program: Listagem11_28.py
# Author: Ramon R. Valeriano
# Description: Feriado nos próximos 60 dias.
# Developed: 17/03/2020 - 10:05

import sqlite3
import datetime

hoje = datetime.date.today()
mais60dias = hoje + datetime.timedelta(days=60)

with sqlite3.connect('brasil.db', detect_types=sqlite3.PARSE_DECLTYPES) as conexao:
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    for feriado in cursor.execute("""
                                  select * from feriados where data = ? and data = ?
                                  """, (hoje, mais60dias)):
        print(f'{feriado["data"].strftime("%d/%m")} {feriado["descricao"]}')

    cursor.close()