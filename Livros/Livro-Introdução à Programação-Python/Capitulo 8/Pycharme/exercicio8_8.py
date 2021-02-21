# Program: exercicio8_8.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 16/09/2020 - 07:00


def mmc(a, b):
    if b == 0:
        return a
    elif a>b:
        c = abs(a*b)
        d = (c/(mmc(a, b)))
        print(d)

mmc(4, 6)
