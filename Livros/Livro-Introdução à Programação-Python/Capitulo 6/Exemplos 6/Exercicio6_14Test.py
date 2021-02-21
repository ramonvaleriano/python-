# Program: Exercicio6_14Test.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 13:56
# Updated:

l = [3,6,1,8,9,10,4,6]
fim=len(l)

for e in range(fim, 1, -1):
    trocou  = False
    for n in range(fim-1):
        if l[n]>l[n+1]:
            trocou = True
            aux = l[n]
            l[n]=l[n+1]
            l[n+1]=aux
    if not trocou:
        break

for g in l:
    print(g)
