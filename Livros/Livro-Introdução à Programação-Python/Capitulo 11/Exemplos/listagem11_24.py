# Program: Listagem11_24.py
# Author: Ramon R. Valeriano
# Description: Criando uma tabela de feriados nacionais
# Developed: 16/03/2020 - 16:27

import sqlite3

feriados = [("2014-01-01", "Confraternização Universal"), ("2014-04-21", "Tiradentes"),
            ("2014-05-01", "Dia do trabalhador"), ("2014-09-07", "Independência"),
            ("2014-10-12", "Padroeira do Brasil"), ("2014-11-02", "Finados"),
            ("2014-11-15", "Proclamação da República"), ("2014-12-25", "Natal")]

with sqlite3.connect('brasil.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("""
                   create table feriados(id integer primary key autoincrement,
                   data date, descricao text) 
                   """)
    cursor.executemany("""
                    insert into feriados(data, descricao)
                    values(?,?)
                    """, feriados)

    cursor.close()