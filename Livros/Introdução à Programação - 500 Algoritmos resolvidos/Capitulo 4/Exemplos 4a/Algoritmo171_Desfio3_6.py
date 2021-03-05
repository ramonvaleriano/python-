# Program: Algoritmo171_Desfio3_6.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 09:06
# Updated:

maximum = 10
for e in range(1, maximum+1):
    for n in range(maximum-e, 0, -1):
        print(" ", end=" ")
    print("%d-%d" %(e, (11-e)))
