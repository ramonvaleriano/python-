# Program: Listagem8_20.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 18:26
# Updated:

def soma(a, b, imprime=False):
    s = a+b
    if imprime:
        print(s)
    return s
print(soma(2,3))
print(soma(3, 4, True))
print(soma(5,8, False))

