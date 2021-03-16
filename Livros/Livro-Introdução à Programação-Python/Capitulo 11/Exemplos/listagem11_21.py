# Program: Listagem11_21.py
# Author: Ramon R. Valeriano
# Description: Usando funções de agregações
# Developed: 16/03/2020 - 15:19

import sqlite3

with sqlite3.connect('brasil.db') as conexao:
    cursor = conexao.cursor()
    print('Região Estados População Mínima   Máximo     Média      Total(Soma)')
    print('====== =======           ======== =======    =======    ===========')
    for regiao in cursor.execute("""
                                select regiao, count(*), min(populacao), max(populacao),
                                avg(populacao), sum(populacao) 
                                from estados
                                group by regiao
                                """):
        print(f'{regiao[0]:6} {regiao[1]:7} {regiao[2]:18} {regiao[3]:10,} '
              f'{regiao[4]:10,.0f} {regiao[5]:13,}')
    resultadoBrasil = cursor.execute(""" 
                                     select count(*), min(populacao), max(populacao),
                                     avg(populacao), sum(populacao)
                                     from estados
                                    """).fetchone()
    print(f'BRASIL: {resultadoBrasil[0]:6} {resultadoBrasil[1]:18,} {resultadoBrasil[2]:10}'
          f' {resultadoBrasil[3]:10,.0f} {resultadoBrasil[4]:13,}')
    cursor.close()