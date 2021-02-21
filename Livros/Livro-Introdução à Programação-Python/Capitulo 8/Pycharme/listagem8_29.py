# Program: listagem8_29.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 18/09/2020 - 06:56

def barra(n=10, c="*"):
    print(c*n)
l = [[5, '-'], [10, '*'], [4], [6, '.']]

for e in l:
    barra(*e)