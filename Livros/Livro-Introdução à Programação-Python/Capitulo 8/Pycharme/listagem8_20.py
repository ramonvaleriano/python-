# Program: listagem8_20.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 06:21

def soma(a, b, imprime = False):
    s = a+b
    if imprime:
        print(s)
    return s

print(soma(2,3))
print(soma(4,7))
print(soma(5,6))
print(soma(2,3, imprime=True))
print(soma(2,2, True))