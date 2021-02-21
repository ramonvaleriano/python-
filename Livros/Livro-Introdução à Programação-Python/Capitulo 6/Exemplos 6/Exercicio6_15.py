# Program: Exercicio6_15.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 21/04/2020 - 13:50
# Updated:

l=[3,3,1,5,4]
fim=len(l)
while fim > 1:
    trocou = False
    x = 0
    while x<(fim-1):
        if l[x] > l[x+1]:
            trocou = True
            temp=l[x]
            l[x]=l[x+1]
            l[x+1]=temp
        x+=1

    if not trocou:
        break
    fim-=1
    
for e in l:
    print(e)


