# Program: exercicio8_7.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 06:55

def mdc(a, b):
    if b == 0:
        return a
    elif a>b:
        c = a%b
        print(mdc(b, c))

mdc(4, 6)

