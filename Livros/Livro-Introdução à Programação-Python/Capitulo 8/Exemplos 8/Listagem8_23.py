# Program: Listagem8_23.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 18:47
# Updated:

def retangulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for e in range(altura):
        print(linha)

retangulo(3,4)
print()
retangulo(largura=3,altura=4)
print()
retangulo(altura=5, largura=3)
print()
retangulo(caractere="$", altura=9, largura=5)
print()
c = "&"
a = 5
l = 28
retangulo(caractere=c, altura=a, largura=l)
