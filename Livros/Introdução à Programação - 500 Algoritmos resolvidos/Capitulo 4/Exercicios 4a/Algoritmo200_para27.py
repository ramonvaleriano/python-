# Program: Algoritmo200_para27.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 12:08
# Updated:

higher = int(input("Enter with the higher number: "))
bottom = int(input("Enter with the bottom number: "))
multiple = int(input("Enter with the multiple wanted: "))

if higher>bottom and multiple>0:
    for e in range(bottom+1, higher):
        if e%multiple==0:
            print(e)
else:
    print("Invalided Option!")
