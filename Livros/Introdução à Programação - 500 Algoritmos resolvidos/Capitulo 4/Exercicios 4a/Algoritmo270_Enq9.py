# Program: Algoritmo270_Enq9.py
# Author: Ramon R. Valeriano
# Description:
# Developed: 03/04/2020 - 11:42
# Updated:

number = int(input("Enter with a number:"))

while number!=-999:
    for e in range(1, number+1):
        if number%e==0:
            print(e, end=" ")
    print()
    number = int(input("Enter with a number:"))
    

