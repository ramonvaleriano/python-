# Program: desafio_096.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 07/10/2020 - 13:25

def area(comprimento, largura, linha):
    area_ = comprimento*largura
    linha()
    print(f'A área é: {area_:}m²')
    linha()

def linha():
    print('='*50)

linha()
comprimento = float(input('Digite o comprimento desejado: '))
largura = float(input('Digite a largura desejada: '))
linha()
area(comprimento, largura, linha)