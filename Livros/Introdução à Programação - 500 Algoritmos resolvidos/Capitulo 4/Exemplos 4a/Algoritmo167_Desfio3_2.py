# Program: Algoritmo167_Desfio3_2.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 08:28
# Updated:

maximum = 10
for e in range(1, maximum+1):
    for n in range(e, maximum+1):
        print("%d-%d" %(e, n), end=" ")
        for t in range(1, e+1):
            print("\t", end=" ")

    #print("\t")
    print("\n")
    #print("\t")
