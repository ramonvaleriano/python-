# Program: Listagem11_10.py
# Author: Ramon R. Valeriano
# Description: Atualizando o Telefone
# Developed: 16/03/2020 - 09:11

import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("""
                update agenda
                set telefone = '13245-6789'
                where nome = 'Ramon'
                """)
conexao.commit()
cursor.close()
conexao.close()

