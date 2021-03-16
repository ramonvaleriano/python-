# Program: Listagem11_19.py
# Author: Ramon R. Valeriano
# Description: Preenchendo a sigla e a região de cada estado.
# Developed: 16/03/2020 - 14:23

import sqlite3

dados = [["SP", "SE", "São Paulo"], ["MG", "SE", "Minas Gerais"], ["RJ", "SE", "Rio de Janeiro"], ["BA", "NE", "Bahia"], ["RS", "S", "Rio Grande do Sul"], ["PR", "S", "Paraná"], ["PE", "NE", "Pernambuco"], ["CE", "NE", "Ceará"], ["PA", "N", "Pará"], ["MA", "NE", "Maranhão"], ["SC", "S", "Santa Catarina"], ["GO", "CO", "Goiás"], ["PB", "NE", "Paraíba"], ["ES", "SE", "Espírito Santo"], ["AM", "N", "Amazonas"], ["RN", "NE", "Rio Grande do Norte"], ["AL", "NE", "Alagoas"], ["PI", "NE", "Piauí"], ["MT", "CO", "Mato Grosso"], ["DF", "CO", "Distrito Federal"], ["MS", "CO", "Mato Grosso do Sul"], ["SE", "NE", "Sergipe"], ["RO", "N", "Rondônia"], ["TO", "N", "Tocantins"], ["AC", "N", "Acre"], ["AP", "N", "Amapá"], ["RR", "N", "Roraima"] ]


with sqlite3.connect('brasil.db') as conexao:
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.executemany("""
                    update estados 
                    set sigla = ?, 
                    regiao = ?
                    where nome = ?
                    """, dados)

    conexao.commit()
    cursor.close()

