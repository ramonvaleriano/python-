# Program: Listagem11_9.py
# Author: Ramon R. Valeriano
# Description: Consulta utilizando Parâmetros
# Developed: 15/03/2020 - 16:17

import sqlite3

name = str(input('Digite o nome a ser procurado: '))

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = ?', (name, ))
x = 0
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        if x == 0:
            print('Nada encontrado')
        break

    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')
    x+=1
cursor.close()
conexao.close()
