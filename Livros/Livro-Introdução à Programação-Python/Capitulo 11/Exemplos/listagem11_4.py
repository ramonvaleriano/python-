# Program: Listagem11_4.py
# Author: Ramon R. Valeriano
# Description: Consulta de multiplos resultados.
# Developed: 15/03/2020 - 14:20

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursos = conexao.cursor()
cursos.execute('select * from agenda')
resultado = cursos.fetchall()
for registro in resultado:
    print(f'Nome: {registro[0]}, Telefone: {registro[1]}')
cursos.close()
conexao.close()
