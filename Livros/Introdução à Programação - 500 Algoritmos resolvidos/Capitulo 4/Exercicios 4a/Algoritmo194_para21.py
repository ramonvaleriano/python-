# Program: Algoritmo194_para21.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:38
# Updated:

higher = int(input("Enter with the higher number: "))
if higher > 0:
    for e in range(1, higher+1):
        #product = higher*2
        print(e, end=" ")
    product = higher*2
    print("\n", product)
else:
    print("Invalided Option!")
