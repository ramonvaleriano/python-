# Program: desafio_049.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 27/09/2020 - 23:11

number = int(input('Digite um número: '))

for e in range(1, 11):
    print('{:02} * {:2} = {:02}'.format(e, number, (number*e)))
