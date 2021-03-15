# Program: Listagem11_8.py
# Author: Ramon R. Valeriano
# Description: Consulta com filtro
# Developed: 15/03/2020 - 15:54

import sqlite3

name = str(input("Digite o nome que deseja procurar: "))
name = name.strip()

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = ?', (name,))
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} Telefone: {resultado[1]}')
cursor.close()
conexao.close()