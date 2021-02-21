# Program: exercicio9_1.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 12:00

nome_arquivo = str(input('Qual o nome do arquivo você deseja coletar dados: '))
arquivo = open(nome_arquivo, 'r')
for leitura in arquivo.readlines():
    print(leitura)
arquivo.close()
