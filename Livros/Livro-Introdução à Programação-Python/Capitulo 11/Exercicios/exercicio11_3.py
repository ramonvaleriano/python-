# Program: exercicio11_3.py
# Author: Ramon R. Valeriano
# Description: 3° Exercicio
# Developed: 15/03/2020 - 16:41

import sqlite3
from contextlib import closing

name = str(input('Digite o valor do carro que deseja procurar: '))
name = name.strip()

with sqlite3.connect('preco.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from preco where nome = ?', (name, ))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                if x == 0:
                    print('Nenhum resultado encontrado!')
            print(f'Nome:{resultado[0]} Valor:{resultado[1]}')
            x+=1
