# Program: Listagem8_30.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 19:33
# Updated:

def soma(*args):
    s = 0
    for e in args:
        s+=e
    return s

print(soma(1, 2))
print(soma(2))
print(soma(5,6,7,8))
print(soma(9,10,11,12,13,14,15,17,18))
