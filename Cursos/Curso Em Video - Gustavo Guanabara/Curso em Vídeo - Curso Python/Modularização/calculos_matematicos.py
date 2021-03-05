# Program: calculos_matematicos.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 08/10/2020 - 17:17

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f*=c
    return f

def soma(*numero):
    soma_=sum(numero)
    return soma_

def dobro(numero):
    return (numero*2)

def triplo(numero):
    return (numero*3)


