# Program: Algoritmo202_para29.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 12:14
# Updated:

higher = int(input("Enter with the higer number: "))
if higher > 0:
    for e in range(1, higher+1):
        if(e%3==0)and(e%5==0):
            print(e, end=" ")
else:
    print("Invalid Option!")
