# Program: Listagem8_29.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 05/06/2020 - 19:28
# Updated:

def barra(n=10, c="*"):
    print(c*n)

l = [[5,"-"],[10,"*"],[5],[6,"."]]
for e in l:
    barra(*e)
