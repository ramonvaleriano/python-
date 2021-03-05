# Program: Algoritmo201_para28.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 02/04/2020 - 12:11
# Updated:

bottom = int(input("Enter with the bottom number: "))
higher = int(input("Enter with the higher number: "))
sum_=0
if higher>bottom:
    for e in range(bottom+1, higher):
        if e%2==0:
            print(e, end=" ")
            sum_+=e
    print()
    print(sum_)
else:
    print("Invalided Option!")
