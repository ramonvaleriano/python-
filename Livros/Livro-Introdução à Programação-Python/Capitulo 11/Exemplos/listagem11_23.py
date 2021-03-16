# Program: Listagem11_23.py
# Author: Ramon R. Valeriano
# Description: Funções de Agregação com order by
# Developed: 16/03/2020 - 16:06

import sqlite3

with sqlite3.connect('brasil.db') as conexao:
    cursor = conexao.cursor()
    print('Região Estados População Mínima   Máximo     Média      Total(Soma)')
    print('====== =======           ======== =======    =======    ===========')
    for regiao in cursor.execute(""" 
                                 select regiao, count(*), min(populacao), max(populacao),
                                 avg(populacao), sum(populacao) as tpop
                                 from estados
                                 group by regiao
                                 having count(*)>5
                                 order by tpop desc
                                 """):
        print(f'{regiao[0]:6} {regiao[1]:7} {regiao[2]:18} {regiao[3]:10,} '
              f'{regiao[4]:10,.0f} {regiao[5]:13,}')

    cursor.close()