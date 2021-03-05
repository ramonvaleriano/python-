# Program: aula_21k.py
# Author: Ramon R. Valeriano
# Description:
# Upadated: 08/10/2020 - 13:14

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f

f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial(9)
print(f1)
print(f2)
print(f3)