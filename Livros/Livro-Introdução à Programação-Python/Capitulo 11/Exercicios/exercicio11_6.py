# Program: exercicio11_6.py
# Author: Ramon R. Valeriano
# Description: 5° Exercicio
# Developed: 16/03/2020 - 10:36

import sqlite3

name = str(input('Digite o nome do carro que deseja: '))
name = name.strip()

conexao = sqlite3.connect('precoNovo.db')
cursor = conexao.cursor()

cursor.execute('select * from precoNovo where nome = ?', (name,))
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome do Carro: {resultado[0]} Valor do carro: R$ {resultado[1]:.2f}')

novo_valor = float(input('Digite o novo valor desejado: '))

cursor.execute('update precoNovo set valor = ? where nome = ?', (novo_valor, name))
print(f'Quantidade de alterações: {cursor.rowcount}')

if cursor.rowcount == 1:
    print('Alteração Realizada!')
    conexao.commit()

else:
    print('Alteração Abortada!')
    conexao.rollback()

cursor.close()
conexao.close()