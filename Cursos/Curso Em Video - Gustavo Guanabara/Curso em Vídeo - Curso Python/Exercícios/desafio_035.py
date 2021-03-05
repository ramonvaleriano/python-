# Program: desafio_035.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 11:59

r1 = float(input(''))
r2 = float(input(''))
r3 = float(input(''))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Pode ser um triângulo')
else:
    print('Não pode ser um triangulo!')