# Program: listagem8_30.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 07:00

def soma(*args):
    s=0
    for x in args:
        s+=x
    return s

print(soma(1, 2))
print(soma(3, 5, 7, 9, 2))
print(soma(9, 10, 29, 34, 56, 12, 34))