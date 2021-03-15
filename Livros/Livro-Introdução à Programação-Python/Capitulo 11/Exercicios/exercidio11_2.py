# Program: exercicio11_2.py
# Author: Ramon R. Valeriano
# Description: Segundo Exercicio
# Developed: 15/03/2020 - 15:12

import sqlite3

conexao = sqlite3.connect('preco.db')
cursor = conexao.cursor()
cursor.execute('select * from preco')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Carro: {resultado[0]} Valor: R$ {resultado[1]} reais')
cursor.close()
conexao.close()