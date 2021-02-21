# Program: Exercicio6_14Test1.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 14:02
# Updated:

l = [3,6,1,8,9,10,4,6]
fim=len(l)

for e in range(fim, 1, -1):
    trocou  = False
    for n in range(fim-1):
        if l[n]>l[n+1]:
            trocou = True
            l[n], l[n+1] = l[n+1], l[n]
    if not trocou:
        break

for g in l:
    print(g)
