# Program: listagem8_23.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 06:30

def retangulo(largura, altura, caracter='*'):
    linha = largura*caracter
    for e in range(altura):
        print(linha)

retangulo(2, 4)