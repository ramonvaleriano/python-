# Program: Algoritmo199_para26.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 12:05
# Updated:

higher = int(input("Enter with the higher number: "))
bottom = int(input("Enter with the bottom number: "))

if higher>bottom:
    for e in range(bottom, higher+1):
        if e%6==0:
            print(e)
else:
    print("Invalided Option!")
