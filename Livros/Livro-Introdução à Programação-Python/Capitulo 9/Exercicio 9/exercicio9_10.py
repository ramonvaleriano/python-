# Program: exercicio9_10.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 14:21

lista_aquivos = ['impares.txt', 'completa.txt', 'pares.txt', 'intervalo.txt', 'entrada.txt']
super_aquivo = open('grande_arquivo.txt', 'w')
for arquivos in lista_aquivos:
    dados = open(arquivos, 'r')
    for linha in dados.readlines():
        super_aquivo.write(linha)
    super_aquivo.write(f'\n\n')
    dados.close()
    print('\n\n')
super_aquivo.close()
