# Program: Algoritmo168_Desfio3_4.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 09:00
# Updated:

maximum = 10

for e in range(2, maximum+1):
    for n in range(1, e):
        print("%3d  -%3d" %(e, n), end=" ")
    print()
