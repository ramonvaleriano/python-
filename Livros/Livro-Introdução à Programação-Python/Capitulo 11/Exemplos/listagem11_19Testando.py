# Program: Listagem11_19Testando.py
# Author: Ramon R. Valeriano
# Description: Preenchendo a sigla e a região de cada estado.
# Developed: 16/03/2020 - 14:30

import sqlite3

with sqlite3.connect('brasil.db') as conexao:
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    for estado  in cursor.execute("select * from estados order by nome"):
        print(f'Id: {estado["id"]:3} - Nome: {estado["nome"]:20} - Siglar: {estado["sigla"]:2} -'
              f' População: {estado["populacao"]:12} - Região: {estado["regiao"]:2}' )

    cursor.close()