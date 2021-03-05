# Program: Algoritmo169_Desfio3_5.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 09:06
# Updated:

maximum=11
for e in range(1, maximum+1):
    cont = e
    for n in range(1, maximum-cont):
        print("%d-%d" %(e, n), end=" ")
    print()
