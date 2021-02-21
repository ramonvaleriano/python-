# Program: Listagem8_25.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 18:53
# Updated:

def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for e in range(altura):
        print(linha)

#retangulo(largura = 3, 4)
retangulo(largura = 3, altura = 4, "-")
