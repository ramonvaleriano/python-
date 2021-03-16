# Program: Listagem11_12.py
# Author: Ramon R. Valeriano
# Description: Atualizando o Telefone
# Developed: 16/03/2020 - 10:03

import sqlite3

conexao = sqlite3.connect('agendaTeste.db')
cursor = conexao.cursor()

cursor.execute("""
                update agendaTeste set Telefone = '1111-1111'
                """)
print(f'Quantidade de Registros alterados: {cursor.rowcount}')
if cursor.rowcount == 1:
    conexao.commit()
    print('Alteração Realizada!')
else:
    conexao.rollback()
    print('Alteração Abortada!')
#cursor.close()
conexao.close()
