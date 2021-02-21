# Program: exercicio9_2.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 04/10/2020 - 12:05

arquivo = open("números.txt", "r")
minimo = int(input('Digite o número que devemos iniciar a contagem: '))
maximo = int(input('Digite o número que debemos fechar a contagem: '))

for linhas in arquivo.readlines(minimo, maximo):
    print(linhas)


arquivo.close()