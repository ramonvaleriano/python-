# Program: aula_21j.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 13:14

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f

n = int(input('Digite um número: '))
print(fatorial(n))