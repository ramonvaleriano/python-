# Program: listagem8_9.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 22:45

def fatorial_meu(number):
    total = 1
    while number>=1:
        total*=number
        number-=1
    return total

numero = int(input('Entre com um número: '))

print(fatorial_meu(numero))