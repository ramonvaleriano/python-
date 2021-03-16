# Program: Listagem11_20.py
# Author: Ramon R. Valeriano
# Description: Agrupando e contando estados por região
# Developed: 16/03/2020 - 15:10

import sqlite3

with sqlite3.connect('brasil.db') as conexao:
    #conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    print('Região Número de estados')
    print("====== =================")
    for regiao in cursor.execute("""
                                select regiao, count(*)
                                from estados 
                                group by regiao
                                """):
        print(f'{regiao[0]:6} {regiao[1]:17}')
    cursor.close()