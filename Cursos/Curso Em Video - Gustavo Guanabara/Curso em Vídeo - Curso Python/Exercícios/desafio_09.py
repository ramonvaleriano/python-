# Programa: desafio_09.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:24

def entrada():
    numero = int(input('Digite o número que deseja obter a tabuada: '))

def tabuada(num):
    recebe = int(num)
    x = 0
    while x<=10:
        result = (x+recebe)
        print('{} + {} = {}'.format(x, num, result))
        x+=1
test = entrada()
tabuada(test)