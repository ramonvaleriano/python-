# Program: Listagem11_2.py
# Author: Ramon R. Valeriano
# Description: Exemplo de Uso do SQlite, em python
# Developed: 15/03/2020 - 13:41

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchone()
