# Program: Listagem11_11.py
# Author: Ramon R. Valeriano
# Description: Atualizando o Telefone
# Developed: 16/03/2020 - 09:50

import sqlite3

conexao = sqlite3.connect('agendaTeste.db')
cursor = conexao.cursor()

cursor.execute("""
                update agendaTeste set telefone = '1234-5678'
                """)
print(f'Registro de quantas auterações: {cursor.rowcount}')

conexao.commit()
cursor.close()
conexao.close()