# Program: Algoritmo172_Desfio3_7.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 09:26
# Updated:

maximum = 10
for e in range(2, maximum+1):
    for n in range(10-e, 0, -1):
        print("\t", end=" ")
    for c in range(12-e, maximum+1):
        print("%d-%d" %(e, c), end=" ")
    print()
