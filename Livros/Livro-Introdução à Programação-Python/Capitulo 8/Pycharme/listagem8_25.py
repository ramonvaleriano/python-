# Program: listagem8_25.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 06:36

def retangulo(largura, altura, caracter='*'):
    linha = largura*caracter
    for e in range(altura):
        print(linha)

retangulo(3, 4)
retangulo(largura=3, altura=4)
retangulo(altura=2, largura=10)
retangulo(altura=2, largura=10, caracter='-')
