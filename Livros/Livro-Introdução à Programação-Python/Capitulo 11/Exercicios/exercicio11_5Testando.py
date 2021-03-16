# Program: exercicio11_5Testando.py
# Author: Ramon R. Valeriano
# Description: 5° Exercicio
# Developed: 16/03/2020 - 10:23

import sqlite3

conexao = sqlite3.connect('precoNovo.db')
cursor = conexao.cursor()

cursor.execute('select * from precoNovo')
while True:
    resultado = cursor.fetchone()
    if resultado ==  None:
        break
    print(f'Nome do carro: {resultado[0]} Valor: R$ {resultado[1]:.2f}')

conexao.commit()
cursor.close()
conexao.close()