# Program: Listagem11_16.py
# Author: Ramon R. Valeriano
# Description: Criação de bando de dados com a população dos estados brasileiros.
# Developed: 16/03/2020 - 13:13

import sqlite3

dados = [["São Paulo",43663672],["Minas Gerais",20593366],["Rio de Janeiro",16369178],["Bahia",15044127],["Rio Grande do Sul",11164050],["Paraná",10997462],["Pernambuco",9208511],["Ceará",8778575],["Pará",7969655],["Maranhão",6794298],["Santa Catarina",6634250],["Goiás",6434052],["Paraíba",3914418],["Espírito Santo",3838363],["Amazonas",3807923],["Rio Grande do Norte",3373960],["Alagoas",3300938],["Piauí",3184165],["Mato Grosso",3182114],["Distrito Federal",2789761],["Mato Grosso do Sul",2587267],["Sergipe",2195662],["Rondônia",1728214],["Tocantins",1478163],["Acre",776463],["Amapá",734995],["Roraima",488072]]

conexao = sqlite3.connect('brasil.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("""
                create table estados(
                id integer primary key autoincrement,
                nome text,
                populacao integer)
                """)

cursor.executemany("""
                    insert into estados(nome, populacao)
                    values(?,?)
                    """, dados)
conexao.commit()
cursor.close()
conexao.close()