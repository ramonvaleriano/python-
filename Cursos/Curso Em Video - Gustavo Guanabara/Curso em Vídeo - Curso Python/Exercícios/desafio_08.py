# Programa: desafio_08.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 22/09/2020 - 22:19

def entrada():
    numero = float(input("Digite um número em Metros"))
    return numero

def convt_cm(num):
    return (num*100)

def convt_mm(num):
    return (num*1000)

test = entrada()
print(convt_cm(test))
print(convt_mm(test))