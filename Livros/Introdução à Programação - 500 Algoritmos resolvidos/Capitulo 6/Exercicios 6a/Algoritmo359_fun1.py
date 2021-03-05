# Programa: Algoritmo359_fun1.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 06/06/2020 - 20:39
# Updated:

def cabecalho(nome, simbolo="*"):
    print(simbolo*(len(nome)+4))
    print(nome)

name = str(input("Digite o nome que deseja imprimir: "))
cabecalho(name)
