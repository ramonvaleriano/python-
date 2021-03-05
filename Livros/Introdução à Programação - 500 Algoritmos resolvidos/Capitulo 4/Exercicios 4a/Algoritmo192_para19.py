# Program: Algoritmo192_para19.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 11:23
# Updated:

higher = int(input("Enter with higher number: "))
if higher > 0:
    for e in range(1, higher):
        if e%2!=0:
            print(e)
else:
    print("Invalid Option!")
