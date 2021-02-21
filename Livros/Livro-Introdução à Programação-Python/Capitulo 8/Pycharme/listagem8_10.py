# Program: listagem8_10.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 15/09/2020 - 22:51

def fatorial_outro(number):
    total = 1
    x = 1
    while x<=number:
        total*=x
        x+=1
    return total

numero = int(input('Digite um número: '))
print(fatorial_outro(numero))